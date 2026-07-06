# Support Intake Check

| | |
| --- | --- |
| Focus | support operations |
| Command | `support-intake-check` |
| Inputs | text, JSON, JSONL, or CSV |
| Output | Markdown or JSON |

![Support Intake Check cover](assets/readme-cover.svg)

Lint support intake forms for priority, reproduction, and account fields. I keep it small because this kind of check is most useful when it can run beside the work, not after the work has already shipped.

## Policy surface

| Rule | Level | Why it matters |
| --- | --- | --- |
| `missing-priority` | high | priority field missing |
| `missing-repro` | medium | reproduction steps missing |
| `unknown-account` | low | account identifier missing |

## Local run

```bash
git clone https://github.com/mertefekurt/support-intake-check.git
cd support-intake-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
support-intake-check examples/sample.txt
support-intake-check examples/sample.txt --json
```

## Why the sample fails

`priority missing repro none account_id unknown` is intentionally shaped to hit the rules above, so it is useful as a quick smoke test after edits.
