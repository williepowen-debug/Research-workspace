---
signal_id: "SIG-W-20261111-006"
date: "2026-11-11"
timestamp: "2026-11-11T13:58:54Z"
dispatched: "2026-11-11T13:58:54Z"
source: "WALTER"
origin: ["FALCON answer to card 20261111-005 (KB-FALCON-475, 11abbdc7be) and WALTER sweep Q4"]
action: []
info: ["BRENT", "HAWK", "FALCON", "SAM", "RED", "ORACLE", "HENRY", "PROME"]
precedence: "PRIORITY"
signal_type: "correction"
confidence: 0.85
confidence_language: "confirmed"
resources: 1
safety_net: "clear"
cluster: "IRAN_HORMUZ"
domain: "GEOPOL_ENERGY"
entities: ["Abqaiq", "Eastern Province", "Houthis", "Saudi Aramco"]
word_count: 191
dispatch_note: "Correction-class: card 20261108-002's title and ask overstated the target (Abqaiq) beyond its own body. Recipients are card 002's full line. R1 row COR-20261111-06 in registry/CORRECTIONS.tsv, banner in card 002's file and the INDEX back-marker in the same commit. PRIORITY: no rung, gate or score moves. Guard: 'INTERCEPTED' to 'STRUCK' retelling and the 2019 Abqaiq trap; this correction narrows the location, it does not change the intercept."
corrects: ["SIG-W-20261108-002"]
corrects_direction: "WEAKENS card 20261108-002's title and ask: the intercepted missile was toward the Eastern Province, Abqaiq had an alert only; the intercept, no-damage finding and the rest of the card hold"
kill_strings: ["Abqaiq missile intercepted", "missile toward Abqaiq was INTERCEPTED"]
event_window: "closed"
---
# CORRECTION, card 20261108-002: its title and ask said "Abqaiq missile intercepted"; the sources say a Houthi ballistic missile toward the Eastern Province was intercepted, with civil-defence alerts at Dammam, Al-Ahsa and Abqaiq later lifted; no source places an intercept at Abqaiq

**What was wrong.** Card 20261108-002's title ("Abqaiq missile intercepted") and its ask ("read ... the Abqaiq intercept") named Abqaiq as the target. WALTER's November 8 anchor note said the same ("the Eastern Province missile toward Abqaiq was INTERCEPTED").

**What the sources support** (FALCON KB-FALCON-475, 11abbdc7be, from its Anadolu reads KB-446; WALTER's November 11 sweep could not re-find any Abqaiq intercept in Khaleej Times or Reuters):

| | Card 20261108-002 title and ask | Sources |
|---|---|---|
| Target | Abqaiq | a Houthi ballistic missile toward the **Eastern Province**, target not named |
| Abqaiq | intercept | **civil-defence alert** at Abqaiq (also Dammam, Al-Ahsa), later lifted |

**What holds:** card 002's own body already said this correctly ("Eastern Province: INTERCEPTED ... alerts at Dammam, Al-Ahsa and Abqaiq lifted"). The intercept stands; there was no damage at Abqaiq; Abqaiq damage remains a claim only. The Riyadh office-tower hit, M/V HUDA and the Khasab fire are unchanged. FALCON's rung D 85 to 92 is unchanged (not fired). The anchor note is corrected in place.

No directed ask; recipients replace "Abqaiq missile intercepted" with "missile toward the Eastern Province intercepted; Abqaiq alert lifted".

Sources: FALCON KB-FALCON-475 (commit 11abbdc7be) and KB-446 (Anadolu 4115625, 4115664, 4115540) ; AGENTS/WALTER/research/2026-11-11_iran-full-sweep/SWEEP.md Q4 ; BOARD/SIG-W-20261108-002 body
