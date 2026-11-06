# WQ-638 A — installation blocked after its one independent read

Will approved the build and installation only after one independent read without blockers. The read is complete: **BLOCK**. Live app, acceptance and PROME hooks are unchanged. Do not install this candidate or treat the earlier waiver as permission for this build.

- `candidate.patch`: frozen implementation against `219752ac53a3c094fe37d541e94e6106e3163d06`; apply only to an isolated checkout at that base.
- `candidate-sha256.txt`: exact reviewed runtime/owner-contract hashes.
- `AUTHOR_CHECKS.md`: author testing and disclosed test errors.
- `INDEPENDENT_REVIEW.md`: unedited Opus 5.5 report, all findings, evidence limits and completion conditions.
- `review-repro/`: reviewer-authored reproduction scripts. They use fixed disposable `/tmp/wq638-rev` and `/tmp/cato-wq638` paths; recreate the isolated candidate and copy scripts into `/tmp/wq638-rev/scripts` before running. They create/reset their own fixture repositories. Never redirect them at production.
- `browser-check.py`: author Chrome fixture; fixed candidate path, temporary Windows profile, no live answer.
- `reader-brief.txt`, `native-probe.py`, `native-probe-settings.json`: exact independent brief and isolated native probe configuration. The wrapper's exit 2 was NOT delivery to the model. Do not install these probe settings.

Recommended return: fix B1 with a fresh published-state/current-answer check at integration preparation while keeping historical replay valid; correct the per-answer intake test and live connection-status display; prevent noninteractive hooks from blocking startup; demonstrate notification in an interactive runtime both active and idle. Ask Will for one bounded follow-up read and conditional installation. No second review or repairs were started after BLOCK. Notification residue 3–8 is retained in the review for that bounded decision, not silently closed or automatically expanded into new work.

One native reader only: Claude Code 2.1.319, actual model `claude-opus-5-5`, session `63863863-8638-4638-8638-638638638638`; completed normally with 33 turns. No production writes by reader, no contact with implementer until its completed report. CATO is implementation author; its testing is not independent verification.
