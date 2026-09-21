import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The section contains 4 articles. We need to extract them from the 'Education & Experience' grid.
# The section is id='services'

section_pattern = r'(<section class=\"services experience-3d-section\" id=\"services\">.*?</section>)'
match = re.search(section_pattern, html, flags=re.DOTALL)

if match:
    section_html = match.group(1)
    
    # Extract the 4 articles
    article_pattern = r'(<article class=\"experience-3d-card.*?</article>)'
    articles = re.findall(article_pattern, section_html, flags=re.DOTALL)
    
    if len(articles) >= 4:
        # Currently: 0: B.Tech, 1: Innovators, 2: CSI, 3: Owl AI
        new_articles = [articles[0], articles[3], articles[1], articles[2]]
        
        # We need to replace the inner content of the grid.
        grid_pattern = r'(<div class=\"services-container experience-3d-grid\">)(.*?)(</div>\s*</section>)'
        
        new_grid_content = '\n\n'.join(new_articles)
        
        new_section_html = re.sub(grid_pattern, r'\g<1>\n' + new_grid_content + r'\n\g<3>', section_html, flags=re.DOTALL)
        
        new_html = html.replace(section_html, new_section_html)
        
        with open('index.html', 'w', encoding='utf-8') as fOut:
            fOut.write(new_html)
        print('Blocks successfully reordered!')
    else:
        print(f'Found only {len(articles)} articles')
else:
    print('Section not found')
