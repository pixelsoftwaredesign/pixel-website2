#!/usr/bin/env python3
"""Create the Cloudflare Email Routing rule commercial@pixelsoftwaredesign.xyz
-> pixelsoftwaredesign@gmail.com.

Run after the destination address is verified (status == verified). Creates a
temporary zone-scoped API token with Email Routing Rules Read/Write, creates the
rule, then deletes the token. Idempotent: skips if the rule already exists.
"""
import json, os, time, urllib.request, urllib.error
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

ACC = os.environ.get("CLOUDFLARE_ACCOUNT_ID", "ab7349e3df49fa223eddcb5995e2ea37")
ZONE = "74ed0a14445a6e7a2c4b02fa1a92c4c1"
ADMIN = os.environ["CLOUDFLARE_API_TOKEN"]
BASE = "https://api.cloudflare.com/client/v4"
DEST_EMAIL = "pixelsoftwaredesign@gmail.com"
SOURCE_EMAIL = "commercial@pixelsoftwaredesign.xyz"

def call(method, url, token, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(BASE + url, data=data, method=method,
        headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        b = e.read().decode()
        try: return e.code, json.loads(b)
        except Exception: return e.code, {"raw": b[:500]}

# 1. Check destination verified
s, d = call("GET", f"/accounts/{ACC}/email/routing/addresses", ADMIN)
dests = (d.get("result") or [])
dest = next((a for a in dests if a["email"] == DEST_EMAIL), None)
if not dest:
    raise SystemExit("Destination address not found; create it first.")
if dest.get("status") != "verified":
    raise SystemExit(f"Destination {DEST_EMAIL} is {dest.get('status')}; verify it first.")

# 2. Create temp token with Rules Read/Write on the zone
payload = {
    "name": "temp-email-rules-" + time.strftime("%Y%m%d%H%M%S"),
    "policies": [{"effect": "allow",
        "resources": {f"com.cloudflare.api.account.zone.{ZONE}": "*"},
        "permission_groups": [
            {"id": "1b600d9d8062443e986a973f097e728a"},  # Rules Read
            {"id": "79b3ec0d10ce4148a8f8bdc0cc5f97f2"},  # Rules Write
        ]}],
    "expires_on": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() + 1800)),
}
s, d = call("POST", f"/accounts/{ACC}/tokens", ADMIN, payload)
if not d.get("success"):
    raise SystemExit("token create failed: " + json.dumps(d.get("errors")))
tok = d["result"]["value"]; tid = d["result"]["id"]
try:
    # 3. Check existing rules
    s, d = call("GET", f"/zones/{ZONE}/email/routing/rules", tok)
    for rule in (d.get("result") or []):
        matchers = rule.get("matchers") or []
        if any(m.get("type") == "literal" and m.get("value") == SOURCE_EMAIL for m in matchers):
            print("Rule already exists:", rule.get("id"), rule.get("enabled"))
            raise SystemExit(0)
    # 4. Create rule
    s, d = call("POST", f"/zones/{ZONE}/email/routing/rules", tok, {
        "name": "Commercial",
        "enabled": True,
        "priority": 0,
        "matchers": [{"type": "literal", "field": "to", "value": SOURCE_EMAIL}],
        "actions": [{"type": "forward", "value": [DEST_EMAIL]}],
    })
    print("create rule =>", s, d.get("success"), json.dumps(d.get("errors"), ensure_ascii=False))
    print(json.dumps(d.get("result"), ensure_ascii=False)[:800])
finally:
    s, d = call("DELETE", f"/accounts/{ACC}/tokens/{tid}", ADMIN)
    print("delete temp token =>", s, d.get("success"))