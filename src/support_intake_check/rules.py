from __future__ import annotations

from support_intake_check.models import Rule

PROJECT_NAME = 'support-intake-check'
SUMMARY = 'Lint support intake forms for priority, reproduction, and account fields.'
SAMPLE_RISK = 'priority missing repro none account_id unknown'
SAMPLE_CLEAN = 'priority p2 repro steps account_id acct_123'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='missing-priority',
        severity='high',
        pattern='priority\\s+(missing|none|unknown)',
        message='priority field missing',
        recommendation='add priority field',
    ),
    Rule(
        code='missing-repro',
        severity='medium',
        pattern='repro\\s+(none|missing|unknown)',
        message='reproduction steps missing',
        recommendation='request repro details',
    ),
    Rule(
        code='unknown-account',
        severity='low',
        pattern='account_id\\s+(unknown|missing|none)',
        message='account identifier missing',
        recommendation='capture account identifier',
    ),
)
