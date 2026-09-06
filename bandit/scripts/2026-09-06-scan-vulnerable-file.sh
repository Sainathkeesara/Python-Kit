# last_verified: 2026-09-06 · bandit 1.9.4

# Create a deliberately vulnerable file and scan it with bandit

cat > /tmp/vulnerable.py << 'EOF'
import os
import subprocess

password = "hunter2"

def run_command(user_input):
    os.system(f"echo {user_input}")
    subprocess.call("ls " + user_input, shell=True)

def unsafe_eval(data):
    eval(data)
EOF

bandit /tmp/vulnerable.py
rm /tmp/vulnerable.py
