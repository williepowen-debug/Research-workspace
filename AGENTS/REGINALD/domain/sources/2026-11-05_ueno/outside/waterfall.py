# All USD millions. Balance sheet base = Q2-26 deck (Jun-26) + Q1-26 FS lender list, FX ~6,150 G/$.
FX=6150
dep_total=2830.0
insured=0.30*dep_total            # Moody's: ~30% of deposits by value insured
public=869.0                      # Bloomberg: G5tn public deposits = 29% at end-June
ips_dep=300.0                     # IPS ~US$345-380M incl. CDAs + bonds; assume ~$300M CDAs (deposits), ~$50M bonds (INFERRED split)
other_public=public-ips_dep
private_unins=dep_total-insured-public
# other creditors
afd=792.4e9/FX/1e6                # secured by pledged loans (Moody's)
bnf=235e9/FX/1e6; zeta=160e9/FX/1e6; basa=150e9/FX/1e6; cont=25e9/FX/1e6
dfi=(52.5+130.07+65.03+32.52+23.25+13.01+10.41+1.95+5.85)*1e9/FX/1e6
notes=350.0; local_sr=300e9/FX/1e6; sub=368.5e9/FX/1e6+25
print(f"insured {insured:.0f} public {public:.0f} (IPS dep {ips_dep:.0f}, other {other_public:.0f}) private uninsured {private_unins:.0f}")
print(f"AFD {afd:.0f} BNF {bnf:.0f} Zeta {zeta:.0f} Basa {basa:.0f} Cont {cont:.0f} foreign DFIs {dfi:.0f} notes {notes:.0f} local sr bonds {local_sr:.0f} sub {sub:.0f}")
# Asset recovery scenarios (liquidation/transfer value)
good_loans=2460-222   # gross loans less Fiscalía-flagged related (US$167M + G343bn ~ $56M = ~$222M)
scen={
 'low':  dict(liquid=300, good=good_loans*0.70, related=222*0.00, soft=650*0.00, ppe=110*0.50, other=300*0.15),
 'base': dict(liquid=450, good=good_loans*0.82, related=222*0.15, soft=650*0.05, ppe=110*0.65, other=300*0.30),
 'high': dict(liquid=600, good=good_loans*0.90, related=222*0.30, soft=650*0.10, ppe=110*0.80, other=300*0.50),
}
for k,s in scen.items():
    tot=sum(s.values())
    avail=tot-afd   # AFD paid from its pledged loans first (approximation)
    tier1=insured+private_unins+ips_dep   # Art.20 a.1 private deposits (all, by linear increment) + social-security deposits
    r1=min(1,avail/tier1); rem=max(0,avail-tier1)
    r3=min(1,rem/other_public) if other_public else 0; rem2=max(0,rem-other_public)
    unsec=notes+local_sr+bnf+zeta+basa+cont+dfi
    ru=min(1,rem2/unsec); rem3=max(0,rem2-unsec)
    fgd_loss=insured*(1-r1)
    hole=(dep_total+afd+bnf+zeta+basa+cont+dfi+notes+local_sr+sub+150)-tot
    print(f"\n{k}: assets recoverable {tot:.0f}; avail after AFD {avail:.0f}")
    print(f"  tier1 (insured+uninsured private+IPS deposits) {tier1:.0f} -> recovery {r1*100:.0f}%")
    print(f"  other public deposits {other_public:.0f} -> {r3*100:.0f}%")
    print(f"  senior unsecured pool (notes, local sr, interbank, DFIs) {unsec:.0f} -> {ru*100:.0f}%  (notes $ {notes*ru:.0f}M)")
    print(f"  FGD net loss after subrogation ~{fgd_loss:.0f}; liabilities-minus-recoverable hole ~{hole:.0f}")
