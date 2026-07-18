import os, re

OLD_NAV_PIECE = '<li><a href="/pixmail/">✉️ PixMail</a></li></ul></li>'
NEW_NAV_PIECE = '<li><a href="/pixmail/">✉️ PixMail</a></li><li style="border-top:1px solid var(--border);margin-top:4px;padding-top:4px"><a href="https://pixmaps.web.app/search.html" target="_blank">🗺️ PixMaps</a></li></ul></li>'

count = 0
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fh:
                content = fh.read()
            new_content = content.replace(OLD_NAV_PIECE, NEW_NAV_PIECE)
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as fh:
                    fh.write(new_content)
                count += 1
                print(f'Updated: {path}')
print(f'\nTotal: {count} files updated')
