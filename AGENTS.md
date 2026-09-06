# Cora Website

## Pages

- index.html - home
- code.html - Cora Code
- gateway.html - Cora Gateway
- sovereignty.html - Sovereignty
- sustainability.html - Sustainability

`robots.txt` and `sitemap.xml` sit alongside them at the root. The sitemap lists
all fifteen URLs with `xhtml:link` alternates; regenerate it when a page is added.

## Languages

Three languages, five pages each. German (Swiss spelling - `ss`, never `ß`) is
the default and lives at the root; English lives under `en/` and French under
`fr/`, with the same five filenames, so `code.html` ↔ `en/code.html` ↔
`fr/code.html`. Filenames stay English in every language - only the prose is
translated. Each page carries a DE/EN/FR switcher in the header, always in that
order with the current language unlinked, and four `rel="alternate" hreflang`
links in its real `<head>` (`de`, `en`, `fr`, `x-default`); `x-default` points at
the German page. `<html lang>` is `de-CH` at the root, `en` under `en/` and `fr`
under `fr/`.

Adding or editing a page means touching all three copies. Two things differ in
the English and French files beyond the prose: asset URLs are `../assets/...`
(one directory up), and the switcher points at `../<page>.html` and
`../<other>/<page>.html` instead of `en/<page>.html` and `fr/<page>.html`.
Attributes React spells in camelCase are written `sc-camel-`-prefixed and
kebab-cased - `hreflang` is `sc-camel-href-lang`, matching the existing
`sc-camel-view-box`.

The French copy addresses the reader as *vous*, where German uses *du* and
English *you*: *tu* would read wrong to the banking, insurance and public-sector
audience the site is written for. It follows French punctuation spacing - a
`&nbsp;` before `:`, `;`, `?` and `!`, and inside `«&nbsp;…&nbsp;»` - so those
entities appear in the French prose and nowhere else. Recurring choices worth
keeping stable: *souveraineté*, *durabilité*, *poids ouverts*, *codage
agentique*, *dépôt* for repository, *tenant* untranslated, *masquage* for
redaction, and *nLPD* where the German says revDSG. Every character French
adds - `é è à ç ô û œ`, the guillemets `«»‹›` and `&nbsp;` - already sits inside
the `latin`/`latin-ext` font cuts that ship, so no new subset is needed.

`bespinian.io` has no French locale, so the footer and the form's error message
link French visitors to the English `bespinian.io/en/...` pages.

## Cora's story

The two home pages carry a `#story` section between the hero band and
`#products`. Omnivor, the adversary, gets three panels - the data harvesting,
the quiet invasion by terms-of-service, and the resource burn (cheap power,
river cooling, diesel, waste heat into the sky) - then Cora's answer runs full
width beneath them, and a six-cell strip maps the fiction onto real features:
four sovereignty cells in amber, two energy cells in the sustainability green.
`sustainability.html` picks the thread up again in its own `#omnivor` section,
just above `#claims`: Omnivor's take-until-nothing-is-left panel against Cora's
same-grid-as-the-country panel, which hands off to the claims table right below
it.

Omnivor is a character, not a competitor: keep him unnamed-in-reality, and keep
the mono footnote that says out loud he is invented, because it is what stops
the section reading as an accusation against a real company. The environmental
copy has the same job as the rest of `sustainability.html` - it says what the
villain does, not what Cora offsets, and the sentence that refuses the
climate-neutral claim has to survive any rewrite.

The story is the only place with a third accent alongside the blue and the
amber: `#f0736a` on the villain eyebrows over `rgba(226,86,77,.09)` panel fills,
against the blue fill on Cora's panel and the green `#4ade80` wherever the copy
turns to energy. The red glow behind both sections is the hero's radial gradient
in red. The story is linked from every page's footer as the first item of the
*Unternehmen* / *Company* / *Entreprise* column, `./#story`, which resolves to
the home page of the current language.

## Contact form

Nine pages carry the same form - the `#contact` section of the home page and
of the two product pages in each of the three languages. It posts to Formspree
(`https://formspree.io/f/xvkobjyb`): name, e-mail, company, a checkbox group
for the two products and a free-text message, plus the two hidden fields
Formspree reads itself - `_subject` and the `_gotcha` honeypot. A third hidden
field names the language the enquiry came from, and its own name is localised
too: `Sprache=Deutsch`, `Language=English`, `Langue=Français`. So are the visible
field names, because Formspree puts them straight into the notification mail -
`Name`/`Unternehmen`/`Interesse`, `Name`/`Company`/`Interest`,
`Nom`/`Entreprise`/`Intérêt`; `email` and `message` stay lowercase English in all
three. Interest is a checkbox group rather than a radio group so one visitor can
ask about Cora Code and Cora Gateway at once.

On `code.html` and `gateway.html` the page's own product is ticked already.
That is `sc-camel-default-checked="true"` - React's `defaultChecked`, not
`checked`: a `checked` attribute would make the box a controlled input the
visitor cannot untick. Apart from that tick and the localised strings the nine
copies are identical, so edit one and copy it to the other eight.

A second script in each of those pages' real `<head>` takes the submit over. It
is delegated off `document`, because the body renders client-side and the form
does not exist when the script runs; it posts with `fetch` and
`Accept: application/json` so the visitor never leaves the page, then hides
`[data-cf-fields]` and prints the confirmation into `[data-cf-status]`. All
four messages - sending, sent, failed, and "pick a product" - come from
`data-cf-*` attributes on the `<form>`, so one script serves all three
languages.
"At least one product" is the only rule it checks itself; everything else is
native constraint validation.

Controls are styled by class - `.cf-label`, `.cf-field`, `.cf-choice`,
`.cf-submit` - in the shared `<style>` block, so the six pages without a form
carry the rules too.

## Responsive and accessibility layer

The pages style themselves with inline `style` attributes, which cannot hold
media queries. Each page therefore ends its `<helmet>` with one shared `<style>`
block - keep the fifteen copies identical. It carries:

- **Header reflow.** Below 880px the four nav links no longer fit beside the
  logo and the actions, so `.site-nav` moves to its own full-width row and
  scrolls horizontally instead of being clipped. The classes the query needs -
  `.site-header-inner`, `.site-nav`, `.site-actions`, `.site-docs-link` - are on
  the header markup; the Docs link is hidden on that breakpoint for room.
- **Model table.** Below 700px `.model-head` is hidden and each `.model-row`
  becomes a card, with every `.model-cell` printing its column name from
  `data-label` via `::before`. Adding a column means adding the matching
  `data-label` (index only).
- **Contact form.** The `.cf-*` control styles - see _Contact form_ above.
- **Focus, motion and anchors.** A `:focus-visible` ring, a `.skip-link` that
  targets the `<main id="main">` landmark, `scroll-margin-top` sized to the
  sticky header at both breakpoints, and a `prefers-reduced-motion` block that
  stops the mascot drift and the blinking caret.

Display type and section padding scale with `clamp()` written directly into the
inline styles (the runtime's `cssToObj` only splits on `;`, so commas inside
`clamp()` and `repeat()` are safe). Keep the min bound at or above ~17px.

Each page's `<head>` also runs a short script that re-applies the URL fragment.
The body renders client-side, so the browser resolves `#contact` before the
target exists and a deep link would otherwise do nothing; the script waits for
the element, then holds the position until layout settles.

## Assets

- `assets/js/` - the Claude Design runtime (`dc-runtime.js`) and local copies of
  React 18.3.1. The runtime resolves React through the `window.__resources` map
  set in each page's `<head>`; without it, it falls back to unpkg, so keep that
  script when editing a page. Every page loads exactly these three files.
  Artwork is plain `<img>` everywhere - `width`/`height` from the file's own
  pixel size, `alt`, `decoding="async"`, and either `loading="lazy"` or, for the
  four hero images, `sc-camel-fetch-priority="high"`. Crop and corners live in
  the inline style (`object-fit:cover`, `border-radius`), so a new image needs no
  script. The `<image-slot>` custom element that used to wrap the subpage images
  is gone with its `dc-components.js`: it was authoring-time scaffolding for
  drag-and-drop filling, and on the published site it only cost 65 KB and pushed
  the images behind a custom-element upgrade.
- `assets/fonts/` - JetBrains Mono and Space Grotesk woff2 subsets, `latin` and
  `latin-ext` only. These are variable-weight faces: one file per subset backs
  every `@font-face` weight alike - 400/500/700 for the mono, 400/500/600/700
  for Space Grotesk. Google Fonts also ships `cyrillic`, `cyrillic-ext`, `greek`
  and `vietnamese` cuts; the German and English copy contains no glyph in those
  ranges, so the files and their `unicode-range` rules were dropped. Re-add the
  matching cut if a page ever needs one.
- `assets/img/` - mascot artwork and icons. Pages reference the `.webp`
  renditions (~1.3 MB in total, down from 8.5 MB); the original `.png`/`.jpeg`
  masters have been removed, so re-encoding a rendition means re-exporting its
  source first, then `magick <src> -resize <w>x\> -strip tmp.png && cwebp -q 82
-alpha_q 90 -m 6`. `cora-og-image.jpg` is the 1200×630 social card and
  `cora-apple-touch-icon.png` the 180×180 iOS icon.

## Metadata

Every page carries its `<title>`, `description`, `rel="canonical"`, `hreflang`
alternates, icons, Open Graph and Twitter card tags and a JSON-LD block in the
**real `<head>`** - the one the parser builds before any script runs, not in the
`<helmet>`. This is deliberate: the `<helmet>` is inside `<body>` and the runtime
only copies it into the head once React has mounted, so a client that does not
execute JavaScript sees none of it. Google renders JS and would cope, but the
social crawlers (Slack, LinkedIn, WhatsApp, X, Facebook) and most AI crawlers do
not - they fetch the raw HTML and read `<head>`, and would find nothing there.

Keep new metadata in `<head>` for the same reason, and do not re-add a copy to
the `<helmet>`: the helmet manager only ever appends to the head, so a duplicate
stays a duplicate. Two things follow from `<head>` being outside `<x-dc>`:
attributes are spelled normally (`hreflang`, not `sc-camel-href-lang` - that
encoding is only needed inside the deck), and every URL is absolute
`https://cora.swiss/...`, so they all need updating if the domain changes.

Canonicals, `og:url` and the sitemap use the directory form for the two home
pages - `https://cora.swiss/` and `https://cora.swiss/en/`, not `/index.html` -
because that is the URL GitHub Pages serves the root at and the one inbound
links point to. Internal links match: `href="./"` for the home page of the
current language, `href="../"` for the other one.

The JSON-LD is one `@graph` per page: `Organization` + `WebSite` on the two home
pages, `BreadcrumbList` on the subpages, plus a `SoftwareApplication` on
`code.html` and `gateway.html`. The `Organization` has no `sameAs` yet - add the
company's social and directory profiles there once they exist; it is the main
signal that ties the domain to a real entity.
