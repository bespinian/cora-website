# Keera - static site

Plain static pages, no build step. Eighteen content `.html` files - six pages in
German at the root, English under `en/`, French under `fr/` - plus `404.html`
and three shared files under `assets/`:

- `assets/css/keera.css` - the whole design layer. Markup carries classes only.
- `assets/js/contact-form.js` - the contact form's submit handler.
- `assets/fonts/`, `assets/img/` - woff2 subsets and artwork.

`robots.txt`, `sitemap.xml` and `.htaccess` sit beside them at the root.
`.htaccess` is the only place a response status, a redirect or a cache lifetime
can be set on this host: it wires up `ErrorDocument 404 /404.html`, turns off
directory listings, collapses http/www onto `https://keera.ch`, and sets the
cache lifetimes.

Edit the HTML by hand. A change to a page's shell - header, footer, contact
form, metadata - has to be made in all three language copies; `AGENTS.md` has
the details, along with the content and design rules the pages are written to.

## Deploy over FTP

`.github/workflows/deploy.yml` mirrors the repo onto the Infomaniak host on
every push to `main` (and on manual dispatch), using `lftp`.

- Host: `h2park-8d750cc5.infomaniak.ch` port 21, user `z27etf_github`.
- Add the password as the repository secret `FTP_PASSWORD`
  (Settings -> Secrets and variables -> Actions).
- The host offers **plain FTP only** - no SFTP and no FTPS - so the workflow
  sets `ftp:ssl-allow false`.
- `REMOTE_DIR` is `.`; change it in the workflow if the FTP user does not land
  directly in the site's document root.
- The mirror runs with `--delete`, so a file removed here is removed on the
  host. Only the site files are uploaded - `.git*`, `AGENTS.md`, `README.md`,
  `.ftpquota` and `.well-known/` are excluded. `.ftpquota` is written by the
  host and cannot be deleted, so it has to stay excluded or every run fails.
