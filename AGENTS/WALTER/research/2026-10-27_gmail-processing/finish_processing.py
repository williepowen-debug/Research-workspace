"""Persist manual dispositions of the previously declared 89-item batch."""
from pathlib import Path
import csv, json, subprocess, sys
from collections import Counter

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
OLD = ROOT / 'AGENTS/WALTER/research/2026-10-26_gmail'

def main():
    rows = list(csv.DictReader((OLD / 'content-dispositions.tsv').open(), delimiter='\t'))
    dispatch = json.loads((OUT / 'dispatch-summary.json').read_text())
    ids = {r['slug']: r['signal_id'] for r in dispatch['rows']}
    routed = {
        1: 'trepp-newmark-refinance-basis',
        9: 'trepp-newmark-refinance-basis', 17: 'trepp-newmark-refinance-basis',
        21: 'american-equity-iowa-loan-source-upgrade',
        28: 'openai-google-distribution-primary',
        29: 'mainstreet-q3-credit-and-funding',
        58: 'jetblue-q3-primary-liquidity-counterevidence',
        63: 'dutch-staffing-plan-not-realized-ai-losses',
        65: 'broadcom-anthropic-63b-committed-structure',
        68: 'townlane-fund-two-commitments',
        71: 'cre-values-distress-sale-denominators',
        72: 'cre-values-distress-sale-denominators',
        73: 'blackjack-remaining-multifamily-maturity',
        77: 'forge-atlanta-primary-restatement-grace',
        82: 'sunbeam-florida-self-funding-plans',
        84: 'trepp-newmark-refinance-basis',
    }
    folds = {
        10: 'Same episode 430; no audio playback or transcript obtained. Keep promotion as context only.',
        18: 'Same episode 430; no audio playback or transcript obtained. Keep promotion as context only.',
        19: 'Same episode 430; no audio playback or transcript obtained. Keep promotion as context only.',
        74: 'Exposed Bisnow body read. BAC/WFC Q3 charge-offs and declining NPLs already covered by GIBBS primary Q3 census; no new loss event.',
        78: 'Exposed Bisnow body read. RESG shrinkage, REO and RaDD extension already covered by OZK primary Q3 work; article profit figure does not overwrite issuer/owner values.',
        80: 'Exposed Bisnow body read. Existing CoreWeave financing repricing coverage, including 20261015-005 correction and VULCAN L782 v3. Anonymous/analyst failure forecasts are not realized defaults; rounded 2030/2032 yields do not upgrade instrument-specific owner marks.',
        81: 'Exposed October 15 personnel body read. Routine reported Brookfield-to-Pretium appointment; no named financing failure, withdrawal or changed fund term established. Historical AUM and fundraising references retained as attributed context.',
        89: 'Invitation is October 29 at 14:00 ET, already visible in delivered email. No webinar analysis yet exists in the invitation; no RSVP, calendar write or promised monitoring.'
    }
    unresolved = {
        22: 'Iowa loan evidence does not identify/validate the teaser captive surplus calculation. Captive identity, reporting basis, dates and original source remain unverified.',
        23: 'Historical Lindberg analogy only in delivered teaser; underlying case record not obtained. No new October failure adopted.',
        25: 'A-Cap South Carolina reference remains teaser-only; original action, entity, date and current status not established.',
        26: 'Earlier card 026 retains plaintiff-source September 21 suit and separate generation quantities. No new court disposition or permit revocation established in this pass.',
        27: 'Earlier card 026 remains qualified. Follow-up public project reporting dates approval to April 21, 2026 and gas-supply proposal to February 2025; municipal original/FID and operating water use not verified. No new October approval or shutdown adopted.',
        56: 'Original Anthropic selected-section work already exists; this pass did not reconcile full cloud-channel mix/gross-net recognition tables. Do not infer incremental revenue from headline proportions.',
        57: 'Goldman prime-broker client-flow attribution remains a linked headline. Original note, observation window and hedge-fund universe not obtained; no total-market flow adopted.',
        60: 'Potential Universal Music go-private talks remain preliminary headline evidence; no signed transaction, financing commitment or distress event adopted.',
        62: 'Starlink opinion lead remains unread full-body context. No new operational/theater event or war-state inference adopted.',
        64: 'Anthropic computing-cost headline overlaps existing selected IPO sections. Full table reconciliation remains outside this pass; no headline figure substituted for owner evidence.',
        66: 'Potential DoorDash/Instacart transaction remains unverified headline evidence. No signed deal or closed acquisition adopted.',
        69: 'Brazil market-pricing opinion remains unreviewed full-body commentary; existing dated unwind and settlement limits stand.',
        70: 'Apple screen-complaint headline remains unverified product evidence; no quantified production, returns or demand change adopted.',
        86: 'Burry delivered teaser read; full historical breadth construction/denominators unavailable. No strategy, historical percentile or trading implication adopted.'
    }
    for r in rows:
        n = int(r['n'])
        r['prior_disposition'] = r['disposition']
        r['prior_ref'] = r['ref']
        if n in routed:
            r.update(disposition='DISPATCH', ref=ids[routed[n]], reason='Source processing and exact limits in the new card and REVIEW.md; merged items share one card.')
        elif n in folds:
            r.update(disposition='FOLD', ref='REVIEW.md', reason=folds[n])
        elif n in unresolved:
            r.update(disposition='NOTE', ref='REVIEW.md', reason=unresolved[n])
        elif r['disposition'] == 'DISPATCH':
            r.update(disposition='DUP', reason='Earlier source-qualified dispatch retained; no new verified delta requiring another packet. Original card remains the reference.')
        elif r['disposition'] == 'NOTE':
            r.update(reason='Delivered text reviewed in first pass. Linked original not recovered/reviewed to decision-bearing scope in this pass; retain as an explicit source lead, no irrelevance or all-clear inference.')
    fields = ['n','email_n','part','gmail_id','title','prior_disposition','prior_ref','disposition','ref','reason']
    with (OUT / 'content-dispositions.tsv').open('w') as f:
        w = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(rows)
    tool = ROOT / 'AGENTS/WALTER/tools/batch_manifest.py'
    for r in rows:
        subprocess.run([sys.executable,str(tool),'--item','BM-20261027-06',r['n'],r['disposition'],r['ref']+'; '+r['title']+'; '+r['reason']],cwd=ROOT,check=True,capture_output=True)
    p = subprocess.run([sys.executable,str(tool),'--close','BM-20261027-06'],cwd=ROOT,check=True,capture_output=True,text=True)
    print(p.stdout.strip())
    counts = dict(Counter(r['disposition'] for r in rows))
    (OUT/'disposition-counts.json').write_text(json.dumps(counts,indent=2)+'\n')
    print(json.dumps(counts))

if __name__ == '__main__': main()
