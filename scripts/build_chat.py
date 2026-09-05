#!/usr/bin/env python3
from pathlib import Path
import shutil, yaml
from common import ROOT, CHAT_SOURCE_FILES, write_zip, write_inventory, fail

dist = ROOT / "dist/chat"
if dist.exists():
    shutil.rmtree(dist)
dist.mkdir(parents=True)

missing = []
for rel in CHAT_SOURCE_FILES:
    src = ROOT / rel
    if not src.exists():
        missing.append(rel)
        continue
    dst = dist / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)

if missing:
    fail("Missing Chat source files: " + ", ".join(missing))

manifest = {
    "name": "Valguiden",
    "distribution": "chat",
    "entrypoint": "assistant/instructions.md",
    "supported_levels": ["Riksdagen", "Region Norrbotten", "Luleå kommun"],
    "requires_web": True,
    "image_generation": False,
    "custom_actions": False,
}
(dist/"chat-distribution.yaml").write_text(
    yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8"
)

(dist/"CHAT-README.md").write_text("""# Valguiden – Chat distribution

Ladda upp ZIP-filen i en ChatGPT-konversation och använd den som GPT/instruktions- och kunskapsunderlag.

Aktuell politisk fakta ska verifieras via webben. Distributionen innehåller stabil metodik och runtime-regler.
""", encoding="utf-8")

write_inventory(dist)
out = ROOT / "dist/valguiden-chat-distribution.zip"
write_zip(dist, out, "valguiden-chat")
print(out)
