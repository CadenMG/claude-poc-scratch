from prometheus_client import start_http_server

from app import record


def handle_checkout(ok: bool) -> None:
    record("success" if ok else "error")


if __name__ == "__main__":
    start_http_server(9100)
