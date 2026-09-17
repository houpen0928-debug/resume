"""Check the built resume routes, content, photo, and project-site asset paths."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

root = Path('_site')
class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
    def handle_starttag(self, tag, attrs):
        self.urls.extend(v for k, v in attrs if k in ('href', 'src') and v)

routes = ('index.html', 'cv/index.html', 'cv-json/index.html', 'transformation/index.html', 'contact/index.html', 'research/index.html')
for route in routes + tuple('en/' + route for route in routes):
    html = (root / route).read_text(encoding='utf-8')
    assert 'Jason Hung' in html, route
    assert 'jason-hung.png' in html, route
    for placeholder in ('Your Sidebar Name', 'Red Brick University', 'none@example.org', 'GitHub University'):
        assert placeholder not in html, (route, placeholder)
    parser = Links()
    parser.feed(html)
    for url in parser.urls:
        parsed = urlsplit(url)
        if parsed.netloc and parsed.netloc != 'houpen0928-debug.github.io':
            continue
        if parsed.scheme and parsed.scheme not in ('http', 'https'):
            continue
        path = unquote(parsed.path)
        if not path:
            continue
        if path == '/resume':
            path += '/'
        assert path.startswith('/resume/'), (route, url)
        local = root / path[len('/resume/'):]
        assert local.exists(), (route, url)

home = (root / 'index.html').read_text(encoding='utf-8')
assert all(s in home for s in ('17+', 'RMB 2M+', '20%+', '0 → 1'))
cv = (root / 'cv/index.html').read_text(encoding='utf-8')
assert '2026-08' in cv and '共同創辦人' in cv and '預計' in cv
assert (root / 'images/jason-hung.png').stat().st_size > 100000
print('Resume pages, dates, claims, local links and portrait: PASS')

class LanguageMarkup(HTMLParser):
    def __init__(self):
        super().__init__()
        self.language = None
        self.switch_depth = False
        self.switches = []
        self.alternates = {}
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.language = attrs.get('lang')
        if tag == 'nav' and attrs.get('class') == 'resume-language-switch':
            self.switch_depth = True
        if tag == 'a' and self.switch_depth:
            self.switches.append(attrs)
        if tag == 'link' and attrs.get('rel') == 'alternate':
            self.alternates[attrs.get('hreflang')] = attrs.get('href')
    def handle_endtag(self, tag):
        if tag == 'nav':
            self.switch_depth = False

for route in routes:
    suffix = route.removesuffix('index.html')
    expected = {'zh-TW': '/resume/' + suffix, 'en': '/resume/en/' + suffix}
    for prefix, language in [('', 'zh-TW'), ('en/', 'en')]:
        parser = LanguageMarkup()
        parser.feed((root / (prefix + route)).read_text(encoding='utf-8'))
        assert parser.language == language, (route, language)
        assert {a['hreflang']: a['href'] for a in parser.switches} == expected
        assert [a['hreflang'] for a in parser.switches if a.get('aria-current') == 'page'] == [language]
        for lang, url in expected.items():
            assert parser.alternates[lang] == 'https://houpen0928-debug.github.io' + url

import json
zh = json.loads(Path('_data/cv.json').read_text(encoding='utf-8'))
en = json.loads(Path('_data/cv_en.json').read_text(encoding='utf-8'))
assert [(w['startDate'], w['endDate']) for w in zh['work']] == [(w['startDate'], w['endDate']) for w in en['work']]
assert [p['id'] for p in zh['projects']] == [p['id'] for p in en['projects']]
research = (root / 'en/research/index.html').read_text(encoding='utf-8')
assert all(s in research for s in ('104,800', 'not realized savings', 'Morris Fan', 'not claimed', '1,113', '20 modeling samples'))
english_cv = (root / 'en/cv/index.html').read_text(encoding='utf-8')
assert all(s in english_cv for s in ('window.print()', '2026-08', 'RMB 2M+', 'estimated benefit', 'Executive MBA'))
print('Bilingual routes, reciprocal switches, metadata, chronology and research attribution: PASS')
