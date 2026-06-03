#!/usr/bin/env python3
"""Compose real Chinese text onto a generated poster background."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont


CANVAS = (1240, 1754)


def as_list(value: Any) -> list[str]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return [line.strip() for line in str(value).splitlines() if line.strip()]


def pick_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    env_font = os.environ.get("POSTER_FONT_BOLD" if bold else "POSTER_FONT")
    candidates = [
        env_font,
        "C:/Windows/Fonts/msyhbd.ttc" if bold else "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/simhei.ttf",
        "C:/Windows/Fonts/simsun.ttc",
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
        "C:/Windows/Fonts/arial.ttf",
    ]
    for path in candidates:
        if path and Path(path).exists():
            return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()


def fit_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for char in text:
        test = current + char
        if draw.textbbox((0, 0), test, font=font)[2] <= width or not current:
            current = test
        else:
            lines.append(current)
            current = char
    if current:
        lines.append(current)
    return lines


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.ImageFont,
    fill: str,
    width: int,
    line_gap: int = 10,
) -> int:
    x, y = xy
    line_height = draw.textbbox((0, 0), "国", font=font)[3] + line_gap
    for line in fit_text(draw, text, font, width):
        draw.text((x, y), line, font=font, fill=fill)
        y += line_height
    return y


def draw_card(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    body: list[str],
    accent: str = "#1266a3",
) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=28, fill=(255, 255, 255, 235), outline="#9fcde0", width=3)
    title_font = pick_font(40, bold=True)
    body_font = pick_font(31)
    draw.text((x1 + 34, y1 + 24), title, font=title_font, fill=accent)
    y = y1 + 88
    for item in body:
        y = draw_wrapped(draw, (x1 + 38, y), f"• {item}", body_font, "#1b2430", x2 - x1 - 76, 8)
        y += 6
        if y > y2 - 42:
            break


def create_base(background: Path | None) -> Image.Image:
    if background and background.exists():
        return Image.open(background).convert("RGB").resize(CANVAS, Image.Resampling.LANCZOS)
    img = Image.new("RGB", CANVAS, "#f7fbff")
    draw = ImageDraw.Draw(img, "RGBA")
    draw.rectangle((0, 0, CANVAS[0], CANVAS[1]), fill="#e9fbff")
    draw.ellipse((-180, -120, 420, 420), fill=(255, 227, 119, 120))
    draw.ellipse((840, 90, 1320, 560), fill=(167, 229, 213, 120))
    draw.ellipse((760, 1320, 1380, 1980), fill=(255, 195, 220, 120))
    return img


def compose(brief: dict[str, Any], background: Path | None, output: Path) -> None:
    img = create_base(background)
    draw = ImageDraw.Draw(img, "RGBA")
    title_font = pick_font(76, bold=True)
    hook_font = pick_font(44, bold=True)
    footer_font = pick_font(28)

    title = str(brief.get("title") or "心理学实验被试招募")
    hook = str(brief.get("hook") or brief.get("study_type") or "")
    draw.text((80, 72), title, font=title_font, fill="#082c4c")
    if hook:
        draw.text((84, 168), hook, font=hook_font, fill="#ef4f75")

    content = as_list(brief.get("experiment_content"))
    eligibility = as_list(brief.get("eligibility"))
    time = [str(brief.get("time") or "时间待补充"), str(brief.get("duration") or "时长待补充")]
    reward = [str(brief.get("compensation") or "报酬待补充")]
    if brief.get("bonus_or_transport"):
        reward.append(str(brief["bonus_or_transport"]))
    signup = [str(brief.get("signup") or "扫码添加主试微信报名")]
    if brief.get("contact"):
        signup.append(f"联系方式：{brief['contact']}")

    draw_card(draw, (72, 270, 1168, 585), "【实验内容】", content or ["实验内容待补充"])
    draw_card(draw, (72, 620, 602, 930), "【实验时间】", time)
    draw_card(draw, (638, 620, 1168, 930), "【实验报酬】", reward, "#d85f00")
    draw_card(draw, (72, 965, 1168, 1285), "【被试要求】", eligibility or ["被试要求待补充"])
    draw_card(draw, (72, 1320, 755, 1595), "【报名方式】", signup, "#1266a3")

    qr_box = (820, 1340, 1090, 1610)
    qr_value = str(brief.get("qr_code") or "").strip()
    qr_path = Path(qr_value) if qr_value else None
    if qr_path and qr_path.is_file():
        qr = Image.open(qr_path).convert("RGB").resize((270, 270), Image.Resampling.LANCZOS)
        img.paste(qr, qr_box[:2])
    else:
        draw.rectangle(qr_box, fill="#ffffff", outline="#111111", width=5)
        qr_font = pick_font(38, bold=True)
        draw.text((qr_box[0] + 55, qr_box[1] + 92), "QR CODE", font=qr_font, fill="#222222")
        draw.text((qr_box[0] + 48, qr_box[1] + 142), "二维码区域", font=pick_font(30, bold=True), fill="#222222")

    footer = str(brief.get("ethics") or "伦理审批信息待补充")
    organizer = str(brief.get("organizer") or "")
    draw.text((80, 1640), organizer, font=footer_font, fill="#243241")
    draw.text((80, 1682), footer, font=footer_font, fill="#243241")
    img.save(output)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("brief", type=Path, help="Path to poster brief JSON")
    parser.add_argument("--background", type=Path, default=None, help="Generated no-text background image")
    parser.add_argument("--output", "-o", type=Path, default=Path("poster.png"))
    args = parser.parse_args()

    brief = json.loads(args.brief.read_text(encoding="utf-8"))
    compose(brief, args.background, args.output)
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
