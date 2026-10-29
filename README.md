# claude-poc-scratch

Scratch repo for the Grafana Assistant Claude cloud-agent POC.

`stats.py` provides small numeric helpers used by an imaginary reporting job.

## Known issue

`average()` returns wrong results — e.g. `average([2, 4, 6])` should be `4.0`
but returns `6.0`. The intended behavior is the arithmetic mean of all values.

Run tests with `python -m pytest`.

## Pizza recommendations

The storefront recommends a pizza on the home page. This change tunes the recommendation copy.
