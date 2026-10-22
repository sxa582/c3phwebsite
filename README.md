# C3PH website

Static website for the Center for Cardiovascular Computational and Precision Health at Houston Methodist. GitHub Pages serves the generated HTML files from the repository root. No JavaScript framework or package installation is required.

## Update content

Edit `content/site.json` for team profiles, selected publications, study spotlights, research programs, and patent records. Study spotlights refer to a publication by its zero-based position in the publication list; update that reference when reordering publications.

Shared templates, the homepage sequence, research highlights, and resource descriptions live in `scripts/build.py`. Shared styling and accessible mobile navigation are in `assets/site.css` and `assets/site.js`.

Regenerate and check the site with Python 3:

```sh
python scripts/build.py
python scripts/check.py
node --check assets/site.js
```

Commit both the source changes and regenerated HTML. GitHub Pages continues to use the existing hosting configuration.

## Editorial notes

- Inventory figures were carried forward from the original center website. The Resources page gives their provenance and explains that modality counts are not a completely paired cohort. Verify the inventory with the center before refreshing its reporting date.
- Research highlights use publication years rather than invented announcement dates. Add confirmed month/day dates when available.
- Project summaries describe published research; they do not imply clinical deployment or regulatory authorization.
- Patent records link to public documents and distinguish grant publications from application publications. Licensing inquiries belong with the relevant institutions.
- The existing team mailbox is retained. Collaboration and training links open an email draft; they do not submit a form or create an application.
- The original hero GIF remains in version control for continuity, but no page loads it. The new hero is a lightweight SVG.

The local `.openai/` and `dist/` directories are preview-only and are not part of GitHub Pages publication.

## Editorial visual system

The second design uses locally hosted Space Grotesk and DM Sans, a charcoal/ivory palette with a warm accent, an editorial research spread, a keyboard-accessible data-perspective explorer, and program disclosures. Fonts and their licenses are in `assets/fonts/`.

`assets/atlas.css` applies the visual system across all pages. `assets/atlas.js` controls the data explorer, program disclosures, and reduced-motion-aware artwork response. `scripts/atlas_design.py` renders the homepage and original SVG artwork. The cardiac point cloud is a conceptual illustration generated from mathematical surfaces, not a patient image or a diagnostic model output.

## Center logo

The header, footer, browser icon, and touch icon use `assets/c3ph-heart-orange.png`, a transparent orange adaptation of the heart-and-circuit logo supplied by C3PH. The compact lockup pairs the symbol with live C3PH text so the name remains legible on small screens. The supplied original remains unchanged.

The orange variant was made with the built-in image generation editor. Edit brief: preserve the supplied heart silhouette and circuit paths; recolor the mark warm orange (`#D9754D`); remove the embedded caption for a compact symbol; make the background and circuit cutouts transparent.

## Funding portfolio

Edit `content/funding.json` for the selected awards involving Sadeer Al-Kindi and Khurram Nasir. `scripts/funding_page.py` renders the Funding page. NIH annual records are grouped by core award and subproject, with recipient institution, investigator roles, project periods, annual record amounts, and original RePORTER links retained. The ACHIEVE entry is shown as earlier award records. Pressure Check is sourced to the PCORI award page and the study’s Houston team; its budget is labeled as the full multisite study budget. No aggregate total or C3PH allocation is inferred from institutional award amounts. Public sources were checked on October 22, 2026.
