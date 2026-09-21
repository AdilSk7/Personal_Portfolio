import re

def update_main():
    with open('main.js', 'r', encoding='utf-8') as f:
        js = f.read()

    js = js.replace('TensorFlow, GenAI, NLP, RAG, CNNs, GitHub, Docker, and Linux', 'HTML, CSS, JavaScript, Postman, GenAI, NLP, RAG, CNNs, GitHub, and Linux')
    js = js.replace('TensorFlow, GenAI, NLP', 'HTML, CSS, JavaScript, Postman, GenAI, NLP')
    js = js.replace('including Scikit-learn and TensorFlow', 'including HTML, CSS, JavaScript, and Scikit-learn')

    with open('main.js', 'w', encoding='utf-8') as f:
        f.write(js)

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove TensorFlow
    html = re.sub(r'\s*<div class="tech-ball" data-tech="TensorFlow".*?</div>\s*</div>', '', html, flags=re.DOTALL)
    # Remove Firebase
    html = re.sub(r'\s*<div class="tech-ball" data-tech="Firebase".*?</div>\s*</div>', '', html, flags=re.DOTALL)
    # Remove Docker
    html = re.sub(r'\s*<div class="tech-ball" data-tech="Docker".*?</div>\s*</div>', '', html, flags=re.DOTALL)

    # Add new balls 
    new_balls = """
                <div class="tech-ball" data-tech="HTML5" data-color="#e34f26">
                    <div class="ball-inner"><i class="fa-brands fa-html5"></i><span>HTML</span></div>
                </div>
                <div class="tech-ball" data-tech="CSS3" data-color="#1572b6">
                    <div class="ball-inner"><i class="fa-brands fa-css3-alt"></i><span>CSS</span></div>
                </div>
                <div class="tech-ball" data-tech="JavaScript" data-color="#f7df1e">
                    <div class="ball-inner"><i class="fa-brands fa-js"></i><span>JavaScript</span></div>
                </div>
                <div class="tech-ball" data-tech="Postman" data-color="#ef5b25">
                    <div class="ball-inner"><strong>PM</strong><span>Postman</span></div>
                </div>
"""

    if "fa-html5" not in html:
        html = html.replace('<div class="tech-ball" data-tech="GitHub"', new_balls + '                <div class="tech-ball" data-tech="GitHub"')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    update_main()
    update_index()
