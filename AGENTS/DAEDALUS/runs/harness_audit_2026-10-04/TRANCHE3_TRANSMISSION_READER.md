# Harness audit tranche 3 — transmission reader

Date: 2026-10-04. Reader: delegated DAEDALUS interpretation reader, not a reciprocal owner session. Source pin: `e63816cb5f8d5297340455a6839f8bec65028dbe`. Scope: FULL text of six charters, with bounded supporting reads. This is another portion of the existing July-7-method harness audit, not a completed fleet audit, domain review, maturity refresh, implementation package, or authorization to change instructions.

## Coverage and method

Read all six charters from the pin in consecutive bounded chunks. Recovered the truncated VULCAN 246–255 output in a separate read; no omitted primary text remains. Read-only Git object exports went to `/tmp/daedalus-harness-tranche3-20261004/`. No owner script, boot, network pull, market research, test, hook, renderer, or Git mutation was run. Only this raw report is written in the repository. Source lines below always refer to the pinned version, not the live working tree.

Applied the three legs of `sweeps/HARNESS_AUDIT_SWEEP.md` and `HARNESS_AUDIT_2026-07-07.md`, read for the existing audit: distinguish action gates from rationale; inspect actual existing invocation/return paths before claiming mechanical coverage; identify the canonical owner rather than create a second rule. July repairs and later corrections are refuters, not automatically reopened defects. Mechanization checks here establish static wiring only. Whether a live session ran or consumed an instrument, the current external state, harness/model behavior, and effective runtime coverage remain UNKNOWN.

| FULL primary read | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| `AGENTS/VULCAN/CLAUDE.md` | 1–278 | 81,862 | `5f66a766074bb14b7aac2a10c812cdd7ed576803dc6dac7cb88adaaa3419cc0d` |
| `AGENTS/ZHAO/CLAUDE.md` | 1–267 | 32,528 | `9e0f464520032ab34e0a937a702ada0531392f527e11ee15fcd0fcded35e54ec` |
| `AGENTS/HAWK/CLAUDE.md` | 1–225 | 28,271 | `f0ad39e1b5f5a933a40f0ba209ec33f0bb7abd3c65928258fc027650269fac9b` |
| `AGENTS/FALCON/CLAUDE.md` | 1–340 | 50,009 | `a640316403d8869b47d9ebe21628c419a923189e84de11ace772875fc06e36ce` |
| `AGENTS/BRENT/CLAUDE.md` | 1–224 | 31,387 | `d14868832ca65ae620206f587cbea7b1ce84dec23b415e85eff49604dd3067ff` |
| `AGENTS/WATT/CLAUDE.md` | 1–202 | 18,364 | `6e1e14cec1addfd206287975f75e96974604bd5ce35e2eb208dbe0f4174b1953` |

These byte measurements are evidence identity/context cost, **not charter breach verdicts**. READ_CAP rule 20 (`BLUEPRINTS/READ_CAP.md:32,40`) excludes injected charters; its sub-agent clarification also excludes the charter itself. The actual resolver at `scripts/read_cap_check.py:162–171` excludes the desk's own charter. Spawn-card claims about what a particular harness injects were not experimentally verified here. They do not establish a runtime truncation finding or authorize a new context cap.

## Ranked retained findings

Ranking is by consequence of following the conflicting instruction, not observed harm. All proposed dispositions below are **UNVERIFIED owner-review directions**, not edits or commissioned tasks.

### T3-1 — WATT's STATUS allowance contradicts root canon and already-repaired invoked code

**Evidence:** `AGENTS/WATT/CLAUDE.md:182` still authorizes STATUS below 64,000 B, a 48,000 B rotation trigger and 44,800 B target, calling this checked at boot. Root `CLAUDE.md:122` binds whole boot reads at 32,550 B above owner-set numbers. `AGENTS/WATT/boot.py:154–177` expressly retires 64,000 B, defines `READ_CAP_BUDGET = 32_550`, and includes STATUS/SCRATCH/PREDICTIONS in scope. Its function at 181–215 calculates against that budget, and actual `main()` calls it at 248–249. A reader can follow the charter's old numbers while the existing instrument says otherwise.

**Disposition:** REWRITE the local STATUS allowance to reference the governing budget and the existing check; preserve rotation without deletion and protection of live obligations. No instrument replacement is supported.

**Refuter / limit:** The code already has the correct constant and an actual invocation. This refutes an allegation that the old 64 KB enforcement still runs, that the July wiring defect remains, or that current STATUS is over budget. Current STATUS was not measured. The finding is the unretired charter mirror, not an owner data-size breach.

### T3-2 — VULCAN's fast boot card still excludes S5 from its liveness gate

**Evidence:** `AGENTS/VULCAN/CLAUDE.md:20` mandates a live read for S1–S4. Full boot step 8 at 53 mandates S1–S5 and expressly says the old four-channel wording was corrected after S5's promotion. Domain scope 96 and channel canon 110–122 make all five core; 151 makes the denominator /25. This is a producing instruction that survived correction of a parallel instruction.

**Disposition:** REWRITE the compact card's channel set to defer to the canonical core-channel list. KEEP the shared-root independence guard at 17 and 122; S5's financing leg is partially independent, not a license to count capex three times.

**Refuter / limit:** Full boot already includes S5; `boot.py:419–429` invokes catalyst/schema/EDGAR legs, including the S3/S5 instrument. This is not evidence of an absent S5 tool or actual omitted review. It does not revive the repaired full-boot instruction or justify new automation.

### T3-3 — ZHAO's categorical brief-pin ban conflicts with the named brief owner

**Evidence:** `AGENTS/ZHAO/CLAUDE.md:37` tells the NEXUS_BRIEF writer not to pin a STATUS commit hash and to use behavior language, “never a SHA.” Closeout 55 still gives the amendment-10 timestamp check. In the pinned owner schema, `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md:162–165` requires the STATUS hash even on no-change closeouts and supersedes the timestamp comparison with amendment 11's equality at brief commit. The checking/fallback description at 205–217 depends on that pin. ZHAO points to NEXUS as schema owner at 55/256 while stating incompatible local semantics.

**Disposition:** Owner reconciliation through the existing handoff, retaining the useful warning about rebase-related delivery verification. Do not silently replace either authority. Distinguish content/subject verification that a push landed (`ZHAO/CLAUDE.md:244`) from the schema's pin-at-commit invariant.

**Refuter / limit:** ZHAO already mandates last-write ordering; no current brief contents or NEXUS checking implementation were audited here. Its rebase concern is real as a documented rationale, not disproved by this reading. Schema 165/175 expressly bars using amendment 11 as a new fleet-wide closeout step. Thus this is a contradictory local restatement for owner disposition, **not** authorization for broad propagation, a runtime broken-stale-check claim, or a new check.

### T3-4 — FALCON's mandatory triad conflicts with its explicitly optional retired-gate backstop

**Evidence:** `AGENTS/FALCON/CLAUDE.md:30` mandates all three PortWatch scripts; 59 says run all three together. Step 5b-4 at 76–80 names the Kharg script but then expressly says its gate is retired, the instrument failed a known-positive control, and running it is optional/not load-bearing. The fast path and specific disposition disagree about required work.

**Disposition:** REWRITE the compact mandate to carry the specific optional scope, keeping the zero-is-uninformative / positive-only safeguard. Retain gate retirement and the known-positive counterexample; do not reinstall a strand gate or a required Kharg leg.

**Actual mechanism / refuter:** Read `scripts/kharg_loadings_watch.py` fully. `main():82–94` calls the fetch and fails loudly on fetch failure/empty response; 112–129 computes nonzero flow and returns 1 for flow continuing, while zero prints UNINFORMATIVE and returns 0. `__main__` dispatches at 132–133. The script is **not** a silent-zero strand confirmation. Its legacy gate wording is subordinate to the charter's retirement. No current fetch or session invocation was attempted; static reachability does not prove live use or source accuracy.

### T3-5 — ZHAO's pre-amendment command resolves only one of three registries from the repo root

**Evidence:** `AGENTS/ZHAO/CLAUDE.md:52` gives a mechanical pre-amendment grep whose WILL_QUEUE argument is root-qualified but whose `PROME/GATES.tsv` and `PROME/DOCKET.tsv` arguments are relative. The same charter's boot 29 expressly supports own-directory launches with a subshell root wrapper; its Git-only root instruction is later at 234. From the documented own-directory starting point, the latter two grep arguments resolve below `AGENTS/ZHAO/`, unless the session independently changed directory. The command can therefore inspect WILL_QUEUE while failing to inspect the other named registries.

**Disposition:** REWRITE the command's path convention for the intended starting directory while keeping the obligation to check operator rulings before changing a prediction. This is a proposed wording correction, not execution or owner-file modification.

**Refuter / limit:** The command works from repo root, and grep would print errors for absent files; this is not a demonstrated silent failure or evidence that any prediction was changed incorrectly. No command was run against live registries and no registry contents were interpreted. The retained claim is bounded launch-context fragility of a prescribed command.

### T3-6 — FALCON retains an unsupported current HAWK invocation claim

**Evidence:** FALCON's legacy-suite FILES row at `CLAUDE.md:339` correctly says DO NOT PORT/FROZEN, then retains “Live finding routed to HAWK” and says HAWK's session opens through the old wrapper. Current HAWK `CLAUDE.md:223` names derived_freshness as the sole live local checker and explicitly freezes all other scripts. `AGENTS/HAWK/scripts/boot.py:5–16` says NOT wired into boot, do not invoke, and records retirement. The retained mirror presents a historical concern as current despite these direct refuters.

**Disposition:** REWRITE only the lifecycle claim as historical/resolved or pending owner confirmation, preserving the no-port result and stale-output evidence. This is lower priority than contradictory active commands.

**Refuter / limit:** Nothing here shows a live HAWK session ran the old wrapper. Its existence and executable body are not invocation. The repaired retirement is a counterexample, so this report does not reopen the July installed-but-unwired item or demand a live-data audit to revive it.

### T3-7 — ZHAO's local charter-cap instruction predates rule 20

**Evidence:** `AGENTS/ZHAO/CLAUDE.md:50` binds “STATUS and this file” to 32,550 B and attributes silent Read truncation to both. Current READ_CAP rule 20 (`BLUEPRINTS/READ_CAP.md:32,40`) distinguishes injected charters from Read surfaces, and `_resolve()` at `scripts/read_cap_check.py:171` excludes the charter.

**Disposition:** REWRITE the scope claim to retain STATUS's whole-read budget and separate charter context cost. No byte ceiling, rotation mandate, instrumentation change, or new monitoring work is derived from this finding.

**Refuter / limit:** ZHAO's charter is below 32,550 B at this pin anyway. There is no current over-budget claim and no verified injection experiment in this tranche. The correction concerns governing scope, not proven operational harm.

## Six per-file three-leg dispositions

| Charter | Action gates versus rationale | Existing mechanisms and actual invocation | Canonical ownership / KEEP, REWRITE, STRIKE |
|---|---|---|---|
| VULCAN | KEEP channel-first scope, shared-root accounting, due-ID retrieval, THESIS reconciliation, dated commitment write-back, and last-write brief fold (17,46,53,61–79). REWRITE T3-2. Repair narratives at 64–76 and dense FILES rows 237–264 can be moved/pointered only after preserving every current rule, cadence, retired-state caveat and obligation. | Actual `boot.py` main 384–431 calls staleness, prediction scan, three vintage functions, catalyst countdown, validator, EDGAR. Wrapper code 269–298 really invokes the countdown/validator; prediction parser 117–145 feeds the due list. Child bodies and current data mostly unread: not an exhaustive correctness pass. Advisory series legs do not fetch, as charter 236 says. | KEEP STATUS state / CHANNEL_DETAIL evidence split (249), docket ownership (65/244), NEXUS schema ownership and no-propagation rider (75–82), and neighbor domain seams (99–104). STRIKE no repaired history merely to shorten it. Stale active-looking narrative such as the “MU has not announced” tail at 263 deserves historical labeling, not a market-data regrade: the same row prominently carries the dated refutation. |
| ZHAO | KEEP triage versus bulk distinction (24–28,43), schema-before-write, after-window grading, self-consumer collision inspection (238), and operator-ruling check intent. REWRITE T3-3/5/7. | `scripts/boot.py:203–224` invokes catalyst_countdown and turns missing/nonzero/recently-fired output into alerts. Predictions 227–268 handles OPEN prefixes and limbo; main 305–340 calls all six sections and uses alert counts. Chronic VX staleness is explicitly advisory (271–302); no existence-only claim that all stale rows block. | KEEP CGB macro/plumbing boundary (5), semiconductor company-capacity exclusion (97–99), and explicit refusal to infer migration from a monthly Belgium pattern (146–175). REWRITE the unqualified Belgium identity at 144 as retired/contextual if owner accepts, but do not reopen the repaired probabilistic doctrine: the nearby box and retired-rule banner control. STRIKE no historical falsifier. Brief form belongs to NEXUS; owner-routed reconciliation only. |
| HAWK | KEEP synthesis/theater split, source disaggregation, scoped prediction reads, exact-recipient intake guard, dormant-book review and derived-input workflow. Narrative can be compacted by pointer, retaining repaired edge cases. No new high-consequence charter defect retained from this bounded read. | FULL `scripts/derived_freshness.py`: main 85–117 invokes capture/record/inspect; inspect 57–73 checks exact dependency/output hashes; record 76–82 refuses changed inputs. This certifies bytes only, explicitly not external freshness or semantic consumption. Charter 53/73 names the workflow. The old `scripts/boot.py` is explicitly retired (header 5–16), not an uncovered required boot. | KEEP owner inputs and sole-live-checker limit (223), sibling ownership and bounded-to-EOF rule (225), frozen legacy states. STRIKE no dormant/theater boundaries. The different local counts in 54 and 69 are a weak prose-count concern, not enough here to declare a vector missing without inspecting the actual book; not retained as a defect. |
| FALCON | KEEP WARRISK file clock and independent row-expiry check (48–70), no-zero-inference rule, primary/manual PMF read, explicit intake membership lookup and temporal/falsification guard. REWRITE T3-4 and T3-6. | Full Kharg source confirms invoked fetch, failure returns, nonzero refutation and explicit uninformative-zero branch. Other instruments are commands in the charter, not proven executions; their internal coverage remains unread. File-level and row-level WARRISK checks are intentionally different, not wasteful duplication. | KEEP current EXIT_PROTOCOL pointer and explicit retirement of old scenario/kill rules (233), B/C/D correction (298), no-port legacy disposition (339), ownership split and acute routing exception (267–280). STRIKE only the unsupported present-tense HAWK invocation claim after owner disposition, never the counterexample or gate retirement. |
| BRENT | KEEP manual residuals after one-command boot, no automatic prediction grading, frozen KB/VX/FLOW distinction, content re-verification or explicit partial brief, generated calendar check and trade/approval boundaries (32–45,61–71,208–224). No high-consequence new instruction conflict retained. | `scripts/boot.py:317–333` iterates BOOT_SEQUENCE and calls run_script; 266–285 invokes child processes and promotes named markers; 385–420 distinguishes failures/findings/advisory warnings and propagates rc. Existing predictions/catalysts in sequence 33–36, ledger nudge 160, and derived calendar check 186 are actual callsites. This is not a review of all child implementations. | KEEP retired routing/threshold mirrors in favor of `_NETWORK` and REGISTRY/THESIS (192,200–204), generated calendar source, and DM-v1 allowlist/local handling. STRIKE no manual judgment because a tool exists: manual event-precondition/STUCK checks and content verification remain outside wrapper proof. Repeated historical explanation is a possible owner compression direction only. |
| WATT | KEEP P1–P4 live review, prediction disposition, brief fold, FORGE boundary and content-preserving rotation. REWRITE T3-1. Trade “live mtime alert” wording at 184 also trails root Data Hygiene 120; reference current canon rather than create a new freshness instruction. | Actual `boot.py:224–249` invokes power_watch, both ledger checks and byte check; 251–278 consumes predictions and returns aggregate failure/review/quiet. Correct 32,550 B implementation refutes reopening old budget enforcement. Child power_watch and shared staleness implementations were not inspected. | KEEP own power-price role and neighbor demand/fuel boundaries, FORGE approval limitation (174), NEXUS compact-variant ownership. STRIKE the retired local numerical allowance only after owner disposition; preserve history elsewhere if required. No current data-size or market-quality verdict. |

## False positives and limits preserved

- No charter-size breach, forced charter rotation, context budget, model diagnosis or launch/injection assertion is established. Rule 20 controls; primary bytes are identity evidence.
- HAWK's old scripts and FALCON's old scenario/gate text are explicitly retired. Their presence does not make them live. FALCON's more specific Kharg demotion governs over its older “gate fires” historical explanation.
- ZHAO's Belgium repair, VULCAN's corrected Micron date / ungradeable missed cadence, FALCON's B/C/D repair and frozen port decision, BRENT's frozen ledgers/generated calendar, and WATT's corrected code are substantive refuters. Historical numbers and marked supersessions are not current domain defects by default.
- General outbox/direct-packet descriptions occur across these charters. Root `CLAUDE.md:123` governs messaging scope and signals must not bypass WALTER. This tranche did not inspect full routing contracts, exceptions or sent packets, so it does not declare an unauthorized route or change the acute FALCON/BRENT seam. Repeated local summaries merit canon references, not inferred new authority.
- Generic local Git summaries are abbreviated; root `CLAUDE.md:95–116` provides governing safeguards. They are not independent evidence of unsafe Git execution. No Git operation beyond read-only source extraction was performed.
- NEXUS's schema explicitly leaves its old 100-line ceiling unenforced (226); VULCAN 78 is immediately qualified by 80. Do not create a line-cap finding from the former sentence alone. READ_CAP's cross-agent whole-read member rule (43) is a distinct budget question; this tranche did not measure briefs or reopen that owner package.
- Human judgment obligations are not proved mechanized by a validator, fingerprint check, nonempty output, or passing rc. No automation is proposed merely because these reads expose a possible gap.

## Supporting source identity and read depth

All support bytes below were exported from the same pin. Full-file hashes do not imply full-file interpretation. Search-only lines supplement the declared ranges; everything outside those ranges remains unread for this tranche.

| Support path | Read depth | Bytes | SHA-256 |
|---|---|---:|---|
| `CLAUDE.md` | PARTIAL 80–133, governing Git/Data Hygiene/messaging | 24,199 | `1b176d7b3c619a78dbabe4128f23451fa32a074554f391804707aec7623a3c73` |
| `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md` | PARTIAL 25–57 (rules 16–20, scope/enforcement) | 25,080 | `a326afd037cc5e037cd9673a011ad7c21bc5990156f9ae645af6f66576cf90a8` |
| `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` | PARTIAL 155–180,201–228, targeted search including header form 47 | 32,141 | `8d8c279c4c56416e5fa34f77b088b6af96d7d34b8269c04c881423526e2f8955` |
| `AGENTS/WATT/boot.py` | PARTIAL 154–278 plus targeted search of wrappers/predictions | 13,499 | `f6d5aa2092d0d1d3c691053e229a9e9ac17bce673b3518e0888d34e0c77104ee` |
| `AGENTS/BRENT/scripts/boot.py` | PARTIAL 25–42,150–188,250–290,300–370,385–424 plus targeted search | 25,047 | `821188a0d0f9ec9bb3d667853dfdfd96a977035722d67e1cb6ab7b08423f0c1d` |
| `AGENTS/ZHAO/scripts/boot.py` | PARTIAL 203–340 | 13,822 | `9d30678c4ea8afcbf388be5c89df240c27cccaac921c9d5b2fcf84520ea929b1` |
| `AGENTS/VULCAN/boot.py` | PARTIAL 117–146,269–305,378–445 plus targeted search | 21,833 | `7151b4228c08d68a09ea1102abef766eda23a369174dfc378c732a0e16662bf7` |
| `AGENTS/HAWK/scripts/derived_freshness.py` | FULL 1–117 | 5,341 | `6fbae2e7915272a339c5c12fcf71d8da34cb8b44dafac28b5692029d72a92ea5` |
| `AGENTS/HAWK/scripts/boot.py` | PARTIAL 1–22, retirement counterexample only | 7,673 | `ed8f259825336871dc8a3a188b7207938f6ed0547a517549fffcc633b0cd62cd` |
| `AGENTS/FALCON/scripts/kharg_loadings_watch.py` | FULL 1–133 | 5,996 | `79a2577a6e3b8cdedfe8335054c94a3d4a1ec8b21874618292623cca4c0e1c51` |
| `scripts/read_cap_check.py` | PARTIAL 162–173 plus targeted search of explicit charter exclusion/reporting | 121,055 | `ff77e3136e36ce474bc5338092afc2b422a32db8bf4d3e14a51ac6720d4e4c03` |

Initially attempted three guessed support paths that do not exist at the pin: `AGENTS/DAEDALUS/READ_CAP.md`, `AGENTS/WATT/scripts/boot.py`, and `AGENTS/FALCON/tools/kharg_watch.py`. Corrected to the explicit canonical paths in the table. These failed navigation guesses are **not missing-file findings**.

Not read: domain STATUS/THESIS/brief/ledger bodies; current prediction/market state; operator registries' substantive rows; referenced historical packets, tests, acceptance reports and owner delivery receipts; unlisted child source bodies; full NEXUS instrumentation; full messaging/roster/build specifications. Existing technical acceptance is neither repeated nor claimed refreshed. The parent owns fleet census/capacity, counterpart reconciliation, review and delivery.

## Delivery disposition and dependencies

This reader portion is complete: six full charters, three-leg per-file dispositions, ranked supported instruction findings, explicit refuters, static invocation evidence and unread limits. Parent synthesis must deduplicate existing findings, independently review the interpretation, and route supported items through the existing authorized owner handoff. Any owner-file, authority or shared-rule change retains existing approval requirements; this report authorizes none and has delivered no owner message. No new control, tool, implementation task or recurring audit has been commissioned. Original October 5 harness-audit deadline and whole-fleet completion clock are unchanged by this portion.

**POST-REVIEW:** transmission challenge retains T3-1/2/4/5 and narrows T3-3/6/7. T3-6 wrapper freeze July9 precedes FALCON July27 allegation: no proven live-then-repaired chronology. Interpret “repaired retirement” above only as current owning-source counterevidence, not historical execution proof. T3-3 requires owner reconciliation, never amendment11 fleet propagation. T3-7 establishes injected-charter rule attribution only; actual manual launch perimeter UNKNOWN.
