import re

def update_index_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    replacements = [
        # Titles & Meta
        ('Ajit Kumar — Software Developer portfolio', 'Shaik Adil — Software Developer portfolio'),
        ('Ajit Kumar | Software Developer', 'Shaik Adil | Software Developer'),
        
        # AI Panel
        ('Ask me about Ajit', 'Ask me about Adil'),
        ("Hi! 👋 I'm Ajit's Portfolio AI.", "Hi! 👋 I'm Adil's Portfolio AI."),
        ('Tell me about Ajit', 'Tell me about Adil'),
        ("What are Ajit's skills?", "What are Adil's skills?"),
        ('How can I contact Ajit?', 'How can I contact Adil?'),
        ('About Ajit', 'About Adil'),
        
        # Logos
        ('AJ<span>.</span>', 'SA<span>.</span>'),
        
        # Hero Section
        ("Hello, I'm", "Hello, I'm"),
        ('Ajit <span>Kumar</span>', 'Shaik <span>Adil</span>'),
        ('Software Developer focused on building modern full-stack\\s+applications, AI-powered solutions and interactive digital\\s+experiences using Java, JavaScript, React, Node.js and AI/ML.',
         'A passionate Computer Science student and developer focused on building modern web applications, intelligent deep learning solutions, and robust backend systems.'),
        
        # Socials
        ('https://github.com/Ajitak8096', 'https://github.com/AdilSk7'),
        ('https://www.linkedin.com/in/ajit-kumar-ak8096', 'https://www.linkedin.com/in/shaik-adil-sk2344/'),
        
        # Alt Text
        ('Ajit Kumar - Software Developer', 'Shaik Adil - Software Developer'),
        
        # About Section
        ("I'm a Computer Science graduate who enjoys building\\s+practical software that combines clean interfaces,\\s+reliable backend systems and intelligent features.",
         "I'm a B.Tech Computer Science student at VIT-AP University. I build practical software that combines clean interfaces, reliable backend systems, and AI-powered solutions."),
        ("My work spans full-stack development, AI/ML,\\s+data analysis and interactive web experiences.",
         "My work spans full-stack development, deep learning, RAG applications, and interactive digital experiences."),
        ("I enjoy solving real problems, learning new technologies\\s+and turning ideas into projects that are useful,\\s+measurable and easy to use.",
         "I enjoy solving real problems, learning new paradigms, and turning ambitious concepts into maintainable software architecture using modern frameworks."),
        
        # Stats
        ('<strong>5\\+</strong>\\s+<span>Projects</span>', '<strong>6+</strong>\n                    <span>Projects</span>'),
        ('<strong>10\\+</strong>\\s+<span>Technologies</span>', '<strong>12+</strong>\n                    <span>Technologies</span>'),
        ('<strong>3\\+</strong>\\s+<span>Internships</span>', '<strong>9.1+</strong>\n                    <span>CGPA</span>'),

        # Contact section
        ('ak8096909@gmail.com', 'adilshaik2004@gmail.com'),
        ('github.com/Ajitak8096', 'github.com/AdilSk7'),
        
        # Footer
        ('Ajit Kumar', 'Shaik Adil'),
        ('© 2026 Ajit Kumar.', '© 2026 Shaik Adil.')
    ]
    
    for old, new in replacements:
        content = re.sub(old, new, content)

    # Note: Experience, Tech Stack, and Projects blocks are large.
    # We will replace them in a combined block replacement strategy here.
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Updated easy strings in index.html")

def update_main_js():
    with open('main.js', 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = content.replace('const GITHUB_USERNAME = "Ajitak8096";', 'const GITHUB_USERNAME = "AdilSk7";')
    content = content.replace("mailto:ajitkumar8096@gmail.com", "mailto:adilshaik2004@gmail.com")
    content = content.replace("'Hello Ajit,'", "'Hello Adil,'")
    
    # Typed JS
    content = content.replace(
        "'Full-Stack Applications',\n\n                'AI-Powered Solutions',\n\n                'Modern Web Experiences',\n\n                'Scalable Digital Products'",
        "'Full-Stack Web Applications',\n\n                'Deep Learning Models',\n\n                'Intelligent AI Solutions',\n\n                'Scalable Backend Systems'"
    )
    
    with open('main.js', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Updated main.js")

if __name__ == "__main__":
    update_index_html()
    update_main_js()
