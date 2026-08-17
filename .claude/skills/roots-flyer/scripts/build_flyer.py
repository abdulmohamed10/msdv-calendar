#!/usr/bin/env python3
"""
Build a self-contained ROOTS-style flyer HTML from a JSON config.

Usage:
    python build_flyer.py config.json out.html

The finished HTML embeds the Playfair Display display face and the background
photo as data URIs, so it renders offline and can be dropped into an Artifact
or handed to scripts/render.cjs to produce a PNG.

Config schema (all keys optional unless noted):
{
  "title":      "Community Barbecue",         # browser/tab title
  "photo":      "photo.jpg",                   # REQUIRED, path to background image
  "photo_pos":  "50% 45%",                     # css background-position (default "50% 50%")
  "accent":     "#e8b04b",                     # one warm accent (default gold)
  "eyebrow":    "A COMMUNITY GATHERING",       # small uppercase kicker (optional)
  "hero":       "community<br>barbecue",       # serif headline; <br> for line breaks (REQUIRED)
  "hero_style": "normal",                      # "normal" or "italic" (default "italic")
  "hero_size":  128,                           # px (default 120)
  "desc":       "It's time for our annual ...",# sans description paragraph (optional)
  "presenter":  {"avatar":"a.jpg","name":"Ust. Name","label":"Heartwork","lead":"with"}, # optional
  "callout":    {"lead":"rsvp at","value":"iccwg.org/bbq"},                                # optional
  "schedule":   {"main":"3pm · Saturday, September 5","subs":["Program: 3–6pm"]},          # optional
  "venue":      "Masons Mill Park — Pavilion 1|3500 Masons Mill Rd, Bryn Athyn",           # optional, "|"=line break, first line bold
  "brand_main": "ICCWG",                       # bold half of the lockup (default "Roots")
  "brand_sub":  "Community"                    # light half of the lockup
}
"""
import base64, json, mimetypes, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
TEMPLATE = SKILL / "assets" / "template.html"
FONT_ROMAN = SKILL / "assets" / "fonts" / "PlayfairDisplay-Roman.ttf"
FONT_ITALIC = SKILL / "assets" / "fonts" / "PlayfairDisplay-Italic.ttf"


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(str(path))[0] or "application/octet-stream"
    b64 = base64.b64encode(path.read_bytes()).decode()
    return f"data:{mime};base64,{b64}"


def font_face_block() -> str:
    roman = data_uri(FONT_ROMAN)
    italic = data_uri(FONT_ITALIC)
    return (
        "@font-face{font-family:'Playfair Display';font-style:normal;"
        f"font-weight:400 900;src:url({roman}) format('truetype');}}\n"
        "@font-face{font-family:'Playfair Display';font-style:italic;"
        f"font-weight:400 900;src:url({italic}) format('truetype');}}"
    )


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build(cfg: dict) -> str:
    html = TEMPLATE.read_text()

    # --- required / core ---
    photo = Path(cfg["photo"])
    if not photo.is_absolute():
        photo = (Path.cwd() / photo)
    repl = {
        "<!--FONTS-->": font_face_block(),
        "{{TITLE}}": cfg.get("title", cfg.get("brand_sub", "Flyer")),
        "{{PHOTO}}": data_uri(photo),
        "{{PHOTO_POS}}": cfg.get("photo_pos", "50% 50%"),
        "{{ACCENT}}": cfg.get("accent", "#e8b04b"),
        "{{HERO}}": cfg["hero"],  # allow <br>, so not escaped
        "{{HERO_STYLE}}": cfg.get("hero_style", "italic"),
        "{{HERO_SIZE}}": str(cfg.get("hero_size", 120)),
        "{{BRAND_MAIN}}": esc(cfg.get("brand_main", "Roots")),
        "{{BRAND_SUB}}": esc(cfg.get("brand_sub", "Community")),
    }

    # --- optional blocks ---
    eyebrow = cfg.get("eyebrow", "")
    repl["{{EYEBROW}}"] = f'<p class="eyebrow">{esc(eyebrow)}</p>' if eyebrow else ""

    desc = cfg.get("desc", "")
    repl["{{DESC}}"] = f'<p class="desc">{esc(desc)}</p>' if desc else ""

    pres = cfg.get("presenter")
    if pres:
        avatar = pres.get("avatar")
        img = f'<img src="{data_uri(Path(avatar))}" alt="">' if avatar else ""
        who = ""
        if pres.get("label"):
            who += f'<b>{esc(pres["label"])}</b><br>'
        if pres.get("name"):
            lead = f'<span class="lead">{esc(pres.get("lead","with"))} </span>' if pres.get("lead") else ""
            who += f'{lead}<b>{esc(pres["name"])}</b>'
        repl["{{PRESENTER}}"] = f'<div class="presenter">{img}<div class="who">{who}</div></div>'
    else:
        repl["{{PRESENTER}}"] = ""

    call = cfg.get("callout")
    if call:
        repl["{{CALLOUT}}"] = (
            f'<div class="callout"><span class="lead">{esc(call.get("lead",""))}</span>'
            f'<span class="val">{esc(call.get("value",""))}</span></div>'
        )
    else:
        repl["{{CALLOUT}}"] = ""

    sched = cfg.get("schedule")
    if sched:
        subs = "".join(f'<span class="sub">{esc(s)}</span>' for s in sched.get("subs", []))
        repl["{{DETAILS}}"] = f'<p class="sched">{esc(sched["main"])}{subs}</p>'
    else:
        repl["{{DETAILS}}"] = ""

    venue = cfg.get("venue", "")
    if venue:
        parts = [esc(p) for p in venue.split("|")]
        parts[0] = f"<b>{parts[0]}</b>"
        repl["{{VENUE}}"] = f'<p class="venue">{"<br>".join(parts)}</p>'
    else:
        repl["{{VENUE}}"] = ""

    for k, v in repl.items():
        html = html.replace(k, v)
    return html


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    cfg = json.loads(Path(sys.argv[1]).read_text())
    Path(sys.argv[2]).write_text(build(cfg))
    print(f"wrote {sys.argv[2]}")


if __name__ == "__main__":
    main()
