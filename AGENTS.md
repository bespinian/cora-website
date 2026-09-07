# Cora Website

Eighteen hand-written static HTML pages, served straight off GitHub Pages with no
build step. Each page is self-contained: its `<head>` carries the metadata and
the whole `<style>` layer, its markup styles itself with inline `style`
attributes, and the only JavaScript on the site is the contact-form handler on
the nine pages that have a form. The pages used to be Claude Design decks -
markup inside `<x-dc>` rendered client-side by `assets/js/dc-runtime.js` and
React - and that is gone: no runtime, no `<helmet>`, no `sc-camel-` attributes,
no props script. Do not reintroduce them; write plain HTML.

## Pages

- index.html - home
- code.html - Cora Code
- gateway.html - Cora Gateway
- story.html - Cora's story
- sovereignty.html - Sovereignty
- sustainability.html - Sustainability

`robots.txt` and `sitemap.xml` sit alongside them at the root. The sitemap lists
all eighteen URLs with `xhtml:link` alternates; regenerate it when a page is added.

The header nav carries five links in this order: the two products,
Sovereignty, Sustainability, the story. It renders three ways, and the two
breakpoints in the shared `<style>` block are sized for exactly those five:
inline beside the logo above 1000px, on its own full-width row from 700px to
1000px, and behind a `☰` disclosure below 700px. The 1000px figure was raised
from 880px when the story link was added, because five labels no longer clear
the actions below roughly 960px. A sixth link means checking the 700-1000px row
again - German has the longest labels and currently ends around 550px of a
710px row, so there is room, but not unlimited room. Below 700px a sixth link
costs nothing; it is one more row in the panel.

## Languages

Three languages, six pages each. German (Swiss spelling - `ss`, never `ß`) is
the default and lives at the root; English lives under `en/` and French under
`fr/`, with the same six filenames, so `code.html` ↔ `en/code.html` ↔
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

The French copy addresses the reader as _vous_, where German uses _du_ and
English _you_: _tu_ would read wrong to the banking, insurance and public-sector
audience the site is written for. It follows French punctuation spacing - a
`&nbsp;` before `:`, `;`, `?` and `!`, and inside `«&nbsp;…&nbsp;»` - so those
entities appear in the French prose and nowhere else. Recurring choices worth
keeping stable: _souveraineté_, _durabilité_, _poids ouverts_, _codage
agentique_, _dépôt_ for repository, _tenant_ untranslated, _masquage_ for
redaction, _groupe_ for Omnivor the company, and _nLPD_ where the German says
revDSG. Every character French
adds - `é è à ç ô û œ`, the guillemets `«»‹›` and `&nbsp;` - already sits inside
the `latin`/`latin-ext` font cuts that ship, so no new subset is needed.

`bespinian.io` has no French locale, so the footer and the form's error message
link French visitors to the English `bespinian.io/en/...` pages.

## Cora's story

The story has its own page, `story.html`, and a teaser on the home pages.

**Cora is the protagonist, not the closing argument.** She is the subject of all
24 panels - named in twenty, a pronoun in the four where she is the continuing
subject - and the arc is hers: powerless witness, then traveller, then witness
again, then builder. Never rewrite the page so she arrives only at the end;
that was the first draft's mistake.

She has a sidekick: **Cache**, a male cat who lives in the server room. Cats
notice what nobody else notices and stare at it until somebody follows their
eyes, so Cache _is_ the audit trail, in fur: he stares at the wall in panel 05
and someone just scratches his ears, and in panel 22 the staring finally has
something to point at - a ledger Cora built for him, where he puts a paw on the
entry flagged red and this time everybody looks. Keep that pairing intact, it is
the story's main payoff. He is male in all three languages; the French copy
calls him _un chat_ and never _une chatte_, which carries vulgar slang. His name
stays _Cache_ everywhere, like Omnivor's - in French it doubles as the word for
a hiding place. An earlier draft used a Swiss marmot called Murmeli; it read as
folklore rather than product, so don't go back to it.

A cast strip sits between the hero band and Act I: Cora (the hero), Cache (the
sidekick) and Omnivor (the adversary), each with a kicker, a name and a role
paragraph. All three portraits are in place as `cora-story-cast-<slug>.webp`
(900x900). Cora has her own cast portrait rather than reusing
`cora-mascot-full-figure.webp`, which stays the hero image on `index.html`.
Omnivor's portrait is its headquarters - a glass tower of server racks at dusk -
not the faceless suited figure the original brief asked for; the role paragraph
reads the same either way, because Omnivor is a company and never appears as a
body (see _Omnivor_ below).

`story.html` runs the arc as four acts over 24 numbered comic panels:

- **Act I - the gift** (01-05). Cora's server room in an unnamed small city,
  still small and unknown; Omnivor arrives with a free plugin that genuinely
  works; Cora watches the team's relief with nowhere to put herself; Cache
  stares at the cable and only Cora follows his eyes.
- **Act II - the quiet invasion** (06-12). Cora steps into the data stream and
  follows it: page 40 of the terms, over the ocean, the windowless hall where a
  Swiss cross glows in one rack, the web form instead of a room, home to a map
  that changed colour - and the price tripling on a door with no lock.
- **Act III - what it doesn't pay for** (13-17). The detour on the way back:
  cheap power, Cache staring at nothing by the warm river, diesel for uptime,
  waste heat
  over dark houses - and on the ridge at first light, Cora decides this is not a
  law of nature.
- **Act IV - the gate** (18-24). She comes back with a list, not a manifesto:
  rebuilt from open weights and vLLM, two regions, the gate, Cache's ledger,
  the heat routed to the valley - and the last panel returns to the Tuesday
  morning of panels 01-02.

Act IV pays off earlier panels by number, and the captions say so out loud:
19 answers Omnivor's key in 12, 21 catches the client name from 05, 23 lights
the houses that were dark in 16, 22 answers Cache's ignored stare in 05, and
24 closes the loop on 01-02. Renumbering or dropping a panel breaks those
references - fix the captions if you do.

Each act is one `<section>` carrying its accent in a radial gradient - red for
I-III, blue for IV. Panel accents move with the point of view rather than the
act: Cora's panels are blue even inside the red acts, and Cache's energy
beats (05, 14, 22, 23) take the sustainability green. Acts open with a
typographic band (act eyebrow, headline, lede); Act IV's opener also carries
`cora-holding-a-key-in-a-swiss-data-centre.webp`. Panels then run in
rows: `pair` rows put two 4:3 panels side by side, `splash` rows one 16:9 panel
capped at 900px, and each act closes on a splash.

Every panel is a `<figure>`: the artwork slot, then a `<figcaption>` whose mono
prefix is the panel number and whose text is the narration. The story is carried
by those captions - keep them reading as a graphic novel, concrete and in
sequence, not as feature bullets.

The story's own setting is **an unnamed small city**, not Bern: the fiction used
to open in a Bern server room, past the Zytglogge, and the city name and the
clock tower came out of the lede, the three meta descriptions and the briefs for
panels 01 and 18 so the setting reads as anywhere. Bern in the footer - _Gebaut
in Bern von bespinian_ and the `© 2026 BESPINIAN · BERN` line - is a real
company fact and stays, on this page like the other seventeen. Zurich and Geneva
in panel 20 are real regions and stay too.

Panel 01 is the only slot with real artwork so far
(`cora-story-01.webp`); the other 23 are dashed placeholders, not `<img>` tags,
so the page renders finished before the artwork exists. Each placeholder shows
its `PANEL NN` label and a short art brief - what that panel should depict - so
the page doubles as the shot list. Each is preceded by an HTML comment holding
the exact `<img>` to paste in its place (`assets/img/cora-story-NN.webp`,
1200×900 for pair panels, 1600×900 for splashes, `loading="lazy"`, the brief
pre-filled as `alt`) and the brief again, because dropping the image in removes
the visible copy. Replace the whole placeholder box, keep the numbering, and
collapse the comment to `<!-- PANEL NN - Brief: ... -->` so the brief survives
as a record. Those panel sizes are a target, not a crop to force: panel 01 ships
at its source's native 1024×768 rather than upscaled, so set `width`/`height`
from the file and keep the 4:3 or 16:9 shape the row expects.

Beneath the acts, an epilogue maps the fiction onto real features in a six-cell
strip - four sovereignty cells in amber, two energy cells in the sustainability
green - followed by the _what we do not claim_ panel and the mono footnote.

The home pages keep a teaser `#story` between the hero band and `#products`,
and it stays a teaser: the eyebrow and headline, a two-sentence lede that
sketches Cora's arc before naming Omnivor, Cora's answer panel, and the mono
footnote - nothing else. It says the one thing that matters and then hands off:
the answer paragraph ends by pointing at the story, and under it a filled button
in the villain red `#f0736a` - the only button on the site that is not blue -
leads to `story.html`, with the sovereignty and sustainability links beside it
as plain mono text. The button opts back out of the row's mono font, so it
carries `font-family:'Space Grotesk',Helvetica,sans-serif` explicitly. An earlier draft also carried a three-cell strip of
one-line villain summaries and a longer answer paragraph; that belongs on
`story.html`, don't put it back here.

`sustainability.html` picks the thread up again in its own `#omnivor` section,
just above `#claims`: Omnivor's take-until-nothing-is-left panel against Cora's
same-grid-as-the-country panel, which hands off to the claims table right below
it.

Omnivor is an invented company, not a real competitor: keep it
unnamed-in-reality, and keep the mono footnote that says out loud it is
invented, because it is what stops the section reading as an accusation against
a real company - it appears on `story.html`, on the home teaser and in
`sustainability.html` alike.

**Omnivor is a company, not a character.** It has no body in any panel: it shows
up as its brand - the colours a hall or a map flips to, the logo on a screen, a
crate in a doorway, the glass tower and the tower's shadow, a key mounted on
that facade like a corporate sculpture. An earlier draft drew it as a giant
figure holding out a gift box and holding up a key; don't go back to that, and
don't let a new panel brief hand it hands, a face or a silhouette. The captions
name it as a company where it enters (03: _a corporation, not an army_), and
panel 10 - no room to walk into, no person to ask, a web form and a 30-day
window - is the point, not a slip. Each language carries it with a noun whose
gender the pronouns then follow: German _der Konzern_ (so _er/ihn/ihm/sein_),
French _un groupe_ (so _il/lui/son_ - never feminine _elle_, which would collide
with Cora), English a plain _it/its_. The mono footnote uses the same noun:
_Den Konzern Omnivor gibt es nicht._ The environmental
copy has the same job as the rest of `sustainability.html` - it says what the
villain does, not what Cora offsets, and the refusal of the climate-neutral
claim has to survive any rewrite. On `story.html` that refusal is its own
panel in the epilogue, under a _what we do not claim_ eyebrow: not free, not
climate-neutral, and here is what we will tell you instead.

The story is the only place with a third accent alongside the blue and the
amber: `#f0736a` on the villain eyebrows over `rgba(226,86,77,.09)` panel fills,
against the blue fill on Cora's panel and the green `#4ade80` wherever the copy
turns to energy. The red glow behind both sections is the hero's radial gradient
in red. The story is linked from every page's footer as the first item of the
_Unternehmen_ / _Company_ / _Entreprise_ column, `story.html`, which resolves
within the current language directory; on `story.html` itself that link carries
`aria-current="page"`.

## Models

`#models` on `code.html` runs two tables, and the order is the argument. The
first is Cora's own - open weights on Swiss GPUs, `MODELL / KONTEXT / LIZENZ /
IDEAL FÜR`, three Cora models and the customer's own fine-tune. Under it, in the
gateway amber `#f5b229` rather than the blue, sits **Gehostete Anbieter**: the
current OpenAI models, `MODELL / KONTEXT / MODELL-ID / IDEAL FÜR`, with the
model IDs in mono because that is what a tenant pastes into a policy. Both use
the same `.model-head` / `.model-row` / `.model-cell` classes, so each table's
`data-label`s have to match its own head row - the two heads differ in the third
column.

The amber block never reads as a recommendation: its lede says the models are
proprietary and run on the provider's infrastructure and not on Swiss GPUs, and
the mono footnote says they are blocked by default and opened per team and data
class. Keep both, or the section stops being consistent with `sovereignty.html`.
That footnote also carries the month the lineup was checked (September 2026),
because third-party model names churn - update the stamp whenever the rows
change. `gateway.html` names the same provider in the MODELLE column of its
architecture diagram, so the two pages move together.

## Gateway web UI screenshot

`#web-ui` on the three `gateway.html` copies sits between the architecture
diagram and the feature cards, and pays off the hero's claim that the gateway is
_administered from the web UI or the CLI_. It is the Sessions screen: an
eyebrow, a headline, two paragraphs describing what the screen totals and what
the left-hand navigation holds, then the shot in a bordered frame, then a mono
footnote. The copy is written off the pixels - the metric tiles, the columns,
the served/refused status, the nav groups - so re-shooting the screen means
re-reading those two paragraphs. It also says out loud that the figures come
from a demo instance, which is what stops `0.00 CHF` reading as a claim.

Both themes ship, and a two-tab toggle switches between them:
`cora-gateway-sessions-dark.webp` and `-light.webp`, 1920x952 each. That is the
same no-JS pattern as the mobile menu, with two radios in place of the one
checkbox - `#ui-shot-dark` is `checked`, and every rule reaches its target as a
following sibling of whichever input is checked, so the input order in the
`<fieldset>` (radios, then `.ui-shot-tabs`, then `.ui-shot-frame`) is load-
bearing. The inputs carry the state and the focus ring; the `<label>`s are what
you see; the visually hidden `<legend>` names the group. Hiding the inactive
shot needs `display: none !important`, because each `<img>` carries
`display:block` in its own `style` attribute.

The two shots are the same screen in two themes, so the toggle is the only
placement that earns both - side by side, two dense dashboards at half width
are illegible, and there is no second screen to pair. If the light one is ever
dropped, the toggle, the `.ui-shot-*` rules and the `<fieldset>` go with it and
the dark `<img>` stays on its own.

The masters were 3840x1987 browser screenshots carrying three artefacts of the
window they were shot in: its own scrollbar rendered as a dark strip down the
sidebar's right edge, its blue focus border down the left (3px on the dark
shot, 2px on the light one - the right and top edges were clean), and a bottom
cut through the signed-in-user card. All three went before encoding: the
scrollbar was spliced out by appending the two crops either side of it, the
frame started 4px in from the left and was cropped to 1890px tall, then the
result was resized to 1920 wide and encoded at `cwebp -q 92` rather than the 82
the artwork uses, because this is small UI type rather than illustration.

Do that trimming on the master, before the downscale, rather than on the
finished file - 2px of window border on the delivered image is 4px on the
master, and cropping the 1920-wide copy instead costs a pixel of real UI and
leaves the width off its round number. Any replacement shot wants the same
pass, and its own `width`/`height` read off the encoded file.

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

On `code.html` and `gateway.html` the page's own product is ticked already -
a plain `checked` attribute, which the visitor can untick. Apart from that tick
and the localised strings the nine copies are identical, so edit one and copy it
to the other eight.

A second script in each of those pages' `<head>` takes the submit over. It is
delegated off `document`, so it can run from the head before the parser has
reached the form; it posts with `fetch` and
`Accept: application/json` so the visitor never leaves the page, then hides
`[data-cf-fields]` and prints the confirmation into `[data-cf-status]`. All
four messages - sending, sent, failed, and "pick a product" - come from
`data-cf-*` attributes on the `<form>`, so one script serves all three
languages.
"At least one product" is the only rule it checks itself; everything else is
native constraint validation.

Controls are styled by class - `.cf-label`, `.cf-field`, `.cf-choice`,
`.cf-submit` - in the shared `<style>` block, so the nine pages without a form
carry the rules too.

## Responsive and accessibility layer

The pages style themselves with inline `style` attributes, which cannot hold
media queries. Each page therefore ends its `<head>` with one shared `<style>`
block - keep the eighteen copies identical. It carries:

- **Header reflow.** Below 1000px the five nav links no longer fit beside the
  logo and the actions, so `.site-nav` moves to its own full-width row. The
  classes the query needs - `.site-header-inner`, `.site-nav`, `.site-actions` -
  are on the header markup. That row used to scroll horizontally with both
  scrollbar-hiding rules set, which on a phone left the last two links off the
  edge with nothing to say they were there; below 700px it is a menu instead,
  and between 700px and 1000px the five labels genuinely fit, so it never
  scrolls.
- **Mobile menu.** Below 700px `.site-nav` is `display:none` and a `☰`
  `.site-menu-toggle` opens it as a full-width panel of one link per row, with
  the DE/EN/FR switcher moved in underneath. The toggle is a `<label>` for a
  visually hidden `.site-menu-state` checkbox that sits just before the `<nav>`,
  and the open state is `.site-menu-state:checked ~ .site-nav`. It is a checkbox
  and not `<details>` on purpose: the same `<nav>` has to render inline above
  the breakpoint, and a closed `<details>` hides its children through a slot
  that CSS cannot reliably re-show. The checkbox is the focusable control and
  the label names it, so keep the visually hidden `.site-menu-text` - it is the
  menu's accessible name. To leave room for the toggle on a 360px row the query
  puts `display:contents` on `.site-actions` so the CTA and the switcher become
  header flex items that can be ordered and hidden separately.
  **Every one of those rules needs `!important`**: `.site-actions` and
  `.site-lang` carry `display:flex` and `flex:0 0 auto` in their own `style`
  attributes, and an inline declaration beats any non-important rule.
- **Touch targets.** Under `pointer: coarse` the nav links, the `.site-lang`
  switcher and the `.site-footer-col` link columns get vertical padding, because
  all three are set in 11-14px type that is easy to miss with a thumb. It is
  gated on the pointer rather than the width so a mouse keeps the tighter
  spacing the design was drawn at.
- **Card tables.** Below 700px `.model-head` is hidden and each `.model-row`
  becomes a card, with every `.model-cell` printing its column name from
  `data-label` via `::before`. Adding a column means adding the matching
  `data-label` (index only). Below 560px the cell stacks the label above the
  value instead of setting the two on one line - a column name as long as
  `WER SIE KONTROLLIERT` otherwise leaves the value a ragged sliver. Three
  tables use these classes: the two in `#models` on `code.html` (see _Models_
  below) and the layer/control/location table on `sovereignty.html`.
- **Architecture diagram.** `#architecture` on `gateway.html` is a five-column
  grid - three panels chained by two `→`. Below 860px `.arch-flow` becomes one
  column and each `.arch-arrow` rotates 90deg so the chain reads down the page.
  The arrows are `aria-hidden`; they are punctuation, not content.
- **Web UI screenshot.** The `.ui-shot-*` rules behind `#web-ui` on
  `gateway.html` - see _Gateway web UI screenshot_ above. Below 860px, the same
  breakpoint the diagram uses, `.ui-shot-frame` scrolls sideways and
  `.ui-shot-img` is pinned to 860px instead of shrinking: a 1920px dashboard
  scaled into a phone is a grey smudge. The scrollbar is deliberately left
  visible - the nav row's hidden one is the mistake not to repeat.
- **Contact form.** The `.cf-*` control styles - see _Contact form_ above. The
  text controls are 16px on purpose: iOS Safari zooms the whole page in when a
  focused input is smaller, so do not tune that number down. The submit goes
  full-width below 560px and the checkboxes are 20px.
- **Product card hover.** `.product-card-code` and `.product-card-gateway` on
  the two cards in `#products`; the rules need `!important` to beat the
  `border-color` in the cards' own `style` attribute.
- **Print.** `print-color-adjust: exact`, because the pages are light text on
  dark panels and a browser that drops backgrounds prints them blank; effects
  and animations are switched off in the same block.
- **Focus, motion and anchors.** A `:focus-visible` ring, a `.skip-link` that
  targets the `<main id="main">` landmark, `scroll-margin-top` sized to the
  sticky header at both breakpoints, and a `prefers-reduced-motion` block that
  stops the mascot drift and the blinking caret.

It also carries three page-wide guards that only matter on a narrow viewport:
`-webkit-text-size-adjust: 100%` so iOS does not inflate the type in landscape,
`overflow-wrap: break-word` so a long unbroken token cannot push the layout
sideways, and `max-width: 100%` on `img`/`svg`.

Display type, section padding and card padding all scale with `clamp()` written
directly into the inline styles - `clamp(20px,5vw,32px)` on a section's
horizontal padding and `clamp(20px,4vw,30px)` on a card's, so a phone does not
spend a third of its width on gutters. Keep the min bound at or above ~17px for
type. Grids are written `repeat(auto-fit,minmax(min(100%,Npx),1fr))`: the
`min(100%,…)` is what lets the track collapse below `N` instead of overflowing,
so keep it when adding one.

Deep links need no help: the markup is in the initial HTML, so the browser
resolves `#contact` against a target that already exists. The script that used
to wait for the client-side render and re-apply the fragment is gone with the
runtime - don't add it back.

## Assets

- There is no `assets/js/`. It held `dc-runtime.js` and local copies of React
  18.3.1 - ~210 KB that every page downloaded and executed before anything was
  visible - and it went when the pages became plain HTML. The `<image-slot>`
  custom element and its `dc-components.js` had gone the same way earlier: both
  were authoring-time scaffolding that only cost the published site bytes and
  pushed the images behind a custom-element upgrade.
  Artwork is plain `<img>` everywhere - `width`/`height` from the file's own
  pixel size, `alt`, `decoding="async"`, and either `loading="lazy"` or, for the
  four hero images, `fetchpriority="high"`. Crop and corners live in the inline
  style (`object-fit:cover`, `border-radius`), so a new image needs no script.
- `assets/fonts/` - JetBrains Mono and Space Grotesk woff2 subsets, `latin` and
  `latin-ext` only. These are variable-weight faces: one file per subset backs
  every `@font-face` weight alike - 400/500/700 for the mono, 400/500/600/700
  for Space Grotesk. Google Fonts also ships `cyrillic`, `cyrillic-ext`, `greek`
  and `vietnamese` cuts; the German and English copy contains no glyph in those
  ranges, so the files and their `unicode-range` rules were dropped. Re-add the
  matching cut if a page ever needs one.
- `assets/img/` - mascot artwork and icons. Pages reference the `.webp`
  renditions (~1.5 MB in total, down from 8.5 MB); the original `.png`/`.jpeg`
  masters have been removed, so re-encoding a rendition means re-exporting its
  source first, then `magick <src> -resize <w>x\> -strip tmp.png && cwebp -q 82
-alpha_q 90 -m 6`. `cora-og-image.jpg` is the 1200×630 social card and
  `cora-apple-touch-icon.png` the 180×180 iOS icon.
- The two product screenshots live there too -
  `cora-gateway-sessions-dark.webp` and `-light.webp`, 1920×952 - and their PNG
  masters are out of the repo like the artwork masters. They are encoded at
  `-q 92` rather than 82; see _Gateway web UI screenshot_ above for why, and for
  the crop the masters needed first.

## Metadata

Every page carries its `<title>`, `description`, `rel="canonical"`, `hreflang`
alternates, icons, Open Graph and Twitter card tags and a JSON-LD block in
`<head>`, where the parser reads them before anything else. The social crawlers
(Slack, LinkedIn, WhatsApp, X, Facebook) and most AI crawlers fetch the raw HTML
and read `<head>` without executing any script, and the whole page is now raw
HTML, so they see the markup and the metadata alike - the reason the metadata was
kept out of the old `<helmet>` in the first place.

Every URL in the metadata is absolute `https://cora.swiss/...`, so they all need
updating if the domain changes.

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
