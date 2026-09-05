#!/usr/bin/env python3
from pathlib import Path
import yaml
from common import ROOT, fail

errors = []

def check(cond, msg):
    if not cond:
        errors.append(msg)

canonical = ROOT / "assistant/instructions.md"
chat = ROOT / "dist/chat/assistant/instructions.md"
custom = ROOT / "dist/custom-gpt/INSTRUCTIONS.md"
contract = ROOT / "distribution-contract.yaml"

for p in [canonical, chat, custom, contract]:
    check(p.exists(), f"Missing required file: {p.relative_to(ROOT)}")

if not errors:
    c = canonical.read_text(encoding="utf-8")
    ch = chat.read_text(encoding="utf-8")
    cu = custom.read_text(encoding="utf-8")

    required_semantics = [
        "Riksdagen","Region Norrbotten","Luleå kommun",
        "OFFICIAL_POLICY","PROPOSAL","VOTE","DECISION","STATEMENT","OUTCOME",
        "VERIFIED","VERIFIED_WITH_LIMITATIONS","DISCOVERY_ONLY","REJECTED",
        "I HUVUDSAK OFÖRÄNDRAD","VISS FÖRSKJUTNING","TYDLIG POSITIONSFÖRÄNDRING",
        "MOTSTRIDIG EVIDENS","OTILLRÄCKLIGT UNDERLAG",
        "MYCKET NÄRA","NÄRA","DELVIS NÄRA","TYDLIG SKILLNAD",
        "HIGH","MEDIUM","LOW","INSUFFICIENT"
    ]
    for token in required_semantics:
        check(token in ch, f"Chat distribution missing semantic token: {token}")
        check(token in cu, f"Custom GPT distribution missing semantic token: {token}")

    for token in ["samma metod", "Frånvaro av evidens"]:
        check(token.lower() in ch.lower(), f"Chat distribution missing behavior marker: {token}")
        check(token.lower() in cu.lower(), f"Custom GPT distribution missing behavior marker: {token}")

    check(len(cu) <= 8000, f"Custom GPT instructions exceed 8000 chars: {len(cu)}")
    knowledge_files = [p for p in (ROOT/"dist/custom-gpt/knowledge").glob("*") if p.is_file()]
    check(len(knowledge_files) <= 20, f"Custom GPT Knowledge exceeds 20 files: {len(knowledge_files)}")

    check(c == ch, "Chat instructions are not synchronized with canonical assistant/instructions.md")

eval_suites = list((ROOT/"tests/evals/suites").glob("*.yaml"))
check(len(eval_suites) >= 10, "Expected eval suites are missing")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print("-", e)
    raise SystemExit(1)

print("VALIDATION OK")
print(f"Eval suites: {len(eval_suites)}")
