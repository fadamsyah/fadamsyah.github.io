# fadamsyah.github.io

Source of [fadamsyah.github.io](https://fadamsyah.github.io), the personal homepage of Fadillah Adamsyah Maani (Adam), AI Research Engineer at MBZUAI.

Built with Jekyll on the [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io) template (MIT License).

## Where the content lives

- `_pages/about.md`: page layout, About Me text, and Selected Publications.
- `_data/news.yml`: News items, each with a `type` (paper, preprint, award, challenge, career, education) that sets its tag and filter.
- `_data/experience.yml`, `_data/honors.yml`, `_data/education.yml`: timeline entries (title, organization, location, dates, highlights).
- `_config.yml`: site title, description, and the sidebar (author block).
- `_data/navigation.yml`: top menu.
- `images/avatar.png` and `images/teasers/`: profile picture and publication teasers.

`_includes/news.html` and `_includes/cv-list.html` render the data files; their styles are at the end of `assets/css/main.scss`.

## Google Scholar citations

The `Get Citation Data` workflow crawls Google Scholar daily and writes the stats to the `google-scholar-stats` branch.
The Scholar profile ID (`W-4975wAAAAJ`) is set in `.github/workflows/google_scholar_crawler.yaml`; GitHub Actions must be enabled for the repository.
To run it immediately, open **Actions → Get Citation Data → Run workflow**.
The page shows the total and per-paper citation counts once that branch exists, and hides them until then.

## Local preview

With Docker Desktop running, from the repository root in PowerShell:

```powershell
docker run --rm -it -p 4000:4000 -p 35729:35729 -v "${PWD}:/srv/site" -v jekyll-gems:/usr/local/bundle -w /srv/site ruby:3.3 bash -c "bundle install && bundle exec jekyll serve --host 0.0.0.0 --livereload --force_polling"
```

Then open http://localhost:4000. Edits are picked up automatically; press Ctrl+C to stop.
The first run downloads the gems; later runs reuse them from the `jekyll-gems` volume.

Without Docker, install Ruby and Bundler, run `bundle install`, then `bash run_server.sh`.
