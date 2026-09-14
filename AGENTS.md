# Keera Website

Eighteen hand-written static content pages plus `404.html`, served straight off
an Infomaniak Apache host with no build step - `.github/workflows/deploy.yml`
mirrors the repo there over FTP on every push to `main`. Response behaviour that
static files cannot express - the 404, the canonical host, cache lifetimes,
directory listings off - lives in `.htaccess` at the root. The markup carries classes only; the whole
design lives in one shared stylesheet, `assets/css/keera.css`, and the only
JavaScript on the site is `assets/js/contact-form.js`, loaded by the nine pages
that carry a form.

Two things this repo used to be and must not become again: Claude Design decks
(markup inside `<x-dc>` rendered client-side by React) and pages that style
themselves with `style` attributes and an identical 800-line `<style>` block
copied into all eighteen heads. Write plain HTML with classes, and put new rules
in the stylesheet.

## The design brief

The site was rebuilt to be read, not admired. Keep it that way:

- **Quiet, one accent, two schemes.** One accent colour on a white or a
  near-black ground, whichever the viewer's system asks for. No gradients, no
  glows, no animation, no second or third accent on a page. The artwork supplies
  all the colour the page needs. Every colour goes through a token, so the dark
  scheme stays one block at the top of the stylesheet - a hex value anywhere
  else is a bug, because it can only be right in one of the two schemes.
  The accent is blue (`--accent`) everywhere but the three sustainability
  pages, which carry `class="theme-leaf"` on `<body>` and run the same design
  in green (`--leaf`). That is a **swap, not an addition** - no page shows both
  - and it is the one page whose subject is the colour: it argues about clean
    power, so the colour it is drawn in is part of the argument. Do not give any
    other page a theme class, and do not let green leak off these three.
- **One idea per section.** A heading, at most two short paragraphs, and either
  three or four short cards or one table. If a section needs a fourth
  paragraph, it is two sections or it is cut.
- **Simple language.** Short sentences, plain words, no stacked qualifiers.
  German uses _du_, English _you_, French _vous_.
- **Keera stays.** The mascot and the comic artwork are the point of difference;
  the flashiness around them was not. The home hero is the mascot with her gun
  (`keera-mascot-with-her-gun.webp`, encoded from `badass2.png` in the sibling
  `artwork/` folder outside this repo), the Keera Code hero is Keera at her
  laptop (`keera-coding-on-a-laptop.webp`, from `laptop.png`), the Keera Gateway
  hero is Keera striding through a lit gate
  (`keera-walking-through-a-gateway.webp`, from `gate.png`), the Souveränität
  hero is Keera patching a server rack
  (`keera-plugging-a-cable-into-a-server-rack.webp`, from `data-center.png`),
  and every other page leads with one illustration of its own. All four of those
  heroes are cut-outs on transparent ground, so they sit in a bare `.hero-art`
  figure. Artwork with its own background would need a border and a surface
  tint under it; the rule that did that was dropped once no page used it.
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

Keera Gateway is the more important of the two products and comes first wherever
they are listed together: the header nav, the footer row, the two home cards,
the interest checkboxes in the form, the sitemap, and the sentence that opens
the home page. Keep new lists in that order.

- `gateway.html` - Keera Gateway: hero, the request-flow diagram
  (`#architecture`), four things it controls (`#security`, cards only - the
  checkpoint-gate vignette that used to sit beside them is gone), the web UI
  shot, the six features (`#features`), the eight questions (`#faq`), the
  form. Its only illustration is the
  hero; the dashboard shot stays because the section is written off its pixels.
  `#security` and `#features` are the same page twice at two altitudes and have
  to stay that way round: `#security` is what the endpoint decides for the
  business, `#features` is what the product is made of - guardrails, smart
  filters, smart routers, the live map, sessions, SSO and roles, one `.card`
  each in a `.grid` on a `band--alt`. It is the one six-card section on the
  site, which is why it is also the one that gets no second sentence of framing:
  three or four cards is the rule everywhere else. The six names are the
  gateway's own, so a card renamed here is a screen renamed in the product;
  check the gateway repo before rewording one. No icons - the set is closed at
  eight glyphs per language. `#faq` is the last word before the form and the
  one section that answers rather than asserts - see below.
- `code.html` - Keera Code: hero, what it is as a four-layer stack (`#what`),
  the model table, where it plugs in (beside the pair-programming
  illustration), the form.
- `sovereignty.html` - the layer table, three questions, what the gateway routes
  abroad and what it does not, the open-source stack. Its hero is its only
  image; the control-room vignette that used to sit beside "Souverän heisst
  nicht abgeschottet" is gone. The argument is Keera
  Gateway's: one endpoint every request passes, a policy and an audit log that
  are yours. Keera Code is one client of it, not the subject.
- `sustainability.html` - two levers and one story: how we pick infrastructure
  partners (`#partners`, on the renewable share that actually runs a site),
  how Keera spends fewer tokens (`#tokens`, smaller models, routing, caching),
  the Omnivor contrast, what we claim and what we do not. Swiss hosting is a
  fact on the page, not the argument - a mono line under `#partners` says out
  loud that a Swiss address alone is not a sustainability argument, and the
  page must not drift back to leading with the grid. It carries its hero
  illustration and no other image: a draft that put the waste-heat rendition
  beside `#partners` was cut, because a page gets one hero image and that is
  it.
- `story.html` - the comic in four acts, four rendered pages, 24 panels.

`robots.txt`, `sitemap.xml`, `llms.txt`, `404.html` and `.htaccess` sit at the
root. The sitemap lists all eighteen content URLs with `xhtml:link` alternates
and a `<lastmod>`; regenerate it when a page is added, and touch the `<lastmod>`
of any page whose content actually changed. It carries no `<changefreq>` and no
`<priority>` - Google ignores both, and `<lastmod>` is the one field it reads.
`404.html` is deliberately not in it.

`llms.txt` is the [llmstxt.org](https://llmstxt.org/) file: an H1, a blockquote
summary, a few lines of orientation, then `## Overview`, `## Products`,
`## Background` and `## Optional`, each a list of `[title](url): description`
links. It is Markdown despite the `.txt` name, and the H1 is what Lighthouse's
llms.txt audit checks for - a missing file reads there as "Fetch of llms.txt
failed", not as "no such file". Only six of the eighteen URLs are in it, the
English copies, with the German and French home pages under `## Optional`: the
file is a short orientation for a model, not a second sitemap, and the pages
carry `hreflang` alternates anyway. The descriptions are the pages' own
`<meta name="description">` strings, so a reworded description belongs in both
places. Add a line here when a page is added, and leave the products in
gateway-then-code order.

## The 404 page

`ErrorDocument 404 /404.html` in `.htaccess` serves `/404.html` for every missing
path in all three language trees - there is no way to give `en/` and `fr/` one
of their own - so it is a single page and it is built differently from the
eighteen. **Without that line Apache answers with its own stock error page and
this file is never reached**, which is what happened for as long as the repo
still assumed it was on GitHub Pages:

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
  `keera-coding-on-a-laptop.webp` and adds no CSS of its own.

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

The header is one flex row: wordmark, five nav links (Gateway, Code,
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

Six line glyphs, all inline `<svg class="icon">` on a 24 viewBox, all drawn
with `stroke="currentColor"` and coloured by CSS - so one piece of markup serves
both schemes - and all `aria-hidden`, because the name they belong to sits right
next to them.

- **The two products**, in the accent: an arrow through a gate line and out
  again for Keera Gateway - one endpoint everything passes through - and a
  terminal prompt (`>` and a line) for Keera Code. Each appears twice per language:
  above the `<h3>` on the home-page product card, and above the eyebrow in that
  product's hero.
- **The three deployment options** on `index.html#deploy`, in `--muted` because
  the cards are deliberately quieter than the products: a cloud for the shared
  Swiss tenant, a two-unit rack for the dedicated one, a building for
  on-premise.

- **The leaf** in the `<h2>` of `#partners` on the sustainability pages, to the
  left of the words rather than above them: the heading carries `.icon-head`
  and the `<svg>` is inside it. It is the one glyph that sits beside a section
  heading rather than over a name, and it belongs to `#partners` because that
  section is the one about where the power comes from - it was drafted over
  `#tokens` and moved. It takes no colour of its own: it is a plain `.icon`,
  and on those three pages the accent is already the green it wants, which is
  why the leaf and the theme swap have to stay together.

That is eight glyphs per language, twenty-four across the site; keep the copies
identical. Nothing else gets an icon - no nav item, no other section heading, no
fact cell. The set reads as meaningful only while it is exactly these six
things.

The two brand marks in `#omnivor` on the sustainability pages are **not** part
of that set and must not be drawn into it: `.logo--keera` and `.logo--omnivor`
are filled marks on a 32 viewBox, each in its own side's colour (`--accent` and
`--omnivor`) rather than the one accent. They are built from the same two parts
on purpose - Keera's K open with the square in its throat, the same square
sealed inside Omnivor's closed O - so the shapes make the section's argument
before the copy does. Keera's is the header wordmark's own geometry; keep it
that way.

Since the page went green, `.logo--keera` follows `--accent` into green and the
pair reads red against green - the one contrast a red-green colour deficiency
flattens. It is why the shapes above are load-bearing rather than decorative:
the open mark against the sealed one has to carry the section on its own, and
the `<h3>` beside each mark names its side in words. Do not rebuild that
section so colour is the only thing telling the two apart.

They also sit differently from the icon set: each one is **inside** its `<h3>`,
to the left of the name, and the heading carries `.logo-head` to lay the two out
as one line. That is why they are 26px against the icon set's 30px - a mark
beside 18px type wants less height than one standing above it.

`.icon-head`, which puts the leaf inside the `#partners` `<h2>`, is the same row
built for the other case and the two share their declarations. The differences
are the ones a section heading forces: it aligns on `flex-start` rather than
`center`, because an `<h2>` that wraps would leave a mark centred against both
lines sitting beside neither, and the glyph is sized `1.15em` rather than in
pixels, because the heading is a `clamp()` and a fixed mark would swamp it at
24px and get lost at 31px.

That `<h2>` is also **the one heading on the site that sits outside `.prose`**,
as a direct child of `.wrap`. The 34rem measure is there to keep paragraphs
readable, and at 31px it is about 30px short of holding the German heading and
the leaf on one line - the wrap looked like an accident, because a flex row puts
the second line under the first rather than under the icon. Out in `.wrap` the
German and English headings hold one line down to a ~500px viewport. The French
one, _Comment nous choisissons nos partenaires d'infrastructure_, needs ~914px
and so still wraps below roughly a 970px viewport; shortening it is the only fix
left, and it is a prose decision, not a layout one. Lifting the heading also put
it under `.band > .wrap > * + *` (28px, the band rhythm) instead of `h2 + p`
(14px, what a heading wants over its own paragraph), which is why
`.icon-head + .prose` restates the gap. Do not take any other `<h2>` out of
`.prose` to match - headings wrapping inside the measure is the site's normal,
and `index.html` has longer ones that do.

## Keera's story

The story has its own page, `story.html`, and a short teaser on the home pages.

**Keera is the protagonist, not the closing argument.** She is the subject of
the arc: powerless witness, then traveller, then witness again, then builder.
Never rewrite the page so she arrives only at the end; that was the first
draft's mistake.

She has a sidekick: **Cache**, a male cat who lives in the server room. Cats
notice what nobody else notices and stare at it until somebody follows their
eyes, so Cache _is_ the audit trail, in fur: he stares at the wall in panel 05
and someone just scratches his ears, and in panel 22 the staring finally has
something to point at - a ledger Keera built for him. Keep that pairing intact,
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
would collide with Keera), English a plain _it/its_. Omnivor is invented, and
the mono footnote that says so out loud is what stops the section reading as an
accusation against a real company - it appears on `story.html`, on the home
teaser and in `sustainability.html` alike, and uses the same noun.

The page runs: hero (title, two-sentence lede, the invented-Omnivor footnote,
and `Vier Akte · 24 Bilder` in the eyebrow), the three-portrait cast strip, the
four acts, the figure-to-function list, the _what we do not claim_ section, and
one closing CTA.

The four acts, each a `<section class="act">` with an eyebrow, a headline and a
one-sentence lede:

- **Act I - the gift** (01-05). The server room; Omnivor arrives with a free
  plugin that genuinely works; Keera watches the relief with nowhere to put
  herself; Cache stares at the cable and only Keera follows his eyes.
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

The 24 panels are **drawn, lettered and numbered inside four rendered comic
pages**, one per act - page 1 is panels 01-05, page 2 is 06-12, page 3 is 13-17,
page 4 is 18-24. The earlier layout, a two-column grid of 24 single-panel
figures with the narration in each `<figcaption>`, is gone; so is the
`keera-story-NN.webp` naming. Do not rebuild it.

Each act therefore holds exactly one `<figure class="comic">`: the page image,
then a `<figcaption>` whose `<details>` opens a `<ol class="script">` transcript
of that page's panels. The transcript is not decoration. A screen reader cannot
read lettering baked into artwork, crawlers cannot either, and act IV's
cross-references only work if the numbering is readable as text - so the `<ol>`
carries `start="1"`, `start="6"`, `start="13"` and `start="18"` and the numbers
come from `list-style: decimal-leading-zero`, which reproduces the artwork's own
`01`-`24`. Its `<li>` text **is** the panel narration the old figcaptions
carried, verbatim: keep it reading as a graphic novel, concrete and in sequence,
not as feature bullets, and keep it short.

The artwork is per language - the lettering is drawn into the panels, so all
three languages carry their own four pages, at
`assets/img/keera-story-<de|fr|en>-page-<1-4>.webp`. All twelve ship. The pages
are portrait and their source dimensions vary per language (page 3 is 1086×1448
in English and 1087×1447 in German and French), so take `width`/`height` from
the file rather than from a table. Encode from the PNG master with
`cwebp -q 82 -m 6 -sharp_yuv`, which lands each page around 270-370 KB; below
q 80 the lettering starts to mush, and all four are `loading="lazy"` so only the
first is on the critical path.

Because the words live in the artwork, **a copy change is a re-render, in three
languages.** Edit a transcript `<li>` and the page above it still says the old
thing. The lettering is generated and drifts from the copy: it has produced
Swiss dialect where the prose is Standard German, inverted whole panels, and
still spells the gate `CORA GATEWAY` in panel 21 from before the rename. Check a
new page against the transcript panel by panel before shipping it.

The `alt` describes the page as a page - what is drawn in its panels, in
sequence - because the transcript below it already carries the words. Do not
paste the narration into `alt` as well.

The story's setting is **an unnamed small city**, not Bern, so it reads as
anywhere. Bern in the footer is a real company fact and stays. Hosting is
described as Swiss without naming zones - don't reintroduce Zurich or Geneva as
region names, in panel 20 or anywhere else.

The home teaser stays a teaser: eyebrow, headline, one paragraph that sketches
the arc and names Omnivor, a quiet button to `story.html`, and the footnote.
Nothing else - no villain strip, no second paragraph. Its headline introduces
**her**, not the product - _Keera gibt es aus einem Grund_ / _Keera exists for a
reason_ / _Si Keera existe, c'est pour une raison_ - and the paragraph then
opens on _she_, so the reader meets a character before a feature. An earlier
draft headlined it _Keera wurde gegen etwas gebaut_ ("Keera was built against
something"), which framed her as a product decision; don't go back to that.

`sustainability.html` picks the thread up in its own `#omnivor` section: the
take-until-nothing-is-left card against Keera's picked-on-renewables card -
each name preceded by its own brand mark, red and blue - the footnote, and a
link to the story. The refusal of the climate-neutral claim
has to survive any rewrite, there and in the story's _what we do not claim_
section.

## The gateway FAQ

`#faq` sits between `#features` and the form on the three `gateway.html`
copies, and nowhere else. Eight questions, each a `<details>` the visitor
opens: a heading, one sentence of framing, then the list in a `.faq`. It is the
one section that answers a question instead of making a claim, which is why it
is the last thing before the form.

The order is the argument, and it is not the order the questions arrive in.
Privacy, security and the AI Act come first because the banking, insurance and
public-sector reader is buying those; the comparison and Claude Code come next
because that is what decides adoption; latency, footprint and cloud-native come
last, as a pair and a coda, because they are the questions that no longer stop
anyone. Re-sorting it by how often a question is asked would put the overhead
question on top and bury the privacy answer, which is the page's strongest.

Three answers are load-bearing and must not be softened into a maybe:

- **The prompt answer draws the line at content, not at the record.** The
  gateway does keep the request - who, when, which model, how many tokens,
  which decision - and that record is what `#security` and `#web-ui` sell two
  sections up as the audit log and the cost-per-team figure. What is never
  stored is the _content_: the prompt and the model's answer. An earlier draft
  answered a flat "No. Never." to "do you store my prompts and requests" and
  contradicted the rest of the page; do not let it drift back. The question is
  about prompts alone for the same reason.
- **The AI Act answer ends by handing the compliance work back.** "Die
  Compliance-Arbeit bleibt deine" is the same refusal as the story's _what we do
  not claim_: the gateway supplies evidence, not a certificate.
- **The latency answer names its own exception.** The microsecond figure is the
  path through policy, budget and log. Smart Filters and Smart Routers call a
  small model and so cost more than that; the answer says so rather than
  letting `#features` contradict it.

The differentiator answer is the sovereignty argument in miniature - enterprise
support from us, and no client or library of its own, so the customer stays
independent "of us as well". Do not rewrite it into a feature comparison
against a named competitor.

`<details>` is the second disclosure on the site after the story transcripts and
needs no JavaScript, so the site still ships one script. It keeps its native
marker: the icon set is closed at eight glyphs and a disclosure triangle is not
a ninth. The questions are plain `<summary>` text rather than headings inside
one - the outline gains little and screen readers announce the nesting badly -
so the JSON-LD below is what carries the Q&A to a crawler.

The eight are mirrored in a `FAQPage` node in each page's JSON-LD `@graph`, and
**that copy is duplicated prose**: edit an answer in the markup and the `@graph`
still says the old thing. Regenerate it from the markup rather than retyping it,
and remember the `<script>` decodes no entities - the French node carries
literal U+00A0 characters where the prose writes `&nbsp;`, exactly as the French
`description` does.

## Models

`#models` on `code.html` runs one table - `MODELL / KONTEXT / IDEAL FÜR`, three
Keera models and the customer's own fine-tune - followed by one sentence naming
the upstreams (Qwen-Coder, Apertus) and the Apache-2.0 licence, and one mono
footnote about hosted providers.

That footnote is load-bearing and replaces what used to be a second table: the
hosted models are proprietary, run on the provider's infrastructure and not on
Swiss GPUs, are blocked by default, and a tenant opens them per team and data
class. It also carries the month the lineup was checked (September 2026), because
third-party model names churn - update the stamp when the sentence changes.
`gateway.html` names the same provider in the models column of its flow, so the
two pages move together.

## Gateway web UI screenshot

`#web-ui` on the three `gateway.html` copies sits between `#security` and the
feature list: a heading, two paragraphs written off the pixels (the metric tiles,
the columns, the served/refused status, the nav groups), the shot in a bordered
`figure.figure--shot`, and a mono caption. The first paragraph is the control
half - web UI and CLI writing the same versioned policy - and the second is the
visibility half: tokens, cost and refused requests per team, model and period,
in the browser or as CSV. That second paragraph is the page's observability
claim and the only place it is made, so it stays even if the rest of the section
is rewritten. Re-shooting the screen means re-reading both
paragraphs. The caption says out loud that the figures come from a demo instance,
which is what stops `0.00 CHF` reading as a claim.

Only the dark shot ships (`keera-gateway-sessions-dark.webp`, 1920×952). The
light one and the two-radio no-JS toggle that switched between them are gone -
the rendition has been deleted too; two dashboards were more chrome than the
section could pay for. Re-adding a light shot means re-shooting it. Below 700px the
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
ask about Keera Gateway and Keera Code at once. On `code.html` and
`gateway.html` the page's own product is ticked already - a plain `checked` the
visitor can untick.

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

`assets/css/keera.css` is the whole design layer, in this order: four
`@font-face` rules, the tokens, the base elements, then the components. Read it
before adding a class - most sections need nothing new.

- **Tokens** on `:root`: thirteen colours - `--bg`, `--surface`, `--card`,
  `--ink`, `--muted`, `--line`, `--accent`, `--accent-hover`, `--btn-ink`,
  `--ok`, `--err`, `--omnivor`, `--leaf` - plus the two font stacks, `--wrap`
  (1040px), `--prose` (34rem) and `--radius`. A second accent on one page is a
  design change, not a tweak. The last two are the exceptions that prove it,
  and each is read from exactly one place: `--omnivor` is the invented
  corporation's red and colours nothing but its brand mark, `--leaf` is the
  green the `.theme-leaf` block hands to `--accent` on the sustainability
  pages. Nothing else may read either one.
- **The green theme**: `.theme-leaf` sits directly under the dark-scheme block
  and is two rules - `--accent: var(--leaf)` plus an `--accent-hover`, and a
  dark-scheme copy that restates the hover shade alone. `--accent` needs saying
  once because `--leaf` is already per-scheme; the hover is a literal hex and so
  is not. Custom properties inherit, so a declaration on `<body>` beats `:root`
  for the whole subtree no matter where it sits in the file or in which media
  block - which is also why the print block needs no copy of it.
- **Dark scheme**: one `@media (prefers-color-scheme: dark)` block right under
  the tokens, redefining those thirteen colours and nothing else. It follows the
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
  the audit log. `.stack` is what Keera Code is, seen in cross-section: four
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
  `code.html` is the only page using it. Collapses to one column at 780px. A
  `.split--narrow` modifier once capped the image at 300px for a square
  vignette; it went with the Souveränität vignette it was written for.
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
  scrolls sideways), `.figure`, `.faq` (the gateway's question list: a
  hairline-ruled column of `<details>` capped at the prose measure), `.hero` /`.hero--split` /
  `.hero-art`, `.btn` / `.btn--quiet` / `.btn-row` / `.arrow`, the form controls
  (`.form`, `.field`, `.label`, `.input`, `.choices`, `.choice`,
  `.form-actions`, `.form-status` with `.is-shown` / `.is-ok` / `.is-error`,
  `.hp`), and the story's `.act`, `.comic`, `.ph`, `.script`, `.cast`.
- **Grids** are written `repeat(auto-fit, minmax(min(100%, Npx), 1fr))`: the
  `min(100%, …)` is what lets a track collapse below `N` instead of overflowing,
  so keep it when adding one.
- **Breakpoints**, all of them: 1000px (nav takes its own row), 780px (a split
  hero stacks), 700px (nav becomes the hamburger panel, and the screenshot
  frame scrolls), 620px (the stack's label column stacks). Plus `pointer: coarse` for touch padding on the three link rows, a
  `print` block, and `prefers-reduced-motion` for the smooth scroll.
- **Page-wide guards** that only matter on a narrow viewport:
  `-webkit-text-size-adjust: 100%`, `overflow-wrap: break-word` and
  `max-width: 100%` on `img`/`svg`.

Text stays at or above 16px in inputs - iOS Safari zooms the page in when a
focused input is smaller, so do not tune that number down.

Deep links need no help: the markup is in the initial HTML, so the browser
resolves `#contact` against a target that already exists.

## Assets

- `assets/css/keera.css` - the stylesheet. One file, no imports.
- `assets/js/contact-form.js` - the form handler, loaded `defer` by the nine
  pages with a form. Nothing else on the site runs JavaScript, and no page needs
  a runtime: the React/`dc-runtime.js` era cost every page ~210 KB before
  anything was visible.
- `assets/fonts/` - JetBrains Mono and Space Grotesk woff2 subsets, `latin` and
  `latin-ext` only. Every head preloads the two `latin` cuts
  (`<link rel="preload" as="font" type="font/woff2" crossorigin>`, after the
  hero image preload and before the stylesheet link): the browser would
  otherwise only discover them after parsing
  `keera.css`, a round trip that delays first paint. `crossorigin` is required
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
  rendition means re-exporting its source first, then `magick <src> -resize
<w>x\> -strip tmp.png && cwebp -q 82 -alpha_q 90 -m 6`. `keera-og-image.jpg`
  is the 1200×630 social card and `keera-apple-touch-icon.png` the 180×180 iOS
  icon. Every rendition in the folder is referenced by a page; the ten that
  had been sitting unused - previous heroes and never-placed spares - were
  deleted rather than carried, since the deploy mirrors the whole folder to the
  host. A new section needs new artwork, encoded from `artwork/` outside this
  repo. Artwork is plain `<img>` everywhere -
  `width`/`height` from the file's own pixel size, `alt`, `decoding="async"`,
  and either `loading="lazy"` or, for the hero images, `fetchpriority="high"`.
  Crop and corners come from the stylesheet, so a new image needs no rule of its
  own. **Every head preloads its own hero image**
  (`<link rel="preload" as="image" fetchpriority="high">`) as the first hint in
  the head, ahead of the two font preloads. The host only speaks HTTP/1.1, so
  the six connections a browser will open are the whole budget and the request
  made first gets one first; discovered down in the body, the hero art used to
  queue behind the fonts and the stylesheet, and PageSpeed measured 1.19s of LCP
  resource load delay against an image that then took 1.83s to arrive. The
  preload href must match the `<img src>` exactly - deploy stamps both with the
  same `?v=` hash, and a mismatch would download the image twice. A page that
  changes its hero changes both.

## Metadata

Every content page carries its `<title>`, `description`, `rel="canonical"`,
`hreflang` alternates, icons, Open Graph and Twitter card tags and a JSON-LD
block in `<head>` (`404.html` is the exception - see above), where the parser reads them before anything else. Social and AI
crawlers fetch the raw HTML and read `<head>` without executing script, and the
whole page is raw HTML, so they see the markup and the metadata alike.

Every URL in the metadata is absolute `https://keera.ch/...`, so they all need
updating if the domain changes. Canonicals, `og:url` and the sitemap use the
directory form for the three home pages - `https://keera.ch/`,
`/en/`, `/fr/`, not `/index.html` - because that is what the host serves for a
directory and what inbound links point to. Internal links match: `href="./"` for the home page
of the current language.

The JSON-LD is one `@graph` per page: `Organization` + `WebSite` on the three
home pages, `BreadcrumbList` on the subpages, plus a `SoftwareApplication` on
`code.html` and `gateway.html`, and a `FAQPage` on `gateway.html` alone.

Keera itself still has no social or directory profiles, so its `Organization`
carries no `sameAs`; the `parentOrganization` node points at bespinian's, which
is what currently ties the domain to a real entity. Give Keera its own `sameAs`
the moment it has a profile of its own - only real, verified URLs belong there.

Every page carries its own Open Graph image, 1200x630, built from that page's
artwork composited on the `#091023` navy of `keera-og-image.jpg`. The home pages
keep `keera-og-image.jpg`; the rest use `keera-og-<page>.jpg`. `og:image:alt`
describes the artwork in the page's own language.
