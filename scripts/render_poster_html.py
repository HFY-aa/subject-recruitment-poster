#!/usr/bin/env python3
"""Render a participant recruitment poster brief JSON into editable HTML."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from typing import Any


def as_list(value: Any) -> list[str]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return [line.strip() for line in str(value).splitlines() if line.strip()]


def text(value: Any, fallback: str = "") -> str:
    value = "" if value is None else str(value)
    value = value.strip()
    return html.escape(value if value else fallback)


def list_items(items: list[str]) -> str:
    if not items:
        return '<li><span class="index">1</span><span>待补充</span></li>'
    return "\n".join(
        f'<li><span class="index">{i}</span><span>{text(item)}</span></li>'
        for i, item in enumerate(items, 1)
    )


def qr_block(qr_code: str) -> str:
    qr_code = str(qr_code or "").strip()
    if not qr_code:
        return '<div class="qr-placeholder">二维码<br>QR CODE</div>'
    return f'<img class="qr-img" src="{html.escape(qr_code)}" alt="报名二维码">'


def render_html(brief: dict[str, Any]) -> str:
    title = text(brief.get("title"), "心理学实验被试招募")
    hook = text(brief.get("hook"), "实验主题待补充")
    study_type = text(brief.get("study_type"), "心理学实验")
    content_items = as_list(brief.get("experiment_content"))
    eligibility_items = as_list(brief.get("eligibility"))
    qr_code = str(brief.get("qr_code") or "").strip()

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    :root {{
      --navy: #071f4d;
      --blue: #0b4b8f;
      --green: #11934a;
      --mint: #eaf8f1;
      --ink: #0b1736;
      --muted: #5d6880;
      --line: #b8cae6;
      --paper: #ffffff;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      min-height: 100vh;
      display: grid;
      place-items: center;
      background: #dce8f5;
      font-family: "Noto Sans SC", "Microsoft YaHei", "Source Han Sans SC", sans-serif;
      color: var(--ink);
    }}
    .poster {{
      width: 937px;
      min-height: 1679px;
      overflow: hidden;
      background: var(--paper);
      position: relative;
      box-shadow: 0 24px 80px rgba(7, 31, 77, .28);
    }}
    .hero {{
      min-height: 480px;
      padding: 72px 64px 52px;
      color: white;
      position: relative;
      overflow: hidden;
      background:
        radial-gradient(circle at 15% 15%, rgba(0, 213, 255, .55), transparent 28%),
        radial-gradient(circle at 78% 32%, rgba(51, 214, 132, .34), transparent 22%),
        linear-gradient(135deg, #051638 0%, #082a64 55%, #061a41 100%);
    }}
    .hero::before {{
      content: "";
      position: absolute;
      inset: -80px auto auto -110px;
      width: 520px;
      height: 520px;
      border-radius: 50%;
      border: 2px solid rgba(79, 209, 255, .35);
      background:
        linear-gradient(80deg, transparent 48%, rgba(105, 226, 255, .45) 49%, transparent 51%),
        linear-gradient(145deg, transparent 48%, rgba(105, 226, 255, .32) 49%, transparent 51%);
      opacity: .85;
    }}
    .hero::after {{
      content: "MRI";
      position: absolute;
      right: 54px;
      bottom: 64px;
      width: 220px;
      height: 220px;
      display: grid;
      place-items: center;
      border: 22px solid rgba(255, 255, 255, .82);
      border-radius: 50%;
      color: rgba(255, 255, 255, .9);
      font-weight: 900;
      font-size: 46px;
      letter-spacing: .08em;
      box-shadow: inset 0 0 0 10px rgba(11, 75, 143, .45);
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 10px 20px;
      border-radius: 999px;
      background: rgba(17, 147, 74, .9);
      font-size: 26px;
      font-weight: 800;
      position: relative;
      z-index: 1;
    }}
    h1 {{
      margin: 34px 0 22px;
      font-size: 86px;
      line-height: 1.08;
      letter-spacing: .02em;
      text-shadow: 0 6px 12px rgba(0, 0, 0, .35);
      position: relative;
      z-index: 1;
    }}
    .hook {{
      display: inline-block;
      max-width: 720px;
      padding: 16px 24px;
      background: rgba(255, 255, 255, .95);
      color: var(--navy);
      border-left: 12px solid var(--green);
      border-radius: 18px;
      font-size: 44px;
      font-weight: 900;
      position: relative;
      z-index: 1;
    }}
    .content {{
      padding: 38px 54px 42px;
      display: grid;
      gap: 22px;
    }}
    .section-title {{
      display: flex;
      align-items: center;
      gap: 14px;
      color: var(--green);
      font-size: 38px;
      font-weight: 900;
      justify-content: center;
      margin: 0 0 6px;
    }}
    .section-title::before,
    .section-title::after {{
      content: "";
      height: 2px;
      flex: 1;
      border-top: 3px dotted var(--line);
    }}
    .content-list {{
      margin: 0;
      padding: 0;
      display: grid;
      gap: 10px;
      list-style: none;
      text-align: center;
      font-size: 34px;
      font-weight: 800;
      line-height: 1.35;
    }}
    .cards {{
      display: grid;
      gap: 14px;
    }}
    .card {{
      display: grid;
      grid-template-columns: 82px 220px 1fr;
      gap: 18px;
      align-items: center;
      border: 2px solid var(--line);
      border-radius: 24px;
      padding: 18px 24px 18px 18px;
      background: linear-gradient(90deg, #fff 0%, #f7fbff 100%);
    }}
    .icon {{
      width: 72px;
      height: 72px;
      display: grid;
      place-items: center;
      border-radius: 20px;
      background: var(--green);
      color: white;
      font-size: 19px;
      font-weight: 900;
      letter-spacing: .04em;
      line-height: 1;
    }}
    .label {{
      color: var(--navy);
      font-size: 34px;
      font-weight: 900;
    }}
    .value {{
      font-size: 34px;
      font-weight: 900;
      line-height: 1.25;
    }}
    .value strong {{
      color: var(--green);
      font-size: 42px;
    }}
    .note {{
      display: block;
      margin-top: 6px;
      color: var(--muted);
      font-size: 24px;
      font-weight: 600;
    }}
    .requirements {{
      border: 2px dashed #7fa6d7;
      border-radius: 24px;
      padding: 22px 28px;
      background: #fbfdff;
    }}
    .requirements h2 {{
      margin: 0 0 14px;
      color: var(--navy);
      font-size: 34px;
    }}
    .requirements ul {{
      margin: 0;
      padding: 0;
      display: grid;
      gap: 11px;
      list-style: none;
      font-size: 28px;
      line-height: 1.35;
    }}
    .requirements li {{
      display: grid;
      grid-template-columns: 42px 1fr;
      gap: 14px;
      align-items: start;
    }}
    .index {{
      width: 36px;
      height: 36px;
      display: grid;
      place-items: center;
      border-radius: 50%;
      background: var(--green);
      color: white;
      font-size: 22px;
      font-weight: 900;
    }}
    .bottom {{
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 24px;
      padding: 24px;
      border-radius: 28px;
      background: linear-gradient(135deg, #061b43 0%, #0b3678 100%);
      color: white;
      align-items: center;
    }}
    .qr-placeholder,
    .qr-img {{
      width: 236px;
      height: 236px;
      border-radius: 14px;
      background: white;
      color: var(--navy);
      display: grid;
      place-items: center;
      text-align: center;
      font-size: 30px;
      font-weight: 900;
      line-height: 1.25;
      object-fit: contain;
    }}
    .signup h2 {{
      margin: 0 0 12px;
      font-size: 34px;
    }}
    .signup p {{
      margin: 8px 0;
      font-size: 27px;
      line-height: 1.35;
      font-weight: 800;
    }}
    .footer {{
      margin-top: 14px;
      padding-top: 14px;
      border-top: 1px solid rgba(255, 255, 255, .32);
      color: rgba(255, 255, 255, .9);
      font-size: 22px;
      line-height: 1.35;
    }}
    @media (max-width: 980px) {{
      .poster {{ width: 100vw; min-height: 179.2vw; }}
    }}
  </style>
</head>
<body>
  <main class="poster">
    <section class="hero">
      <div class="badge">{study_type}</div>
      <h1>{title}</h1>
      <div class="hook">{hook}</div>
    </section>

    <section class="content">
      <h2 class="section-title">【实验内容】</h2>
      <ul class="content-list">
        {''.join(f'<li>{text(item)}</li>' for item in content_items) or '<li>实验内容待补充</li>'}
      </ul>

      <div class="cards">
        <div class="card">
          <div class="icon">DATE</div>
          <div class="label">【实验时间】</div>
          <div class="value"><strong>{text(brief.get("time"), "时间待补充")}</strong></div>
        </div>
        <div class="card">
          <div class="icon">TIME</div>
          <div class="label">【实验时长】</div>
          <div class="value">{text(brief.get("duration"), "时长待补充")}</div>
        </div>
        <div class="card">
          <div class="icon">FEE</div>
          <div class="label">【实验报酬】</div>
          <div class="value">{text(brief.get("compensation"), "报酬待补充")}<span class="note">{text(brief.get("bonus_or_transport"), "")}</span></div>
        </div>
        <div class="card">
          <div class="icon">SITE</div>
          <div class="label">【实验地点】</div>
          <div class="value">{text(brief.get("location"), "地点待补充")}</div>
        </div>
      </div>

      <section class="requirements">
        <h2>【被试要求】</h2>
        <ul>
          {list_items(eligibility_items)}
        </ul>
      </section>

      <section class="bottom">
        {qr_block(qr_code)}
        <div class="signup">
          <h2>【参与方式】</h2>
          <p>{text(brief.get("signup"), "扫码或添加主试微信报名")}</p>
          <p>联系方式：{text(brief.get("contact"), "待补充")}</p>
          <div class="footer">
            <div>{text(brief.get("organizer"), "课题组/实验室待补充")}</div>
            <div>{text(brief.get("ethics"), "伦理审批信息待补充")}</div>
          </div>
        </div>
      </section>
    </section>
  </main>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("brief", type=Path, help="Path to poster brief JSON")
    parser.add_argument("--output", "-o", type=Path, default=Path("poster.html"))
    args = parser.parse_args()

    brief = json.loads(args.brief.read_text(encoding="utf-8"))
    args.output.write_text(render_html(brief), encoding="utf-8")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
