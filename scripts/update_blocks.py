import re

def update_blocks():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Experience Sections Replacement
    # Since there are 3 cards, let's redefine the inner grid.
    
    experience_new = """    <div class="services-container experience-3d-grid">

        <!-- ================= CERTIFICATION ================= -->
        <article class="experience-3d-card certificate-card">
            <div class="card-glow"></div>
            <div class="card-top-line"></div>
            <div class="experience-3d-content">
                <div class="experience-3d-icon">
                    <i class="fa-brands fa-aws"></i>
                    <span class="icon-orbit"></span>
                </div>
                <div class="experience-meta">
                    <span class="experience-type">CERTIFICATION</span>
                    <span class="experience-date">Amazon</span>
                </div>
                <span class="experience-company">AWS</span>
                <h3>Certified Cloud <span>Practitioner</span></h3>
                <p>
                    Demonstrated overall understanding of the AWS Cloud platform, covering basic cloud concepts and security.
                </p>
                <div class="experience-tech-row">
                    <span>Cloud</span>
                    <span>AWS</span>
                    <span>Security</span>
                </div>
                <div class="experience-action muted-action">
                    <span>Certification</span>
                    <i class="fa-solid fa-cloud"></i>
                </div>
            </div>
        </article>

        <!-- ================= EDUCATION ================= -->
        <article class="experience-3d-card ai-card">
            <div class="card-glow"></div>
            <div class="card-top-line"></div>
            <div class="experience-3d-content">
                <div class="experience-3d-icon">
                    <i class="fa-solid fa-graduation-cap"></i>
                    <span class="icon-orbit"></span>
                </div>
                <div class="experience-meta">
                    <span class="experience-type">EDUCATION</span>
                    <span class="experience-date">2022 - 2026</span>
                </div>
                <span class="experience-company">VIT-AP UNIVERSITY</span>
                <h3>B.Tech in Computer <span>Science & Engineering</span></h3>
                <p>
                    Pursuing undergraduation with a CGPA of 9.13. Focused on Data Structures, Algorithms, Software Engineering, and AI.
                </p>
                <div class="experience-tech-row">
                    <span>Data Structures</span>
                    <span>Algorithms</span>
                    <span>AI</span>
                </div>
                <div class="experience-action muted-action">
                    <span>University</span>
                    <i class="fa-solid fa-building-columns"></i>
                </div>
            </div>
        </article>

        <!-- ================= PUBLICATION ================= -->
        <article class="experience-3d-card internship-card">
            <div class="card-glow"></div>
            <div class="card-top-line"></div>
            <div class="experience-3d-content">
                <div class="experience-3d-icon">
                    <i class="fa-solid fa-book"></i>
                    <span class="icon-orbit"></span>
                </div>
                <div class="experience-meta">
                    <span class="experience-type">PUBLICATION</span>
                    <span class="experience-date">IEEE Xplore</span>
                </div>
                <span class="experience-company">RESEARCH</span>
                <h3>Beyond Daylight <span>Solar Panel Performance</span></h3>
                <p>
                    Presented advanced techniques for real-time sensor data analysis and regression modeling to optimize solar energy capture.
                </p>
                <div class="experience-tech-row">
                    <span>Data Analysis</span>
                    <span>Regression</span>
                    <span>Sensors</span>
                </div>
                <div class="experience-action muted-action">
                    <span>Research Paper</span>
                    <i class="fa-solid fa-scroll"></i>
                </div>
            </div>
        </article>

    </div>
</section>"""

    # Use regex to replace everything between <div class="services-container experience-3d-grid"> and </section> for Experience
    html = re.sub(r'<div class="services-container experience-3d-grid">.*?</section>', experience_new, html, flags=re.DOTALL)


    # 2. Tech Stack section replacement. It has a 'tech-world' container.
    new_tech = """    <div class="tech-world" id="tech-world">
        <div class="tech-glow glow-left"></div>
        <div class="tech-glow glow-right"></div>

        <div class="tech-ball" data-tech="React" data-color="#61dafb">
            <div class="ball-inner"><i class="fa-brands fa-react"></i><span>React</span></div>
        </div>
        <div class="tech-ball" data-tech="Node.js" data-color="#68a063">
            <div class="ball-inner"><i class="fa-brands fa-node-js"></i><span>Node.js</span></div>
        </div>
        <div class="tech-ball" data-tech="Python" data-color="#3776ab">
            <div class="ball-inner"><i class="fa-brands fa-python"></i><span>Python</span></div>
        </div>
        <div class="tech-ball" data-tech="Java" data-color="#e76f00">
            <div class="ball-inner"><i class="fa-brands fa-java"></i><span>Java</span></div>
        </div>
        <div class="tech-ball" data-tech="TensorFlow" data-color="#ff6f00">
            <div class="ball-inner"><i class="fa-solid fa-network-wired"></i><span>TensorFlow</span></div>
        </div>
        <div class="tech-ball" data-tech="MongoDB" data-color="#47a248">
            <div class="ball-inner"><i class="fa-solid fa-leaf"></i><span>MongoDB</span></div>
        </div>
        <div class="tech-ball" data-tech="Express.js" data-color="#ffffff">
            <div class="ball-inner"><strong>ex</strong><span>Express.js</span></div>
        </div>
        <div class="tech-ball" data-tech="Firebase" data-color="#ffca28">
            <div class="ball-inner"><i class="fa-solid fa-fire"></i><span>Firebase</span></div>
        </div>
        <div class="tech-ball" data-tech="MySQL" data-color="#00758f">
            <div class="ball-inner"><i class="fa-solid fa-database"></i><span>MySQL</span></div>
        </div>
        <div class="tech-ball" data-tech="Docker" data-color="#2496ed">
            <div class="ball-inner"><i class="fa-brands fa-docker"></i><span>Docker</span></div>
        </div>
        <div class="tech-ball" data-tech="AI / ML" data-color="#a78bfa">
            <div class="ball-inner"><i class="fa-solid fa-brain"></i><span>AI / ML</span></div>
        </div>
        <div class="tech-ball" data-tech="GitHub" data-color="#ffffff">
            <div class="ball-inner"><i class="fa-brands fa-github"></i><span>GitHub</span></div>
        </div>

        <div class="tech-info">
            <div class="tech-info-icon"><i class="fa-solid fa-code"></i></div>
            <div>
                <h3>I love building with technology.</h3>
                <p>From modern web interfaces to scalable backend APIs and intelligent machine learning applications.</p>
            </div>
        </div>
    </div>
</section>"""
    html = re.sub(r'<div class="tech-world" id="tech-world">.*?</section>', new_tech, html, flags=re.DOTALL)


    # 3. Projects section replacement.
    new_projects = """    <div class="portfolio-container projects-3d-grid">

        <!-- ================= PROJECT 01 ================= -->
        <article class="portfolio-box project-3d-card featured-project">
            <div class="project-card-glow"></div>
            <div class="project-card-shine"></div>
            <div class="featured-label"><i class="fa-solid fa-star"></i> Featured Project</div>
            <div class="project-image-wrap">
                <img src="assets/1.jpg" alt="CareerLens AI" loading="lazy">
                <div class="image-overlay"></div>
            </div>
            <div class="project-content">
                <div class="project-top">
                    <div class="project-number">01</div>
                    <span class="project-category">AI / WEB</span>
                </div>
                <div class="project-tags">
                    <span>React</span>
                    <span>FastAPI</span>
                    <span>Gemini / Groq</span>
                </div>
                <h3>CareerLens AI</h3>
                <p>
                    AI-driven platform that matches candidates against job descriptions, identifies skill gaps, creates personalized roadmaps, and conducts AI mock interviews.
                </p>
                <a href="https://github.com/AdilSk7" target="_blank" rel="noopener noreferrer" class="project-link">
                    <span>View GitHub</span>
                    <i class="fa-solid fa-arrow-up-right-from-square"></i>
                </a>
            </div>
        </article>

        <!-- ================= PROJECT 02 ================= -->
        <article class="portfolio-box project-3d-card">
            <div class="project-card-glow"></div>
            <div class="project-card-shine"></div>
            <div class="project-image-wrap">
                <img src="assets/2.jpg" alt="BookMyTrack" loading="lazy">
                <div class="image-overlay"></div>
            </div>
            <div class="project-content">
                <div class="project-top">
                    <div class="project-number">02</div>
                    <span class="project-category">FULL STACK</span>
                </div>
                <div class="project-tags">
                    <span>Node.js</span>
                    <span>Express</span>
                    <span>MongoDB</span>
                </div>
                <h3>BookMyTrack</h3>
                <p>
                    Developed a robust railway reservation system featuring smart seat allocation, elderly priority booking, authentications, and role-based access.
                </p>
                <a href="https://github.com/AdilSk7" target="_blank" rel="noopener noreferrer" class="project-link">
                    <span>View GitHub</span>
                    <i class="fa-solid fa-arrow-up-right-from-square"></i>
                </a>
            </div>
        </article>

        <!-- ================= PROJECT 03 ================= -->
        <article class="portfolio-box project-3d-card">
            <div class="project-card-glow"></div>
            <div class="project-card-shine"></div>
            <div class="featured-label"><i class="fa-solid fa-star"></i> Featured Project</div>
            <div class="project-image-wrap">
                <img src="assets/3.jpg" alt="PropertyAI" loading="lazy">
                <div class="image-overlay"></div>
            </div>
            <div class="project-content">
                <div class="project-top">
                    <div class="project-number">03</div>
                    <span class="project-category">WEB APP</span>
                </div>
                <div class="project-tags">
                    <span>React</span>
                    <span>Firebase</span>
                    <span>Firestore</span>
                </div>
                <h3>PropertyAI</h3>
                <p>
                    Smart property discovery platform utilizing AI for matching, location-based filtering, real-time notifications, and a comprehensive admin dashboard.
                </p>
                <a href="https://github.com/AdilSk7" target="_blank" rel="noopener noreferrer" class="project-link">
                    <span>View GitHub</span>
                    <i class="fa-solid fa-arrow-up-right-from-square"></i>
                </a>
            </div>
        </article>

        <!-- ================= PROJECT 04 ================= -->
        <article class="portfolio-box project-3d-card">
            <div class="project-card-glow"></div>
            <div class="project-card-shine"></div>
            <div class="project-image-wrap">
                <img src="assets/4.jpg" alt="PDF Q&A RAG System" loading="lazy">
                <div class="image-overlay"></div>
            </div>
            <div class="project-content">
                <div class="project-top">
                    <div class="project-number">04</div>
                    <span class="project-category">DATA / ML</span>
                </div>
                <div class="project-tags">
                    <span>Python</span>
                    <span>GenAI</span>
                    <span>ChromaDB</span>
                </div>
                <h3>PDF Q&A RAG System</h3>
                <p>
                    A document intelligence model querying PDFs using Retrieval-Augmented Generation, chunking, embeddings, caching, and integrated LLMs for precise contextual answers.
                </p>
                <a href="https://github.com/AdilSk7" target="_blank" rel="noopener noreferrer" class="project-link">
                    <span>View GitHub</span>
                    <i class="fa-solid fa-arrow-up-right-from-square"></i>
                </a>
            </div>
        </article>

        <!-- ================= PROJECT 05 ================= -->
        <article class="portfolio-box project-3d-card">
            <div class="project-card-glow"></div>
            <div class="project-card-shine"></div>
            <div class="project-image-wrap">
                <img src="assets/5.jpg" alt="Cardiovascular Disease Prediction" loading="lazy">
                <div class="image-overlay"></div>
            </div>
            <div class="project-content">
                <div class="project-top">
                    <div class="project-number">05</div>
                    <span class="project-category">DEEP LEARNING</span>
                </div>
                <div class="project-tags">
                    <span>CNN</span>
                    <span>VGG16</span>
                    <span>TensorFlow</span>
                </div>
                <h3>ECG Cardiac Analysis</h3>
                <p>
                    Built Deep Learning architectures classifying ECG recordings for cardiovascular disease prediction, using hyperparameter optimization and GridSearchCV.
                </p>
                <a href="https://github.com/AdilSk7" target="_blank" rel="noopener noreferrer" class="project-link">
                    <span>View GitHub</span>
                    <i class="fa-solid fa-arrow-up-right-from-square"></i>
                </a>
            </div>
        </article>

        <!-- ================= PROJECT 06 ================= -->
        <article class="portfolio-box project-3d-card">
            <div class="project-card-glow"></div>
            <div class="project-card-shine"></div>
            <div class="project-image-wrap">
                <img src="assets/6.jpg" alt="Brain Tumor Detection" loading="lazy">
                <div class="image-overlay"></div>
            </div>
            <div class="project-content">
                <div class="project-top">
                    <div class="project-number">06</div>
                    <span class="project-category">AI / WEB</span>
                </div>
                <div class="project-tags">
                    <span>Flask</span>
                    <span>Xception</span>
                    <span>TensorFlow</span>
                </div>
                <h3>Brain Tumor Detection</h3>
                <p>
                    A web application that authenticates and accepts MRI images, utilizing a trained model to output brain tumor classifications and confidence scores.
                </p>
                <a href="https://github.com/AdilSk7" target="_blank" rel="noopener noreferrer" class="project-link">
                    <span>View GitHub</span>
                    <i class="fa-solid fa-arrow-up-right-from-square"></i>
                </a>
            </div>
        </article>

    </div>
</section>"""
    html = re.sub(r'<div class="portfolio-container projects-3d-grid">.*?</section>', new_projects, html, flags=re.DOTALL)


    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Blocks updated successfully!")

if __name__ == "__main__":
    update_blocks()
