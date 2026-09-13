#!/usr/bin/env python3
"""Stamp a content hash onto every asset URL, in place, before the upload.

The site is hand-written static files pushed over FTP, so no filename here
carries a content hash and an illustration is normally replaced in place under
the name it already has. That is what kept Cache-Control down to a month: a
longer lifetime would have left visitors holding a replaced file with no way to
learn it had changed.

A query string is part of a cache key, so `?v=<hash>` buys the same guarantee a
hashed filename would, without renaming anything. Deploy runs this, the repo
keeps its plain URLs, and only the uploaded copy carries the stamps - which is
the trade: the deployed HTML no longer matches the HTML in git.

Run it from anywhere; it always rewrites the checkout it lives in. It is NOT
idempotent-safe by accident - it skips any URL that already has a query string,
so a second run is a no-op rather than a double stamp.
"""

import hashlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]

# Everything served as a static asset. HTML is deliberately absent: pages carry
# the stamps, so they have to stay revalidated or nobody ever learns a hash
# changed.
STAMPED = {".css", ".js", ".webp", ".jpg", ".jpeg", ".png", ".svg", ".woff2"}

HTML_REF = re.compile(r'\b(src|href)="([^"]*)"')
CSS_REF = re.compile(r'url\("([^"]*)"\)')

_digests: dict[pathlib.Path, str] = {}


def digest(path: pathlib.Path) -> str:
    """Eight hex characters of the file's SHA-256 - collision-proof enough for
    a cache key, short enough to keep the URLs readable in View Source."""
    if path not in _digests:
        _digests[path] = hashlib.sha256(path.read_bytes()).hexdigest()[:8]
    return _digests[path]


def resolve(doc: pathlib.Path, url: str) -> pathlib.Path | None:
    """The file a URL points at, or None if this URL is not ours to stamp.

    Absolute URLs are skipped on purpose. The only ones in the site are the
    og:image and ld+json values, which are read by crawlers rather than loaded
    by the page - a query string there buys nothing and some scrapers mishandle
    it. Anything already carrying a query or a fragment is skipped too, which is
    what makes a second run a no-op.
    """
    if not url or "://" in url or url.startswith(("data:", "mailto:", "#")):
        return None
    if "?" in url or "#" in url:
        return None
    if pathlib.PurePosixPath(url).suffix.lower() not in STAMPED:
        return None
    target = ROOT / url.lstrip("/") if url.startswith("/") else doc.parent / url
    try:
        target = target.resolve()
        target.relative_to(ROOT)
    except (OSError, ValueError):
        return None
    return target if target.is_file() else None


def stamp(doc: pathlib.Path, pattern: re.Pattern, group: int) -> int:
    text = original = doc.read_text()
    count = 0

    def replace(match: re.Match) -> str:
        nonlocal count
        url = match.group(group)
        target = resolve(doc, url)
        if target is None:
            return match.group(0)
        count += 1
        return match.group(0).replace(f'"{url}"', f'"{url}?v={digest(target)}"')

    text = pattern.sub(replace, text)
    if text != original:
        doc.write_text(text)
    return count


def main() -> int:
    stylesheets = sorted(ROOT.glob("assets/css/*.css"))
    pages = sorted(p for p in ROOT.glob("**/*.html") if ".git" not in p.parts)

    # The stylesheet's own @font-face URLs have to be stamped before anything
    # hashes the stylesheet, or the CSS would go up under the digest of its
    # pre-rewrite self and every deploy would advertise a hash that no longer
    # matched the bytes being served.
    fonts = sum(stamp(css, CSS_REF, 1) for css in stylesheets)
    if any(css in _digests for css in stylesheets):
        print("BUG: a stylesheet was hashed before its own URLs were stamped", file=sys.stderr)
        return 1

    assets = sum(stamp(page, HTML_REF, 2) for page in pages)

    # The check has to find leftovers WITHOUT reusing the patterns above: an
    # earlier version scanned with the same regexes, so a regex that quietly
    # stopped matching src= also stopped finding its own omissions and the run
    # reported success while stamping two thirds of the URLs. Searching for the
    # asset filenames themselves is independent of how references are matched.
    names = sorted(
        {f.name for f in (ROOT / "assets").rglob("*") if f.is_file()},
        key=len, reverse=True,
    )
    missed = []
    for doc in stylesheets + pages:
        text = doc.read_text()
        for name in names:
            for hit in re.finditer(re.escape(name), text):
                if text[hit.end():].startswith("?v="):
                    continue
                # og:image and the ld+json logo are absolute on purpose: they
                # are read by crawlers, not loaded by the page, so they carry
                # no stamp and must not be reported as omissions.
                if "https://keera.ch/" in text[max(0, hit.start() - 40):hit.start()]:
                    continue
                missed.append((doc.relative_to(ROOT), name))
    if missed:
        for doc, name in sorted(set(missed)):
            print(f"BUG: left unstamped: {doc} -> {name}", file=sys.stderr)
        return 1

    print(f"stamped {assets} asset URLs across {len(pages)} pages "
          f"and {fonts} font URLs across {len(stylesheets)} stylesheets")
    return 0


if __name__ == "__main__":
    sys.exit(main())
