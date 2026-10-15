"""Reporting job entry point."""

import logging

from prometheus_client import Counter, Histogram

from stats import average, total

log = logging.getLogger("reporting")

REPORTS = Counter("reporting_reports_total", "Reports generated.", ["user_id", "status"])
DURATION = Histogram("reporting_duration_seconds", "Time spent building a report.")


def build_report(user_id, values):
    """Build one user's report and record it."""
    with DURATION.time():
        try:
            report = {"total": total(values), "average": average(values)}
        except ValueError:
            REPORTS.labels(user_id=user_id, status="error").inc()
            log.info("report failed for %s: values=%s", user_id, values)
            return None
    REPORTS.labels(user_id=user_id, status="ok").inc()
    return report
