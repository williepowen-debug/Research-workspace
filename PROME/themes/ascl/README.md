# ASCL (ASCLEPIUS) — biotech / pharma / healthcare theme home

**Created:** 2026-10-22 (Will-approved, verbatim: "name is okay but I want to address it as ASCL for short" / "yes go ahead and build it").
**Status:** Lightweight THEME folder. Not a fleet desk. No STATUS, no inbox, no spawn protocol, no roster entry.
**Name etymology:** Asclepius, Greek god of medicine and healing.
**Owner:** PROME (acts as research librarian; migrates to a desk owner on promotion).

## Scope

The whole category — biotech, pharma, healthcare — not just event-driven options.
- **Catalyst / event trades:** binary readouts (Phase 2/3, FDA decisions, AdComms, ESMO/ASCO), sell-the-news setups, platform-premium unwinds.
- **Franchise theses:** Keytruda, Opdivo, GLP-1s, mRNA platforms, gene editing, personalized vaccines, sequencing/dx.
- **Rotation reads:** biotech vs big pharma, growth-biotech vs defensive health, managed care, hospitals.
- **Second-order:** who gets hit when a drug class is disrupted, insurer/payer effects, CDMO/supplier reads.

## What belongs here

- `catalysts.tsv` — upcoming dated binary events worth tracking
- `ideas/` — individual research reports (one per file, dated)
- `theses/` — standing theses with evidence trail (updated, not duplicated)
- `log.md` — one-line entry per session touch; not a duplicate of memory/

## What does NOT belong here

- Trade construction (TERRY)
- Position-truth or FORGE mirror (PROME/FORGE)
- Signal routing (WALTER)
- Credit / HY-biotech specifically (DEWEY if commissioned)

## Upgrade path to a full desk

If/when Will promotes this to an active fleet desk:

```
git mv PROME/themes/ascl AGENTS/ASCL
# then add in that directory:
#   CLAUDE.md  (identity, responsibilities, evidence standards, owned paths)
#   STATUS.md
#   inbox/, outbox/, workbook/
#   workbook/CATALYSTS.tsv  (promote from catalysts.tsv)
# then register in:
#   PROME/ROSTER.md
#   AGENTS/_NETWORK.md
#   AGENTS/DAEDALUS/FLEET_MAP.tsv
```

Promotion is a ~15-minute lift. Nothing in this theme folder blocks it.

## Session 1 provenance (2026-10-22)

The eight research reports in `ideas/` were produced by Sonnet subagents spawned by PROME at Will's direction after Will spotted MRNA −24.94% intraday on an apparent early leak of its mRNA-4157 Phase 3 melanoma vaccine data (full ESMO Sat 10/24). The two theses in `theses/` consolidate the session's findings. Devil's-advocate adversarial read (H) was Opus-grade.

Session log → `log.md`.
