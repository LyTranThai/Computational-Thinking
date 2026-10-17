#!/usr/bin/env python3
"""
render_html.py - Render Markdown files to clean, attractive, self-contained HTML.
Adheres to HCMUS FIT Computational Thinking submission requirements:
"Submit both of the Markdown file and a rendered version (.pdf / .html)
 that displays the Markdown file correctly and attractively."
"""

import sys
import os
import re
import html
from pathlib import Path

CSS_STYLES = """
:root {
  --color-canvas-default: #ffffff;
  --color-canvas-subtle: #f6f8fa;
  --color-border-default: #d0d7de;
  --color-border-muted: #d8dee4;
  --color-fg-default: #1f2328;
  --color-fg-muted: #656d76;
  --color-accent-fg: #0969da;
  --color-neutral-muted: rgba(175,184,193,0.2);
  --color-code-bg: #f6f8fa;
  --font-body: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-canvas-default: #0d1117;
    --color-canvas-subtle: #161b22;
    --color-border-default: #30363d;
    --color-border-muted: #21262d;
    --color-fg-default: #e6edf3;
    --color-fg-muted: #8b949e;
    --color-accent-fg: #4493f8;
    --color-neutral-muted: rgba(110,118,129,0.4);
    --color-code-bg: #161b22;
  }
}

* {
  box-sizing: border-box;
}

body {
  font-family: var(--font-body);
  font-size: 16px;
  line-height: 1.6;
  word-wrap: break-word;
  background-color: var(--color-canvas-default);
  color: var(--color-fg-default);
  margin: 0;
  padding: 32px;
}

.markdown-body {
  max-width: 900px;
  margin: 0 auto;
  padding: 40px;
  background-color: var(--color-canvas-default);
  border: 1px solid var(--color-border-default);
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

h1, h2, h3, h4, h5, h6 {
  margin-top: 24px;
  margin-bottom: 16px;
  font-weight: 600;
  line-height: 1.25;
  color: var(--color-fg-default);
}

h1 {
  font-size: 2em;
  padding-bottom: 0.3em;
  border-bottom: 1px solid var(--color-border-muted);
}

h2 {
  font-size: 1.5em;
  padding-bottom: 0.3em;
  border-bottom: 1px solid var(--color-border-muted);
}

h3 { font-size: 1.25em; }
h4 { font-size: 1em; }

p, blockquote, ul, ol, dl, table, pre, details {
  margin-top: 0;
  margin-bottom: 16px;
}

a {
  color: var(--color-accent-fg);
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

hr {
  height: 0.25em;
  padding: 0;
  margin: 24px 0;
  background-color: var(--color-border-default);
  border: 0;
}

blockquote {
  padding: 0 1em;
  color: var(--color-fg-muted);
  border-left: 0.25em solid var(--color-border-default);
}

ul, ol {
  padding-left: 2em;
}

li + li {
  margin-top: 0.25em;
}

code {
  padding: 0.2em 0.4em;
  margin: 0;
  font-size: 85%;
  white-space: break-spaces;
  background-color: var(--color-neutral-muted);
  border-radius: 6px;
  font-family: var(--font-mono);
}

pre {
  padding: 16px;
  overflow: auto;
  font-size: 85%;
  line-height: 1.45;
  color: var(--color-fg-default);
  background-color: var(--color-code-bg);
  border: 1px solid var(--color-border-muted);
  border-radius: 6px;
  font-family: var(--font-mono);
}

pre code {
  padding: 0;
  margin: 0;
  font-size: 100%;
  word-break: normal;
  white-space: pre;
  background: transparent;
  border: 0;
}

table {
  border-spacing: 0;
  border-collapse: collapse;
  display: block;
  width: max-content;
  max-width: 100%;
  overflow: auto;
  margin-top: 0;
  margin-bottom: 16px;
}

table th {
  font-weight: 600;
  background-color: var(--color-canvas-subtle);
}

table th, table td {
  padding: 8px 14px;
  border: 1px solid var(--color-border-default);
}

table tr {
  background-color: var(--color-canvas-default);
  border-top: 1px solid var(--color-border-muted);
}

table tr:nth-child(2n) {
  background-color: var(--color-canvas-subtle);
}

img {
  max-width: 100%;
  box-sizing: content-box;
  border-radius: 4px;
}

.footer {
  margin-top: 32px;
  padding-top: 16px;
  border-top: 1px solid var(--color-border-muted);
  font-size: 0.85em;
  color: var(--color-fg-muted);
  text-align: right;
}

@media print {
  body {
    padding: 0;
    background: #fff;
    color: #000;
  }
  .markdown-body {
    border: none;
    box-shadow: none;
    padding: 0;
    max-width: 100%;
  }
  a {
    color: #000;
    text-decoration: underline;
  }
  pre, code, table {
    page-break-inside: avoid;
  }
}
"""

def parse_inline(text):
    # Escape HTML characters first
    text = html.escape(text)

    # Images: ![alt](url)
    text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1" />', text)

    # Links: [text](url)
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)

    # Inline code: `code`
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)

    # Bold + Italic: ***text*** or ___text___
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text)

    # Bold: **text** or __text__
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)

    # Italic: *text* or _text_
    text = re.sub(r'(?<!\*)\*(?!\*)(.*?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    text = re.sub(r'(?<!_)_(?!_)(.*?)(?<!_)_(?!_)', r'<em>\1</em>', text)

    # Strikethrough: ~~text~~
    text = re.sub(r'~~(.*?)~~', r'<del>\1</del>', text)

    return text

def parse_markdown(md_text):
    lines = md_text.splitlines()
    html_out = []
    i = 0
    n = len(lines)

    in_list = None # 'ul' or 'ol'
    in_blockquote = False

    def close_list():
        nonlocal in_list
        if in_list:
            html_out.append(f"</{in_list}>")
            in_list = None

    def close_blockquote():
        nonlocal in_blockquote
        if in_blockquote:
            html_out.append("</blockquote>")
            in_blockquote = False

    while i < n:
        line = lines[i]

        # 1. Code blocks (```)
        if line.strip().startswith("```"):
            close_list()
            close_blockquote()
            lang = line.strip()[3:].strip()
            code_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(html.escape(lines[i]))
                i += 1
            i += 1 # skip closing ```
            lang_attr = f' class="language-{lang}"' if lang else ''
            html_out.append(f'<pre><code{lang_attr}>' + "\n".join(code_lines) + '</code></pre>')
            continue

        # 2. Blank line
        if not line.strip():
            close_list()
            close_blockquote()
            i += 1
            continue

        # 3. Blockquote
        if line.startswith(">"):
            close_list()
            if not in_blockquote:
                html_out.append("<blockquote>")
                in_blockquote = True
            content = line.lstrip("> ").strip()
            html_out.append(f"<p>{parse_inline(content)}</p>")
            i += 1
            continue
        else:
            close_blockquote()

        # 4. Table detection (| ... |)
        if line.strip().startswith("|") and line.strip().endswith("|"):
            close_list()
            table_lines = []
            while i < n and lines[i].strip().startswith("|") and lines[i].strip().endswith("|"):
                table_lines.append(lines[i].strip())
                i += 1

            if len(table_lines) >= 2 and re.match(r'^\|[\s\-:|]+\|$', table_lines[1]):
                # Valid markdown table
                headers = [c.strip() for c in table_lines[0].strip('|').split('|')]
                align_raw = [c.strip() for c in table_lines[1].strip('|').split('|')]
                alignments = []
                for a in align_raw:
                    if a.startswith(":") and a.endswith(":"):
                        alignments.append(' align="center"')
                    elif a.endswith(":"):
                        alignments.append(' align="right"')
                    elif a.startswith(":"):
                        alignments.append(' align="left"')
                    else:
                        alignments.append('')

                tbl_html = ['<table>', '<thead>', '<tr>']
                for idx, h in enumerate(headers):
                    align = alignments[idx] if idx < len(alignments) else ''
                    tbl_html.append(f'<th{align}>{parse_inline(h)}</th>')
                tbl_html.extend(['</tr>', '</thead>', '<tbody>'])

                for row in table_lines[2:]:
                    cells = [c.strip() for c in row.strip('|').split('|')]
                    tbl_html.append('<tr>')
                    for idx, cell in enumerate(cells):
                        align = alignments[idx] if idx < len(alignments) else ''
                        tbl_html.append(f'<td{align}>{parse_inline(cell)}</td>')
                    tbl_html.append('</tr>')

                tbl_html.extend(['</tbody>', '</table>'])
                html_out.append("\n".join(tbl_html))
                continue
            else:
                # Not a table header separator, treat as text
                for tl in table_lines:
                    html_out.append(f"<p>{parse_inline(tl)}</p>")
                continue

        # 5. Headings
        header_match = re.match(r'^(#{1,6})\s+(.*)', line)
        if header_match:
            close_list()
            level = len(header_match.group(1))
            heading_text = parse_inline(header_match.group(2).strip())
            html_out.append(f'<h{level}>{heading_text}</h{level}>')
            i += 1
            continue

        # 6. Horizontal rule
        if re.match(r'^(\-{3,}|\*{3,}|_{3,})$', line.strip()):
            close_list()
            html_out.append("<hr />")
            i += 1
            continue

        # 7. Unordered list (- or *)
        ul_match = re.match(r'^[\*\-]\s+(.*)', line)
        if ul_match:
            if in_list != 'ul':
                close_list()
                html_out.append("<ul>")
                in_list = 'ul'
            item_text = parse_inline(ul_match.group(1).strip())
            html_out.append(f"<li>{item_text}</li>")
            i += 1
            continue

        # 8. Ordered list (1. 2. etc.)
        ol_match = re.match(r'^\d+\.\s+(.*)', line)
        if ol_match:
            if in_list != 'ol':
                close_list()
                html_out.append("<ol>")
                in_list = 'ol'
            item_text = parse_inline(ol_match.group(1).strip())
            html_out.append(f"<li>{item_text}</li>")
            i += 1
            continue

        # 9. Regular paragraph
        close_list()
        para_lines = [line.strip()]
        i += 1
        while i < n and lines[i].strip() and not lines[i].strip().startswith(("#", "-", "*", ">", "```", "|")) and not re.match(r'^\d+\.\s+', lines[i].strip()):
            para_lines.append(lines[i].strip())
            i += 1
        para_text = parse_inline(" ".join(para_lines))
        html_out.append(f"<p>{para_text}</p>")

    close_list()
    close_blockquote()
    return "\n".join(html_out)

def render_markdown_file(md_path, output_path=None):
    md_file = Path(md_path).resolve()
    if not md_file.exists():
        raise FileNotFoundError(f"Markdown file not found: {md_file}")

    if output_path is None:
        output_file = md_file.with_suffix('.html')
    else:
        output_file = Path(output_path).resolve()

    content = md_file.read_text(encoding='utf-8')
    title = md_file.stem.replace('_', ' ').title()

    # Check for top-level # heading as title
    top_heading = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if top_heading:
        title = top_heading.group(1).strip()

    body_html = parse_markdown(content)

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <style>
{CSS_STYLES}
  </style>
</head>
<body>
  <article class="markdown-body">
{body_html}
    <div class="footer">
      Rendered for submission &bull; HCMUS FIT Computational Thinking
    </div>
  </article>
</body>
</html>
"""

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(full_html, encoding='utf-8')
    print(f"[OK] Rendered HTML: {output_file}")
    return output_file

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python render_html.py <path_to_markdown_file> [output_html_path]")
        sys.exit(1)

    input_md = sys.argv[1]
    out_html = sys.argv[2] if len(sys.argv) > 2 else None
    render_markdown_file(input_md, out_html)
