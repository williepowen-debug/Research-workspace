# AGENTS — Private Credit / Insurance

Canonical paths remain `AGENTS/<NAME>/`. This file is an index only.

## Core private-credit chain

| Agent | Path | Role |
|---|---|---|
| BROCK | [`BROCK/`](./BROCK/) | BDCs, private credit, CLOs, gates, NAV/PIK stress, public vehicle signals. |
| SHADE | [`SHADE/`](./SHADE/) | PE-insurance-captive plumbing, Athene/Apollo-style wrappers, FABN/FHLB/statutory stress. |

## Transmission map

```text
BROCK → SHADE → LIQUID
   ↘ REGINALD when private-credit/NDFI exposure reaches banks
   ↘ VIOLET when credit stress leads vol complacency
```

## Key neighboring surfaces

| Neighbor | Path | Why it matters |
|---|---|---|
| LIQUID | [`LIQUID/`](./LIQUID/) | Funding pullability / Treasury plumbing amplifier. |
| REGINALD | [`REGINALD/`](./REGINALD/) | Bank bridge for NDFI/private-credit stress. |
| BOND | [`BOND/`](./BOND/) | Public credit, HY/IG/CDX/cash market structure. |
| VIOLET | [`VIOLET/`](./VIOLET/) | Credit-to-vol lag detection. |
| NEXUS | [`NEXUS/`](./NEXUS/) | Convergence synthesis across chains. |

## Closest bridges

- Credit/bank stress → [`_CREDIT.md`](./_CREDIT.md)
- Funding/market structure → [`_FUNDING_MACRO.md`](./_FUNDING_MACRO.md)
- Trade construction / adversarial review → [`_SYNTHESIS_OPS.md`](./_SYNTHESIS_OPS.md)
