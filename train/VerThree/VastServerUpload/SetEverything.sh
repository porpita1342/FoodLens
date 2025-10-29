#!/usr/bin/env bash
set -euo pipefail

# Upgrade packaging tools first to reduce build quirks
python -m pip install --upgrade pip setuptools wheel

# Install Python deps (pure wheels usually okay)
python -m pip install --no-cache-dir -r requirements.txt

# Install system libs needed at runtime
export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y --no-install-recommends \
  libgl1 \
  libglib2.0-0
rm -rf /var/lib/apt/lists/*

# Install your local repo last so it resolves against installed deps
python -m pip install VastServerUpload/ultralytics

# Optional: quick import sanity checks (fail fast if something’s missing)
python - <<'PY'
import importlib
for mod in ["ultralytics"]:
    importlib.import_module(mod)
print("Imports OK")
PY
