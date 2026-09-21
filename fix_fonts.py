import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

def add_style(match):
    content = match.group(0)
    # Target all <p> in this section except the section switcher/kicker
    # Also handle if they were already targeted
    content = content.replace('<p>', '<p style="font-size: 1.85rem !important; line-height: 1.9 !important; margin-bottom: 2rem !important; color: #f7f9fc !important;">')
    return content

text = re.sub(r'(<div class="about-content about-modern-content">.*?<div class="about-stats">)', add_style, text, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Styles injected inline successfully!')
