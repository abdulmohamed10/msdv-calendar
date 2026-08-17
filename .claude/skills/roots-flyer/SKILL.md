---
name: roots-flyer
description: >-
  Generate event flyers in the ROOTS (@rootsdfw) visual identity — an editorial,
  magazine-cover look with a full-bleed atmospheric photo, a dark scrim, an
  elegant serif headline, warm-white sans details, and an "Org / Category"
  lockup bottom-right. Use this whenever someone wants a flyer, poster, or
  Instagram graphic for a community, masjid, MSA, or nonprofit event and wants it
  to match the ROOTS / Roots Community Space aesthetic (or references "the roots
  flyers", "roots style", a serif-over-photo look, or asks why their flyer
  "doesn't look like roots"). Produces a self-contained HTML template plus a
  ready-to-hand-off PNG (baseline for a designer to rebuild in Canva). Reach for
  this even when they don't say "ROOTS" by name but describe that calm
  serif-headline-over-photo style.
---

# ROOTS-style flyer

Produce a flyer that matches the ROOTS event-flyer look: one atmospheric photo,
a dark scrim, an elegant serif hero, warm-white sans details, and an
`Org / Category` lockup bottom-right. The goal is usually a **baseline PNG** a
graphic designer then rebuilds in Canva — so getting the *look and structure*
right matters more than pixel-perfect code.

**Read `references/design-system.md` first** — it's the distilled recipe (photo,
scrim, the two typefaces, palette, the anatomy, spacing, do/don'ts). The template
and script below just mechanize it.

## Workflow

The pipeline is: **config JSON → build a self-contained HTML → render a PNG.**

1. **Gather the content.** From the user (or an existing flyer they want
   restyled), collect: the headline, an optional eyebrow/series name, a short
   description, schedule (day + times), venue, the `Org / Category` lockup, and
   any presenter or RSVP line. Keep copy tight — ROOTS descriptions are 2–4 lines.

2. **Choose a photo.** One atmospheric, on-theme image with a calm area for text
   (see the design system's "Photograph" section). In this environment only
   GitHub hosts are reachable, so pull an openly-licensed photo from a public
   repo (e.g. Unsplash-licensed images bundled in MIT template repos) and save it
   locally. `assets/sample/sample-bbq.jpg` is a warm placeholder to fall back on.
   If the user supplies their own photo, prefer it.

3. **Write the config.** Create a JSON file following the schema documented at
   the top of `scripts/build_flyer.py`. Only `photo`, `hero`, and the brand
   fields are required; eyebrow / description / presenter / callout / schedule /
   venue are optional and simply collapse when omitted.

4. **Build + render:**
   ```bash
   python3 scripts/build_flyer.py config.json flyer.html
   node    scripts/render.cjs      flyer.html flyer.png
   ```
   `build_flyer.py` inlines the bundled Playfair Display face and the photo as
   data URIs, so `flyer.html` is fully self-contained (also publishable as an
   Artifact). `render.cjs` uses the environment's headless Chromium to output a
   1080×1350 @2× PNG.

5. **Review the PNG and iterate.** Look at it. Check the ROOTS tells: serif hero,
   warm-white text, legible over the scrim, details in the corners, air
   preserved, lockup bottom-right. Common fixes: adjust `hero_size` so the
   headline fills 1–3 lines; nudge `photo_pos` to move the subject out from under
   the text; deepen the scrim (in `template.html`) if any line is hard to read;
   shorten the description if it runs long.

6. **Deliver.** Send the PNG (that's the baseline for the designer). Offer the
   annotated anatomy/spec sheet too when a designer will rebuild it — it names
   the fonts, sizes, palette, and spacing. Note the photo's license/source so
   they can license or swap it.

## Typefaces

The signature is the **serif hero**. The bundled **Playfair Display**
(`assets/fonts/`, SIL OFL — free to embed and redistribute) is the closest
open-licensed match to the Canela/Tiempos face ROOTS uses; the real brand font
can be substituted by the designer later. Body/UI text uses the system sans
(Helvetica/SF-like), which needs no embedding. **Never** put a casual or script
font in the hero — that single swap is what breaks the ROOTS look.

## Files
- `references/design-system.md` — the full recipe. Read before building.
- `assets/template.html` — the parameterized layout (tokens + CSS).
- `scripts/build_flyer.py` — config JSON → self-contained HTML (schema in its docstring).
- `scripts/render.cjs` — HTML → 1080×1350 @2× PNG via headless Chromium.
- `assets/fonts/` — Playfair Display Roman + Italic (OFL) and the license.
- `assets/sample/` — a warm placeholder photo.

## Scope note
This produces a faithful *baseline*, not a final brand asset. The exact ROOTS
brand fonts, licensed photography, and logo lockups are theirs to add. Hand the
PNG (and anatomy sheet) to a designer as the target to rebuild.
