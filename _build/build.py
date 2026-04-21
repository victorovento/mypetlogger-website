#!/usr/bin/env python3
"""Build localized HTML pages for the MyPetLogger marketing site.

For each locale module under _build/lang/, generates:
  /{code}/index.html
  /{code}/privacy/index.html
  /{code}/terms/index.html
  /{code}/age-rating/index.html

Each locale module must define:
  LANG, DIR, LABEL — html lang attr, ltr|rtl, native label
  HOME, PRIVACY, TERMS, AGE  — list[(en_str, tr_str)]
"""
from __future__ import annotations
import os, re, sys, importlib, pkgutil, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
LANG_DIR = pathlib.Path(__file__).resolve().parent / 'lang'

PAGE_FILES = {
    'HOME':    'index.html',
    'PRIVACY': 'privacy/index.html',
    'TERMS':   'terms/index.html',
    'AGE':     'age-rating/index.html',
}
PAGE_OUT = {
    'HOME':    'index.html',
    'PRIVACY': 'privacy/index.html',
    'TERMS':   'terms/index.html',
    'AGE':     'age-rating/index.html',
}

def load_locales():
    sys.path.insert(0, str(LANG_DIR.parent))
    locales = []
    for p in sorted(LANG_DIR.glob('*.py')):
        if p.name.startswith('_'): continue
        mod = importlib.import_module(f'lang.{p.stem}')
        importlib.reload(mod)
        locales.append((p.stem.replace('_', '-'), mod))
    return locales

def localize_paths(html: str, code: str) -> str:
    if not code:
        return html
    # Language-switcher links carry hreflang="..." — leave those absolute.
    re_pairs = [
        (r'href="/privacy/"(?!\s*hreflang)',     f'href="/{code}/privacy/"'),
        (r'href="/terms/"(?!\s*hreflang)',       f'href="/{code}/terms/"'),
        (r'href="/age-rating/"(?!\s*hreflang)',  f'href="/{code}/age-rating/"'),
        (r'href="/"(?!\s*hreflang)',             f'href="/{code}/"'),
    ]
    for pat, repl in re_pairs:
        html = re.sub(pat, repl, html)
    pairs = [
        ('href="/#features"',     f'href="/{code}/#features"'),
        ('href="/#pricing"',      f'href="/{code}/#pricing"'),
        ('href="/#faq"',          f'href="/{code}/#faq"'),
        ('href="/#download"',     f'href="/{code}/#download"'),
        ('https://mypetlogger.com/age-rating/', f'https://mypetlogger.com/{code}/age-rating/'),
        ('https://mypetlogger.com/privacy/',    f'https://mypetlogger.com/{code}/privacy/'),
        ('https://mypetlogger.com/terms/',      f'https://mypetlogger.com/{code}/terms/'),
        ('<link rel="canonical" href="https://mypetlogger.com/">',
         f'<link rel="canonical" href="https://mypetlogger.com/{code}/">'),
    ]
    for a, b in pairs:
        html = html.replace(a, b)
    return html

def set_lang_dir(html: str, lang: str, direction: str) -> str:
    html = re.sub(r'<html lang="[^"]*"(?: dir="[^"]*")?>',
                  f'<html lang="{lang}" dir="{direction}">', html, count=1)
    return html

def set_lang_label(html: str, label: str) -> str:
    return html.replace(
        '<span class="nav__lang__current">English</span>',
        f'<span class="nav__lang__current">{label}</span>',
    )

def apply_translations(html: str, pairs) -> str:
    for en, tr in pairs:
        if en in html:
            html = html.replace(en, tr)
        # silent no-op if string drifted; report in --verbose mode if needed
    return html

def build():
    locales = load_locales()
    written = []
    for code, mod in locales:
        out_dir = ROOT / code
        for key, src_rel in PAGE_FILES.items():
            src_path = ROOT / src_rel
            if not src_path.exists():
                continue
            html = src_path.read_text()
            html = set_lang_dir(html, mod.LANG, mod.DIR)
            html = set_lang_label(html, mod.LABEL)
            html = localize_paths(html, code)
            pairs = getattr(mod, key, [])
            html = apply_translations(html, pairs)
            out_path = out_dir / PAGE_OUT[key]
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(html)
            written.append(str(out_path.relative_to(ROOT)))
    print(f"Wrote {len(written)} files:")
    for w in written:
        print(' ', w)

if __name__ == '__main__':
    build()
