# X Bookmarks → WALTER — Your Setup Card (~15–20 min, one time)

**No — you never give WALTER your login.** You never type your X password anywhere near WALTER. You log into X in **your own browser**, click "Allow" once, and X hands WALTER a limited, **read-only** key (a token). You can revoke that key anytime (last section). WALTER can *read your bookmarks and nothing else* — it can't post, can't delete a bookmark, can't see your DMs or password.

This is a one-time setup. After it, you just **bookmark a post** on X instead of screenshotting it, and WALTER picks it up at its next launch.

---

## What you do (in order)

**1. Create a developer app**
- Go to **developer.x.com** → sign in with your X account → open the **Developer Portal** → **Projects & Apps** → create a Project, then an **App** inside it (any name, e.g. "WALTER-bookmarks").

**2. Turn on user login for the app**
- In the app's **Settings** → **User authentication settings** → **Set up**.
- **App permissions:** **Read** (not Read and write). This matters — read-only is the whole point.
- **Type of App:** choose **Native App** (this is a "public client", which uses the secure PKCE method — no secret to leak).
- **Callback URI / Redirect URL:** paste exactly:
  ```
  http://localhost:8723/callback
  ```
- **Website URL:** anything valid (e.g. your X profile URL). Save.

**3. Copy your Client ID**
- On the app's **Keys and tokens** page, copy the **OAuth 2.0 Client ID**.
- Tell WALTER to put it in its private `.env` file (never in git), OR paste it into `AGENTS/WALTER/.env` yourself as one line:
  ```
  X_CLIENT_ID=<the client id you copied>
  ```
  *(If the portal made you a "Confidential" client instead and gave a Client Secret, also add `X_CLIENT_SECRET=<secret>`. Native/public app = no secret, which is simpler.)*

**4. Add a little prepaid credit**
- In the portal, add **~$10** of prepaid credit and set a **$10/month cap** (your approved terms). Reads are about **$0.005 per post**; your bookmark volume runs ~$1–2/month, so $10 lasts a long time.
- ⚠️ *To confirm while you're in there:* the **minimum** credit purchase (we weren't sure it's exactly $10), and whether **bookmark folders** need Premium — if a folder is free, you can make a folder for "things for WALTER" and keep personal bookmarks out of its queue. If folders need Premium, WALTER just reads all your bookmarks (fine for the pilot).

**5. Authorize once (this is the "Allow" click)**
- In the WALTER terminal, run:
  ```
  python3 AGENTS/WALTER/tools/x_bookmarks_scan.py --authorize
  ```
- It prints a URL. Open it **in your browser** (where you're logged into X). You'll see X's own "Authorize WALTER-bookmarks to access your account?" screen listing **read-only** permissions. Click **Authorize**.
- The tab says "authorization received — you can close this." Done. WALTER has stored a read-only token in its private `.env` and set today as the "start line" (your existing bookmarks are ignored; only ones you add from now on get picked up).

---

## After setup — your whole job
**Bookmark the post.** That's it. At WALTER's next launch it reads new bookmarks, tells you "N new bookmarks since last launch, M dispatched," and routes them like any other signal. Telegram and screenshots still work too — nothing changed there.

## If you ever want to cut it off
- **X side (kills the key entirely):** X app/website → **Settings → Security and account access → Apps and sessions → Connected apps** → "WALTER-bookmarks" → **Revoke access**. The token dies instantly.
- **WALTER side:** delete the `X_BOOKMARK_*` lines from `AGENTS/WALTER/.env`.

## What WALTER can and can't do with this
- **Can:** read your bookmarks (post text + who posted), read your user id to find your bookmark list.
- **Can't:** post, reply, like, follow, add/remove a bookmark, read DMs, or see your password. Scope is `tweet.read users.read bookmark.read` + a refresh token so it doesn't re-ask every few hours. No write scope exists on the token.

---
*Pilot terms (WQ-373, approved 2026-10-03): ~$10 prepaid / $10-mo cap · post IDs + WALTER's own notes kept, never your post text in git · processed at WALTER launches only (no unattended runs in Phase 1). Two-week review ~10/20. Running "regularly between launches" is a separate decision (Phase 1b), not switched on here.*
