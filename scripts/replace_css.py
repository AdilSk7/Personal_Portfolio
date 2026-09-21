import re

new_css = """/* =========================================================
   PREMIUM PROFILE CARD — NEW DESIGN
   Only replaces the HERO profile-picture styling
========================================================= */

.home-img {
    position: relative;
    width: 450px;
    height: 540px;
    flex-shrink: 0;

    display: flex;
    align-items: center;
    justify-content: center;

    isolation: isolate;
}


/* -----------------------------------------
   Ambient glow behind profile
----------------------------------------- */

.home-img::before {
    content: "";
    position: absolute;
    width: 390px;
    height: 390px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(89, 178, 244, 0.20),
            rgba(124, 108, 255, 0.10) 45%,
            transparent 72%
        );

    filter: blur(35px);

    z-index: -2;

    animation: profileGlow 6s ease-in-out infinite;
}


/* -----------------------------------------
   Main Glass Profile Card
----------------------------------------- */

.profile-card {
    position: relative;

    width: 370px;
    height: 475px;

    padding: 7px;

    overflow: hidden;

    border-radius: 3rem;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.14),
            rgba(255,255,255,0.025)
        );

    border: 1px solid rgba(255,255,255,0.14);

    box-shadow:
        0 30px 80px rgba(0,0,0,0.45),
        0 0 50px rgba(89,178,244,0.08);

    backdrop-filter: blur(18px);

    transform: rotate(2deg);

    transition:
        transform 0.55s cubic-bezier(.22,1,.36,1),
        box-shadow 0.55s ease;

    z-index: 2;
}


/* Gradient border */

.profile-card::before {
    content: "";

    position: absolute;

    inset: 0;

    padding: 1.5px;

    border-radius: inherit;

    background:
        linear-gradient(
            135deg,
            rgba(89,178,244,0.9),
            rgba(89,178,244,0.15) 35%,
            rgba(124,108,255,0.15) 60%,
            rgba(124,108,255,0.9)
        );

    -webkit-mask:
        linear-gradient(#fff 0 0) content-box,
        linear-gradient(#fff 0 0);

    -webkit-mask-composite: xor;

    mask-composite: exclude;

    pointer-events: none;

    z-index: 5;
}


/* Inner dark surface */

.profile-card::after {
    content: "";

    position: absolute;

    inset: 7px;

    border-radius: 2.5rem;

    background:
        linear-gradient(
            180deg,
            rgba(5,10,20,0.05),
            rgba(5,10,20,0.15) 55%,
            rgba(5,10,20,0.65)
        );

    pointer-events: none;

    z-index: 2;
}


/* Hover */

.profile-card:hover {
    transform:
        rotate(0deg)
        translateY(-10px)
        scale(1.015);

    box-shadow:
        0 35px 90px rgba(0,0,0,0.5),
        0 0 55px rgba(89,178,244,0.16),
        0 0 90px rgba(124,108,255,0.10);
}


/* -----------------------------------------
   Profile Image
----------------------------------------- */

.profile-card img {
    position: relative;

    width: 100%;
    height: 100%;

    object-fit: cover;

    object-position: center top;

    border-radius: 2.45rem;

    transition:
        transform 0.7s cubic-bezier(.22,1,.36,1),
        filter 0.5s ease;

    z-index: 1;
}


/* Subtle image zoom */

.profile-card:hover img {
    transform: scale(1.035);

    filter:
        brightness(1.04)
        contrast(1.02);
}


/* -----------------------------------------
   Clean image gradient
----------------------------------------- */

.profile-card .profile-image-overlay {
    position: absolute;

    inset: 7px;

    border-radius: 2.5rem;

    background:
        linear-gradient(
            180deg,
            transparent 55%,
            rgba(5,9,18,0.08) 68%,
            rgba(5,9,18,0.55) 100%
        );

    pointer-events: none;

    z-index: 3;
}


/* -----------------------------------------
   Browser-style top dots
----------------------------------------- */

.profile-top {
    position: absolute;

    top: 1.7rem;
    left: 2rem;

    display: flex;

    gap: 0.65rem;

    z-index: 6;
}

.profile-top span {
    width: 0.75rem;
    height: 0.75rem;

    border-radius: 50%;

    background:
        rgba(255,255,255,0.55);

    box-shadow:
        0 0 8px rgba(255,255,255,0.08);
}


/* -----------------------------------------
   Elegant Neon Accent Line
----------------------------------------- */

.profile-card .profile-accent {
    position: absolute;

    left: 50%;
    bottom: 1.5rem;

    width: 80px;
    height: 3px;

    transform: translateX(-50%);

    border-radius: 999px;

    background:
        linear-gradient(
            90deg,
            var(--blue),
            var(--purple)
        );

    box-shadow:
        0 0 12px rgba(89,178,244,0.55),
        0 0 22px rgba(124,108,255,0.35);

    z-index: 6;
}


/* -----------------------------------------
   Floating Cards
----------------------------------------- */

.floating-card {
    position: absolute;

    z-index: 10;

    display: flex;
    align-items: center;

    gap: 1rem;

    padding: 1.15rem 1.35rem;

    min-width: 175px;

    border:
        1px solid rgba(255,255,255,0.12);

    border-radius: 1.5rem;

    background:
        linear-gradient(
            145deg,
            rgba(18,27,45,0.88),
            rgba(10,16,29,0.78)
        );

    box-shadow:
        0 20px 50px rgba(0,0,0,0.38),
        0 0 25px rgba(89,178,244,0.05);

    backdrop-filter: blur(20px);

    transition:
        transform 0.4s ease,
        border-color 0.4s ease,
        box-shadow 0.4s ease;

    animation:
        premiumFloat 5s ease-in-out infinite;
}


/* Floating card icon */

.floating-card i {
    display: flex;

    align-items: center;
    justify-content: center;

    width: 3.7rem;
    height: 3.7rem;

    flex-shrink: 0;

    border-radius: 1.1rem;

    color: var(--blue);

    background:
        linear-gradient(
            145deg,
            rgba(89,178,244,0.16),
            rgba(124,108,255,0.08)
        );

    box-shadow:
        inset 0 0 15px rgba(89,178,244,0.04);
}


/* Floating card text */

.floating-card strong {
    display: block;

    color: #ffffff;

    font-size: 1.15rem;

    font-weight: 800;

    white-space: nowrap;
}

.floating-card small {
    display: block;

    margin-top: 0.2rem;

    color: #7f8da5;

    font-size: 0.9rem;

    white-space: nowrap;
}


/* Left card */

.card-code {
    left: -2.5rem;
    bottom: 6.5rem;
}


/* Right card */

.card-ai {
    right: -2.5rem;
    top: 8rem;

    animation-delay: -2.5s;
}


/* Floating card hover */

.floating-card:hover {
    transform: translateY(-7px) scale(1.03);

    border-color:
        rgba(89,178,244,0.35);

    box-shadow:
        0 25px 55px rgba(0,0,0,0.42),
        0 0 25px rgba(89,178,244,0.10);
}


/* -----------------------------------------
   Background Tech Rings
   Much more subtle than the old rings
----------------------------------------- */

.profile-ring {
    position: absolute;

    border-radius: 50%;

    pointer-events: none;

    border:
        1px solid rgba(89,178,244,0.12);

    z-index: -1;
}

.ring-one {
    width: 470px;
    height: 470px;

    border-color:
        rgba(89,178,244,0.16);

    animation:
        premiumRing 25s linear infinite;
}

.ring-two {
    width: 535px;
    height: 535px;

    border:
        1px dashed rgba(124,108,255,0.12);

    animation:
        premiumRing 35s linear infinite reverse;
}


/* -----------------------------------------
   Animations
----------------------------------------- */

@keyframes premiumFloat {

    0%,
    100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-9px);
    }
}


@keyframes premiumRing {

    from {
        transform: rotate(0deg);
    }

    to {
        transform: rotate(360deg);
    }
}


@keyframes profileGlow {

    0%,
    100% {
        opacity: 0.7;
        transform: scale(0.95);
    }

    50% {
        opacity: 1;
        transform: scale(1.05);
    }
}


/* =========================================================
   RESPONSIVE PROFILE CARD
========================================================= */

@media (max-width: 1200px) {

    .home-img {
        width: 410px;
        height: 510px;
    }

    .profile-card {
        width: 340px;
        height: 445px;
    }

    .ring-one {
        width: 450px;
        height: 450px;
    }

    .ring-two {
        width: 510px;
        height: 510px;
    }
}


@media (max-width: 1000px) {

    .home-img {
        margin-top: 2rem;
    }

    .card-code {
        left: -1.5rem;
    }

    .card-ai {
        right: -1.5rem;
    }
}


@media (max-width: 600px) {

    .home-img {
        width: 320px;
        height: 410px;
    }

    .profile-card {
        width: 270px;
        height: 350px;

        border-radius: 2.5rem;
    }

    .profile-card img {
        border-radius: 2rem;
    }

    .ring-one {
        width: 340px;
        height: 340px;
    }

    .ring-two {
        width: 390px;
        height: 390px;
    }

    .floating-card {
        padding: 0.9rem 1rem;

        min-width: 145px;

        gap: 0.7rem;
    }

    .floating-card i {
        width: 3rem;
        height: 3rem;
    }

    .floating-card strong {
        font-size: 1rem;
    }

    .floating-card small {
        font-size: 0.78rem;
    }

    .card-code {
        left: -1rem;
        bottom: 4rem;
    }

    .card-ai {
        right: -1rem;
        top: 5rem;
    }
}


@media (max-width: 420px) {

    .home-img {
        width: 290px;
        height: 380px;
    }

    .profile-card {
        width: 245px;
        height: 325px;
    }

    .card-code {
        left: -0.5rem;
    }

    .card-ai {
        right: -0.5rem;
    }
}

"""

with open('styles.css', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace block from "PROFILE" to "ABOUT"
import re
new_text = re.sub(
    r'/\* =========================================================\s*PROFILE\s*========================================================= \*/.*?(?=/\* =========================================================\s*ABOUT\s*========================================================= \*/)',
    new_css + '\n\n\n',
    text,
    flags=re.DOTALL
)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("CSS updated successfully")
