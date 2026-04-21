#!/usr/bin/env python3
"""
banxico_reverse.py — Pull Banxico remittances by Mexican state (CE100), reverse-map
to implied US-state sender volumes using historical migrant-corridor ratios.

Outputs two TSVs under AGENTS/MARCO/baselines/:
  banxico_destination_states.tsv  — raw Banxico quarterly series 2019-present
  us_state_sender_implied.tsv     — reverse-mapped implied US-state sender flows

Methodology:
  1. Download Banxico CE100 (Ingresos por remesas por entidad federativa) XLS.
  2. For each Mexican state M, apply a 50-state US sender-share vector w[M] from
     historical ENADID/MPI/HTA corridor research (see BANXICO_STATE_REVERSE.md).
  3. Sum w[M] * remittances[M,t] across M for each US state to get implied flows.

Anchors (hardcoded, vintage 2018-2022, stale by 2026):
  - MPI 2018-22 aggregate: CA 36 / TX 22 / IL 6 / AZ 5 / FL+WA+GA+NV+NC+NY ~13
  - Corridor tilts: Zacatecas→IL+CA, Oaxaca/Yucatán→CA, border-states→TX+AZ, etc.

Constraints: stdlib + requests + pandas. One-shot. Fail loudly.
"""
import sys, datetime, pathlib
import requests
import pandas as pd

OUT_DIR = pathlib.Path(__file__).resolve().parents[1] / "baselines"
OUT_DIR.mkdir(exist_ok=True)

BANXICO_URL = (
    "https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do"
    "?accion=consultarCuadro&idCuadro=CE100&sector=1&locale=es"
    "&fechaInicio={fi}&fechaFin={ff}&formatoXLS.x=1"
)

# US state 2-letter codes we track (non-listed states absorbed into "OTHER")
US_STATES = ["CA", "TX", "IL", "AZ", "FL", "WA", "GA", "NV", "NC", "NY",
             "CO", "OR", "NM", "UT", "MI", "MN", "IN", "WI", "OTHER"]

# Sender-share matrix: per Mexican state, fraction of its migrants residing in each US state.
# Rows sum to 1.0. Values anchor on:
#   - MPI "Mexican Immigrants in the US" 2018-22 aggregate shares
#   - Durand & Massey / Pew historical corridor research
#   - Hometown-association geography (Rivera-Salgado, Wilson Center)
#   - Border-state → TX/AZ tilt; Pacific-South → CA; Bajío → CA+IL+TX
# Approximations; see BANXICO_STATE_REVERSE.md for citations and caveats.
SENDER_RATIOS = {
    # Bajío / traditional migration core
    "Guanajuato":        {"CA":0.30,"TX":0.22,"IL":0.12,"AZ":0.04,"FL":0.02,"WA":0.02,"GA":0.03,"NV":0.02,"NC":0.03,"NY":0.01,"CO":0.03,"OR":0.02,"NM":0.01,"UT":0.02,"MI":0.02,"MN":0.02,"IN":0.03,"WI":0.02,"OTHER":0.02},
    "Jalisco":           {"CA":0.42,"TX":0.14,"IL":0.09,"AZ":0.05,"FL":0.02,"WA":0.03,"GA":0.02,"NV":0.03,"NC":0.02,"NY":0.01,"CO":0.03,"OR":0.03,"NM":0.01,"UT":0.03,"MI":0.01,"MN":0.01,"IN":0.02,"WI":0.02,"OTHER":0.01},
    "Michoacán":         {"CA":0.44,"TX":0.10,"IL":0.14,"AZ":0.03,"FL":0.02,"WA":0.03,"GA":0.02,"NV":0.02,"NC":0.02,"NY":0.01,"CO":0.02,"OR":0.02,"NM":0.01,"UT":0.02,"MI":0.02,"MN":0.01,"IN":0.03,"WI":0.02,"OTHER":0.02},
    "Zacatecas":         {"CA":0.38,"TX":0.15,"IL":0.20,"AZ":0.03,"FL":0.01,"WA":0.02,"GA":0.01,"NV":0.02,"NC":0.01,"NY":0.01,"CO":0.04,"OR":0.02,"NM":0.01,"UT":0.02,"MI":0.01,"MN":0.01,"IN":0.02,"WI":0.02,"OTHER":0.01},
    "Aguascalientes":    {"CA":0.36,"TX":0.18,"IL":0.11,"AZ":0.04,"FL":0.02,"WA":0.02,"GA":0.02,"NV":0.02,"NC":0.02,"NY":0.01,"CO":0.04,"OR":0.02,"NM":0.01,"UT":0.02,"MI":0.02,"MN":0.02,"IN":0.03,"WI":0.02,"OTHER":0.02},
    "San Luis Potosí":   {"CA":0.28,"TX":0.28,"IL":0.10,"AZ":0.03,"FL":0.02,"WA":0.02,"GA":0.03,"NV":0.02,"NC":0.03,"NY":0.01,"CO":0.03,"OR":0.02,"NM":0.02,"UT":0.02,"MI":0.02,"MN":0.02,"IN":0.02,"WI":0.02,"OTHER":0.01},
    # Pacific-South / Indigenous-heavy → CA concentration
    "Oaxaca":            {"CA":0.55,"TX":0.08,"IL":0.04,"AZ":0.02,"FL":0.03,"WA":0.03,"GA":0.02,"NV":0.02,"NC":0.03,"NY":0.05,"CO":0.02,"OR":0.03,"NM":0.01,"UT":0.01,"MI":0.01,"MN":0.01,"IN":0.01,"WI":0.01,"OTHER":0.02},
    "Guerrero":          {"CA":0.50,"TX":0.10,"IL":0.08,"AZ":0.02,"FL":0.02,"WA":0.02,"GA":0.02,"NV":0.02,"NC":0.02,"NY":0.06,"CO":0.02,"OR":0.02,"NM":0.01,"UT":0.01,"MI":0.01,"MN":0.01,"IN":0.02,"WI":0.02,"OTHER":0.01},
    "Puebla":            {"CA":0.22,"TX":0.12,"IL":0.06,"AZ":0.02,"FL":0.03,"WA":0.02,"GA":0.03,"NV":0.02,"NC":0.03,"NY":0.25,"CO":0.02,"OR":0.02,"NM":0.01,"UT":0.01,"MI":0.02,"MN":0.02,"IN":0.03,"WI":0.02,"OTHER":0.05},
    "Veracruz":          {"CA":0.20,"TX":0.18,"IL":0.05,"AZ":0.03,"FL":0.05,"WA":0.02,"GA":0.05,"NV":0.02,"NC":0.06,"NY":0.08,"CO":0.02,"OR":0.02,"NM":0.02,"UT":0.01,"MI":0.02,"MN":0.02,"IN":0.03,"WI":0.02,"OTHER":0.10},
    "Hidalgo":           {"CA":0.25,"TX":0.10,"IL":0.04,"AZ":0.02,"FL":0.03,"WA":0.02,"GA":0.02,"NV":0.02,"NC":0.03,"NY":0.22,"CO":0.02,"OR":0.02,"NM":0.01,"UT":0.01,"MI":0.02,"MN":0.02,"IN":0.03,"WI":0.02,"OTHER":0.10},
    "Morelos":           {"CA":0.35,"TX":0.10,"IL":0.08,"AZ":0.03,"FL":0.03,"WA":0.02,"GA":0.02,"NV":0.04,"NC":0.02,"NY":0.08,"CO":0.03,"OR":0.02,"NM":0.01,"UT":0.02,"MI":0.02,"MN":0.02,"IN":0.02,"WI":0.02,"OTHER":0.07},
    "Tlaxcala":          {"CA":0.20,"TX":0.15,"IL":0.06,"AZ":0.02,"FL":0.03,"WA":0.02,"GA":0.02,"NV":0.02,"NC":0.03,"NY":0.20,"CO":0.02,"OR":0.02,"NM":0.01,"UT":0.01,"MI":0.02,"MN":0.02,"IN":0.03,"WI":0.02,"OTHER":0.10},
    "Chiapas":           {"CA":0.28,"TX":0.22,"IL":0.05,"AZ":0.02,"FL":0.08,"WA":0.03,"GA":0.04,"NV":0.02,"NC":0.04,"NY":0.04,"CO":0.02,"OR":0.02,"NM":0.01,"UT":0.01,"MI":0.01,"MN":0.02,"IN":0.02,"WI":0.02,"OTHER":0.05},
    # Yucatán peninsula → CA + FL
    "Yucatán":           {"CA":0.55,"TX":0.08,"IL":0.03,"AZ":0.02,"FL":0.08,"WA":0.02,"GA":0.02,"NV":0.02,"NC":0.02,"NY":0.04,"CO":0.02,"OR":0.02,"NM":0.01,"UT":0.01,"MI":0.01,"MN":0.01,"IN":0.01,"WI":0.01,"OTHER":0.02},
    "Campeche":          {"CA":0.30,"TX":0.20,"IL":0.04,"AZ":0.02,"FL":0.10,"WA":0.02,"GA":0.04,"NV":0.02,"NC":0.03,"NY":0.04,"CO":0.02,"OR":0.02,"NM":0.02,"UT":0.01,"MI":0.01,"MN":0.02,"IN":0.02,"WI":0.02,"OTHER":0.06},
    "Quintana Roo":      {"CA":0.30,"TX":0.20,"IL":0.05,"AZ":0.02,"FL":0.12,"WA":0.02,"GA":0.04,"NV":0.02,"NC":0.03,"NY":0.04,"CO":0.02,"OR":0.02,"NM":0.01,"UT":0.01,"MI":0.01,"MN":0.01,"IN":0.02,"WI":0.02,"OTHER":0.05},
    "Tabasco":           {"CA":0.25,"TX":0.28,"IL":0.04,"AZ":0.02,"FL":0.06,"WA":0.02,"GA":0.04,"NV":0.02,"NC":0.03,"NY":0.04,"CO":0.02,"OR":0.02,"NM":0.01,"UT":0.01,"MI":0.01,"MN":0.02,"IN":0.02,"WI":0.02,"OTHER":0.07},
    # Border / Northern states → TX, AZ, border-adjacent
    "Tamaulipas":        {"CA":0.15,"TX":0.55,"IL":0.03,"AZ":0.03,"FL":0.03,"WA":0.02,"GA":0.03,"NV":0.02,"NC":0.02,"NY":0.02,"CO":0.02,"OR":0.01,"NM":0.02,"UT":0.01,"MI":0.01,"MN":0.01,"IN":0.01,"WI":0.01,"OTHER":0.01},
    "Nuevo León":        {"CA":0.18,"TX":0.50,"IL":0.04,"AZ":0.03,"FL":0.03,"WA":0.02,"GA":0.03,"NV":0.02,"NC":0.02,"NY":0.02,"CO":0.02,"OR":0.01,"NM":0.02,"UT":0.01,"MI":0.01,"MN":0.01,"IN":0.02,"WI":0.01,"OTHER":0.01},
    "Coahuila":          {"CA":0.18,"TX":0.52,"IL":0.04,"AZ":0.03,"FL":0.02,"WA":0.02,"GA":0.03,"NV":0.02,"NC":0.02,"NY":0.02,"CO":0.02,"OR":0.01,"NM":0.02,"UT":0.01,"MI":0.01,"MN":0.01,"IN":0.02,"WI":0.01,"OTHER":0.01},
    "Chihuahua":         {"CA":0.22,"TX":0.40,"IL":0.04,"AZ":0.06,"FL":0.02,"WA":0.02,"GA":0.02,"NV":0.03,"NC":0.02,"NY":0.01,"CO":0.04,"OR":0.02,"NM":0.04,"UT":0.02,"MI":0.01,"MN":0.01,"IN":0.01,"WI":0.01,"OTHER":0.00},
    "Sonora":            {"CA":0.35,"TX":0.10,"IL":0.02,"AZ":0.35,"FL":0.01,"WA":0.03,"GA":0.01,"NV":0.03,"NC":0.01,"NY":0.01,"CO":0.02,"OR":0.02,"NM":0.01,"UT":0.01,"MI":0.01,"MN":0.00,"IN":0.01,"WI":0.00,"OTHER":0.00},
    "Baja California":   {"CA":0.70,"TX":0.05,"IL":0.02,"AZ":0.06,"FL":0.01,"WA":0.03,"GA":0.01,"NV":0.03,"NC":0.01,"NY":0.01,"CO":0.01,"OR":0.02,"NM":0.01,"UT":0.01,"MI":0.00,"MN":0.00,"IN":0.01,"WI":0.00,"OTHER":0.02},
    "Baja California Sur":{"CA":0.65,"TX":0.06,"IL":0.02,"AZ":0.06,"FL":0.01,"WA":0.03,"GA":0.01,"NV":0.04,"NC":0.01,"NY":0.01,"CO":0.01,"OR":0.03,"NM":0.01,"UT":0.01,"MI":0.00,"MN":0.00,"IN":0.01,"WI":0.00,"OTHER":0.04},
    "Sinaloa":           {"CA":0.52,"TX":0.08,"IL":0.03,"AZ":0.12,"FL":0.01,"WA":0.04,"GA":0.02,"NV":0.03,"NC":0.02,"NY":0.01,"CO":0.02,"OR":0.03,"NM":0.01,"UT":0.02,"MI":0.01,"MN":0.01,"IN":0.01,"WI":0.01,"OTHER":0.01},
    "Nayarit":           {"CA":0.50,"TX":0.10,"IL":0.05,"AZ":0.04,"FL":0.01,"WA":0.03,"GA":0.02,"NV":0.03,"NC":0.02,"NY":0.01,"CO":0.03,"OR":0.04,"NM":0.01,"UT":0.02,"MI":0.01,"MN":0.01,"IN":0.02,"WI":0.02,"OTHER":0.03},
    "Colima":            {"CA":0.48,"TX":0.12,"IL":0.05,"AZ":0.04,"FL":0.02,"WA":0.03,"GA":0.02,"NV":0.03,"NC":0.02,"NY":0.01,"CO":0.03,"OR":0.03,"NM":0.01,"UT":0.02,"MI":0.01,"MN":0.01,"IN":0.03,"WI":0.02,"OTHER":0.02},
    "Durango":           {"CA":0.35,"TX":0.20,"IL":0.10,"AZ":0.03,"FL":0.01,"WA":0.02,"GA":0.02,"NV":0.02,"NC":0.02,"NY":0.01,"CO":0.04,"OR":0.02,"NM":0.02,"UT":0.02,"MI":0.01,"MN":0.01,"IN":0.02,"WI":0.02,"OTHER":0.06},
    # Central — CDMX, Edomex, Querétaro (more dispersed profile, closer to national average)
    "Ciudad de México":  {"CA":0.30,"TX":0.18,"IL":0.07,"AZ":0.03,"FL":0.04,"WA":0.02,"GA":0.03,"NV":0.02,"NC":0.03,"NY":0.08,"CO":0.03,"OR":0.02,"NM":0.01,"UT":0.01,"MI":0.02,"MN":0.02,"IN":0.02,"WI":0.02,"OTHER":0.05},
    "Estado de México":  {"CA":0.28,"TX":0.16,"IL":0.08,"AZ":0.03,"FL":0.03,"WA":0.02,"GA":0.03,"NV":0.02,"NC":0.03,"NY":0.10,"CO":0.03,"OR":0.02,"NM":0.01,"UT":0.01,"MI":0.02,"MN":0.02,"IN":0.03,"WI":0.02,"OTHER":0.06},
    "Querétaro":         {"CA":0.30,"TX":0.22,"IL":0.08,"AZ":0.03,"FL":0.03,"WA":0.02,"GA":0.03,"NV":0.02,"NC":0.03,"NY":0.04,"CO":0.03,"OR":0.02,"NM":0.01,"UT":0.02,"MI":0.02,"MN":0.02,"IN":0.03,"WI":0.02,"OTHER":0.03},
}


def fetch_banxico() -> pd.DataFrame:
    fi = int(datetime.datetime(2019, 1, 1).timestamp() * 1000)
    ff = int(datetime.datetime.now().timestamp() * 1000)
    r = requests.get(BANXICO_URL.format(fi=fi, ff=ff), timeout=30,
                     headers={"User-Agent": "Mozilla/5.0 MARCO/banxico_reverse"})
    r.raise_for_status()
    if len(r.content) < 1000:
        raise RuntimeError(f"Banxico returned <1KB: {r.content[:300]!r}")
    tmp = OUT_DIR / "_banxico_raw.xls"
    tmp.write_bytes(r.content)
    raw = pd.read_excel(tmp, header=None, sheet_name="Hoja1")
    tmp.unlink()
    # Row 9 = quarter headers; rows 12..43 = 32 states; row 44 = TOTAL
    headers = raw.iloc[9, 2:].tolist()
    states, rows = [], []
    for i in range(12, 44):
        label = str(raw.iloc[i, 1]).replace(" ", "").replace(" ", "").replace("●", "").strip()
        vals = [float(v) for v in raw.iloc[i, 2:].tolist()]
        states.append(label)
        rows.append(vals)
    df = pd.DataFrame(rows, index=states, columns=headers)
    df.index.name = "mx_state"
    if len(df) != 32:
        raise RuntimeError(f"Expected 32 Mexican states, got {len(df)}")
    return df


def reverse_map(dest: pd.DataFrame) -> pd.DataFrame:
    missing = set(dest.index) - set(SENDER_RATIOS)
    if missing:
        raise RuntimeError(f"Missing sender ratios for: {missing}")
    out = pd.DataFrame(0.0, index=US_STATES, columns=dest.columns)
    for mx_state, row in dest.iterrows():
        w = SENDER_RATIOS[mx_state]
        s = sum(w.values())
        if abs(s - 1.0) > 0.03:
            raise RuntimeError(f"Ratios for {mx_state} sum to {s:.3f}, drift >3%")
        # Normalize so each MX state's weights sum to exactly 1.0 (absorbs hand-tuning rounding)
        for us in US_STATES:
            out.loc[us] += row.values * (w[us] / s)
    out.index.name = "us_state"
    return out


def main() -> None:
    print("Fetching Banxico CE100...", file=sys.stderr)
    dest = fetch_banxico()
    dest_path = OUT_DIR / "banxico_destination_states.tsv"
    dest.to_csv(dest_path, sep="\t", float_format="%.3f")
    print(f"Wrote {dest_path} — {dest.shape[0]} states x {dest.shape[1]} quarters", file=sys.stderr)

    print("Reverse-mapping to US-state senders...", file=sys.stderr)
    implied = reverse_map(dest)
    us_path = OUT_DIR / "us_state_sender_implied.tsv"
    implied.to_csv(us_path, sep="\t", float_format="%.3f")
    print(f"Wrote {us_path} — {implied.shape[0]} US states x {implied.shape[1]} quarters", file=sys.stderr)

    # Sanity: sum(implied) should equal sum(destination minus nothing) per quarter
    for q in dest.columns[-4:]:
        d = dest[q].sum()
        u = implied[q].sum()
        pct = 100.0 * (u - d) / d
        print(f"  {q}: dest={d:,.1f}M  implied={u:,.1f}M  diff={pct:+.2f}%", file=sys.stderr)


if __name__ == "__main__":
    main()
