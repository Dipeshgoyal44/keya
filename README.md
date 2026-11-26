# HybridAI website

Static, dependency-free rebuild of the HybridAI site (Home, Team, Platform, Careers, Contact).

- `python3 build.py` regenerates the HTML pages; styles in `assets/style.css`, behaviour in `assets/app.js`.
- Open `index.html` directly or serve the folder with any static server.
- Includes responsive layout, mobile menu, keyboard-accessible tabs, dark mode, form validation and scroll animations.
- Team photos are initials placeholders; drop real images into `assets/` and update `build.py`.

## Needs confirmation from HybridAI
- Email domains: contact page uses `hybrid.ai`, careers uses `hybridai.com` (`EMAIL_CONTACT` / `EMAIL_CAREERS` in `build.py`).
- Social profile URLs (`SOCIAL`) and team LinkedIn URLs (`LINKEDIN`) in `build.py`.
- "100 years domain expertise" figure after the leadership changes.
- Copy for the Optimize / Recommend / Orchestrate platform tabs, Privacy and Terms text, Blog posts.

## Deploy
Vercel: import the repo, framework preset "Other", leave build command empty (`vercel.json` sets it). Output is the repo root.
After editing `build.py`, run `python3 build.py` and commit the regenerated HTML.
