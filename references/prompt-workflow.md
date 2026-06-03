# Prompt-First Poster Generation Workflow

## Default Decision

1. Use the image generation tool first.
2. If the model is GPT image or is known to render Chinese text accurately, generate the full poster directly with exact text.
3. If the model is not reliable for Chinese text, generate a no-text background with blank text panels and QR space, then overlay text with a deterministic script.
4. Use HTML only when image generation is unavailable or explicitly requested.

## Direct Text Prompt Template

Use with GPT image models:

```text
Create a finished Chinese participant recruitment poster.
Canvas: [vertical 9:16 / landscape 16:9], [size].
Style: [style_direction selected from style-system.md].
Research-relevant background: [2-4 motifs that directly match the study task/method/population, not generic decoration].
Layout density: [compact / standard / explainer]. Emphasize [primary_message]. Compress [secondary_details].
Render all Chinese text exactly as provided. Do not add extra text, fake characters, or gibberish.
Keep the QR area as a clean blank white square labeled only if requested: [QR placeholder instruction].

Text:
Title: ...
Subtitle / hook: ...
Sections:
【实验内容】...
【实验时间】...
【实验时长】...
【实验报酬】...
【实验地点】...
【被试要求】...
【报名方式】...
Ethics: ...

Layout:
...
Visual motifs:
...
```

## Background-Only Prompt Template

Use with non-GPT image models:

```text
Create a clean recruitment poster background only. No readable text, no fake letters, no pseudo-Chinese, no numbers.
Canvas: [vertical 9:16 / landscape 16:9], [size].
Background must be related to the research content: [task/method/population] represented by [specific motifs].
Layout density: [compact / standard / explainer]. Keep [primary_message area] dominant, leave [secondary card areas] quieter.
Reserve blank content areas for later real text overlay:
- Large title area: [position and size]
- Section card 1: [position]
- Section card 2: [position]
- Section card 3: [position]
- QR code blank white square: [position and size]
- Footer strip: [position]
Style: [style_direction selected from style-system.md].
Visual motifs: [specific motifs selected from the research-content map below].
Use high-contrast but light text panels, leaving enough negative space. Avoid busy textures behind text areas.
Do not include any text or symbols that look like text.
```

## Research Content To Background Motifs

Select 2-4 motifs that make the study identifiable without overwhelming the text:

| Study content | Good motifs | Avoid |
|---|---|---|
| Behavioral judgment, visual attention, decision task | grid cells, target dots, reaction buttons, keyboard keys, decision cards, simple game board | unrelated brain scanners, generic medical imagery |
| Memory, language, vocabulary, reading | word cards without readable text, book pages as abstract shapes, memory tiles, speech bubbles, pen/paper | fake letters or pseudo-Chinese in generated background |
| fNIRS / natural communication / interaction | two-person silhouettes, head-cap outline, soft signal waves, conversation bubbles, lightweight sensor lines | hospital-like surgery imagery or radiation symbols |
| EEG / brain electrical activity | head silhouette, electrode dots, waveforms, soft blue/cyan gradients | scary medical wires or intense lightning unless urgent/comic style |
| MRI / fMRI / nuclear magnetic resonance | scanner ring, tunnel perspective, brain network mesh, safe-tech blue/green charts | claustrophobic dark tunnel as main visual |
| Online questionnaire / game / platform task | laptop, phone, form cards, cloud nodes, avatar tiles, webcam icon if required | fake interface text or unreadable UI labels |
| Acoustic / speech / voice task | sound waves, microphone, ear icon, speech bubbles | loudspeaker dominating the whole page unless recruiting urgently |
| Child/campus study | campus building silhouette, classroom shapes, warm stationery, soft playful forms | childish style if recruiting adults |
| Urgent shortage / gender-specific slots | warning badge, megaphone, bold red highlight, scarcity tag | cluttered alarms that reduce trust |

## Layout Density Rules

Choose detail level before prompting:

- `compact`: 4-6 total modules. Use for urgent recruitment or small participant count. Keep title, time, location, reward, requirements, QR. Put explanation behind QR or omit.
- `standard`: 6-8 modules. Use for most posters. Use 3-5 cards: content, time/duration, reward, requirements, location/signup. Keep each bullet within one line when possible.
- `explainer`: long method reassurance is needed, e.g. fNIRS/tES/MRI safety. Use a two-column layout or a right sidebar. Keep the main CTA and reward prominent; move background explanation into 2 short paragraphs or 4 bullets.

Information hierarchy:

- Level 1: title/hook, reward or urgency, QR/CTA.
- Level 2: time, duration, location/platform, participant target.
- Level 3: task details, exclusions, ethics, payment conditions.
- Level 4: long technique explanation; include only when it reduces participant anxiety or clarifies safety.

Compression rules:

- Combine time + duration when space is tight.
- Combine reward + payment condition in one card.
- Keep requirements to 4-6 bullets; move rare exclusions to signup form unless safety-critical.
- Ethics approval can be footer-sized unless it is required by the lab template.

## Text Structure Patterns From User Examples

Landscape information card:

- Huge title line: `诚招被试 | 多人匿名互动实验 for 6月`.
- Left column: mascot or symbolic image above QR.
- Right area: 2x2 cards for `受试者要求`, `实验内容`, `实验报酬`, `实验地点`.
- Bottom CTA strip: scan QR, add WeChat, remark format, ethics approval.

Minimal list poster:

- Center title.
- Linear labeled paragraphs: `【实验内容】`, `【实验时长】`, `【实验报酬】`, `【实验地点】`, `【被试要求】`, `【注意事项】`.
- QR in lower right; ethics approval near bottom.
- Light decorative grid/circle background, text is the primary design.

Urgent large-word poster:

- Very large emotional title, e.g. `缺人速来`.
- First card: location, content, requirements, explanation.
- Second card: duration, compensation, participation method.
- QR lower left or bottom area; decorative collage elements around the edges.

Two-column science explainer:

- Left main column: task, duration, reward, requirements, time/location, investigator, QR.
- Right sidebar: plain-language explanation of technique and study purpose.
- Works for fNIRS/EEG/tES when the method needs reassurance.

Plain watercolor notice:

- Soft background, centered title.
- Compact label list plus numbered requirements.
- QR at bottom; minimal ornamentation.
- Useful for urgent small-batch recruitment.

Comic warning poster:

- Heavy title, warning badge, highlighted urgent note.
- Large pill-shaped labels for location, time, requirements, reward, contact.
- Red emphasis for gender/slot/real-name constraints.
- QR lower right.

Tech vertical poster:

- Oversized reward or hook at top, e.g. `200+报酬`.
- Vertical `JOIN US` or similar decorative typography.
- Stacked rounded cards for experiment situation, participant requirements, signup.
- Small QR embedded inside signup card.
