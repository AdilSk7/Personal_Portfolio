import re

def build():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # SECTION 02 HTML (4 Cards)
    section_02 = """
        <section class="services experience-3d-section" id="services">

            <div class="section-heading experience-heading">
                <p class="section-kicker">02 / CREDENTIALS</p>
                <h2 class="heading">Education & <span>Experience</span></h2>
                <p>Academic milestones, marketing outreach, and professional internships.</p>
            </div>

            <div class="services-container experience-3d-grid">

                <!-- 1. EDUCATION -->
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
                        <p>Pursuing undergraduation with a CGPA of 9.13. Focused on Data Structures, Algorithms, Software Engineering, and AI.</p>
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

                <!-- 2. CLUB -->
                <article class="experience-3d-card">
                    <div class="card-glow"></div>
                    <div class="card-top-line"></div>
                    <div class="experience-3d-content">
                        <div class="experience-3d-icon">
                            <i class="fa-solid fa-bullhorn"></i>
                            <span class="icon-orbit"></span>
                        </div>
                        <div class="experience-meta">
                            <span class="experience-type">EXPERIENCE</span>
                            <span class="experience-date">Oct 2023 - May 2024</span>
                        </div>
                        <span class="experience-company">Innovators Quest Club</span>
                        <h3>Marketing <span>Member</span></h3>
                        <p>Promoted events, managed outreach campaigns, and enhanced club engagement through targeted campus marketing initiatives.</p>
                        <div class="experience-tech-row">
                            <span>Marketing</span>
                            <span>Outreach</span>
                            <span>Leadership</span>
                        </div>
                        <div class="experience-action muted-action">
                            <span>Club</span>
                            <i class="fa-solid fa-users"></i>
                        </div>
                    </div>
                </article>

                <!-- 3. CLUB -->
                <article class="experience-3d-card">
                    <div class="card-glow"></div>
                    <div class="card-top-line"></div>
                    <div class="experience-3d-content">
                        <div class="experience-3d-icon">
                            <i class="fa-solid fa-chalkboard-user"></i>
                            <span class="icon-orbit"></span>
                        </div>
                        <div class="experience-meta">
                            <span class="experience-type">EXPERIENCE</span>
                            <span class="experience-date">Aug 2024 - May 2025</span>
                        </div>
                        <span class="experience-company">Computer Society of India (CSI)</span>
                        <h3>V-Guide <span>Member</span></h3>
                        <p>Assisted in coordinating technical workshops, guiding junior students, and fostering a collaborative programming community.</p>
                        <div class="experience-tech-row">
                            <span>Mentoring</span>
                            <span>Workshops</span>
                            <span>Community</span>
                        </div>
                        <div class="experience-action muted-action">
                            <span>Society</span>
                            <i class="fa-solid fa-users-gear"></i>
                        </div>
                    </div>
                </article>

                <!-- 4. INTERNSHIP -->
                <article class="experience-3d-card certificate-card">
                    <div class="card-glow"></div>
                    <div class="card-top-line"></div>
                    <div class="experience-3d-content">
                        <div class="experience-3d-icon">
                            <i class="fa-solid fa-laptop-code"></i>
                            <span class="icon-orbit"></span>
                        </div>
                        <div class="experience-meta">
                            <span class="experience-type">INTERNSHIP</span>
                            <span class="experience-date">Dec 2025 - Feb 2026</span>
                        </div>
                        <span class="experience-company">Owl AI (Overload Ware Labs)</span>
                        <h3>Front End Developer <span>Intern</span></h3>
                        <p>Remote virtual internship focused on developing responsive frontend interfaces, independently completing tasks within given deadlines.</p>
                        <div class="experience-tech-row">
                            <span>Frontend</span>
                            <span>Development</span>
                            <span>Remote</span>
                        </div>
                        <div class="experience-action muted-action">
                            <span>Internship</span>
                            <i class="fa-solid fa-briefcase"></i>
                        </div>
                    </div>
                </article>

            </div>
        </section>
"""

    # SECTION 05 HTML (6 Cards)
    section_05 = """
        <!-- ================= ACHIEVEMENTS ================= -->

        <section class="services experience-3d-section" id="achievements">
            <div class="section-heading experience-heading">
                <p class="section-kicker">05 / ACHIEVEMENTS</p>
                <h2 class="heading">Certifications & <span>Publications</span></h2>
                <p>Professional certifications, research papers, and technical project exhibitions.</p>
            </div>

            <div class="services-container experience-3d-grid">

                <!-- 1. CERT -->
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
                        </div>
                        <span class="experience-company">AWS</span>
                        <h3>Certified Cloud <span>Practitioner</span></h3>
                        <p>Demonstrated overall understanding of the AWS Cloud platform, covering basic cloud concepts and security.</p>
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

                <!-- 2. CERT -->
                <article class="experience-3d-card ai-card">
                    <div class="card-glow"></div>
                    <div class="card-top-line"></div>
                    <div class="experience-3d-content">
                        <div class="experience-3d-icon">
                            <i class="fa-brands fa-microsoft"></i>
                            <span class="icon-orbit"></span>
                        </div>
                        <div class="experience-meta">
                            <span class="experience-type">CERTIFICATION</span>
                            <span class="experience-date">Jun 2025</span>
                        </div>
                        <span class="experience-company">Microsoft</span>
                        <h3>Azure AI Engineer <span>Associate</span></h3>
                        <p>Successfully passed all requirements for Microsoft Certified: Azure AI Engineer Associate (Credential ID: FD91F95356940E82).</p>
                        <div class="experience-tech-row">
                            <span>Azure</span>
                            <span>AI Services</span>
                            <span>Engineering</span>
                        </div>
                        <div class="experience-action muted-action">
                            <span>Certification</span>
                            <i class="fa-solid fa-certificate"></i>
                        </div>
                    </div>
                </article>

                <!-- 3. CERT -->
                <article class="experience-3d-card">
                    <div class="card-glow"></div>
                    <div class="card-top-line"></div>
                    <div class="experience-3d-content">
                        <div class="experience-3d-icon">
                            <i class="fa-solid fa-database"></i>
                            <span class="icon-orbit"></span>
                        </div>
                        <div class="experience-meta">
                            <span class="experience-type">CERTIFICATION</span>
                            <span class="experience-date">Jul 2025</span>
                        </div>
                        <span class="experience-company">Oracle University</span>
                        <h3>OCI Gen AI <span>Professional</span></h3>
                        <p>Recognized as Oracle Certified Professional for Cloud Infrastructure 2025 Generative AI workloads and architecture.</p>
                        <div class="experience-tech-row">
                            <span>Oracle OCI</span>
                            <span>Gen A.I.</span>
                            <span>Cloud</span>
                        </div>
                        <div class="experience-action muted-action">
                            <span>Certification</span>
                            <i class="fa-solid fa-certificate"></i>
                        </div>
                    </div>
                </article>

                <!-- 4. CERT -->
                <article class="experience-3d-card internship-card">
                    <div class="card-glow"></div>
                    <div class="card-top-line"></div>
                    <div class="experience-3d-content">
                        <div class="experience-3d-icon">
                            <i class="fa-brands fa-js"></i>
                            <span class="icon-orbit"></span>
                        </div>
                        <div class="experience-meta">
                            <span class="experience-type">CERTIFICATION</span>
                            <span class="experience-date">May 2024</span>
                        </div>
                        <span class="experience-company">Cisco / OpenEDG</span>
                        <h3>JavaScript <span>Essentials 1 (JSE)</span></h3>
                        <p>Completed JavaScript language syntax basics, structural programming, and algorithm design through Cisco Networking Academy.</p>
                        <div class="experience-tech-row">
                            <span>JavaScript</span>
                            <span>Algorithms</span>
                            <span>Syntax</span>
                        </div>
                        <div class="experience-action muted-action">
                            <span>Certification</span>
                            <i class="fa-solid fa-certificate"></i>
                        </div>
                    </div>
                </article>

                <!-- 5. PUB -->
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
                        <p>Presented advanced techniques for real-time sensor data analysis and regression modeling to optimize solar energy capture.</p>
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

                <!-- 6. ACHI -->
                <article class="experience-3d-card">
                    <div class="card-glow"></div>
                    <div class="card-top-line"></div>
                    <div class="experience-3d-content">
                        <div class="experience-3d-icon">
                            <i class="fa-solid fa-trophy"></i>
                            <span class="icon-orbit"></span>
                        </div>
                        <div class="experience-meta">
                            <span class="experience-type">ACHIEVEMENT</span>
                        </div>
                        <span class="experience-company">VIKAS Expo</span>
                        <h3>Project <span>Exhibition</span></h3>
                        <p>Presented a cutting-edge "Hand Gesture-based Controlled Car" showcasing sensor integration, robotics, and embedded systems programming.</p>
                        <div class="experience-tech-row">
                            <span>Robotics</span>
                            <span>Sensors</span>
                            <span>Embedded</span>
                        </div>
                        <div class="experience-action muted-action">
                            <span>Exhibition</span>
                            <i class="fa-solid fa-medal"></i>
                        </div>
                    </div>
                </article>

            </div>
        </section>
"""

    # First, replace the existing services section (which has the older items)
    pattern_old_section = r'<section class="services experience-3d-section" id="services">.*?</section>'
    
    html = re.sub(pattern_old_section, section_02, html, flags=re.DOTALL)

    # Next, insert Section 05 right AFTER the portfolio section.
    # We find where portfolio section ends: `</section>\n\n\n        <!-- ================= CONTACT ================= -->`
    # Or just `</section>` after `id="portfolio"`.
    
    port_end_pattern = r'(<section class="portfolio projects-3d-section" id="portfolio">.*?</section>)'
    
    if "id=\"achievements\"" not in html: # Prevent duplicate runs
        html = re.sub(port_end_pattern, r'\1\n\n' + section_05, html, flags=re.DOTALL)


    # Finally update navigation to "Achievements" or keep "Credentials"
    html = html.replace('href="#services">Credentials</a>', 'href="#services">Experience</a>')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Files successfully generated.")


if __name__ == "__main__":
    build()
