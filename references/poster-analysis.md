# ECNU 被试招募海报与群聊文案分析

Source: local WeChat export JSONL files under `聊天记录/` plus visible poster images in the working folder used during skill creation.

## Data Notes

- 5 WeChat group exports were inspected.
- 582 message records were found, including 275 image messages and 265 unique referenced image paths.
- Image messages are stored as `type=7` with paths like `../images/*.jpg`. Resolved relative to the JSONL files, these point to an adjacent `images/` folder; that directory was not present in the creation workspace.
- Available visual evidence came from the local generated poster image `poster_qr_replaced_larger_clean_down.png`, size 937x1679 px, approximately 9:16.
- Text evidence came from messages near image posts and recruitment copy in the logs.

## Field Frequency In Text Messages

Approximate message counts containing each module:

| Module | Count |
|---|---:|
| 招募/被试 | 145 |
| 报名/联系方式 | 139 |
| 报酬/补贴 | 129 |
| 时间/时长 | 98 |
| 地点 | 73 |
| 实验内容 | 64 |
| 要求/筛选 | 62 |
| 伦理/审批 | 0 in chat text; visible in local poster footer |

Interpretation: WeChat recruitment posts optimize for fast action. Signup/contact, compensation, and participant target should be highly visible. Ethics approval appears more often on formal posters than in short group text.

## Common Content Modules

Required:

- Title: `心理学实验被试招募`, `磁共振实验 被试招募`, `普陀校区 行为实验被试招募`, `近红外多人互动实验被试招募`.
- Hook or study theme: examples include working memory, AI reading/scoring, decision task, voice production, online game, questionnaire.
- Time/date: exact slots, date ranges, or `持续招募中`.
- Duration: `约35分钟`, `约60分钟`, `90分钟`, `180分钟`, or multi-day structure.
- Compensation: fixed amount, per-minute amount, base + bonus, route subsidy, payment conditions.
- Location/platform: campus, building, room, lab, online platform, link.
- Eligibility/exclusion: age, gender, major, health history, sensory constraints, device requirements, repeat-participation limits.
- Signup method: QR code, WeChat ID, phone, link, and remark format.

Recommended for formal posters:

- Organizer/lab/institution.
- Ethics approval number.
- Data validity/payment caveats.
- Safety exclusions for MRI/fNIRS/EEG.

## Repeated Wording Patterns

Use these patterns directly or adapt them:

- `【实验内容】...`
- `【实验时间】6月持续招募中`
- `【实验地点】某大学...`
- `【实验时长】约90分钟`
- `【实验报酬】60元基础被试费+0-30元奖励`
- `路程较远被试可以申请15CNY路费补贴`
- `请按照要求备注后发送好友申请，谢谢配合！`
- `请备注：被试+性别+姓名+年级专业`
- `参加过本人实验及相关系列实验的同学不可重复参加`
- `实验轻松简单，欢迎扫码报名`

## Observed Compensation Patterns

- Online questionnaire: `1-2元`, often paid after quality check.
- Online game: `10元/30min + 额外奖励`.
- Short behavioral/voice task: `1元/分钟`, `45元基础 + 浮动奖励`.
- 60-100 minute lab tasks: `60-120元`.
- MRI/nuclear magnetic resonance: often `150元 + 0-20元浮动`.
- Principal investigator/helper recruitment: `150r/天`.
- Transport subsidies: `10元路补`, `15CNY路费补贴`.

## Visual Structure From Available Poster

Poster ratio: 937x1679, near 9:16.

Structure:

- Hero top: dark blue science-tech background, large white title, brain/MRI illustration.
- Theme line: oversized subtitle, e.g. `大脑奥秘：工作记忆研究`.
- Middle cards: white background with blue/green accents for `实验内容`, `实验时间`, `实验时长`, `实验报酬`.
- Requirement area: numbered checklist with icons.
- Location area: map pin icon plus building/lab text.
- Bottom signup area: QR code on left, contact/remark on right, organizer and ethics approval at footer.

Visual language:

- Academic, neuroscience, blue-green palette.
- High contrast titles, strong numeric emphasis.
- Rounded white cards, dotted dividers, simple line icons.
- QR code remains square and high contrast.

## Template Variants

MRI / fMRI:

- Motifs: MRI scanner, brain silhouette, network mesh, waveform/chart.
- Safety criteria: metal implants, metal pigments/permanent makeup, claustrophobia, neurological/psychiatric history, pregnancy if relevant.
- Emphasize location and duration because commitment is high.

fNIRS / EEG / eye tracking:

- Motifs: brain cap, waveforms, sensors, interaction scene.
- Criteria: hair/head constraints only if relevant, normal/corrected vision, no neurological history.
- Include preparation time separately from task time.

Behavioral lab:

- Motifs: checklist, laptop, campus building, simple task cards.
- Emphasize flexible slots, exact room, compensation.

Online questionnaire/game:

- Motifs: phone/laptop, link/QR, cloud/platform.
- Include device requirements, camera/microphone needs, attention checks, repeated ID invalidation, quality-based payment rule.

Urgent group post:

- Use a compact poster or image card.
- Lead with slot scarcity: `急招今晚`, `缺2位`, `仅招男生`.
- Keep only time, location, compensation, requirements, and signup.

## Default Poster Checklist

Before generating, ensure these are present:

- Main title and study hook.
- At least 2 task/content bullets.
- Time and duration.
- Compensation and payment condition.
- Eligibility and exclusions.
- Location/platform.
- Signup method with QR/contact.
- Organizer.
- Ethics approval or placeholder.
