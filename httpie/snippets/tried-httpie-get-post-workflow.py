import subprocess
import json
import sys

url = sys.argv[1] if len(sys.argv) > 1 else "https://jsonplaceholder.typicode.com/posts/1"

result = subprocess.run(
    ["http", "--json", "GET", url],
    capture_output=True,
    text=True,
)

if result.returncode != 0:
    print("httpie failed:", result.stderr, file=sys.stderr)
    sys.exit(1)

data = json.loads(result.stdout)
print(json.dumps(data, indent=2))
