# ROOTS flyer design system

Distilled from the @rootsdfw event flyers (Heartwork "The Messenger", "Circles",
"Brotherly Rock Climbing", "convert connection", "The Secrets of Prayer",
"The Pursuit of Happiness", "fajr & breakfast"). The look is calm, editorial, and
photographic — closer to a magazine cover than a Canva event graphic. Everything
below is the recipe for reproducing it.

## The one-sentence version

A full-bleed atmospheric **photo**, dimmed by a single dark **scrim**, with an
elegant **serif headline** and clean **sans** details in **warm white**, tucked
into the corners with lots of empty space — and a **`Roots / Category`** lockup
locked to the bottom-right.

## Format
- Instagram portrait, **1080 × 1350** (4:5). Render at 2× for crisp text.
- Full-bleed rectangle. (Instagram rounds the corners itself; the asset shouldn't.)

## Photograph — the foundation
- **One** photo, full-bleed, chosen for *mood* over literal documentation. The
  Secrets of Prayer uses a red prayer-carpet; The Messenger a green dome; Circles
  a cloudy sky; Convert Connection a soft-focus gathering. None of them is a busy
  stock close-up of the activity.
- Each photo has a **dominant hue** (green, red, blue, amber) that becomes the
  flyer's color. Pick the accent and neutrals *from the photo*.
- The composition must leave a **calm region** (usually left, top-left, or the
  lower third) where text can sit without fighting detail.
- If the only available photo is busy (e.g. a grill close-up), **darken it hard**
  so it recedes into a background rather than competing with the words.

## Scrim — why the text is always readable
- A **single dark gradient** (deep navy/near-black, `#0e1526`) sits over the whole
  photo. It is **heavier on the side the text lives** and fades toward the open
  space — not a flat 50% wash.
- The template stacks three gentle gradients: a diagonal from the text corner, a
  bottom-up gradient for the footer, and a soft top gradient for the eyebrow.
- Goal: text reads cleanly everywhere while the photo still breathes. If any word
  is hard to read, deepen the scrim — never add a hard box behind the text.

## Typography — two faces, used with discipline
1. **Display serif** — a high-contrast Didone/transitional serif. ROOTS uses a
   Canela/Tiempos-style face; the closest open-licensed match is **Playfair
   Display** (bundled in `assets/fonts/`, SIL OFL). This carries the hero and the
   occasional italic flourish (e.g. an `rsvp at` label). Two moods:
   - **Italic, title-case** for named series/titles: *The Messenger*,
     *The Secrets of Prayer*, *The Pursuit of Happiness*.
   - **Upright, lowercase** for single concept words: `circles`,
     `convert connection`.
   Set it **large** (100–140px on the 1080 canvas), tight leading (~0.98), hugging
   the top-left.
2. **Body / UI sans** — a clean neutral grotesque (ROOTS reads as SF Pro /
   Helvetica Now). Use the system sans (`-apple-system`/Helvetica) or **Inter**.
   Carries everything else: eyebrow, description, presenter, schedule, venue, and
   the brand lockup.

Never let the sans creep into the hero, and never let a casual/script/hand face
in anywhere — that single substitution is what makes a flyer stop reading as ROOTS.

## Color
- Text is **warm white** `#F4F1EA` (primary) and a ~80% version for secondary
  lines. Not pure `#FFFFFF` — the warm white feels considered.
- **One accent**, warm and pulled from the photo — often a gold `#EAB24C`. Used
  sparingly: small labels, day names, the category word, or a highlighted hero
  word. Circles tints its day labels and the `Adults` category in pale yellow;
  fajr & breakfast sets the ampersand in gold.
- Neutrals for the scrim are a **navy-biased near-black**, not a flat grey.
- Monochrome discipline: aside from the photo and the single accent, the palette
  is just warm-white text on a dark scrim.

## Anatomy (top → bottom)
1. **Eyebrow / kicker** *(optional)* — sans, ~20px, UPPERCASE, wide tracking
   (~0.34em). Names the series: "A HEARTWORK SERIES", "A THIRTY & UP SERIES",
   "BY IMAM AL GHAZALI".
2. **Hero headline** — the serif, top-left, 1–3 lines.
3. **Description** *(optional)* — sans, ~26px, 2–4 lines, narrow measure (~45–55%
   width) so it never runs full-bleed.
4. **Presenter chip** *(optional)* — circular avatar + two lines: bold series/role
   on top, `with Ust. Name` below (the "with" often italic). Seen on Heartwork,
   Thirty & Up.
5. **Callout pill** *(optional)* — a translucent rounded chip with an italic serif
   lead (`rsvp at`, `rsvp by july 10th`) over a sans URL. Seen on Circles,
   Brotherly Rock Climbing.
6. **Schedule** — sans **bold**, ~34px, the day/time ("Monday nights",
   "Saturday, July 25th"), with optional lighter sub-lines ("Doors open & Suhbah:
   6pm", "Program: 7:00pm – 8:00pm").
7. **Venue block** — sans, ~23px. Bold place name, lighter address lines
   ("Roots Community Space / 4200 International Pkwy / Carrollton, TX 75007").
8. **Brand lockup** — sans, ~30px, bottom-right, **always**: bold **`Roots`**, a
   thin slash, then a lighter **category** word (Community, Adults, Brothers,
   Converts). Swap `Roots` for the org (e.g. `ICCWG`, `MSDV`).

Items 3–5 are the modular middle — include only what the event needs. The four
fixed anchors are: eyebrow(optional)+hero top-left, schedule+venue bottom-left,
lockup bottom-right, photo+scrim behind everything.

## Layout & spacing
- Outer padding ≈ 6–7% of the width (~66–74px on 1080).
- Content hugs the **left edge** and the **bottom corners**; the rest is open
  photo. Generous negative space is a feature, not wasted room.
- A `.spacer` between the top cluster and the footer pushes the details to the
  bottom regardless of how much middle content there is.

## Do / Don't
- **Do** pick a moody, on-theme photo and pull the palette from it.
- **Do** keep one serif + one sans, warm-white text, one accent.
- **Do** anchor the `Org / Category` lockup bottom-right every time.
- **Don't** use bright saturated headline colors, script/handwriting fonts, or a
  busy literal photo with text laid straight over the clutter.
- **Don't** box the text — deepen the scrim instead.
- **Don't** center everything or fill the whole frame; protect the empty space.
