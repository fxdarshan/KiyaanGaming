"""Build the draft preview site into preview/.

Run from the repository root:  python3 tools/build_preview.py
Edit GAMES below to change the games; styles live in preview/styles.css.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / 'preview'
EMAIL = 'info@kiyaangaming.com'

# Titles and artwork are placeholders until the real games are added.
GAMES = [
    {'slug': 'moonlit-peaks', 'title': 'Moonlit Peaks', 'thumb': 'thumb-1-moonlit-peaks.jpg',
     'status': 'Playable demo', 'demo': True},
    {'slug': 'desert-dusk', 'title': 'Desert Dusk', 'thumb': 'thumb-2-desert-dusk.jpg',
     'status': 'Concept', 'demo': False},
    {'slug': 'deep-sea', 'title': 'Deep Sea', 'thumb': 'thumb-3-deep-sea.jpg',
     'status': 'Concept', 'demo': False},
    {'slug': 'night-forest', 'title': 'Night Forest', 'thumb': 'thumb-4-night-forest.jpg',
     'status': 'Concept', 'demo': False},
    {'slug': 'ember-peak', 'title': 'Ember Peak', 'thumb': 'thumb-5-ember-peak.jpg',
     'status': 'Coming soon', 'demo': False},
]
TAGLINE = '[One line on the theme and the main feature of this game.]'

PLAY = ('<svg aria-hidden="true" width="14" height="14" viewBox="0 0 14 14" fill="currentColor">'
        '<path d="M2 1.2v11.6L12.4 7z"/></svg>')
ARROW = ('<svg aria-hidden="true" width="14" height="14" viewBox="0 0 14 14" fill="none" '
         'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
         '<path d="M2 7h10M8 3l4 4-4 4"/></svg>')


def layout(title, body, root='', active='', script=False):
    def nav(label, href, key):
        current = ' aria-current="page"' if key == active else ''
        return f'<a href="{root}{href}"{current}>{label}</a>'

    js = f'\n<script src="{root}site.js"></script>' if script else ''
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title} | Kiyaan Gaming (draft preview)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}styles.css">
</head>
<body>
<header class="site-header">
<div class="wrap">
<a class="brand" href="{root}index.html"><span class="mark" aria-hidden="true"></span><b>KIYAAN</b><span class="sub">GAMING</span></a>
<nav class="nav" aria-label="Main">
{nav('Games', 'games.html', 'games')}
{nav('Studio', 'studio.html', 'studio')}
{nav('Contact', 'contact.html', 'contact')}
</nav>
</div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
<div class="wrap">
<div class="about">
<p>Kiyaan Gaming creates slot games, art and animation. We do not operate gambling services.</p>
<p>Draft preview. Game titles, artwork and some text are placeholders.</p>
<p>© 2026 Kiyaan Gaming. All rights reserved.</p>
</div>
<nav class="footer-nav" aria-label="Footer">
<a href="{root}games.html">Games</a>
<a href="{root}studio.html">Studio</a>
<a href="{root}contact.html">Contact</a>
<a href="{root}privacy.html">Privacy Policy</a>
</nav>
</div>
</footer>{js}
</body>
</html>
"""


def card(game, root='', featured=False):
    cls = 'game-card featured' if featured else 'game-card'
    return f"""<a class="{cls}" href="{root}games/{game['slug']}.html">
<img src="{root}media/{game['thumb']}" alt="Placeholder artwork for {game['title']}" loading="lazy">
<span class="meta"><span class="name">{game['title']}</span><span class="status">{game['status']}</span></span>
</a>"""


def cta(root=''):
    return f"""<section class="cta wrap">
<div class="cta-box">
<div>
<h2>Interested in a game, or a production partner?</h2>
<p>We reply to every enquiry.</p>
</div>
<a class="btn" href="{root}contact.html">Get in touch</a>
</div>
</section>"""


def home():
    top = GAMES[0]
    cards = '\n'.join(card(g, featured=(g is top)) for g in GAMES)
    return layout('Home', f"""<section class="hero wrap">
<div class="hero-banner">
<img src="media/hero-moonlit-peaks.jpg" alt="Placeholder artwork for {top['title']}">
<p class="eyebrow">Featured game</p>
<h1>{top['title']}</h1>
<p class="lede">{TAGLINE}</p>
<a class="btn" href="games/{top['slug']}.html#demo">{PLAY}Play demo</a>
</div>
</section>

<section class="section wrap" id="games">
<div class="section-head">
<h2>Games</h2>
<a class="arrow-link quiet" href="games.html">All games {ARROW}</a>
</div>
<div class="games-grid five">
{cards}
</div>
</section>

<section class="band">
<div class="split wrap">
<h2>A studio built around slot games.</h2>
<div class="stack">
<p>Kiyaan Gaming creates original slot games. Our games are available for licensing, and our team is available to studios worldwide as a production partner.</p>
<a class="arrow-link" href="studio.html">About the studio {ARROW}</a>
</div>
</div>
</section>

{cta()}""")


def games():
    cards = '\n'.join(card(g, featured=g['demo']) for g in GAMES)
    return layout('Games', f"""<section class="page-head wrap">
<h1>Games</h1>
<p class="lede">Original slot games designed and built by Kiyaan Gaming. Every game is available for licensing or acquisition.</p>
</section>

<section class="wrap" style="padding-bottom: clamp(64px, 6.8vw, 96px)">
<div class="games-grid five">
{cards}
</div>
</section>

{cta()}""", active='games')


def game_page(game):
    root = '../'
    others = '\n'.join(card(g, root) for g in GAMES if g is not game)
    tag_cls = 'tag live' if game['demo'] else 'tag'
    demo_btn = f'<a class="btn" href="#demo">{PLAY}Play demo</a>' if game['demo'] else ''
    enquire_cls = 'arrow-link' if game['demo'] else 'btn'
    enquire_tail = f' {ARROW}' if game['demo'] else ''
    demo = f"""
<section class="wrap" id="demo" style="padding-bottom: clamp(48px, 5vw, 72px)">
<div class="section-head"><h2>Demo</h2></div>
<div class="demo-panel">
<strong>The playable demo will load here.</strong>
<span>Free demo. No real money, no wagering.</span>
</div>
</section>
""" if game['demo'] else ''
    return layout(game['title'], f"""<div class="wrap">
<p class="crumbs"><a href="{root}games.html">Games</a> / {game['title']}</p>
<section class="game-detail">
<div class="art"><img src="{root}media/{game['thumb']}" alt="Placeholder artwork for {game['title']}"></div>
<div class="info">
<span class="{tag_cls}">{game['status']}</span>
<h1>{game['title']}</h1>
<p class="lede">{TAGLINE}</p>
<dl class="facts">
<dt>Type</dt><dd>Video slot</dd>
<dt>Layout</dt><dd>[Reels and rows]</dd>
<dt>Main feature</dt><dd>[Feature name]</dd>
<dt>Availability</dt><dd>Licensing or acquisition</dd>
</dl>
<div class="actions">
{demo_btn}
<a class="{enquire_cls}" href="{root}contact.html?game={game['slug']}">Enquire about this game{enquire_tail}</a>
</div>
<p class="note">Placeholder title and artwork.</p>
</div>
</section>
</div>
{demo}
<section class="band">
<div class="section wrap">
<div class="section-head">
<h2>More games</h2>
<a class="arrow-link quiet" href="{root}games.html">All games {ARROW}</a>
</div>
<div class="games-grid">
{others}
</div>
</div>
</section>""", root=root, active='games')


def studio():
    return layout('Studio', f"""<section class="page-head wrap">
<h1>A specialist studio for slot games.</h1>
<p class="lede">Kiyaan Gaming is a slot game studio based in India. We create original slot games, and we offer our team to game studios around the world as a production partner.</p>
</section>

<section class="band">
<div class="block wrap">
<h2>What we do</h2>
<div class="cols">
<div>
<h3>Original games</h3>
<p>We design and build our own slot games, from the first idea to a playable prototype. Each game on this site is available for licensing or acquisition.</p>
</div>
<div>
<h3>Production partner</h3>
<p>Studios can bring us in to produce a complete game package or to add capacity to their own team. We deliver game art and Spine 2D animation in organised files that are ready for development.</p>
</div>
</div>
</div>
</section>

<section class="band">
<div class="block wrap">
<h2>How we work</h2>
<ol class="steps">
<li><span class="num">01</span><h3>Brief</h3><p>We learn your theme, audience, market and technical requirements.</p></li>
<li><span class="num">02</span><h3>Concept and art</h3><p>We develop the look of the game and agree it with you before animation begins.</p></li>
<li><span class="num">03</span><h3>Animation</h3><p>We bring the approved art to life and review it with you in stages.</p></li>
<li><span class="num">04</span><h3>Handoff</h3><p>We deliver files your developers can use straight away, and stay available while they integrate them.</p></li>
</ol>
</div>
</section>

<section class="band">
<div class="block wrap">
<h2>Leadership</h2>
<div class="prose">
<p>Kiyaan Gaming is led by senior specialists in slot art direction and animation. Experienced leadership oversees every project, from the first brief to the final delivery.</p>
<p>We focus on slot games only, so the whole team understands how a slot is designed, animated and built.</p>
</div>
</div>
</section>

<section class="band">
<div class="block wrap">
<h2>Where we are going</h2>
<ol class="steps">
<li><span class="num">Today</span><h3>Games and production</h3><p>Original slot games, and art and animation production for partner studios.</p></li>
<li><span class="num">Next</span><h3>Co-development</h3><p>Building slot games together with partner studios.</p></li>
<li><span class="num">Later</span><h3>Our own library</h3><p>A growing library of Kiyaan slot games and brands.</p></li>
</ol>
</div>
</section>

<div style="padding-top: clamp(24px, 3vw, 40px)">
{cta()}
</div>""", active='studio')


def contact():
    options = '\n'.join(f'<option value="{g["slug"]}">{g["title"]}</option>' for g in GAMES)
    return layout('Contact', f"""<section class="page-head wrap">
<h1>Get in touch</h1>
<p class="lede">Tell us about your project, or ask about one of our games. We reply to every enquiry.</p>
</section>

<section class="wrap">
<div class="contact-grid">
<form id="enquiry-form" novalidate>
<div class="row">
<div class="field"><label for="name">Name</label><input id="name" name="name" type="text" autocomplete="name" required></div>
<div class="field"><label for="company">Company</label><input id="company" name="company" type="text" autocomplete="organization"></div>
</div>
<div class="field"><label for="email">Work email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
<div class="row">
<div class="field"><label for="interest">I am interested in</label>
<select id="interest" name="interest">
<option value="production">Art and animation production</option>
<option value="game">Licensing or buying a game</option>
<option value="partnership">Partnership or investment</option>
<option value="other">Something else</option>
</select></div>
<div class="field"><label for="game">Game (optional)</label>
<select id="game" name="game">
<option value="">No specific game</option>
{options}
</select></div>
</div>
<div class="field"><label for="message">Message</label><textarea id="message" name="message" required></textarea></div>
<button class="btn" type="submit">Send enquiry</button>
<p class="form-status" id="form-status" role="status" tabindex="-1" hidden>This is a draft preview, so the form is not connected yet and nothing was sent. Please email <a href="mailto:{EMAIL}">{EMAIL}</a> instead.</p>
</form>
<aside>
<div><h2>Email</h2><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<div><h2>Studio</h2><p>Kiyaan Gaming Studio Team<br>[City], India</p></div>
</aside>
</div>
</section>""", active='contact', script=True)


def privacy():
    return layout('Privacy Policy', f"""<section class="page-head wrap">
<h1>Privacy Policy</h1>
<p class="lede">The full privacy policy will be added here before the site launches.</p>
</section>
<section class="wrap" style="padding-bottom: clamp(64px, 6.8vw, 96px)">
<div class="prose">
<p>This draft preview does not collect or store any personal information. The contact form is not connected and does not send anything.</p>
<p>Questions: <a href="mailto:{EMAIL}" style="color: var(--accent)">{EMAIL}</a></p>
</div>
</section>""")


def main():
    (OUT / 'games').mkdir(parents=True, exist_ok=True)
    pages = {'index.html': home(), 'games.html': games(), 'studio.html': studio(),
             'contact.html': contact(), 'privacy.html': privacy()}
    for game in GAMES:
        pages[f"games/{game['slug']}.html"] = game_page(game)
    for name, html in pages.items():
        (OUT / name).write_text(html, encoding='utf-8')
    print('built', len(pages), 'pages in', OUT)


if __name__ == '__main__':
    main()
