# Style System

Use this file to choose a visual direction that improves on the reference examples instead of copying them. Pick one primary style and optionally one accent style. The poster must still prioritize readable Chinese text, clear QR placement, and research-relevant background motifs.

## Selection Rule

Choose style by matching four constraints:

- `study_method`: behavioral, questionnaire, fNIRS, EEG, eye-tracking, MRI, online game, child/campus, speech/acoustic.
- `conversion_hook`: reward, urgency, easy task, safety reassurance, academic credibility, fun/novelty.
- `detail_level`: compact, standard, explainer.
- `audience`: undergraduate group chat, graduate participants, parents/children, general campus.

If unsure, use `editorial-minimal` for text-heavy posters, `warm-social-lab` for fNIRS/social interaction, `neuro-tech-premium` for MRI/EEG/fNIRS with higher reward, and `urgent-comic` only for urgent or gender-specific slots.

## Style Directions

### neuro-tech-premium

Best for: MRI, EEG, fNIRS, high-reward neuroscience studies, formal lab recruitment.

Visual language: deep navy/cyan/emerald gradient, brain network mesh, scanner ring or head silhouette, subtle signal charts, glass cards.

Layout: large hero title, 3-5 translucent information cards, QR in a high-contrast footer or bottom corner.

Use when: the poster needs credibility, safety, and a premium research feel.

Avoid: dark backgrounds behind dense body text, fake medical dashboards, overdramatic radiation/illness visuals.

### warm-social-lab

Best for: interpersonal interaction, natural communication, emotion exchange, conversation tasks, multi-person fNIRS.

Visual language: warm cream or pale blue base, two abstract people/avatars, dialogue bubbles, soft signal waves connecting heads, friendly rounded cards.

Layout: title + friendly hook, paired cards for requirements/content, reward and location as small cards, QR CTA strip.

Use when: the task involves human interaction and should feel low-pressure.

Avoid: cold hospital mood or overly childish cartooning.

### editorial-minimal

Best for: text-heavy behavioral, EEG, MRI, and official posters where clarity matters more than decoration.

Visual language: off-white or light gray paper, strong black/blue typography, thin rules, sparse geometric accents, restrained highlight color.

Layout: magazine-like hierarchy with one large title, labeled paragraphs, generous line spacing, QR in a strict grid.

Use when: there are many constraints, safety exclusions, or exact time slots.

Avoid: too many cards, emoji-like icons, gradients under body text.

### data-card

Best for: behavioral decision tasks, online experiments, questionnaires, AI/reading/scoring tasks.

Visual language: modular cards, tiny charts, checkboxes, reaction buttons, abstract forms, dashboard-like but human.

Layout: 2x2 or stacked card system; numbers such as reward/time are emphasized as data chips.

Use when: the poster should look efficient, modern, and credible.

Avoid: fake UI text or tiny unreadable labels in the generated background.

### playful-collage

Best for: light tasks, student-friendly recruitment, "缺人速来", natural communication, short questionnaires.

Visual language: cutout stickers, paper clips, magnifier, keyboard, mascot, soft shadows, hand-drawn arrows.

Layout: oversized emotional title, tilted cards, QR as a prominent sticker block.

Use when: you need attention in a busy WeChat group.

Avoid: clutter near body text and random decorations unrelated to the study.

### urgent-comic

Best for: urgent slots, gender-specific recruitment, same-day online screening, "只缺男生/女生".

Visual language: bold black/red title, yellow warning labels, megaphone, alert badge, comic motion lines.

Layout: headline and urgent notice first, then pill labels for location/time/requirements/reward, QR lower right.

Use when: speed and clarity matter more than elegance.

Avoid: making formal neuroscience studies look unsafe or unserious.

### soft-watercolor

Best for: small-batch campus recruitment, child/education tasks, low-risk memory/language/voice experiments.

Visual language: pale blue/cream watercolor wash, soft clouds, gentle paper texture, minimal icons.

Layout: centered title, linear labels, QR at bottom, compact numbered requirements.

Use when: the study should feel calm and approachable.

Avoid: low contrast text or busy watercolor under body copy.

### retro-digital

Best for: online games, human-computer interaction, programming/coding tasks, pixel/avatar experiments.

Visual language: pixel grid, retro monitor, neon accents, game tiles, avatar cards, 8-bit-inspired but clean.

Layout: strong hook, task flow as step cards, device requirements and reward as badges, QR as "start" panel.

Use when: the recruitment needs a playful online/game identity.

Avoid: illegible pixel fonts for Chinese body text.

### safety-explainer

Best for: MRI, fNIRS, tES, EEG, experiments requiring reassurance or safety explanation.

Visual language: calm medical-tech palette, clean sidebar, simple method illustration, safety checkmarks.

Layout: main recruitment column plus explainer sidebar; CTA and reward remain prominent.

Use when: participants may worry about devices, radiation, electrical stimulation, or recording.

Avoid: burying signup information under long science explanation.

### campus-zine

Best for: undergraduate group chats, student-to-student recruitment, informal but credible posters.

Visual language: campus bulletin, sticker notes, tape, grid paper, campus building silhouette, friendly typography.

Layout: zine-like title, 2-3 paper cards, big QR, footer with ethics/organizer.

Use when: the poster should feel peer-made but polished.

Avoid: messy alignment or too many fonts.

### high-reward-billboard

Best for: high compensation, large participant target, "200+报酬", MRI/interaction studies with strong incentive.

Visual language: huge reward typography, clean luxury-academic background, vertical or diagonal JOIN/SCAN accent, minimal body cards.

Layout: reward/hook dominates top third; details are structured beneath; QR remains large.

Use when: compensation is the strongest conversion driver.

Avoid: making reward look clickbait or hiding requirements.

### clinical-trust

Best for: formal ethics-heavy, older participants, health-related screening, high-safety requirements.

Visual language: white, blue, teal, precise spacing, institutional calm, shield/check motifs.

Layout: official title, clear eligibility/exclusion list, safety and ethics footer, QR with contact.

Use when: trust and seriousness are more important than viral attention.

Avoid: playful mascots, slang, or exaggerated urgency.

## Combining Styles

Use only one combination at a time:

- `warm-social-lab + data-card`: social fNIRS with structured task details.
- `neuro-tech-premium + safety-explainer`: MRI/EEG posters with safety reassurance.
- `campus-zine + playful-collage`: casual student recruitment with approachable visuals.
- `urgent-comic + editorial-minimal`: urgent but still readable and not chaotic.
- `high-reward-billboard + neuro-tech-premium`: high-pay neuroscience recruitment.

## Prompt Add-On

Append this to image prompts after choosing a style:

```text
Style direction: [style_direction].
Make the result more polished than a typical WeChat recruitment screenshot: stronger typographic hierarchy, cleaner spacing, fewer random decorations, research-relevant motifs, and a clear QR/CTA zone.
Do not copy any reference image exactly. Use the references only to understand information structure.
```

