# MyPetLogger — Marketing Site

Pure HTML / CSS / JS. No build step. Deploy to Netlify by dropping this folder in.

## Structure

```
/                     English home
/es/                  Spanish home
/privacy/             Privacy Policy (EN)
/terms/               Terms of Service (EN)
/es/privacy/          Privacy Policy (ES)
/es/terms/            Terms of Service (ES)
/assets/css/style.css
/assets/js/main.js
/assets/img/          Logo and future screenshots
netlify.toml          Headers + redirects
robots.txt
sitemap.xml
```

## Before going live

1. **Google Analytics** — replace `G-XXXXXXXXXX` in `index.html`, `es/index.html`,
   `privacy/index.html`, `terms/index.html`, `es/privacy/index.html`, `es/terms/index.html`
   with your real GA4 property ID.
2. **App Store URL** — replace `https://apps.apple.com/app/mypetlogger/` with the real
   App Store link once the app is live.
3. **Screenshots** — the hero and feature sections use placeholder phone frames.
   Drop PNG screenshots into `assets/img/` and replace the `.phone__screen--placeholder`
   blocks with `<img src="/assets/img/screenshot-XYZ.png">` inside the `.phone__screen`.
4. **Social handles** — confirm `twitter.com/mypetlogger` and `instagram.com/mypetlogger`
   work, or update the links in the footers.
5. **Open Graph image** — optional: replace `/assets/img/logo.png` references in the
   `og:image` meta tags with a 1200x630 social-card image.

## Deploy to Netlify

**Drag-and-drop:** drag the `mypetlogger-website` folder onto https://app.netlify.com/drop

**Git-based:** push this folder to a repo, then "Add new site" → "Import an existing project"
in Netlify. Build command: none. Publish directory: `.` (root).

**Custom domain:** in Netlify site settings → Domain management → add `mypetlogger.com`
and `www.mypetlogger.com`. Netlify provisions a free Let's Encrypt cert automatically.

## Design notes

- Colors are lifted from the app's Summary tab ambient gradient
  (`lavender / coral / blue` blooms over a lavender-washed white or deep indigo base).
- Font: Nunito (rounded sans) via Google Fonts.
- Dark mode is `prefers-color-scheme` driven, no toggle.
- Scroll reveals use IntersectionObserver; bloom backgrounds parallax with requestAnimationFrame.
- All animation respects `prefers-reduced-motion`.
