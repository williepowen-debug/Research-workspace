# Mail Processing Protocol

**Read this file when spawned for inbox processing. Follow it exactly.**

---

## Inbox Processing Steps

1. **Read each signal** in `inbox/` (skip `processed/`) — who sent it, what's the data, what priority?
2. **Cross-reference workbook** — check KB.tsv, VX.tsv, FLOW.tsv, PREDICTIONS.tsv. Does this connect to something you already track?
3. **For each signal, decide:** INTEGRATE (full KB entry + STATUS update), LOG (KB entry only), or DISCARD (stale/duplicate/irrelevant)
4. **Log to KB.tsv** — one row per atomic claim. Use 13-column schema from `workbook/SCHEMA.tsv`. Validate enums against `AGENTS/VOCABULARIES.tsv`.
5. **Update VX.tsv** if any vector changed state (YELLOW→ORANGE, etc.)
6. **Update FLOW.tsv** if a transmission pathway was confirmed, changed speed, or newly identified
7. **Update STATUS.md** if scenario probabilities, convergence scores, or situation tiers changed
8. **Write outbox signals** only if: (a) you have new info the sender doesn't have, (b) their signal contains an error, or (c) it triggers a cross-agent threshold. Silence = received and integrated.
9. **Move processed signals** to `inbox/processed/`
10. **Write `RECEIPT.md`** (this folder) — LAST action. See format below.

---

## Outbox Format

One `.md` file per signal in `outbox/`:
- **Filename:** `YYYY-MM-DD_to-[target]_[short_description].md`
- **Content:**
```
## YYYY-MM-DD — To: [TARGET_AGENT]
**Signal:** [one-line summary]
**Detail:** [2-3 sentences — what changed, why it matters to them]
**Source:** [where this came from]
**Priority:** 🔴/🟠/🟡
```

---

## Processing Receipt (RECEIPT.md)

After EVERY inbox run, **overwrite** `RECEIPT.md` in this folder. This is how PROME audits your work.

```markdown
# Inbox Processing Receipt — YYYY-MM-DD HH:MM UTC
## Agent: CRUISE

### Signals Processed
| # | Signal File | Action | KB Entries Created | VX/FLOW Changes |
|---|-------------|--------|-------------------|-----------------|
| 1 | SIG-xxx.md | INTEGRATE | KB-CRU-001 | VX-CRU-01 → RED |

### STATUS.md Changes
- [Key metric]: [old value] → [new value]

### Outbox Signals Written
- to-[AGENT]: [one-line summary]
- (none)

### Files Modified
KB.tsv, VX.tsv, FLOW.tsv, STATUS.md

### Skipped / Issues
- (none)
```
