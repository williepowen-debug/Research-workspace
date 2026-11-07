# Acceptance: fetch.py bare futures roots, DOCKET L925, written before the edit

**Defect:** `fetch.py price CL` prints Colgate-Palmolive with rc=0 and no warning. NG, BZ, RB, ES, WTI and GOLD do the same.

**Conditions**
1. `price` given a registered bare root refuses, rc=2, prints nothing on stdout, fetches nothing, and names the working form on stderr.
2. Any case (`cl`) refuses. A list with one bare root refuses as a whole, so no partial table reads as complete.
3. `--equity` serves the symbol as typed, for someone who means Colgate.
4. Futures forms (`CL=F`, `CLX26`, `CLX26.NYM`) and ordinary tickers are unaffected. `dashboard.py` and programmatic `price_fetch` callers are unaffected: the guard is at the CLI only.
5. A futures quote under $20 keeps four decimals in the data and the table (HO 4.3359), everything else keeps two.
6. A table with a futures row says vendor futures quotes run about 10 minutes behind.
7. The bare-dated error names `.CMX`.

**Neighbours:** ordinary: CL. Overlap: a real equity sharing a root, condition 3. Wrong owner: N/A, FORGE tool owned by PROME. Missing information: the registry is the roots the fleet uses as =F, on both CLI ticker paths; an unlisted root such as ZS or KC can still resolve to an unrelated name, declared residue (corrected after the read: "unregistered roots already error" was false). Concurrent activity: N/A, no shared state added.

**Not in this pass:** the `day` branch's wall-clock check stays open on L925. Sibling surfaces (`snapshot`, `--json` compact view) keep two decimals and no delay note, reader ⚠️.

**State:** IMPLEMENTED and TESTED. One counterexample read found two ❌, both fixed after it; INDEPENDENTLY VERIFIED withheld.
