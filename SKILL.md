---
name: subject-recruitment-poster
description: Generate psychology, neuroscience, behavioral, questionnaire, online-game, fNIRS, EEG, eye-tracking, MRI, and campus participant recruitment posters with prompt-first image generation. Use when the user wants a 被试招募海报, participant recruitment flyer, study recruitment visual, WeChat group recruitment image, poster copy, QR-code recruitment poster, or a reusable poster prompt/template for human-subject experiments; prioritize image generation tools, use GPT image models for direct text rendering when available, use background-plus-text overlay for other image models, and fall back to HTML only when image generation is unavailable.
---

# Subject Recruitment Poster

## Workflow

Use this skill to turn study details into a clear, credible Chinese recruitment poster optimized for WeChat group sharing.

1. Gather missing essentials before designing: study type, participant target, task/content, time/date, duration, compensation, location or online platform, eligibility/exclusion criteria, signup method, contact/QR code, institution/lab, and ethics/approval note if applicable.
2. If the user provides chat logs, previous posters, QR codes, lab logos, or brand constraints, inspect them first and preserve the established wording and visual conventions unless asked to redesign.
3. Create a structured poster brief and a text-layout plan before visual generation. Keep the brief short enough to fit on the target poster.
4. Derive background motifs from the actual research content before prompting. The background must support the study theme rather than use generic decoration.
5. Generate an image prompt first. Use the available image generation tool before any HTML workflow.
6. If using a GPT image model or another model known to render Chinese text accurately, generate the complete poster with real text directly.
7. If using a model that is unreliable with Chinese text, generate only the illustrated background and empty text panels, then overlay real text and reserve/insert QR with `scripts/compose_poster_text.py`.
8. Use HTML only as a fallback when no image generation tool is available or the user explicitly asks for HTML.
9. Verify research relevance, layout balance, legibility, field completeness, QR space, and ethical claims before finishing.

## User Input Prompt

When the user's request lacks key details, ask them to paste/fill this concise template instead of asking many separate questions. Use `references/input-template.md` for the full template and examples.

```text
请按下面信息生成被试招募海报：
1. 实验名称/标题：
2. 一句话卖点/招募重点：
3. 实验类型/方法：
4. 实验内容：
5. 实验时间和时长：
6. 实验地点或线上平台：
7. 被试要求：
8. 报酬/奖励/路补：
9. 报名方式/二维码/联系人：
10. 备注格式：
11. 伦理批准号/课题组：
12. 风格偏好/参考图：
```

## Required Poster Brief

Normalize user input into this schema:

```yaml
title: "心理学实验被试招募"
hook: "大脑奥秘：工作记忆研究"
study_type: "磁共振 / 近红外 / 行为实验 / 线上问卷 / 游戏实验 / 眼动 / 脑电"
experiment_content:
  - "完成 2 个工作记忆任务"
  - "填写问卷"
time: "6月4日上午、6月5日下午"
duration: "共100分钟"
compensation: "完成全程 120 元被试费"
bonus_or_transport: "路途较远可补贴 10-15 元"
eligibility:
  - "18-35周岁"
  - "无精神/神经疾病史"
  - "未参加过本系列实验"
location: "某大学实验楼 / 示例脑成像实验室 / 线上平台"
signup: "扫码添加微信，备注：被试+姓名+性别+年级专业"
contact: "微信号 / 手机号 / 链接"
ethics: "已获伦理审批，编号：..."
organizer: "课题组 / 实验室 / 学校"
qr_code: "path-or-url-if-provided"
qr_slot: "bottom-left / bottom-right / left-column / reserved blank square"
style: "choose from references/style-system.md, e.g. neuro-tech-premium / warm-social-lab / editorial-minimal / urgent-comic / soft-watercolor / retro-digital / data-card / campus-zine / safety-explainer / playful-collage"
generation_mode: "gpt-image-direct-text / background-plus-overlay / html-fallback"
output: "png / prompt / html-fallback"
```

Ask a concise follow-up only for fields that materially affect compliance or usability: signup method, compensation, time/duration, target participants, or QR code. Otherwise make reasonable placeholders and mark them as placeholders.

## Content Structure

Use this priority order for most posters:

1. Top hero: large recruitment title plus study hook. Make the title immediately readable in a WeChat thumbnail.
2. Study value/content: one short theme line and 2-4 task bullets.
3. Time and duration: prominent card near the top-middle.
4. Compensation: high-contrast card with exact amount and settlement rule.
5. Eligibility/exclusion criteria: checklist with age, health, gender/professional requirements, repeat-participation limits, device requirements for online studies, and safety constraints for MRI/fNIRS/EEG.
6. Location or platform: building/lab/room or online platform link.
7. Signup: QR code/contact plus exact remark format.
8. Footer: organizer, lab/institution, ethics approval, privacy note, or "名额有限/持续招募" if space permits.

Use `references/poster-analysis.md` when you need examples, field frequencies, or wording patterns from the ECNU chat-log analysis.
Use `references/input-template.md` when the user needs a fill-in input prompt.
Use `references/style-system.md` when choosing a poster visual direction beyond the user-provided examples.

## Generation Mode Decision

Use this order:

1. **GPT image direct text**: Use when the image tool is a GPT image model or has demonstrated reliable Chinese text rendering. Prompt it with the exact title, labels, body text, QR placeholder, layout, palette, and instruction to render no extra text.
2. **Background plus overlay**: Use when the image model may distort Chinese text. Prompt for a clean poster background with empty cards, blank label ribbons, visual motifs, and a reserved QR square. Then run the overlay script to place real Chinese text.
3. **HTML fallback**: Use only when no image generation tool is available or the user specifically requests an editable web draft.

For prompt templates and model-specific instructions, read `references/prompt-workflow.md`.

Before writing prompts, choose:

- `primary_message`: the one thing the viewer should remember first, usually title/hook, reward, urgency, or study type.
- `required_modules`: time, duration, reward, location/platform, requirements, signup, ethics.
- `detail_level`: compact, standard, or explainer. Use compact for urgent small-slot posters, standard for most group posters, and explainer only when the method needs reassurance or safety context.
- `background_motifs`: 2-4 motifs tied to the research content, not generic visual filler.
- `style_direction`: one style from `references/style-system.md`, selected by research type, audience, urgency, and information density. Do not copy the reference images literally.

## Text Overlay Script

For non-GPT image models, generate a background first, then place text:

```bash
pip install -r requirements.txt
python scripts/compose_poster_text.py assets/example-brief.json --background background.png --output poster.png
```

If no background is passed, the script creates a clean placeholder poster. The output reserves a high-contrast QR area; replace it with the actual QR code if provided in `qr_code`. For better Chinese typography, set `POSTER_FONT` and `POSTER_FONT_BOLD` to local CJK font paths when needed.

## HTML Fallback

When image generation is unavailable, use the bundled HTML script:

```bash
python scripts/render_poster_html.py assets/example-brief.json --output poster.html
```

The script accepts the Required Poster Brief as JSON and creates a standalone 9:16 HTML poster. Use this as a fallback, not the default path.

## Layout Rules

Default to a vertical poster for WeChat sharing: 9:16 or close to 1240x1754, 937x1679, or 1080x1920 px. Use landscape only when examples or user requirements indicate a wide WeChat card. Keep safe margins of at least 5% width.

Recommended composition:

```text
[0-28%] hero illustration, title, experiment theme
[28-48%] experiment content, time, duration, compensation cards
[48-72%] eligibility checklist and caution notes
[72-86%] location card
[86-100%] QR code/contact, signup remark, organizer, ethics
```

Design guidance:

- Use strong hierarchy: title 2.5-4x body size, section labels 1.3-1.8x body size.
- Highlight numbers such as dates, minutes, and compensation with a second color.
- Use bracketed labels common in the source corpus: `【实验内容】`, `【实验时间】`, `【实验报酬】`, `【被试要求】`, `【参与方式】`.
- Use semantic text badges to make the poster scannable. Prefer compact meaningful words such as `DATE`, `TIME`, `FEE`, `SITE`, `SCAN`, or `JOIN` over decorative single-character placeholders like `日`, `时`, `￥`, `地`.
- Keep QR codes unwarped, high contrast, and no smaller than 18-22% of poster width.
- Avoid more than 6-8 checklist items; split long criteria into short phrases.
- For MRI/fNIRS/EEG posters, use restrained science visuals: brain outline, scanner, network mesh, waveforms, charts. Do not make medical treatment claims.
- For online questionnaires or games, reduce lab imagery and emphasize "线上可参与", device requirements, validation checks, and link/QR access.
- For prompt-first generation, separate "background visual prompt" from "exact text payload" unless the model is a GPT image model.
- Keep background relevance explicit: behavioral tasks can use grids, decision cards, game controllers, keyboards, or visual target shapes; fNIRS/EEG/tES can use head-cap silhouettes, gentle waveforms, social interaction scenes, or signal lines; MRI can use scanner rings, brain networks, or tunnel-perspective grids; online questionnaires can use phone/laptop/forms; child/campus studies can use soft campus/classroom cues.
- Keep details proportional: hero title and CTA must be visible at thumbnail size, core modules should fit in 3-5 cards or labeled blocks, long explanations should move to a sidebar or be reduced to 2-3 reassurance bullets.

## Copywriting Rules

Write in concise Chinese suitable for campus WeChat groups. Prefer concrete, low-friction wording:

- "持续招募中"
- "时间可选"
- "完成全程：120元被试费"
- "路途较远可申请10元路补"
- "扫码添加主试微信"
- "请备注：被试+姓名+性别+年级专业"
- "参加过本系列实验的同学不可重复参加"

For urgent slots, add a small badge such as "急招今晚", "仅招男生", "本周名额", or "缺2位", but keep the main title stable.

Avoid vague or risky wording:

- Do not write "无风险", "保证通过", "治疗", "诊断", or any claim that overstates benefits.
- Do not hide inconvenient requirements such as MRI contraindications, camera/microphone needs, attention checks, or payment conditions.
- Do not imply compensation is unconditional if payment depends on completion, screening, or data validity.

## Compliance Check

Before final output, verify:

- The poster states who can participate and who should not participate.
- Compensation has an amount, condition, and payout timing if known.
- Duration and location/platform are unambiguous.
- Signup path works visually: QR code, WeChat ID, link, or contact is present.
- Human-subject posters include ethics approval or a clear placeholder if unavailable.
- Medical-device studies include relevant safety exclusions, especially for MRI: metal implants, claustrophobia, permanent makeup/metal pigments, pregnancy if applicable, and neurological/psychiatric history where relevant.
- Personal data collection is not overexposed on the poster; detailed forms should live behind QR/link.

## Output Patterns

When generating a poster prompt for an image model, include:

- aspect ratio and size;
- exact Chinese text blocks;
- typography hierarchy;
- color palette;
- visual motif;
- study-content relevance: background motifs should reflect the task/method/population;
- detail balance: what is emphasized, what is compressed, and where long explanation goes;
- QR placement instruction;
- instruction for either direct text rendering or empty background panels;
- "render all Chinese text accurately, no extra text, no gibberish" only when using a GPT image model or equivalent reliable text renderer.

When generating a background for later overlay, explicitly require: no readable text, no fake letters, empty text boxes, reserved QR square, and enough negative space for the planned modules.

When using HTML fallback, implement the content as real text and reserve a fixed QR/image slot. Use CSS variables for palette and verify mobile/thumbnail legibility.

When the user asks for only analysis or skill design, return a concise design spec and point to the generated skill folder.
