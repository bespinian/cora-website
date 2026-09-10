# Cora - static site

Plain static pages, no build step. Eighteen content `.html` files - six pages in
German at the root, English under `en/`, French under `fr/` - plus `404.html`
and three shared files under `assets/`:

- `assets/css/cora.css` - the whole design layer. Markup carries classes only.
- `assets/js/contact-form.js` - the contact form's submit handler.
- `assets/fonts/`, `assets/img/` - woff2 subsets and artwork.

Edit the HTML by hand. A change to a page's shell - header, footer, contact
form, metadata - has to be made in all three language copies; `AGENTS.md` has
the details, along with the content and design rules the pages are written to.

## Deploy on GitHub Pages

1. Push the contents of this folder to a repo (root or a `docs/` folder).
2. Settings → Pages → Source: "Deploy from a branch", pick the branch and folder.
3. `index.html` is the home page; `.nojekyll` keeps Jekyll from touching the files.
