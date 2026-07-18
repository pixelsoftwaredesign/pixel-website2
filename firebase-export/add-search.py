import os

count = 0
for root, dirs, files in os.walk('.'):
    for f in files:
        if not f.endswith('.html'):
            continue
        path = os.path.join(root, f)
        with open(path, 'r', encoding='utf-8') as fh:
            content = fh.read()
        if 'pixsearch.js' in content:
            continue
        if '</body>' in content:
            new_content = content.replace('</body>', '<script src="/static/js/pixsearch.js"></script>\n</body>')
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(new_content)
            count += 1
            print(f'Updated: {path}')
print(f'\nTotal: {count} files updated')
