# Keera - static site

Plain static pages, no build step. Eighteen content `.html` files - six pages in
German at the root, English under `en/`, French under `fr/` - plus `404.html`
and three shared files under `assets/`:

- `assets/css/keera.css` - the whole design layer. Markup carries classes only.
- `assets/js/contact-form.js` - the contact form's submit handler.
- `assets/fonts/`, `assets/img/` - woff2 subsets and artwork.

Edit the HTML by hand. A change to a page's shell - header, footer, contact
form, metadata - has to be made in all three language copies; `AGENTS.md` has
the details, along with the content and design rules the pages are written to.

## Deploy over SFTP

`.github/workflows/deploy.yml` mirrors the repo onto the Infomaniak host on
every push to `main` (and on manual dispatch), using `lftp` over SFTP.

- Host: `h2park-8d750cc5.infomaniak.ch` port 21, user `z27etf_github`.
- Add the password as the repository secret `SFTP_PASSWORD`
  (Settings -> Secrets and variables -> Actions).
- `REMOTE_DIR` is `.`; change it in the workflow if the SFTP user does not land
  directly in the site's document root.
- The mirror runs with `--delete`, so a file removed here is removed on the
  host. Only the site files are uploaded - `.git*`, `AGENTS.md`, `README.md`
  and `.well-known/` are excluded.
