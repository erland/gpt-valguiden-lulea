# L7 – pilotfixar: validering

- [x] canonical_rule_added
- [x] custom_rule_added
- [x] custom_under_8000
- [x] regression_H3_016_present
- [x] regression_is_critical
- [x] build_passed
- [x] pilot_rerun_all_pass
- [x] zero_pilot_critical_issues
- [x] release_validation_rc2

- Custom GPT instruktion: **6729 tecken**
- Pilot rerun: **12/12 PASS**

## Release validation

```text
RELEASE VALIDATION OK
Tag: v1.0.0-rc.2
Version: 1.0.0-rc.2
Chat asset: valguiden-chat-1.0.0-rc.2.zip
Custom GPT asset: valguiden-custom-gpt-1.0.0-rc.2.zip
Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/generated/interface/models.py", line 32317, in hydrate_crdt_from_proto
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/rpc/remote.py", line 749, in __call__
  File "/tmp/tmp.L2TH2Y5coc/artifact_tool_v2-2.8.22/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
```

Resultat: OK
