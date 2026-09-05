#!/usr/bin/env python3
from pathlib import Path
import shutil, zipfile, yaml, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
VERSION = "0.0.0-test"

# Build fresh distributions first.
subprocess.run([sys.executable, str(ROOT/"scripts/build_all.py")], check=True, cwd=ROOT/"scripts")

# Stamp test version and create versioned ZIPs exactly as release workflow does.
chat_meta = DIST/"chat/chat-distribution.yaml"
custom_meta = DIST/"custom-gpt/custom-gpt.yaml"

for path in [chat_meta, custom_meta]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["version"] = VERSION
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")

artifacts = [
    (DIST/"chat", DIST/f"valguiden-chat-{VERSION}.zip", "valguiden-chat"),
    (DIST/"custom-gpt", DIST/f"valguiden-custom-gpt-{VERSION}.zip", "valguiden-custom-gpt"),
]
for base, out, top in artifacts:
    if out.exists():
        out.unlink()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(base.rglob("*")):
            if p.is_file():
                zf.write(p, Path(top)/p.relative_to(base))

subprocess.run([
    sys.executable,
    str(ROOT/"scripts/validate_release.py"),
    "--tag", f"v{VERSION}",
    "--dir", str(DIST)
], check=True)

print("RELEASE SELF-TEST OK")
