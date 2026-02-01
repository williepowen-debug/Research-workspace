# Japanese Source Registry

**Purpose:** Catalog of Japanese-language sources for SAM research with translation workflows.

**Updated:** 2026-01-25

---

## Priority Sources

### Tier 1: Daily (English Bridges)

Sources with English versions or sections that can be monitored directly:

| Source | URL | Coverage | Cadence | Notes |
|--------|-----|----------|---------|-------|
| Nikkei Asia | asia.nikkei.com | Japan markets, BOJ, regional banks | Daily | English version of Nikkei |
| Japan Times | japantimes.co.jp | Politics, BOJ commentary | Daily | English coverage |
| BOJ English | boj.or.jp/en | Official statements, data | Per release | Official translations |
| Reuters Japan | reuters.com/world/asia-pacific/japan | Breaking news | Continuous | Wire service |

### Tier 2: Weekly (Translation Required)

Japanese-language sources requiring AI translation for key articles:

| Source | URL | Coverage | Keywords | Priority |
|--------|-----|----------|----------|----------|
| Nikkei (日経) | nikkei.com | Regional banks, corporate | 地方銀行, 国債, 日銀 | HIGH |
| NHK | nhk.or.jp | Political/BOJ | 金利, 日本銀行, 選挙 | HIGH |
| Shinkin Central Bank Research | scbri.jp | Regional bank analysis | 信用金庫, 地域金融 | MEDIUM |

### Tier 3: Periodic (Translation Required)

In-depth research reports published periodically:

| Source | Type | Frequency | Key Content | Priority |
|--------|------|-----------|-------------|----------|
| BOJ Financial System Report | PDF | Semi-annual (Apr, Oct) | Regional bank exposure quant, JGB stress tests | CRITICAL |
| Life Insurer IR | Web/PDF | Quarterly | Individual company JGB/UST positions | HIGH |
| Regional Bank Disclosures | PDF | Semi-annual | JGB exposure by institution | HIGH |
| GPIF Reports | PDF | Quarterly | Asset allocation changes | MEDIUM |

---

## Japanese Keywords for Monitoring

### Bond Market
| Japanese | Romaji | English |
|----------|--------|---------|
| 国債 | kokusai | Government bonds (JGB) |
| 日本銀行 / 日銀 | nihon ginkou / nichigin | Bank of Japan (BOJ) |
| 金利 | kinri | Interest rate |
| 利回り | mawari | Yield |
| 超長期国債 | chou chouki kokusai | Super-long JGB (30Y, 40Y) |
| 入札 | nyuusatsu | Auction |

### Regional Banks
| Japanese | Romaji | English |
|----------|--------|---------|
| 地方銀行 / 地銀 | chihou ginkou / chigin | Regional banks |
| 信用金庫 | shinkin | Shinkin banks (credit unions) |
| 農林中央金庫 | nourin chuuou kinko | Norinchukin |
| 預金 | yokin | Deposits |
| 含み損 | fukumi son | Unrealized losses |

### Life Insurance
| Japanese | Romaji | English |
|----------|--------|---------|
| 生命保険 | seimei hoken | Life insurance |
| 生保 | seiho | Life insurer (abbrev.) |
| 外債 | gaisai | Foreign bonds |
| 為替 | kawase | Foreign exchange |
| ヘッジ | hejji | Hedge |

### Political
| Japanese | Romaji | English |
|----------|--------|---------|
| 選挙 | senkyo | Election |
| 財政 | zaisei | Fiscal |
| 予算 | yosan | Budget |
| 首相 | shushou | Prime Minister |
| 与党 | yotou | Ruling party |

---

## Translation Workflow

### Step 1: Identify Article

Search Japanese sources using keywords above. Prioritize articles containing:
- Quantitative data (numbers, percentages)
- Named institutions (Norinchukin, specific regional banks, life insurers)
- Policy statements (BOJ, MOF)
- Market reactions (JGB yields, bank stocks)

### Step 2: AI Translation

Use structured prompt for translation:

```
Translate the following Japanese financial news article to English.

CRITICAL INSTRUCTIONS:
1. Preserve all numbers, percentages, and dates exactly as written
2. Preserve all institution names in both Japanese and English (e.g., "農林中央金庫 (Norinchukin)")
3. Preserve all proper nouns (people, companies, places)
4. Use standard financial terminology
5. Flag any ambiguous terms with [?]

After translation, provide:
- SUMMARY: 2-3 sentence summary
- KEY ENTITIES: List of institutions/people mentioned
- KEY NUMBERS: All quantitative data mentioned
- TAGS: Relevant categories (JGB, Regional_Bank, Life_Insurer, BOJ, Political)

Article:
[PASTE JAPANESE TEXT]
```

### Step 3: Log Translation

Record in TRANSLATION_LOG.tsv with:
- Date
- Source
- URL
- Title (translated)
- Summary
- Key entities
- Tags
- Routed To (which agent inbox)

### Step 4: Route Findings

| Content Type | Route To |
|--------------|----------|
| Regional bank losses | SAM + REGINALD |
| JGB/bond market | SAM |
| Life insurer positions | SAM |
| BOJ policy | SAM |
| Funding/liquidity | SAM + LIQUID |
| Political/fiscal | SAM |

### Step 5: Create ML Entry

Log to SAM's ML.tsv with:
- Data quality tag: "TRANSLATED"
- Source reference
- Translation date
- Any confidence caveats

---

## Research Gaps to Fill

| Gap | Source Needed | Status |
|-----|---------------|--------|
| Japan regional bank unrealized losses | BOJ FSR | PENDING - await next report |
| Life insurer JGB/UST breakdown | Individual IR | PENDING |
| Norinchukin CLO position details | Annual report | PENDING |
| Shinkin sector aggregate stress | Shinkin Central research | PENDING |

---

*Japanese Source Registry v1.0 | Created: 2026-01-25*
