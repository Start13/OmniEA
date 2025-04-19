import os
import subprocess

REPO_DIR = os.path.dirname(os.path.abspath(__file__))

def run(cmd):
    result = subprocess.run(cmd, cwd=REPO_DIR)
    return result.returncode == 0

def has_changes():
    result = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_DIR, capture_output=True, text=True)
    return bool(result.stdout.strip())

# Inizializza repo se serve
run(["git", "init"])
run(["git", "add", "."])

# Solo se ci sono modifiche
if has_changes():
    run(["git", "commit", "-m", "🟢 Auto update log"])
else:
    print("🔄 Nessuna modifica da committare")

# Resto dei comandi
run(["git", "branch", "-M", "main"])
run(["git", "remote", "remove", "origin"])  # rimuove se già presente
run(["git", "remote", "add", "origin", "https://github.com/Start13/OmniEA.git"])
run(["git", "push", "-u", "origin", "main", "--force"])

