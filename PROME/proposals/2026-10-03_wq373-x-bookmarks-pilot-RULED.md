# WQ-373 — X bookmarks → WALTER, two-week pilot — RULED

**Ruled:** 2026-10-03 09:28 ET, Will in-session, verbatim *"373 approved go with your recs"*. **Written:** 2026-10-03 09:3x ET (`prome-ed`).
**Row:** `PROME/WILL_QUEUE.md` WQ-373 (registered 2026-10-02 21:2x ET from WALTER `LAST_COMPLETION.md` §WILL_NEEDS 2b; now RECENTLY DONE). **Plan:** `AGENTS/WALTER/research/2026-10-02_x-intake-pilot-plan.md` (21e4eaad1).

## The ruling, as PROME's recs stood on the row

| Term | Ruled |
|---|---|
| (1) Spend | APPROVE: an X developer app with ~$10 prepaid credit, cap $10/month |
| (2) Storage | APPROVE: post IDs + WALTER's own summary only; no post text in git (X's 24-hour deletion rule) |
| (3) Trigger | APPROVE: bookmarks are processed at the next WALTER launch |
| Phase 2 | HELD until the two-week measure (a 10–15-account official feed, ~$45–70/mo, is a fresh ask) |

## What the word does NOT cover (carried)

- **Boot-step wiring** — adding the scan to WALTER's boot is a WALTER protocol change (its RULE 8). Asked of Will in the same message as this ruling; WALTER wires only on that word.
- **Unattended WALTER runs** — out of scope; the autonomy question is WQ-369.
- **Unconfirmed facts** — X's minimum credit purchase; whether empty reads are billed (WALTER's plan §2).

## The access mechanism (Will asked: "Do I just give WALTER my login?")

No. WALTER never holds Will's X password. The app gets its own identity (a Client ID from X's developer portal). Will authorizes it ONCE, in his own browser while logged in as himself, for the bookmark-read scope only (OAuth 2.0 with PKCE; scopes `tweet.read users.read bookmark.read offline.access`). X returns a token to WALTER's tool; the token lives in a local `.env` on this box, never in git; it can be revoked at any time from X's connected-apps settings. The exact click-path is WALTER's to write into a setup card (portal screens change; nothing here is to be guessed).

## Probe receipts that shaped the rec (full text on the row via `git log -p`)

- WALTER's Friday "402 on direct fetch" came from the harness WebFetch tool, not X's web server.
- A direct page fetch (browser-UA `curl -L`) returns 200 and a ~274–299-character PREVIEW in the page's meta tags (a prefix of the post; SternDrew 299 of 1,192 chars). WALTER's "hollow page" was retracted (NUL bytes put grep in binary mode).
- Full text today needs `api.fxtwitter.com` (unofficial, terms risk) or the official API ($0.005 per post). The pilot buys compliance, durability and full text; the bookmarks-as-queue case stands on its own.

## Registered at the ruling

DOCKET L598 (build + Will's hands; WALTER wakes Mon 10/05 if not live) · L599 (two-week review, provisional 2026-10-20) · WALTER packet `AGENTS/WALTER/inbox/2026-10-03_from-PROME_WQ-373-RULED-x-bookmarks-pilot-phase-1.md` · fleet memory `finding_negative_reachability_is_a_claim_about_your_request` instance 5.

## Will's direction after the ruling (sourced; shapes the build, changes no term)

2026-10-03 09:31 ET, verbatim: *"now I think I like the idea of WALTER being able to check my bookmarks regularly. It would be easier for me to just bookmark things on my end rather then me snapping screen shots or sharing links like I have been."* Read: the operator wants bookmarks to become the PRIMARY channel for X items, and wants pickup to be regular. Phase 1 as ruled delivers the first (bookmark instead of screenshot; WALTER reads at each launch, WQ-377 asks the boot-step word). "Regularly" between launches is NOT an unattended WALTER session (WQ-369 class; conflicts with the one-machine git rule); the architecture-consistent form is a RESEARCH-INTAKE collector that pulls bookmark IDs on the lane's schedule and a Telegram line on a watch-term hit — the WQ-187 digest plumbing, which still needs Will's tokens. Candidate Phase 1b for the L599 review, not a change to tonight's terms. WALTER told the same minute. *(Appended 2026-10-03 09:3x ET, `prome-ed`.)*

## Post-build direction, sourced (WALTER by SendMessage 2026-10-03 11:1x ET; no decision yet)

Will, on Telegram with WALTER, is weighing the ~$1–2/mo API cost and asked for free alternatives. WALTER's menu: (1) the SHARE-SHEET path — tap Share on a post → iOS Shortcut → push the link into RESEARCH-INTAKE `phone_inbox/`, which WALTER reads at launch (the already-built phone-signal path, receiving side shipped 7/27; only Will's Shortcut + the Contents:write PAT remain = WQ-204, owed since 9/19); (2) a free browser extension WALTER would build and maintain; (3) X's full-archive export (clunky). **PROME's framing, sent to WALTER the same minute so the desks agree:** the share-sheet captures the pick for free and is durable; it does NOT change the full-text question — a shared LINK still reads as a ~300-char preview on a direct fetch, full text needs `api.fxtwitter.com` (terms risk) or the official API, exactly as this morning's probes established; the bookmark API's edges are the native bookmark button as the trigger, compliant full text, and quoted posts/media; both routes need ~15–20 min of Will's hands, and WQ-204's have been owed two weeks. If Will picks the share-sheet: WQ-373's pilot → SUPERSEDED or DEFERRED on his word (a new RECENTLY DONE line, never a silent edit), WQ-377 moot, L598/L599 re-dispositioned, WQ-204 becomes the live item with a fresh date. Nothing moves until he says.

**SIDE-TABLED 2026-10-03 11:2x ET** — Will in PROME's terminal 11:26 ET, verbatim: *"okay lets side table that for now and go back to PROME focused tasks."* No decision between API pilot / share-sheet / park; the build stays BUILT (eafe678d6), the card released but unused, WQ-377 open, L598/L599 pending on a live run that is not scheduled. WALTER told the same minute to stand down. Re-opens on Will's word only.

**LANE PICKED 2026-10-03 11:3x ET** — Will to WALTER on Telegram 11:37 ET (15:37Z), verbatim: *"Okay cool I will work on the API angle where do I go to create that."* ⇒ the side-table is lifted by his own word; WQ-373 proceeds AS RULED (direct official API, Phase 1 terms); the vendor comparison is OFF (not asked); the share-sheet route stays WQ-204 as it was. WALTER is walking him through the setup live (developer.x.com → Project + App → Read-only permission, Native App type → OAuth scopes → Client ID → ~$10 credit → `--authorize`). The LIVE FIRST RUN (L1–L4) is the active gate; WQ-377 boot wiring stays withheld until L1–L2 pass; WALTER reports the first-successful-scan date (L599 → +14 d), the WSL2-localhost answer, and the seed-failure behaviour if he authorizes before credit loads.
