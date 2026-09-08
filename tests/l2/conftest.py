"""L2 fixtures: a real server on a real socket.

Default: start uvicorn on a free localhost port for the session and stop it
afterwards. Set BASE_URL (e.g. http://127.0.0.1:8000 or the deployed URL) to
run the same tests against an already-running instance instead; that is the
L3 use of this suite.
"""

import os
import socket
import subprocess
import sys
import time

import httpx
import pytest


def _free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _wait_for(url: str, timeout: float = 15.0) -> None:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            if httpx.get(url, timeout=1.0).status_code == 200:
                return
        except httpx.HTTPError:
            pass
        time.sleep(0.1)
    raise RuntimeError(f"server at {url} did not become healthy within {timeout}s")


@pytest.fixture(scope="session")
def base_url() -> str:
    external = os.environ.get("BASE_URL")
    if external:
        _wait_for(external.rstrip("/") + "/health", timeout=5.0)
        yield external.rstrip("/")
        return

    port = _free_port()
    url = f"http://127.0.0.1:{port}"
    proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "src.main:app", "--host", "127.0.0.1", "--port", str(port)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        _wait_for(url + "/health")
        yield url
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()


@pytest.fixture
def http(base_url: str) -> httpx.Client:
    with httpx.Client(base_url=base_url, timeout=5.0) as client:
        yield client
