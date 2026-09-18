# Carta hook warning — investigation

Date: 2026-09-18. Reviewer: CATO. Repository snapshot: `1a3fe9c53`; plugin/config evidence is outside Git and is a live-machine snapshot.

## Assignment and disposition

Will asked why TERRY now displays a non-blocking Carta UserPromptSubmit error despite having no Carta account/subscription. Investigation complete; no plugin repair, disablement, account change or external message performed. Recommended next action: disable the unused synced plugin. Upstream enablement provenance remains unverified.

## Findings

**Medium — enabled synced plugin has an unexecutable dispatcher.** `claude plugin list --json` reports `carta-investors@synced`, version `6.26.0`, scope `synced`, enabled `true`. Its installed root is `~/.claude/plugins/synced/<account-bucket>/carta-investors~g2/`. `hooks/hooks.json` registers an unconditional UserPromptSubmit command directly invoking `hooks/dispatch.sh capture-slash-skill`. The dispatcher is owned by the current user but mode `0644`; `os.access(..., os.X_OK)` is false. Parent directories are traversable. This explains the pasted `/bin/sh: ... dispatch.sh: Per…` as a permission-denied failure before the dispatcher starts. The pasted message is truncated; no new live hook execution was used to reproduce the full message. Claude labels the failure non-blocking, so that failed hook does not prevent TERRY processing the prompt. It does not establish that all other TERRY functionality is healthy.

**Explained — the plugin arrived through Claude account sync, not an ordinary local marketplace installation.** The installed Claude Code version is `2.1.276`. Anthropic documents terminal plugin sync beginning with `2.1.273`: account-enabled and organization-enabled plugins download under `plugins/synced` and need no ordinary install record. Local `installed_plugins.json` has no Carta entry; the sync manifest and live plugin listing do. The sync manifest describes Carta as `knowledge-work-plugins`, installation preference `available`, generation 2, revision `0145`, updated `2026-09-17T14:57:25.967584Z`. This sync revision is distinct from package version `6.26.0`. Dispatcher filesystem ctime is September 17 at 13:12 local; ctime is a metadata-change time, not proof of the original install time. The newly supported sync mechanism plus these timestamps is a strong explanation for why the warning appeared recently. This review cannot establish who enabled Carta upstream, whether an organization default supplied it, or exactly which update lost executable permissions.

**No account/subscription inference is justified.** Local package README installation steps separately add the Carta MCP endpoint and require `/mcp` OAuth authentication. The plugin root contains no `.mcp.json` and its manifest declares no MCP server. No Carta MCP configuration was found in the inspected `~/.claude.json` configuration, and the plugin listing supplies no Carta `mcpServers`. These observations do not audit cloud connector authentication, billing, or every possible configuration source. The warning itself indicates neither a Carta subscription nor a Carta login attempt.

**Privacy scope — do not equate this failure with a data transfer or certify zero historical transfers.** The packaged `hooks/src/handlers/capture_skills.go` handler recognizes slash commands and records matching plugin skill use in local session state. An ordinary greeting such as Will's TERRY boot prompt returns without recording a skill. In this failing invocation the dispatcher never starts. Other packaged hooks include session context injection, model capture and instrumentation: `inject_instrumentation.go` attaches session/model/skill and token-usage metadata to matching Carta MCP tool requests. README explicitly discloses telemetry. Therefore this is not grounds to label the whole plugin telemetry-free. No network capture, historical activity audit, cloud account inspection, malware certification or binary/source reproducibility verification was performed.

## Proposed action

For a plugin Will does not use, disable it through the supported user-level control:

```sh
claude plugin disable carta-investors@synced
```

Then restart the affected Claude Code session and confirm the next prompt has no Carta hook warning. Verify with `claude plugin list --json` that Carta is disabled. These are proposed acceptance checks, not performed results. Anthropic documents that this choice is saved under user-level `enabledPlugins`. Turning the plugin off in the Claude account is the option for removing it across synced environments. Do not treat `chmod +x` as the preferred fix here: that would activate code from an unwanted plugin. No need to disable all plugins to address this finding.

## Evidence and checks

Read-only checks: installed CLI version; plugin list JSON; file mode/ownership and parent traversal; synced manifest/metadata and ordinary install registry; relevant local configuration keys; package manifest, README, hook declarations, dispatcher and selected Go handlers. Checks confirm enabled state, sync provenance and missing execute permission. Source review is static; the shipped native binaries were not executed. No tokens, credentials or account-bucket identifiers are reproduced in this report.

Primary documentation: [Anthropic plugin reference — synced plugins](https://code.claude.com/docs/en/plugins-reference#plugins-synced-from-claudeai); [Carta plugin repository](https://github.com/carta/plugins). Local package contents are the version-specific evidence; upstream HEAD was not assumed identical.

Concurrent BROCK, SAM, BRENT and PROME work was preserved. Only this report and CATO continuity were authored. Closeout checks and actual commit/push receipt are delivered in-session; no independent second review was commissioned. Next session: orient and await Will; configuration changes have not been assigned.

Closeout checks: weekday claim check passed on the three existing PROME queue/gate files; orphan advisory identified concurrent owner files, left untouched. The fleet read-cap tool returned CANNOT-EVALUATE/2 because CATO has no CLAUDE.md; this is not a pass. Direct byte counts of CATO startup entry files were checked against the 32,550-byte ceiling.
