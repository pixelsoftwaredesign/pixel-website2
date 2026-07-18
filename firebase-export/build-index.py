import os, re, json

pages = []
base = '.'

skip = {'fix_pixmap.py', 'search-index.json'}

for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith('.html') or f in skip:
            continue
        path = os.path.join(root, f)
        rel = os.path.relpath(path, base)
        if rel.startswith('.'):
            continue
        with open(path, 'r', encoding='utf-8') as fh:
            html = fh.read()
        title_m = re.search(r'<title>(.*?)</title>', html)
        title = title_m.group(1) if title_m else ''
        desc_m = re.search(r'<meta\s+name="description"\s+content="(.*?)"', html, re.I)
        if not desc_m:
            desc_m = re.search(r'<meta\s+content="(.*?)"\s+name="description"', html, re.I)
        desc = desc_m.group(1) if desc_m else ''
        text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()[:800]
        url = '/' + rel.replace('index.html', '')
        if url == '/.':
            url = '/'
        pages.append({
            'title': title,
            'desc': desc,
            'url': url,
            'text': text
        })

# deduplicate URLs
seen = set()
unique = []
for p in pages:
    if p['url'] not in seen:
        seen.add(p['url'])
        unique.append(p)

with open('search-index.json', 'w', encoding='utf-8') as f:
    json.dump(unique, f, ensure_ascii=False, indent=0)

print(f'Indexed {len(unique)} pages')
for p in unique:
    print(f"  {p['url']} — {p['title']}")
