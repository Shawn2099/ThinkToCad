# Memory

Per-design attempt history + lessons learned. The agent learns from every attempt.

```
memory/
├── designs/
│   └── <design_name>/
│       ├── attempt_1.yaml   # what was tried, what failed
│       ├── attempt_2.yaml
│       └── final.yaml       # the validated design
└── lessons/
    └── "spacer_sleeve_fails_at_30mm.md"
```

Each attempt yaml: mechanism, status, verification (interference, clearance, mass), timestamp.
Failed attempts are as valuable as successes.
