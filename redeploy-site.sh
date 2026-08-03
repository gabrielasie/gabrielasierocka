#!/usr/bin/env bash
set -euo pipefail

# 1. Go to the project folder on the VPS
cd /root/gabrielasierocka

# 2. Force the local repo to match origin/main exactly
git fetch
git reset origin/main --hard

# 3. Stop and remove the old containers, then rebuild and start fresh
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build

echo "Redeploy complete. Container status:"
docker compose -f docker-compose.prod.yml ps
