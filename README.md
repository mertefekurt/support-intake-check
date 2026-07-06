# Support Intake Check

<p align="center">
  <img src="assets/readme-cover.svg" alt="Support Intake Check cover" width="100%" />
</p>

![stack](https://img.shields.io/badge/stack-Python-7c3aed?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-0891b2?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-b45309?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-be185d?style=flat-square)

Lint support intake forms for priority, reproduction, and account fields.

## The short version

`support-intake-check` is intentionally small: feed it a file, get deterministic findings, and decide whether the result should block a merge or just guide cleanup.

## Rule surface

| Rule | Severity | What it catches |
| --- | --- | --- |
| `missing-priority` | high | priority field missing |
| `missing-repro` | medium | reproduction steps missing |
| `unknown-account` | low | account identifier missing |

## Usage

```bash
python -m pip install -e ".[dev]"
support-intake-check examples/sample.txt
support-intake-check examples/sample.txt --json --fail-on medium
```

## Useful defaults

| Option | Reason |
| --- | --- |
| `--json` | machine-readable output for scripts |
| `--fail-on medium` | stricter CI gate when warnings matter |
| `--format auto` | let the reader detect text, CSV, JSON, or JSONL |

## Local checks

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m support_intake_check --help
```
