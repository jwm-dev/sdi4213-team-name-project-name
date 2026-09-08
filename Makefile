# Fuel Inventory Management System — one entry point for local dev and CI.
# `make` or `make help` lists targets. CI runs `make ci`.

PYTHON  ?= python3
VENV    ?= .venv
PY      := $(VENV)/bin/python
STAMP   := $(VENV)/.installed
HOST    ?= 0.0.0.0
PORT    ?= 8000

.DEFAULT_GOAL := help
.PHONY: help venv install test test-l2 test-all ci run smoke clean

help: ## Show this help
	@grep -E '^[a-zA-Z0-9_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

$(VENV)/bin/activate:
	$(PYTHON) -m venv $(VENV)

$(STAMP): $(VENV)/bin/activate requirements.txt
	@$(PY) -m pip --version >/dev/null 2>&1 || $(PY) -m ensurepip --upgrade --default-pip
	$(PY) -m pip install --quiet -r requirements.txt
	@touch $(STAMP)

venv: $(VENV)/bin/activate ## Create the virtual environment
install: $(STAMP) ## Install/refresh dependencies into the venv

test: install ## L0: fast in-process tests (default pytest run)
	$(PY) -m pytest

test-l2: install ## L2: over HTTP against a uvicorn the fixture starts (or BASE_URL)
	$(PY) -m pytest -m l2

test-all: install ## Every tier
	$(PY) -m pytest -m "l0 or l1 or l2"

ci: test test-l2 ## What GitHub Actions runs

run: install ## Serve on $(HOST):$(PORT) with auto-reload
	$(PY) -m uvicorn src.main:app --host $(HOST) --port $(PORT) --reload

smoke: install ## Start on 0.0.0.0, curl the endpoints, stop
	scripts/smoke.sh $(PORT)

clean: ## Remove venv and caches
	rm -rf $(VENV) .pytest_cache
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
