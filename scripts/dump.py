import re
with open('styles.css') as f:
    text = f.read()

matches = re.findall(r'\.planet-[a-z]+\s*\{[^}]*\}', text)
output = '\n'.join(matches)

with open('planets_dump.txt', 'w', encoding='utf-8') as f:
    f.write(output)
