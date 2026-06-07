import json
import subprocess
import sys

# Parse pipdeptree JSON output and list packages with zero dependencies
data = json.loads(subprocess.check_output(["pipdeptree", "--json"]))
# TODO: handle missing pipdeptree gracefully
leaf_packages = [p for p in data if not p.get("dependencies")]
for pkg in leaf_packages:
    print(f"{pkg['package']['key']}=={pkg['package']['installed_version']}")
