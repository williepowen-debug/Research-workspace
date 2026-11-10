# 2026-11-10 — Acceptance condition: boot.py [2] "PBOC rate" line reads the source

**Written before the code.** Authority: PROME prome-07, 11/10, on Will's fewer-checkers default (USER.md, 10/31). This improves an existing control; it adds no new checker. Root cause: KB-ZHAO-262 (the KB-238 miss). **Scope is this one line only**; no other key figure changes.

**Change.** In `section_key_ages()`, the `PBOC rate` row (VX-ZHAO-6.06) still prints the stored value and its age. When the network is allowed, it also reads the newest PBOC 公开市场业务交易公告 that reports a **fixed-rate (固定利率) reverse-repo operation**, from the list at `https://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/index.html`, newest first, at most 5 notices. It then prints that notice's number, date, tenor and rate beside the stored value.

| Case | Required behaviour |
|---|---|
| **A. Match.** The live tenor and rate equal the stored tenor and rate (the stored cell's leading `<rate> <tenor>`, e.g. `1.25 overnight`, `1.4 (7d repo)`) | Prints `✓ matches PBOC <notice> (<tenor> <rate>%)`. No alert. The source is the verdict, so the age of ZHAO's stamp does not raise an alert here. |
| **B. Mismatch.** The tenor differs or the rate differs (by more than 0.001) | Prints `🔴 MISMATCH vs PBOC <notice>: live <tenor> <rate>% ≠ stored ...`. Counts **1** alert. |
| **C. Unreachable or unparseable.** A network error, a non-200 response, no fixed-rate notice in the newest 5, or a stored cell that cannot be parsed | Prints `⚠️ PBOC notice UNREACHABLE (<reason>), age test only`. The existing 14-day age test decides the alert, unchanged. An unparseable stored cell is treated as a mismatch (🔴), never as a pass. |
| **D. `--quick`** | No network. Prints `(source check skipped, --quick), age test only`. The age test decides. |

**Tests (run before commit; results in the commit body):** A with the live 11/10 page and the current cell `1.25 overnight`; B with the live page and the pre-11/02 cell `1.4 (7d repo)`, which is the exact miss; C with the list URL pointed at an unreachable host; D with `--quick`. A full `boot.py` run must still complete.
