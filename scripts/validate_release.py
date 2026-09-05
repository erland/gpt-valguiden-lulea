#!/usr/bin/env python3
from pathlib import Path
import argparse, re, zipfile, yaml, sys

ROOT = Path(__file__).resolve().parents[1]

VERSION_RE = re.compile(r"^(?:v)?(?P<version>\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?)$")

def fail(msg):
    print("RELEASE VALIDATION FAILED")
    print("-", msg)
    raise SystemExit(1)

def read_yaml_from_zip(zip_path: Path, suffix: str):
    with zipfile.ZipFile(zip_path) as zf:
        matches = [n for n in zf.namelist() if n.endswith(suffix)]
        if len(matches) != 1:
            fail(f"{zip_path.name}: expected exactly one {suffix}, found {len(matches)}")
        with zf.open(matches[0]) as fh:
            return yaml.safe_load(fh.read().decode("utf-8"))

def ensure_zip_has(zip_path: Path, required_suffixes):
    with zipfile.ZipFile(zip_path) as zf:
        names = zf.namelist()
    for suffix in required_suffixes:
        if not any(n.endswith(suffix) for n in names):
            fail(f"{zip_path.name}: missing required file {suffix}")

parser = argparse.ArgumentParser()
parser.add_argument("--tag", required=True, help="Release tag, e.g. v1.0.0")
parser.add_argument("--dir", default=str(ROOT/"dist"), help="Directory containing release assets")
args = parser.parse_args()

m = VERSION_RE.match(args.tag)
if not m:
    fail(f"Invalid release tag format: {args.tag}")
version = m.group("version")

dist = Path(args.dir)
chat_zip = dist / f"valguiden-chat-{version}.zip"
custom_zip = dist / f"valguiden-custom-gpt-{version}.zip"

for p in [chat_zip, custom_zip]:
    if not p.exists():
        fail(f"Missing release asset: {p}")

ensure_zip_has(chat_zip, [
    "assistant/instructions.md",
    "chat-distribution.yaml",
    "distribution-contract.yaml",
])
ensure_zip_has(custom_zip, [
    "INSTRUCTIONS.md",
    "custom-gpt.yaml",
    "distribution-contract.yaml",
])

chat_meta = read_yaml_from_zip(chat_zip, "chat-distribution.yaml")
custom_meta = read_yaml_from_zip(custom_zip, "custom-gpt.yaml")

if str(chat_meta.get("version")) != version:
    fail(f"Chat metadata version mismatch: {chat_meta.get('version')} != {version}")
if str(custom_meta.get("version")) != version:
    fail(f"Custom GPT metadata version mismatch: {custom_meta.get('version')} != {version}")

with zipfile.ZipFile(custom_zip) as zf:
    instruction_names = [n for n in zf.namelist() if n.endswith("INSTRUCTIONS.md")]
    if len(instruction_names) != 1:
        fail("Custom GPT ZIP must contain exactly one INSTRUCTIONS.md")
    instruction = zf.read(instruction_names[0]).decode("utf-8")
    if len(instruction) > 8000:
        fail(f"Custom GPT instructions exceed 8000 chars: {len(instruction)}")
    knowledge_files = [
        n for n in zf.namelist()
        if "/knowledge/" in n and not n.endswith("/")
    ]
    if len(knowledge_files) > 20:
        fail(f"Custom GPT Knowledge exceeds 20 files: {len(knowledge_files)}")

with zipfile.ZipFile(chat_zip) as zf:
    names = zf.namelist()
    forbidden = [n for n in names if any(x in n for x in ["/tests/", "/.github/", "/scripts/"])]
    if forbidden:
        fail(f"Chat release ZIP contains development-only files: {forbidden[:5]}")

print("RELEASE VALIDATION OK")
print("Tag:", args.tag)
print("Version:", version)
print("Chat asset:", chat_zip.name)
print("Custom GPT asset:", custom_zip.name)
