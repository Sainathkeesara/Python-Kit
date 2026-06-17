# Check a package in pipdeptree JSON and print its dep chain
import json, subprocess, sys
target = sys.argv[1].lower()
data = json.loads(subprocess.check_output(["pipdeptree", "--json"], text=True))
entry = next((p for p in data if p["package"]["key"].lower() == target), None)
if not entry:
    print(f"{target}: not found"); sys.exit(1)
# Walk dep chain — pipdeptree resolves cycles already
stack = [(entry, 0)]
while stack:
    item, depth = stack.pop()
    v = item["package"].get("installed_version", "?")
    print(f"{'  ' * depth}{item['package']['key']}=={v}")
    stack.extend((d, depth + 1) for d in item.get("dependencies", []))
