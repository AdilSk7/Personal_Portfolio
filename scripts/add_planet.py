import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Add <a href="#certifications" ... 
# We'll inject it right after the planet-contact element.
target_str = """                <a href="#contact" class="about-planet planet-contact">
                    <div class="planet-circle">
                        <i class="fa-regular fa-envelope"></i>
                    </div>
                    <div class="planet-label">
                        <strong>Contact</strong>
                        <small>Get in touch</small>
                    </div>
                </a>"""

cert_str = """
                <a href="#certifications" class="about-planet planet-certifications">
                    <div class="planet-circle">
                        <i class="fa-solid fa-certificate"></i>
                    </div>
                    <div class="planet-label">
                        <strong>Certifications</strong>
                        <small>My achievements</small>
                    </div>
                </a>"""

idx = text.find(target_str)
if idx != -1:
    text = text[:idx + len(target_str)] + cert_str + text[idx + len(target_str):]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Injected into index.html")
else:
    print("Target string not found in index.html!")

# Now add CSS for planet-certifications to styles.css
css_str = """
.planet-certifications {
    left: 20%;
    top: -5%;
}

@media (max-width: 1200px) {
    .planet-certifications { left: 18%; top: -6%; }
}
@media (max-width: 1000px) {
    .planet-certifications { display: none; }
}

.planet-certifications .planet-circle {
    background:
        radial-gradient(circle at 30% 24%,
            #fff4e5 0%,
            #ff7382 10%,
            #e41b3c 28%,
            #8e071e 52%,
            #47020d 74%,
            #170003 100%) !important;

    border-color:
        rgba(255, 68, 93, 0.95) !important;

    box-shadow:
        inset -18px -20px 30px rgba(45, 0, 7, 0.8),
        inset 9px 7px 18px rgba(255, 175, 185, 0.22),
        0 0 16px rgba(230, 20, 50, 0.8),
        0 0 40px rgba(200, 10, 35, 0.45) !important;
}

.planet-certifications .planet-circle i {
    color: #ffd8df;
}
"""

with open('styles.css', 'r', encoding='utf-8') as f:
    css_text = f.read()

# Insert right after planet-contact class definitions (if any) or simply append to file.
css_text += css_str

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css_text)
print("Injected into styles.css")

