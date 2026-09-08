#!/usr/bin/env bash
# Start the API on 0.0.0.0, hit it over the LAN address, stop it.
# Usage: scripts/smoke.sh [port]
set -euo pipefail
PORT="${1:-8000}"
cd "$(dirname "$0")/.."
PY=".venv/bin/python"; [ -x "$PY" ] || PY="python3"

"$PY" -m uvicorn src.main:app --host 0.0.0.0 --port "$PORT" >/tmp/fims-uvicorn.log 2>&1 &
PID=$!
trap 'kill $PID 2>/dev/null || true' EXIT

timeout 15 bash -c "until curl -sf http://127.0.0.1:$PORT/health >/dev/null; do :; done" \
  || { echo "server did not come up"; cat /tmp/fims-uvicorn.log; exit 1; }

LAN_IP="$(hostname -I 2>/dev/null | awk '{print $1}')"
echo "listening: $(ss -ltnp 2>/dev/null | grep ":$PORT " | awk '{print $4}')"
echo "GET /health via 127.0.0.1 -> $(curl -s http://127.0.0.1:$PORT/health)"
[ -n "$LAN_IP" ] && echo "GET /health via $LAN_IP -> $(curl -s http://$LAN_IP:$PORT/health)"
echo "POST /fuelstocks -> $(curl -s -X POST http://127.0.0.1:$PORT/fuelstocks \
  -H 'content-type: application/json' \
  -d '{"site_id":1,"fuel_type":"diesel","quantity_gallons":4000,"capacity_gallons":10000}')"
echo "GET /fuelstocks -> $(curl -s http://127.0.0.1:$PORT/fuelstocks)"
echo "GET /docs -> HTTP $(curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:$PORT/docs)"
