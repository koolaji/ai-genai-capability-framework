#!/usr/bin/env python3
"""Render a Markdown framework document to a styled, leadership-ready PDF.

Usage:
    render_pdf.py <input.md> <output.pdf> [--rtl] [--title "..."] [--subtitle "..."]

RTL mode flips direction for Persian/Farsi while keeping code blocks LTR.
Uses system Noto fonts (Noto Sans Arabic for Persian, DejaVu for Latin).
"""
import argparse
import re
import markdown
from weasyprint import HTML

LTR_FONTS = '"DejaVu Sans", "Noto Sans Arabic", sans-serif'
RTL_FONTS = '"Noto Sans Arabic", "DejaVu Sans", sans-serif'
MONO = '"DejaVu Sans Mono", monospace'


def build_css(rtl: bool) -> str:
    direction = "rtl" if rtl else "ltr"
    body_font = RTL_FONTS if rtl else LTR_FONTS
    text_align = "right" if rtl else "left"
    page_side = "left" if rtl else "right"  # page number outer corner
    return f"""
@page {{
    size: A4;
    margin: 22mm 18mm 20mm 18mm;
    @bottom-{page_side} {{
        content: counter(page);
        font-family: {body_font};
        font-size: 9pt;
        color: #888;
    }}
    @bottom-center {{
        content: "AI / GenAI Capability Evaluation Framework";
        font-family: {body_font};
        font-size: 8pt;
        color: #bbb;
    }}
}}
@page :first {{
    @bottom-center {{ content: ""; }}
    @bottom-{page_side} {{ content: ""; }}
}}
html {{ direction: {direction}; }}
body {{
    direction: {direction};
    text-align: {text_align};
    font-family: {body_font};
    font-size: 10.2pt;
    line-height: 1.55;
    color: #1f2933;
}}
h1, h2, h3, h4, h5 {{ font-family: {body_font}; color: #0b2545; line-height: 1.25; }}
h1 {{ font-size: 24pt; margin: 0 0 4pt 0; }}
h2 {{
    font-size: 16pt; margin: 22pt 0 8pt 0; padding-bottom: 4pt;
    border-bottom: 2px solid #1d4e89; page-break-after: avoid;
}}
h3 {{ font-size: 12.5pt; margin: 14pt 0 6pt 0; color: #1d4e89; page-break-after: avoid; }}
h4 {{ font-size: 11pt; margin: 10pt 0 4pt 0; color: #2a4d69; }}
p {{ margin: 5pt 0; }}
a {{ color: #1d4e89; text-decoration: none; }}
strong {{ color: #0b2545; }}
hr {{ border: none; border-top: 1px solid #d9e2ec; margin: 16pt 0; }}
ul, ol {{ margin: 5pt 0; padding-{'right' if rtl else 'left'}: 20pt; }}
li {{ margin: 2pt 0; }}
blockquote {{
    margin: 10pt 0; padding: 6pt 12pt;
    background: #f0f4f8; border-{'right' if rtl else 'left'}: 4px solid #1d4e89;
    color: #334e68; font-size: 9.6pt;
}}
code {{
    font-family: {MONO}; font-size: 8.8pt; background: #eef2f7;
    padding: 1px 4px; border-radius: 3px; direction: ltr; unicode-bidi: embed;
}}
pre {{
    font-family: {MONO}; font-size: 8.6pt; background: #1b2733; color: #e6edf3;
    padding: 10pt; border-radius: 5px; overflow-wrap: anywhere;
    white-space: pre-wrap; direction: ltr; text-align: left;
}}
pre code {{ background: transparent; color: inherit; padding: 0; }}
table {{
    border-collapse: collapse; width: 100%; margin: 10pt 0;
    font-size: 8.8pt; direction: {direction};
}}
thead {{ display: table-header-group; }}
tr {{ page-break-inside: avoid; }}
th, td {{
    border: 1px solid #c4d0db; padding: 5pt 7pt;
    text-align: {text_align}; vertical-align: top;
}}
th {{ background: #1d4e89; color: #fff; font-weight: bold; }}
tr:nth-child(even) td {{ background: #f4f7fa; }}
/* keep latin/code inside RTL cells readable */
td code, th code {{ direction: ltr; unicode-bidi: embed; }}

.cover {{
    page-break-after: always; text-align: center; padding-top: 55mm;
}}
.cover h1 {{ font-size: 30pt; color: #0b2545; border: none; }}
.cover .subtitle {{ font-size: 13pt; color: #486581; margin-top: 10pt; }}
.cover .meta {{ font-size: 10pt; color: #829ab1; margin-top: 30mm; }}
.toc h2 {{ border-bottom: 2px solid #1d4e89; }}
.toc ul {{ list-style: none; padding-{'right' if rtl else 'left'}: 0; }}
.toc li {{ margin: 3pt 0; font-size: 10pt; }}
.toc a {{ color: #243b53; }}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--rtl", action="store_true")
    ap.add_argument("--title", default="AI / GenAI Capability Evaluation Framework")
    ap.add_argument("--subtitle", default="A research-based framework for regulated DevOps organizations")
    ap.add_argument("--meta", default="Draft for review · Generated with Claude Code")
    args = ap.parse_args()

    text = open(args.input, encoding="utf-8").read()

    # Drop the first H1 (it becomes the cover title) to avoid duplication.
    text = re.sub(r"^#\s+.*\n", "", text, count=1)

    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "sane_lists", "toc", "attr_list", "md_in_html"],
        extension_configs={"toc": {"toc_depth": "2-2"}},
    )
    body_html = md.convert(text)
    toc_html = md.toc  # generated table of contents (h2 only)

    cover = f"""
    <div class="cover">
      <h1>{args.title}</h1>
      <div class="subtitle">{args.subtitle}</div>
      <div class="meta">{args.meta}</div>
    </div>
    <div class="toc">
      <h2>{'فهرست مطالب' if args.rtl else 'Contents'}</h2>
      {toc_html}
    </div>
    """

    html_doc = f"""<!DOCTYPE html><html lang="{'fa' if args.rtl else 'en'}" dir="{'rtl' if args.rtl else 'ltr'}">
<head><meta charset="utf-8"><style>{build_css(args.rtl)}</style></head>
<body>{cover}{body_html}</body></html>"""

    HTML(string=html_doc).write_pdf(args.output)
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
