#!/usr/bin/env python3
from pathlib import Path
import shutil, yaml
from common import ROOT, CUSTOM_KNOWLEDGE_FILES, write_zip, write_inventory, fail

dist = ROOT / "dist/custom-gpt"
if not dist.exists():
    fail("dist/custom-gpt is missing. I2 must have created the Custom GPT source distribution.")

instructions = dist / "INSTRUCTIONS.md"
if not instructions.exists():
    fail("Custom GPT INSTRUCTIONS.md is missing.")

# Rebuild knowledge from source-of-truth files while preserving generated runtime-reference.
knowledge = dist / "knowledge"
runtime_ref = knowledge / "runtime-reference.md"
runtime_text = runtime_ref.read_text(encoding="utf-8") if runtime_ref.exists() else None
if knowledge.exists():
    shutil.rmtree(knowledge)
knowledge.mkdir(parents=True)

for rel in CUSTOM_KNOWLEDGE_FILES:
    src = ROOT / rel
    if not src.exists():
        fail(f"Missing Knowledge source: {rel}")
    shutil.copy2(src, knowledge / src.name)

if runtime_text:
    (knowledge/"runtime-reference.md").write_text(runtime_text, encoding="utf-8")

contract = ROOT / "distribution-contract.yaml"
if contract.exists():
    shutil.copy2(contract, dist/"distribution-contract.yaml")

write_inventory(dist)
out = ROOT / "dist/valguiden-custom-gpt-distribution.zip"
write_zip(dist, out, "valguiden-custom-gpt")
print(out)
