import json, subprocess, sys

target = sys.argv[1].lower()
data = json.loads(subprocess.check_output(["pipdeptree", "--json"], text=True))
entry = next((p for p in data if p["package"]["key"].lower() == target), None)
if not entry:
    print(f"{target} not found")
    raise SystemExit(1)

stack = [(entry, 0)]
while stack:
    item, indent = stack.pop()
    version = item["package"]["installed_version"] or "unknown"
    print("  " * indent, f"{item['package']['key']}=={version}", sep="")
    stack.extend((dep, indent + 1) for dep in item.get("dependencies", []))
