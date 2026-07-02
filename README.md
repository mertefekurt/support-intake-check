# support-intake-check

> Lint support intake forms for priority, reproduction, and account fields.

## Spec sheet Overview

Lint support intake forms for priority, reproduction, and account fields. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts support intake schema. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
support-intake-check examples/sample.txt
support-intake-check examples/sample.txt --json --fail-on medium
python -m support_intake_check --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `missing-priority` | high | priority field missing |
| `missing-repro` | medium | reproduction steps missing |
| `unknown-account` | low | account identifier missing |

## Validation Notes

```bash
ruff check .
pytest
python -m support_intake_check --help
```

Example risky input:

```text
priority missing repro none account_id unknown
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
