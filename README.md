# claude-poc-scratch

Scratch repo for the Grafana Assistant Claude cloud-agent POC.

`stats.py` provides small numeric helpers used by an imaginary reporting job.

## Functions

- `total(values)` — sum of all values.
- `average(values)` — arithmetic mean of all values; raises `ValueError` on
  empty input.

Run tests with `python -m pytest`.
