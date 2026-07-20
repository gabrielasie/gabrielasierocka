#!/usr/bin/env bash
set -euo pipefail

# 1. Go to the project folder
cd /root/gabrielasierocka

# 2. Force the local repo to match origin/main exactly
git fetch
git reset origin/main --hard

# 3. Enter the virtual environment and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# 4. Restart the service to pick up the new code
sudo systemctl restart myportfolio

echo "Redeploy complete. Service status:"
systemctl is-active myportfolio
