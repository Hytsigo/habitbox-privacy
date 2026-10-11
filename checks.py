"""Read-only checks for this static site; Python standard library only."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json

ROOT = Path(__file__).resolve().parent
EMAIL = "rioscleiver49@gmail.com"
PAIRS = [("privacy.html", "privacy-en.html"), ("terms.html", "terms-en.html"),
         ("delete-account-es.html", "delete-account.html")]


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.alternates = {}
        self.counts = {}
        self.lang = None
        self.feed(text)
        self.close()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.counts[tag] = self.counts.get(tag, 0) + 1
        if tag == "html":
            self.lang = attrs.get("lang")
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f'Duplicate id: {attrs["id"]}'
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if key in attrs:
                self.links.append(attrs[key])
        if tag == "link" and attrs.get("rel") == "alternate":
            self.alternates[attrs["hreflang"]] = attrs["href"]


def main():
    expected = {"index.html"} | {name for pair in PAIRS for name in pair}
    pages = {}
    for name in sorted(expected):
        text = (ROOT / name).read_text(encoding="utf-8")
        assert text.lower().startswith("<!doctype html>"), name
        assert "habitbox.app" not in text, f"Unowned domain in {name}"
        assert "[EMAIL" not in text and "contact-pending" not in text, name
        assert EMAIL in text, f"Missing contact in {name}"
        page = Page(text)
        assert page.lang in ("es", "en"), name
        for tag in ("html", "head", "title", "body", "main", "h1"):
            assert page.counts.get(tag) == 1, f"Expected one {tag} in {name}"
        assert not any(page.counts.get(tag) for tag in ("script", "form", "iframe")), name
        pages[name] = page
    for spanish, english in PAIRS:
        for name, lang in ((spanish, "es"), (english, "en")):
            assert pages[name].lang == lang, name
            assert pages[name].alternates == {"es": spanish, "en": english}, name
    links = 0
    for name, page in pages.items():
        for href in page.links:
            url = urlsplit(href)
            if url.scheme:
                assert url.scheme in ("https", "mailto"), href
                if url.scheme == "mailto":
                    assert url.path == EMAIL, href
                continue
            assert not url.netloc, href
            target = name if not url.path else ("index.html" if url.path == "./" else url.path)
            target_path = (ROOT / target).resolve()
            assert target_path.is_relative_to(ROOT) and target_path.is_file(), f"Broken link: {name} -> {href}"
            if url.fragment:
                assert unquote(url.fragment) in pages[target].ids, f"Broken anchor: {name} -> {href}"
            links += 1
    config = json.loads((ROOT / "vercel.json").read_text())
    assert config["cleanUrls"] is True and config["trailingSlash"] is False
    print(f"OK: {len(pages)} pages, 3 bilingual pairs, {links} local links, contact and Vercel routes.")


if __name__ == "__main__":
    main()
