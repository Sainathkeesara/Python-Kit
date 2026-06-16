import json, subprocess

result = subprocess.run(
    ["pipdeptree", "--json"], capture_output=True, text=True
)
pkgs = json.loads(result.stdout)

count = 0
for p in pkgs:
    if not p.get("dependencies"):
        count += 1
        print(f"{p['package']['key']} ({p['package']['installed_version']})")
print(f"\n{count} leaf packages found.")
