#!/usr/bin/env python3
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"

steps = [
    [sys.executable, str(SCRIPTS/"build_chat.py")],
    [sys.executable, str(SCRIPTS/"build_custom_gpt.py")],
    [sys.executable, str(SCRIPTS/"validate.py")],
]
for cmd in steps:
    print("+", " ".join(cmd))
    subprocess.run(cmd, check=True, cwd=SCRIPTS)
print("BUILD OK")
