import os, re

old_footer = '<div class="flinks"><a href="/">Accueil</a><a href="/prix/">Prix</a></div>'
new_footer = '<div class="flinks"><a href="tel:+21652675027">📞 +216 52 675 027</a><a href="/">Accueil</a><a href="/prix/">Prix</a></div>'

count = 0
for root, dirs, files in os.walk('.'):
    for f in files:
        if not f.endswith('.html'):
            continue
        path = os.path.join(root, f)
        with open(path, 'r', encoding='utf-8') as fh:
            content = fh.read()
        new_content = content.replace(old_footer, new_footer)
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(new_content)
            count += 1
            print(f'Updated: {path}')
print(f'\nTotal: {count} files updated')
