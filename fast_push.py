import os
import subprocess

# Percorso repo Git
REPO_DIR = os.path.dirname(os.path.abspath(__file__))

# Comandi Git
commands = [
    ["git", "init"],
    ["git", "add", "."],
    ["git", "commit", "-m", "🟢 Auto update log"],
    ["git", "branch", "-M", "main"],
    ["git", "remote", "add", "origin", "https://github.com/Start13/OmniEA.git"],
    ["git", "push", "-u", "origin", "main"]
]

# Esegui comandi uno per uno
for cmd in commands:
    result = subprocess.run(cmd, cwd=REPO_DIR)
    if result.returncode != 0:
        print(f"❌ Errore con: {' '.join(cmd)}")
        break
