# Cora - static site

Plain static pages. No build step: each `.html` is ordinary HTML that links to
shared files under `assets/`, so the browser streams and caches them normally.

## Deploy on GitHub Pages

1. Push the contents of this folder to a repo (root or a `docs/` folder).
2. Settings → Pages → Source: "Deploy from a branch", pick the branch and folder.
3. `index.html` is the home page; `.nojekyll` keeps Jekyll from touching the files.
