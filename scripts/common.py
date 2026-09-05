#!/usr/bin/env python3
from pathlib import Path
import yaml, zipfile, shutil

ROOT = Path(__file__).resolve().parents[1]

CHAT_SOURCE_FILES = [
    "README.md",
    "PROJECT.md",
    "assistant/instructions.md",
    "assistant/policies/canonical-behavior.md",
    "assistant/policies/election-level.md",
    "assistant/policies/responsibility-level.md",
    "assistant/policies/evidence-classification.md",
    "assistant/policies/symmetric-comparison.md",
    "assistant/policies/political-neutrality.md",
    "assistant/policies/source-policy.md",
    "assistant/policies/source-riksdagen.md",
    "assistant/policies/source-region-norrbotten.md",
    "assistant/policies/source-lulea-kommun.md",
    "assistant/policies/web-research-flow.md",
    "assistant/policies/source-verification.md",
    "assistant/policies/short-answer.md",
    "assistant/policies/party-comparison-response.md",
    "assistant/policies/deep-evidence-analysis.md",
    "assistant/policies/position-change-response.md",
    "assistant/policies/user-priority-analysis.md",
    "assistant/policies/candidate-model.md",
    "assistant/policies/candidate-activity-metrics.md",
    "assistant/policies/candidate-comparison-response.md",
    "knowledge/README.md",
    "knowledge/swedish-responsibility-model.md",
    "knowledge/evidence-model.md",
    "knowledge/riksdagen.md",
    "knowledge/region-norrbotten.md",
    "knowledge/lulea-kommun.md",
    "knowledge/neutral-comparison-method.md",
    "docs/web-research-flow.md",
    "docs/source-verification.md",
    "docs/response-design-short.md",
    "docs/response-design-party-comparison.md",
    "docs/response-design-deep-evidence-analysis.md",
    "docs/response-design-position-change.md",
    "docs/response-design-user-priorities.md",
    "docs/candidate-model.md",
    "docs/candidate-activity-metrics.md",
    "docs/response-design-candidate-comparison.md",
    "distribution-contract.yaml",
]

CUSTOM_KNOWLEDGE_FILES = [
    "knowledge/swedish-responsibility-model.md",
    "knowledge/evidence-model.md",
    "knowledge/riksdagen.md",
    "knowledge/region-norrbotten.md",
    "knowledge/lulea-kommun.md",
    "knowledge/neutral-comparison-method.md",
]

def write_zip(base: Path, zip_path: Path, top_dir: str):
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(base.rglob("*")):
            if p.is_file():
                zf.write(p, Path(top_dir) / p.relative_to(base))

def write_inventory(base: Path):
    lines = ["# Filinventering", ""]
    for p in sorted(base.rglob("*")):
        if p.is_file() and p.name != "FILE-INVENTORY.md":
            lines.append(f"- `{p.relative_to(base)}`")
    (base / "FILE-INVENTORY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

def fail(msg: str):
    raise SystemExit(msg)
