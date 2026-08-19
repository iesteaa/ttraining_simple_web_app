# Decision Protocol

Ask exactly one decision per conversational turn unless two choices are inseparable.

Use this format:

## 判断: <short title>

**推奨:** <recommended option>

**根拠:** <repository evidence, existing component, or verified Vuetify capability>

**提案:** `<component or approach>` を使用します。

- **はい** — 推奨案で計画を確定する
- **いいえ** — この案を使わず、代替案を再調査する
- **カスタム** — ユーザーが希望する構成や制約を指定する

**影響:** <layout, maintainability, accessibility, or implementation impact>

Do not phrase a predetermined repository rule as an optional preference. State it as a constraint and ask only about the remaining product decision.

Do not ask about arbitrary values such as exact padding, icon pixels, or Vuetify visual props when design tokens or defaults already define them.

Before asking, search for evidence. Never ask “Which component should we use?” without first proposing the best existing candidate.
