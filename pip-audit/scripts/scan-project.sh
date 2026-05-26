#!/bin/bash
# Scan my project for vulnerabilities with pip-audit

pip install pip-audit
echo "Scanning dependencies..."
pip-audit --requirement requirements.txt --local
