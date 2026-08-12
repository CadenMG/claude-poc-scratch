# claude-poc-scratch

Scratch repo for the Grafana Assistant Claude cloud-agent POC.

`stats.py` provides small numeric helpers used by an imaginary reporting job.

## Fixed issue: `average()` off-by-one denominator

`average()` previously divided the sum of the values by `len(values) - 1`
instead of `len(values)`. This off-by-one denominator caused two problems:

- **Wrong mean for lists with more than one element** — e.g.
  `average([2, 4, 6])` should be `4.0` but returned `6.0`.
- **`ZeroDivisionError` for single-element lists** — e.g. `average([5])`
  raised an exception instead of returning `5.0`, since
  `len(values) - 1 == 0`.

The fix divides by `len(values)` (the correct denominator for an arithmetic
mean), so `average()` now returns the correct result for lists of any
non-empty size while still raising `ValueError` for empty input.

Run tests with `python -m pytest`.
