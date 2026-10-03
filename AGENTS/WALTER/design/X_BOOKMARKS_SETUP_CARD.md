# X Bookmarks → WALTER — Your Setup Card (~15–20 min, one time)

**No — you never give WALTER your login.** You never type your X password anywhere near WALTER. You log into X in **your own browser**, click "Allow" once, and X hands WALTER a limited, **read-only** key (a token). You can revoke it anytime (last section). WALTER can *read your bookmarks and nothing else* — it can't post, delete a bookmark, see your DMs, or see your password.

One-time setup. After it, you **bookmark a post** on X instead of screenshotting it, and WALTER picks it up at its next launch — **including an older post you bookmark for the first time.** (One limit: if you bookmark something WALTER already processed, un-bookmark it, then bookmark it *again*, it won't re-surface — just send that one by Telegram.)

> Values below (menu names, button labels, pricing) are **how the X developer portal looked when this was written** — X moves things. If a label differs, match by meaning, and tell WALTER what you actually see rather than forcing a mismatch.

---

## What you do (in order)

**1. Create a developer app**
- Go to **developer.x.com** → sign in with your X account → **Developer Portal** → **Projects & Apps** → create a Project, then an **App** inside it (any name, e.g. "WALTER-bookmarks").

**2. Turn on user login**
- App **Settings** → **User authentication settings** → **Set up**.
- **App permissions: Read** (not Read and write). Read-only is the point.
- **Type of App: Native App** (a "public client" — uses the secure PKCE method, no secret to leak).
- **Callback URI / Redirect URL** — paste exactly: `http://localhost:8723/callback`
- **Website URL:** anything valid (e.g. your X profile). Save.
- *(If the portal only offers a "Confidential" client and gives a Client Secret, that's fine too — add `X_CLIENT_SECRET=<secret>` in step 3 as well.)*

**3. Put your Client ID where WALTER can read it**
- On the app's **Keys and tokens** page, copy the **OAuth 2.0 Client ID**.
- The file WALTER reads is `AGENTS/WALTER/.env` — a hidden file in the repo that **does not exist yet** and is **never committed to git** (it's git-ignored). Easiest: **tell WALTER** "my X client id is <id>" and it creates the file. Or make it yourself: in the repo root (`/home/willi/Research-workspace`), create `AGENTS/WALTER/.env` containing one line:
  ```
  X_CLIENT_ID=<the client id you copied>
  ```

**4. Add a little prepaid credit**
- In the portal, add **~$10** of prepaid credit, set a **$10/month cap** (your approved terms).
- ⚠️ *Confirm while you're there* (WALTER can't see the portal): the **minimum** purchase, whether a read bills **per post or per request**, and whether **bookmark folders** need Premium (a free folder would let you keep personal bookmarks out of WALTER's queue). Cost scale: to find new bookmarks WALTER reads your recent bookmarks newest-first until it reaches a page it has already seen — **1–2 pages (up to ~100 posts) on a normal launch, up to ~500 at the most**, plus a one-time read of your existing bookmarks at setup. So cost tracks *how often WALTER launches*. Per-post vs per-request billing is the portal unknown above; the **$10/month cap is the hard stop** either way.

**5. Authorize once — the "Allow" click**
- ⚠️ **Type this in your own terminal** (don't have WALTER run it through a tool — it needs to print a URL and wait for your browser). In the repo root, run:
  ```
  .venv/bin/python3 AGENTS/WALTER/tools/x_bookmarks_scan.py --authorize
  ```
- It prints a URL. Open it **in your browser** (where you're logged into X). You'll see X's own "Authorize WALTER-bookmarks?" screen listing **read-only** permissions. Click **Authorize**.
- The tab says "authorization received — close this." Done: WALTER stored a read-only token in `.env` and marked all your *current* bookmarks as already-seen, so only ones you add from now on get surfaced.
- **If you click Cancel / change your mind:** the tab says "cancelled," the command stops on its own within 5 minutes (or press **Ctrl-C**), and nothing is saved. Just re-run the command to try again.

---

## After setup — your whole job
**Bookmark the post.** At WALTER's next launch it reads new bookmarks, tells you "N new bookmarks since last launch, M dispatched," and routes them like any other signal. Telegram and screenshots still work — nothing changed there.

## If you ever want to cut it off
- **X side (kills the key):** X app or x.com → **Settings → Security and account access → Apps and sessions → Connected apps** → "WALTER-bookmarks" → **Revoke access**.
- **WALTER side:** delete the `X_BOOKMARK_*` lines from `AGENTS/WALTER/.env`.

## If something goes wrong (common cases)
- **"Set X_CLIENT_ID …"** — step 3 didn't land; the `.env` line is missing or misspelled.
- **"No refresh_token returned — is `offline.access` among the app's scopes?"** — the app's User-authentication scopes are missing `offline.access`; re-open step 2 and make sure the read scopes include it, then re-authorize.
- **"Timed out" / "cancelled or denied"** — the browser Allow didn't complete; just re-run the authorize command.
- **The URL never appears** — you (or WALTER) ran it through a non-interactive tool; run it directly in a terminal.
- **"Token refresh FAILED … Re-run --authorize"** — the saved key expired and couldn't renew. Re-authorizing is **safe**: it only refreshes the key and does **not** discard any bookmarks you haven't routed yet.
- **The "authorization received" page won't load after you click Allow** — this box runs under WSL; if your browser is on Windows it has to reach `http://localhost:8723` inside WSL. Usually that just works; if it doesn't, tell WALTER — we may need a different redirect address. (This is the one step not yet tested live.)

## What WALTER can and can't do with this
- **Can:** read your bookmarks (post text + who posted) and your user id.
- **Can't:** post, reply, like, follow, add or remove a bookmark, read DMs, or see your password. Scope is exactly `tweet.read users.read bookmark.read` + `offline.access` (so it needn't re-ask every couple hours). **No write scope exists on the token.**

---
*Pilot terms (WQ-373, approved 2026-10-03): ~$10 prepaid / $10-mo cap · post IDs + WALTER's own notes kept, never your post text in git · processed at WALTER launches only (no unattended runs in Phase 1). Two-week review runs **about two weeks after your first successful scan** (the clock starts then, not on a fixed date). "Regularly between launches" is a separate decision (Phase 1b), not switched on here.*
