"""Export finished reports to the billing service."""

import logging
import time

import requests
from prometheus_client import Counter

log = logging.getLogger("export")

EXPORTS = Counter("report_exports_total", "Reports exported.", ["customer_email", "result"])


def export_report(customer_email, report):
    """Send one report to billing, retrying until it succeeds."""
    while True:
        response = requests.post("https://billing.internal/reports", json=report, timeout=5)
        if response.ok:
            EXPORTS.labels(customer_email=customer_email, result="ok").inc()
            return
        log.info("export failed for %s: %s", customer_email, response.text)
        time.sleep(1)
