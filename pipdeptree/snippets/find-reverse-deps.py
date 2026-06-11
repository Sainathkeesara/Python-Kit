import json
import subprocess


# took me a bit to figure out how to ask pipdeptree for reverse deps
# --reverse flips the tree so dependents appear before their dependencies
data = json.loads(subprocess.check_output(["pipdeptree", "--json", "--reverse"]))
target = "requests"  # change me

reverse = {}
for entry in data:
    dep = entry["package"]["key"]
    for child in entry.get("dependencies", []):
        pkg_key = child["package"]["key"]
        reverse.setdefault(pkg_key, []).append(dep)

print(f"Packages that depend on {target}:")
for d in reverse.get(target, []):
    print(f"  - {d}")
