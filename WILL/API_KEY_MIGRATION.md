# Anthropic API Key Migration — DEADLINE SUN APR 5 3PM ET

**Why:** Anthropic cutting subscription auth for third-party tools (OpenClaw) starting Apr 5 12pm PT / 3pm ET. All agents go dark if not switched.

**Current config:** `~/.openclaw/openclaw.json` → `auth.profiles.anthropic:default.mode = "token"` (subscription OAuth)

---

## Steps

### 1. Get API Key (~3 min)
- Go to **console.anthropic.com**
- Sign in (may need separate account from Pro subscription)
- Navigate to **API Keys** → **Create Key**
- Copy the key (starts with `sk-ant-...`)
- Add a **payment method** (credit card) for pay-as-you-go billing
- Check if "extra usage bundles" are available — might be cheaper than pure pay-as-you-go

### 2. Set the Key on the Server (~2 min)

SSH into the box and run:

```bash
# Option A: Environment variable (preferred)
echo 'export ANTHROPIC_API_KEY=sk-ant-YOUR-KEY-HERE' >> ~/.bashrc
source ~/.bashrc

# Option B: Or set it in OpenClaw config directly
# openclaw config set auth.profiles.anthropic:default.mode api-key
# (check openclaw docs for exact syntax)
```

### 3. Restart Gateway (~1 min)

```bash
openclaw gateway restart
openclaw gateway status  # verify it's running
```

### 4. Test (~1 min)

Send a message to Prome on Telegram. If I respond, we're good.

---

## Cost Estimates

| Model | Input | Output |
|-------|-------|--------|
| Opus 4 | $15/MTok | $75/MTok |
| Sonnet 4 | $3/MTok | $15/MTok |

Rough daily cost: **$5-20/day** depending on spawns. Heavy days (multiple agent passes) could hit $30+.

**Cost reduction options:**
- Switch default model to Sonnet for routine spawns, Opus for synthesis/decisions only
- Boris (Anthropic) submitted PRs to improve OpenClaw prompt cache efficiency — may already be merged
- Check the discounted "extra usage bundles" mentioned in the announcement

---

## If You Miss the Deadline

All OpenClaw ↔ Anthropic calls fail. Agents can't respond. Claude Code agents (CARL, REGINALD, SAM, RED) may also be affected if they auth through the same subscription.

**Recovery:** Do steps 1-3 above. No data loss — just downtime.

---

## Refund / Credit

Anthropic offering:
- One-time credit = your monthly plan cost
- Full refund available via link in email they're sending
- Check email for the refund link

*Delete this file after migration is complete.*
