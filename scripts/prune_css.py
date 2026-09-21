import re

with open('styles.css') as f:
    text = f.read()

# I want to delete the lines containing these classes and their blocks from the end of the file.
# The user's new CSS also has responsive queries BUT they are safely above the global RESPONSIVE block, Or we can just let Python parse them out of the global RESPONSIVE block at the end.
# Actually, the user's new CSS was injected before ABOUT, meaning the global RESPONSIVE block is beneath it.

# Let's cleanly remove ONLY the specific classes from the global RESPONSIVE block:
# We find the start of the global responsive block
responsive_start = text.find('/* =========================================================\n   RESPONSIVE')

if responsive_start != -1:
    before = text[:responsive_start]
    after = text[responsive_start:]
    
    # We remove these classes from `after` block
    targets = [
        r'\.home-img\s*\{[^}]*\}',
        r'\.profile-card\s*\{[^}]*\}',
        r'\.profile-card img\s*\{[^}]*\}',
        r'\.ring-one\s*\{[^}]*\}',
        r'\.ring-two\s*\{[^}]*\}',
        r'\.floating-card.*?\s*\{[^}]*\}',
        r'\.card-ai\s*\{[^}]*\}',
        r'\.card-code\s*\{[^}]*\}',
        r'\.profile-top\s*\{[^}]*\}',
        r'\.profile-top span\s*\{[^}]*\}',
        r'\.profile-accent\s*\{[^}]*\}',
        r'\.profile-image-overlay\s*\{[^}]*\}',
    ]
    
    for t in targets:
        after = re.sub(t, '', after, flags=re.DOTALL)
        
    text = before + after

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(text)

print("Old responsive blocks pruned successfully")
