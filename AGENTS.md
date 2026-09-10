# Cora Website

Eighteen hand-written static content pages plus `404.html`, served straight off
GitHub Pages with no build step. The markup carries classes only; the whole design lives in one
shared stylesheet, `assets/css/cora.css`, and the only JavaScript on the site is
`assets/js/contact-form.js`, loaded by the nine pages that carry a form.

Two things this repo used to be and must not become again: Claude Design decks
(markup inside `<x-dc>` rendered client-side by React) and pages that style
themselves with `style` attributes and an identical 800-line `<style>` block
copied into all eighteen heads. Write plain HTML with classes, and put new rules
in the stylesheet.

## The design brief

The site was rebuilt to be read, not admired. Keep it that way:

- **Quiet, one accent, two schemes.** One blue (`--accent`) on a white or a
  near-black ground, whichever the viewer's system asks for. No gradients, no
  glows, no animation, no second or third accent colour. The artwork supplies
  all the colour the page needs. Every colour goes through a token, so the dark
  scheme stays one block at the top of the stylesheet - a hex value anywhere
  else is a bug, because it can only be right in one of the two schemes.
- **One idea per section.** A heading, at most two short paragraphs, and either
  three or four short cards or one table. If a section needs a fourth
  paragraph, it is two sections or it is cut.
- **Simple language.** Short sentences, plain words, no stacked qualifiers.
  German uses _du_, English _you_, French _vous_.
- **Cora stays.** The mascot and the comic artwork are the point of difference;
  the flashiness around them was not. The home hero is the mascot with her gun
  (`cora-mascot-with-her-gun.webp`, encoded from `badass2.png` in the sibling
  `artwork/` folder outside this repo), and every other page leads with one
  illustration of its own.
- **Let the visuals carry it.** Now that the copy is short, a diagram or an
  illustration is the faster read, so each product page gets one diagram and
  two images rather than another paragraph. A diagram has to say something the
  prose does not - the order of the checks a request passes, the steps of a
  task - or it is decoration and should go.

Things that were deliberately removed and should not come back: the industry
logo strip, the fake terminal session, the four-cell benefit grid, the
integration cards, the pricing tiers, the customer quote, the compliance chip
row (it is one mono line now), the hosted-provider model table, the dark/light
screenshot toggle, and the visible art briefs on the story panels. Two
intermediate drafts of `code.html` went the same way: a five-step `#how` chain
of one task, and a three-up _what it does_ grid (repo-wide reasoning, sandbox,
diff-first). Both described what the agent does step by step before the page
had said what the product **is**; `#what` answers that first. If the sandbox
and the diff-first review need saying again, they belong in a line of an
existing section, not in a grid of their own.

## Pages

- `index.html` - home: hero, the two products, three sovereignty facts, three
  ways to run it as quiet cards, the story teaser, the form.
- `code.html` - Cora Code: hero, what it is as a four-layer stack (`#what`),
  the model table, where it plugs in (beside the pair-programming
  illustration), the form.
- `gateway.html` - Cora Gateway: hero, the request-flow diagram
  (`#architecture`), the web UI shot, four things it controls (beside the
  checkpoint-gate vignette), the form.
- `sovereignty.html` - the layer table, three questions, the open-source stack.
- `sustainability.html` - where the power comes from, the Omnivor contrast, what
  we claim and what we do not.
- `story.html` - the comic in four acts over 24 panels.

`robots.txt`, `sitemap.xml` and `404.html` sit at the root. The sitemap lists all
eighteen content URLs with `xhtml:link` alternates; regenerate it when a page is
added. `404.html` is deliberately not in it.

## The 404 page

GitHub Pages serves `/404.html` for every missing path in all three language
trees - there is no way to give `en/` and `fr/` one of their own - so it is a
single page and it is built differently from the eighteen:

- **Every URL in it is root-absolute** (`/assets/...`, `/code.html`, `/`). It is
  rendered under the URL that was requested, so `en/nope.html` would resolve a
  relative `assets/...` against `/en/` and load nothing. This is the one place in
  the repo where `../assets/...` is wrong.
- **It carries `noindex, follow`** and no canonical, no `hreflang`, no Open
  Graph and no JSON-LD. A soft 404 in the index is worse than none, and there is
  no other-language copy of a page that does not exist to point `hreflang` at.
- **The three languages sit in the body, not in the header.** The DE/FR/EN
  switcher is dropped - it has nothing to switch to - and a `.facts` three-up
  under the hero carries one sentence and one home link per language, each in a
  `<div lang="...">`. The `<h1>` names all three ("Seite nicht gefunden · Page
  not found · Page introuvable") so no language is privileged in the prose.
- Header, footer and nav labels stay German, matching `x-default`. There is no
  form, so it does not load `contact-form.js`. It uses
  `cora-mascot-full-figure.webp` and adds no CSS of its own.

## Languages

Three languages, six pages each. German (Swiss spelling - `ss`, never `ß`) is
the default and lives at the root; English lives under `en/` and French under
`fr/`, with the same six filenames, so `code.html` ↔ `en/code.html` ↔
`fr/code.html`. Filenames stay English in every language - only the prose is
translated. Each page carries a DE/FR/EN switcher in the header, always in that
order with the current language unlinked, and four `rel="alternate" hreflang`
links in `<head>` (`de`, `fr`, `en`, `x-default`); `x-default` points at the
German page. `<html lang>` is `de-CH` at the root, `en` under `en/` and `fr`
under `fr/`.

Adding or editing a page means touching all three copies. Beyond the prose, only
two things differ: asset URLs are `../assets/...` one directory up, and the
switcher points at `../<page>.html` and `../<other>/<page>.html` instead of
`en/<page>.html` and `fr/<page>.html`.

The French copy addresses the reader as _vous_: _tu_ would read wrong to the
banking, insurance and public-sector audience the site is written for. It
follows French punctuation spacing - a `&nbsp;` before `:`, `;`, `?` and `!`,
and inside `«&nbsp;…&nbsp;»` - so those entities appear in the French prose and
nowhere else. **Exception:** `<meta name="description">` and the JSON-LD reuse
the same string, and entities are not decoded inside a `<script>`, so the French
descriptions carry a literal U+00A0 character instead of `&nbsp;`. Recurring
choices worth keeping stable: _souveraineté_, _durabilité_, _poids ouverts_,
_codage agentique_, _dépôt_ for repository, _tenant_ untranslated, _masquage_
for redaction, _groupe_ for Omnivor the company, and _nLPD_ where the German
says revDSG. Every character French adds - `é è à ç ô û œ`, the guillemets
`«»‹›` and the non-breaking space - already sits inside the `latin` /
`latin-ext` font cuts that ship, so no new subset is needed.

`bespinian.io` has no French locale, so the French footer links to the English
`bespinian.io/en/...` imprint.

## Header and footer

The header is one flex row: wordmark, five nav links (the two products,
Sovereignty, Sustainability, the story), and the DE/FR/EN switcher. There is no
header CTA button and no header Contact link - the form is reached from the
hero CTA and from the footer.

It renders three ways: the five labels inline beside the wordmark above 1000px,
on a full-width row of their own between 700px and 1000px, and behind a
hamburger below 700px, where the switcher stays visible beside the toggle so
changing language never needs the menu opened.

The toggle is a `<label>` for the visually hidden `.site-menu-state` checkbox,
and the open state is `.site-menu-state:checked ~ .site-nav` - so the menu needs
no JavaScript. Three things about it are load-bearing:

- The checkbox has to be the `<nav>`'s **preceding sibling**, which is why the
  switcher sits before the nav in the DOM and the row's visual order comes from
  `order` on `.site-nav` (1), `.lang` (2) and `.site-menu-toggle` (3 below
  700px). Reordering the markup breaks the sibling selector.
- It is a checkbox and **not `<details>`**: the same `<nav>` has to render inline
  above the breakpoint, and a closed `<details>` hides its children through a
  slot that CSS cannot reliably re-show.
- The toggle shows only the bars, but the word stays in the markup as
  `.site-menu-text`, hidden with a clip. It is the checkbox's accessible name -
  delete it and the control is announced as unlabelled. It is localised
  (`Menü` / `Menu` / `Menu`).

Because nothing in the header carries inline styles any more, none of these
rules need `!important`, unlike the version of this menu that shipped before.

The footer is one line of prose, one row of links (the five pages, Contact,
Imprint) and one mono line with the copyright and the inference regions. The
older three-column footer with Über uns / Jobs / Security / Models / Deployment
is gone; do not rebuild it.

## Icons

Five line glyphs, all inline `<svg class="icon">` on a 24 viewBox, all drawn
with `stroke="currentColor"` and coloured by CSS - so one piece of markup serves
both schemes - and all `aria-hidden`, because the name they belong to sits right
next to them.

- **The two products**, in the accent: a terminal prompt (`>` and a line) for
  Cora Code, and an arrow through a gate line and out again for Cora Gateway -
  one endpoint everything passes through. Each appears twice per language:
  above the `<h3>` on the home-page product card, and above the eyebrow in that
  product's hero.
- **The three deployment options** on `index.html#deploy`, in `--muted` because
  the cards are deliberately quieter than the products: a cloud for the shared
  Swiss tenant, a two-unit rack for the dedicated one, a building for
  on-premise.

That is seven glyphs per language, twenty-one across the site; keep the copies
identical. Nothing else gets an icon - no nav item, no section heading, no fact
cell. The set reads as meaningful only while it is exactly these five things.

The two brand marks in `#omnivor` on the sustainability pages are **not** part
of that set and must not be drawn into it: `.logo--cora` and `.logo--omnivor`
are filled marks on a 32 viewBox, each in its own side's colour (`--accent` and
`--omnivor`) rather than the one accent. They are built from the same two parts
on purpose - Cora's C open with the square at its mouth, the same square sealed
inside Omnivor's closed O - so the shapes make the section's argument before the
copy does. Cora's is the header wordmark's own geometry; keep it that way.

They also sit differently from the icon set: each one is **inside** its `<h3>`,
to the left of the name, and the heading carries `.logo-head` to lay the two out
as one line. That is why they are 26px against the icon set's 30px - a mark
beside 18px type wants less height than one standing above it.

## Cora's story

The story has its own page, `story.html`, and a short teaser on the home pages.

**Cora is the protagonist, not the closing argument.** She is the subject of the
arc: powerless witness, then traveller, then witness again, then builder. Never
rewrite the page so she arrives only at the end; that was the first draft's
mistake.

She has a sidekick: **Cache**, a male cat who lives in the server room. Cats
notice what nobody else notices and stare at it until somebody follows their
eyes, so Cache _is_ the audit trail, in fur: he stares at the wall in panel 05
and someone just scratches his ears, and in panel 22 the staring finally has
something to point at - a ledger Cora built for him. Keep that pairing intact,
it is the story's main payoff. He is male in all three languages; the French
copy calls him _un chat_ and never _une chatte_, which carries vulgar slang. An
earlier draft used a Swiss marmot called Murmeli; it read as folklore rather
than product, so don't go back to it.

**Omnivor is a company, not a character.** It has no body in any panel: it shows
up as its brand - the colours a hall or a map flips to, the logo on a screen, a
crate in a doorway, the glass tower, a key mounted on that facade like corporate
sculpture. Its cast portrait is its headquarters, not a suited figure. Each
language carries it with a noun whose pronouns then follow: German _der Konzern_
(_er/ihn/sein_), French _un groupe_ (_il/lui/son_ - never feminine _elle_, which
would collide with Cora), English a plain _it/its_. Omnivor is invented, and the
mono footnote that says so out loud is what stops the section reading as an
accusation against a real company - it appears on `story.html`, on the home
teaser and in `sustainability.html` alike, and uses the same noun.

The page runs: hero (title, two-sentence lede, the invented-Omnivor footnote,
and `Vier Akte · 24 Bilder` in the eyebrow), the three-portrait cast strip, the
four acts, the figure-to-function list, the _what we do not claim_ section, and
one closing CTA.

The four acts, each a `<section class="act">` with an eyebrow, a headline and a
one-sentence lede:

- **Act I - the gift** (01-05). The server room; Omnivor arrives with a free
  plugin that genuinely works; Cora watches the relief with nowhere to put
  herself; Cache stares at the cable and only Cora follows his eyes.
- **Act II - the quiet invasion** (06-12). Page 40 of the terms, over the ocean,
  the windowless hall with a Swiss cross in one rack, a web form instead of a
  room, a map that changed colour, and the price tripling on a door with no lock.
- **Act III - what it doesn't pay for** (13-17). Cheap power, Cache by the warm
  river, diesel for uptime, waste heat over dark houses, and the decision on the
  ridge that this is not a law of nature.
- **Act IV - the gate** (18-24). Rebuilt from open weights and vLLM, two
  regions, the gate, Cache's ledger, the heat routed to the valley, and a return
  to the Tuesday morning of panels 01-02.

Act IV pays off earlier panels **by number, in the caption text**: 19 answers
the key in 12, 21 catches the client name from 05, 23 lights the houses that
were dark in 16, and 24 closes the loop on 01-02. Renumbering or dropping a
panel breaks those sentences - fix the captions if you do.

Panels run in a two-column grid. The four act-closing panels (05, 12, 17, 24)
carry `panel--wide`: full width, 16:9, capped at 860px; the rest are 4:3. Every
panel is a `<figure class="panel">` holding the artwork slot and a
`<figcaption>` whose `<b>` is the panel number and whose text is the narration.
The story is carried by those captions - keep them reading as a graphic novel,
concrete and in sequence, not as feature bullets, and keep them short.

Panel 01 is the only slot with real artwork (`cora-story-01.webp`). The other 23
are `<div class="ph">` boxes showing nothing but `PANEL NN`, because the art
brief is production information and does not belong on a public page. Each
placeholder is preceded by an HTML comment holding the exact `<img>` to paste in
its place (`assets/img/cora-story-NN.webp`, 1200×900 for pair panels, 1600×900
for splashes, `loading="lazy"`, the brief pre-filled as `alt`) and the brief
again as a record. Replace the whole placeholder `<div>`, keep the numbering,
and collapse the comment to `<!-- PANEL NN - Brief: ... -->`. Those sizes are a
target, not a crop to force: panel 01 ships at its source's native 1024×768, so
set `width`/`height` from the file and keep the shape the row expects.

The story's setting is **an unnamed small city**, not Bern, so it reads as
anywhere. Bern in the footer is a real company fact and stays. Hosting is
described as Swiss without naming zones - don't reintroduce Zurich or Geneva as
region names, in panel 20 or anywhere else.

The home teaser stays a teaser: eyebrow, headline, one paragraph that sketches
the arc and names Omnivor, a quiet button to `story.html`, and the footnote.
Nothing else - no villain strip, no second paragraph. Its headline introduces
**her**, not the product - _Cora gibt es aus einem Grund_ / _Cora exists for a
reason_ / _Si Cora existe, c'est pour une raison_ - and the paragraph then
opens on _she_, so the reader meets a character before a feature. An earlier
draft headlined it _Cora wurde gegen etwas gebaut_ ("Cora was built against
something"), which framed her as a product decision; don't go back to that.

`sustainability.html` picks the thread up in its own `#omnivor` section: the
take-until-nothing-is-left card against Cora's same-grid-as-the-country card -
each name preceded by its own brand mark, red and blue - the footnote, and a
link to the story. The refusal of the climate-neutral claim
has to survive any rewrite, there and in the story's _what we do not claim_
section.

## Models

`#models` on `code.html` runs one table - `MODELL / KONTEXT / IDEAL FÜR`, three
Cora models and the customer's own fine-tune - followed by one sentence naming
the upstreams (Qwen3-Coder, Apertus) and the Apache-2.0 licence, and one mono
footnote about hosted providers.

That footnote is load-bearing and replaces what used to be a second table: the
hosted models are proprietary, run on the provider's infrastructure and not on
Swiss GPUs, are blocked by default, and a tenant opens them per team and data
class. It also carries the month the lineup was checked (September 2026), because
third-party model names churn - update the stamp when the sentence changes.
`gateway.html` names the same provider in the models column of its flow, so the
two pages move together.

## Gateway web UI screenshot

`#web-ui` on the three `gateway.html` copies sits between the flow and the
feature list: a heading, one paragraph written off the pixels (the metric tiles,
the columns, the served/refused status, the nav groups), the shot in a bordered
`figure.figure--shot`, and a mono caption. Re-shooting the screen means re-reading that
paragraph. The caption says out loud that the figures come from a demo instance,
which is what stops `0.00 CHF` reading as a claim.

Only the dark shot ships (`cora-gateway-sessions-dark.webp`, 1920×952). The
light one and the two-radio no-JS toggle that switched between them are gone;
two dashboards were more chrome than the section could pay for. Below 700px the
frame scrolls sideways rather than shrinking - a 1920px dashboard scaled into a
phone is a grey smudge.

The masters were 3840×1987 browser screenshots carrying three artefacts of the
window they were shot in: the scrollbar as a dark strip down the sidebar's right
edge, a blue focus border down the left, and a bottom cut through the
signed-in-user card. All three went before encoding, on the master rather than
on the finished file, and the result was resized to 1920 wide and encoded at
`cwebp -q 92` rather than the 82 the artwork uses, because this is small UI type
rather than illustration. Any replacement wants the same pass and its own
`width`/`height` read off the encoded file.

## Contact form

Nine pages carry the same form - the `#contact` section of the home page and of
the two product pages in each of the three languages. It posts to Formspree
(`https://formspree.io/f/xvkobjyb`): name, e-mail, company, a checkbox group for
the two products and a free-text message, plus the two hidden fields Formspree
reads itself, `_subject` and the `_gotcha` honeypot. A third hidden field names
the language the enquiry came from, and its own name is localised too:
`Sprache=Deutsch`, `Language=English`, `Langue=Français`. So are the visible
field names, because Formspree puts them straight into the notification mail -
`Name`/`Unternehmen`/`Interesse`, `Name`/`Company`/`Interest`,
`Nom`/`Entreprise`/`Intérêt`; `email` and `message` stay lowercase English in
all three. Interest is a checkbox group rather than radios so one visitor can
ask about Cora Code and Cora Gateway at once. On `code.html` and `gateway.html`
the page's own product is ticked already - a plain `checked` the visitor can
untick.

`assets/js/contact-form.js` takes the submit over. It is delegated off
`document`, posts with `fetch` and `Accept: application/json` so the visitor
never leaves the page, then hides `[data-cf-fields]` and prints the confirmation
into `[data-cf-status]`. All four messages - sending, sent, failed, and "pick a
product" - come from `data-cf-*` attributes on the `<form>`, so one file serves
all nine pages in all three languages. The status line's colour comes from the
classes the handler sets (`is-shown` plus `is-ok` or `is-error`), not from an
inline `style`, so it follows the colour scheme. "At least one product" is the only rule
it checks itself; everything else is native constraint validation.

## The stylesheet

`assets/css/cora.css` is the whole design layer, in this order: four `@font-face`
rules, the tokens, the base elements, then the components. Read it before adding
a class - most sections need nothing new.

- **Tokens** on `:root`: twelve colours - `--bg`, `--surface`, `--card`,
  `--ink`, `--muted`, `--line`, `--accent`, `--accent-hover`, `--btn-ink`,
  `--ok`, `--err`, `--omnivor` - plus the two font stacks, `--wrap` (1040px),
  `--prose` (34rem) and `--radius`. A second accent is a design change, not a
  tweak. `--omnivor` is the exception that proves it: it is the invented
  corporation's red, it colours nothing but that one brand mark, and it stays
  out of buttons, links and headings.
- **Dark scheme**: one `@media (prefers-color-scheme: dark)` block right under
  the tokens, redefining those twelve colours and nothing else. It follows the
  system setting; there is no toggle, and adding one would mean JavaScript plus
  a stored preference on a site that ships neither. `:root` carries
  `color-scheme: light dark` so the UA paints form controls and scrollbars to
  match. The artwork is not touched: the mascot is transparent and sits on
  either ground, and the panels and the screenshot are framed images that carry
  their own light. `@media print` puts the light values back, because a dark
  page prints as a black slab.
- **Contrast**: every text-on-ground pair is at least 5.5:1 in light and 6.7:1
  in dark, and button ink on `--accent` is 6.5:1 / 8:1. Recheck if you retune a
  colour - `--muted` and `--accent` are the two with the least headroom.
- **Layout**: `.wrap` centres and pads any band, `.prose` caps a text column at
  34rem, `.band` is a section with a hairline top border, `.band--alt` adds the
  grey ground. Bands alternate white and grey down the page.
- **Type**: `h1`/`h2` scale with `clamp()`, `.lede` is the 19px intro,
  `.eyebrow` the small mono label above a heading, `.note` the small mono
  footnote, `.mono` for inline code-ish words.
- **Diagrams**: `.flow` is the gateway's request path - three `.flow-stage`
  boxes chained by two `.flow-arrow`s, the middle one `--main` in the accent
  with an ordered `.flow-steps` list, and `.flow-branch` hanging under it for
  the audit log. `.stack` is what Cora Code is, seen in cross-section: four
  `.stack-layer` rows (the API, the models, the inference server, the place)
  sharing their borders inside one rounded block, each a `.stack-label` beside
  a `.stack-text`, with `.stack-layer--api` carrying an inset accent bar
  because the API is the only layer a client touches; it sits in a `.stack-fig`
  `<figure>` with a mono `figcaption`. Both are HTML and CSS, not SVG, so they
  reflow from a row into a column (the flow at 860px, with its arrows rotated
  90deg; the stack's label column at 620px), inherit the colour tokens in both
  schemes, and stay in source order for a screen reader. Arrows are
  `aria-hidden` - they are punctuation, not content.
- **`.split`**: text beside an illustration, one band down from the hero;
  `.split--narrow` gives the image a narrower column and caps it at 300px, for
  a square vignette that would otherwise set the height of the band. Both
  collapse to one column at 780px.
- **`.icon`**: the 30px glyph, coloured from `--accent`; `.card .icon` and
  `.hero .icon` only set its bottom margin.
- **`.card--quiet`**: a card with no border on a `--surface` tint and a
  `--muted` icon - the deployment options, which must not compete with the two
  product cards above them on the same page.
- **Blocks**: `.grid` (auto-fit cards, `.grid--two` for the two product cards),
  `.card`, `.facts` (borderless three-up, `.facts--four` for a four-item group,
  which goes two-up rather than three plus an orphan), `.plain-list`
  (dash-marked list), `.table-wrap` + plain `<table>` (`td.tight` keeps a short
  value like `dein Tenant` on one line; below its `min-width` the wrap
  scrolls sideways), `.figure`, `.hero` /`.hero--split` /
  `.hero-art`, `.btn` / `.btn--quiet` / `.btn-row` / `.arrow`, the form controls
  (`.form`, `.field`, `.label`, `.input`, `.choices`, `.choice`,
  `.form-actions`, `.form-status` with `.is-shown` / `.is-ok` / `.is-error`,
  `.hp`), and the story's `.act`, `.panels`,
  `.panel`, `.panel--wide`, `.ph`, `.cast`.
- **Grids** are written `repeat(auto-fit, minmax(min(100%, Npx), 1fr))`: the
  `min(100%, …)` is what lets a track collapse below `N` instead of overflowing,
  so keep it when adding one.
- **Breakpoints**, all of them: 1000px (nav takes its own row), 780px (a split
  hero stacks), 700px (nav becomes the hamburger panel, and the screenshot
  frame scrolls), 620px (story panels go one column, and the stack's label
  column stacks). Plus `pointer: coarse` for touch padding on the three link rows, a
  `print` block, and `prefers-reduced-motion` for the smooth scroll.
- **Page-wide guards** that only matter on a narrow viewport:
  `-webkit-text-size-adjust: 100%`, `overflow-wrap: break-word` and
  `max-width: 100%` on `img`/`svg`.

Text stays at or above 16px in inputs - iOS Safari zooms the page in when a
focused input is smaller, so do not tune that number down.

Deep links need no help: the markup is in the initial HTML, so the browser
resolves `#contact` against a target that already exists.

## Assets

- `assets/css/cora.css` - the stylesheet. One file, no imports.
- `assets/js/contact-form.js` - the form handler, loaded `defer` by the nine
  pages with a form. Nothing else on the site runs JavaScript, and no page needs
  a runtime: the React/`dc-runtime.js` era cost every page ~210 KB before
  anything was visible.
- `assets/fonts/` - JetBrains Mono and Space Grotesk woff2 subsets, `latin` and
  `latin-ext` only. Every head preloads the two `latin` cuts
  (`<link rel="preload" as="font" type="font/woff2" crossorigin>`, before the
  stylesheet link): the browser would otherwise only discover them after parsing
  `cora.css`, a round trip that delays first paint. `crossorigin` is required
  even though the files are same-origin - fonts are fetched in anonymous CORS
  mode, and without it the preload is thrown away and fetched a second time. The
  two `latin-ext` cuts are deliberately **not** preloaded: German umlauts and
  French accents all sit inside `latin`, so `latin-ext` rarely matches and
  preloading it would compete with the hero image for bandwidth. Both are variable-weight faces, so one file per subset backs
  a whole `font-weight: 400 700` range and the stylesheet needs exactly four
  `@font-face` rules. Google Fonts also ships `cyrillic`, `cyrillic-ext`, `greek`
  and `vietnamese` cuts; no page contains a glyph in those ranges, so they were
  dropped. Re-add the matching cut if one ever does.
- `assets/img/` - mascot artwork and icons. Pages reference the `.webp`
  renditions; the `.png`/`.jpeg` masters have been removed, so re-encoding a
  rendition means re-exporting its source first, then
  `magick <src> -resize <w>x\> -strip tmp.png && cwebp -q 82 -alpha_q 90 -m 6`.
  `cora-og-image.jpg` is the 1200×630 social card and `cora-apple-touch-icon.png`
  the 180×180 iOS icon. Seven renditions are currently unused and are fair game
  for a new section: `cora-mascot-full-figure`,
  `cora-the-swiss-sovereign-coding-agent-mascot` (the previous home hero),
  `cora-firing-an-energy-beam`, `cora-at-a-dashboard-of-dials-and-gauges`,
  `cora-redacting-confidential-data`,
  `cora-routing-data-centre-waste-heat-to-a-town` and
  `cora-gateway-sessions-light`. Artwork is plain `<img>` everywhere - `width`/`height`
  from the file's own pixel size, `alt`, `decoding="async"`, and either
  `loading="lazy"` or, for the hero images, `fetchpriority="high"`. Crop and
  corners come from the stylesheet, so a new image needs no rule of its own.

## Metadata

Every content page carries its `<title>`, `description`, `rel="canonical"`,
`hreflang` alternates, icons, Open Graph and Twitter card tags and a JSON-LD
block in `<head>` (`404.html` is the exception - see above), where the parser reads them before anything else. Social and AI
crawlers fetch the raw HTML and read `<head>` without executing script, and the
whole page is raw HTML, so they see the markup and the metadata alike.

Every URL in the metadata is absolute `https://cora.swiss/...`, so they all need
updating if the domain changes. Canonicals, `og:url` and the sitemap use the
directory form for the three home pages - `https://cora.swiss/`,
`/en/`, `/fr/`, not `/index.html` - because that is what GitHub Pages serves and
what inbound links point to. Internal links match: `href="./"` for the home page
of the current language.

The JSON-LD is one `@graph` per page: `Organization` + `WebSite` on the three
home pages, `BreadcrumbList` on the subpages, plus a `SoftwareApplication` on
`code.html` and `gateway.html`. The `Organization` has no `sameAs` yet - add the
company's social and directory profiles there once they exist; it is the main
signal that ties the domain to a real entity.
