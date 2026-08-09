// spine_audit.workflow.js — weekly spine-reconciliation mini-audit (PROME).
//
// PURPOSE: boot-read/protocol docs accumulate canon-contradicting claims between
// Will-triggered deep audits (the 7/1 24-file audit found 9 of 24 files carrying
// rot, incl. a boot-read STATUS with a canon-contradicting push directive). This
// is the standing catch-all: 7 read-only readers over the 14-file spine set vs
// enumerated canon anchors. Companion to the deterministic canon-change mirror
// sweep (PROME/SYSTEM.md → Canonical → Mirrors map, CLOSEOUT Chunk-3 trigger).
//
// RUN:  Workflow({ scriptPath: "PROME/tools/spine_audit.workflow.js",
//                  args: { today: "YYYY-MM-DD" } })   // pass today's date in
// CADENCE: when the PROME/STATUS.md header "Last spine audit" stamp is >7d
// (checked at boot step 8 / closeout Chunk 3). Update the stamp after each run.
// OUTPUT: consolidated per-file verdicts; PROME applies fixes same-session
// (pathspec commits; shared docs Will-gated) and re-stamps STATUS.
// COST: ~7 agents, roughly 1/4 of the 7/1 verify round.

export const meta = {
  name: 'spine-audit',
  description: 'Weekly reconciliation of PROME boot-read/protocol docs against canon anchors',
  phases: [{ title: 'Audit', detail: '7 readers x 2 spine files vs canon anchors' }],
}

// args must be a JSON OBJECT ({ today: "YYYY-MM-DD", repo?: "/abs/path" }). The
// 7/28 run passed it as a JSON-encoded STRING and readers ran UNSTAMPED — so
// self-defend: parse a string arg, then validate the date shape either way.
let ARGS = args
if (typeof ARGS === 'string') { try { ARGS = JSON.parse(ARGS) } catch (e) { ARGS = null } }
const TODAY = (ARGS && typeof ARGS.today === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(ARGS.today))
  ? ARGS.today
  : 'UNSTAMPED — ask PROME to pass args as a JSON object { today: "YYYY-MM-DD" }'
// S4 fix (8/9): repo path from args with fallback — was hardcoded only.
const REPO = (ARGS && typeof ARGS.repo === 'string' && ARGS.repo.startsWith('/'))
  ? ARGS.repo
  : '/home/willi/Research-workspace'

// The spine set: every doc PROME boot-reads or operates the session from,
// paired 2-per-reader. Keep in sync with PROME/BOOT.md's boot sequence.
const GROUPS = [
  ['CLAUDE.md', 'PROME/CLAUDE.md'],
  ['PROME/BOOT.md', 'PROME/CLOSEOUT.md'],
  ['PROME/STATUS.md', 'PROME/SCRATCH.md'],
  ['PROME/ACTIVE_DECISIONS.md', 'HEARTBEAT.md'],
  ['PROME/GIT_COORDINATION.md', 'PROME/SYSTEM.md'],
  // S4 coverage fix (DAEDALUS 7/28 audit, shipped 8/9): the four omitted
  // protocol/spine docs join as two pairs — 7 readers / 14 files.
  ['PROME/HANDOFF.md', 'PROME/AUTONOMY.md'],
  ['PROME/MACHINE_LOCAL.md', 'PROME/COMPLETION_SPEC.md'],
]

const CANON = `CANON ANCHORS (read these FIRST; they win on any conflict):
- Git/push/commit protocol: ${REPO}/CLAUDE.md "Git Protocol" section (serial multi-machine; non-ff abort = routine 'git pull --rebase' + re-push, escalate only on out-of-dir conflicts or mid-session recurrence; ALL git ops from repo root; pathspec commits only).
- Machine model: ${REPO}/PROME/MACHINE_LOCAL.md (serial multi-machine, desktop <-> laptop, one box at a time).
- Forward catalyst dates: ${REPO}/PROME/DOCKET.tsv (canonical docket — prose date claims must match it).
- Roster/classification: ${REPO}/PROME/ROSTER.md.
- Trigger bands/levels: ${REPO}/FORGE/tools/market-data/config.py + ${REPO}/AGENTS/LIQUID/workbook/KILL_MEMO_HY_OAS_260.md (HY >280 X1 / <260 two-closes re-kill; NEVER cite market LEVELS as current from state files — only band DEFINITIONS are checkable).
- Mirror map: ${REPO}/PROME/SYSTEM.md "Canonical -> Mirrors" table (which doc owns which fact).`

const SCHEMA = {
  type: 'object',
  properties: {
    files: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          file: { type: 'string' },
          verdict: { type: 'string', enum: ['CLEAN', 'FLAG'] },
          issues: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                severity: { type: 'string', enum: ['blocking', 'minor'] },
                description: { type: 'string' },
                location: { type: 'string' },
              },
              required: ['severity', 'description', 'location'],
            },
          },
        },
        required: ['file', 'verdict', 'issues'],
      },
    },
  },
  required: ['files'],
}

function prompt(pair) {
  return `You are a READ-ONLY spine auditor in a multi-agent research repo. Do NOT edit, write, commit, or run any state-changing command. Today is ${TODAY}.

Repo root: ${REPO}. Your two files: ${pair.map(f => REPO + '/' + f).join(' and ')}

${CANON}

For EACH of your two files:
1. Read it ENTIRELY — including the spine below any fresh header (append-on-top docs rot in the body while the header stays current).
2. Check every load-bearing DIRECTIVE and CLAIM against the canon anchors above: push/git rules, machine-model phrasing, catalyst dates (vs DOCKET.tsv), roster names, trigger-band definitions, ownership claims.
3. Check internal consistency: does the header contradict a row/section below? Do two sections state different rules?
4. Spot-check outbound file pointers (backticked paths) — do they exist on the filesystem? A line that itself declares a path dead/retired is fine.
5. Ignore market LEVELS (prices/spreads change daily by design and state files self-flag "refresh before citing") — flag only stale RULES, DATES, BANDS, POINTERS, and contradictions.

Severity: 'blocking' = a directive/date/band a boot reader would act on wrongly; 'minor' = wording drift, dated phrasing, cosmetic. Verdict CLEAN only if zero blocking issues. Be precise with locations (section name + approximate line). Do not pad — an empty issues list on a genuinely clean file is the correct output. Your final action: return the structured output.`
}

phase('Audit')
const results = await parallel(GROUPS.map(pair => () =>
  agent(prompt(pair), { label: 'spine:' + pair.map(p => p.split('/').pop()).join('+'), schema: SCHEMA })))

const files = results.filter(Boolean).flatMap(r => r.files)
const blocking = files.flatMap(f => f.issues.filter(i => i.severity === 'blocking').map(i => ({ file: f.file, ...i })))
log(`${files.length} files audited; ${files.filter(f => f.verdict === 'FLAG').length} flagged; ${blocking.length} blocking`)
return { files, blocking_count: blocking.length }
