# Housing bookmark bounded verification — 2026-10-20

Claim: @WOLF_Financial post `2112549327847461073`, timestamp supplied by parent `2026-10-20T14:19:43Z`, attributes September pending existing-home sales −7.3% MoM and a record low since 2001 to Bloomberg/NAR.

Verdict: **CORRECTED-framing / partly CONFIRMED; record-low component INDETERMINATE on opened primary evidence.** New dated print, not an established duplicate. Route the verified decline to HOMER; preserve the record claim as unverified rather than a fleet fact. No grade or trade recommendation.

| Evidence locator | Observation / limit |
|---|---|
| [NAR release](https://www.nar.realtor/newsroom/pending-home-sales-decreased-7-3-percent-in-september), dated October 20, 2026; opening paragraph and “September 2026 National/Regional Pending Home Sales” | Body explicitly identifies September **2026**, −7.3% MoM, −11.3% YoY, with all four regions falling on both bases. It does **not** state an index level or record low. Full body retrieved directly using Python urllib after web open/click failures; not merely a search snippet. |
| Same release, methodological footnote | Pending means signed contracts awaiting closing, generally leading closings by one or two months. 2001 is its index reference year. This is national contract activity, not completed existing-home sales and not a regional record. |
| [NAR data page](https://www.nar.realtor/research-and-statistics/housing-statistics/pending-home-sales), web-open lines 731–741, retrieved October 20 | Independently displays the September decline and contract basis. No opened monthly table supplies the claimed level/history. A next-release line mislabels September while another says October; use the explicitly dated release for month/year. |
| [Actual X image](https://pbs.twimg.com/media/HVFIQ_nWQAAeRyd.jpg), downloaded and visually inspected October 20 | House photograph with a sale-pending sign; no chart, data, date or record evidence. It does not establish Florida-specific data despite the tropical scene. |
| `AGENTS/HOMER/STATUS.md:66`, read October 20 | Owner still carries August index 71.2, +0.3% MoM, −4.7% YoY, above 69.0 COVID trough. September is newer; never overwrite owner figures. |
| `BOARD/INDEX.md` and BOARD/HOMER text search, October 20 | Found historical June print `SIG-W-20260717-006` and August chart correction `SIG-W-20260822-004` (correcting `SIG-W-20260819-013`). No match for this post ID or September −7.3% print. Search supports novelty, not proof of exhaustive semantic deduplication. |

The accessible NAR release omits both “66.0” and “record low.” Secondary search results mention them but were not used to verify the absolute claim. Deriving approximately 66.0 from the owner's August level and rounded monthly percentage cannot establish a historical minimum or reconcile revisions. Owner validation of actual monthly table/history is the bounded residual if record framing is needed.

Runtime/dependencies: Codex helper, filesystem and web tools verified. Optional `bs4` absent; Python standard-library HTMLParser succeeded, so no remaining execution dependency. Root/local rules explicitly read; no git, credential, live-bookmark API or owner-file edits. Helper closeout: COMPLETE; no remaining helper work. Parent retains routing/marking and any owner follow-up.
