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

for route in ('index.html', 'cv/index.html', 'cv-json/index.html', 'transformation/index.html', 'contact/index.html', 'research/index.html'):
    html = (root / route).read_text(encoding='utf-8')
    assert '洪承洋' in html, route
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
