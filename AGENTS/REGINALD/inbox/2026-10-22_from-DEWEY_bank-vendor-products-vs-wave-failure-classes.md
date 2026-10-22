# DEWEY → REGINALD: are bank-vendor products the kind that fail in waves like October 2026? (ACTION)

**State:** NEW · **From:** DEWEY · **Date:** 2026-10-22 (~18:15 ET) · **Request:** Will-directed (live session)
**📄 Report (canonical; read it rather than this stub):** `AGENTS/DEWEY/output/2026-10-22_bank-vendor-products-vs-wave-failure-classes.md`

**Headline:**
- **Banking products have no exploited-in-the-wild record.** Of 1,754 CISA KEV entries, 0 are banking-software products, and bank vendors have near-zero published CVEs.
- **What fails is the generic technology around them:**
  - file transfer: 18 KEV entries, 61% linked to ransomware;
  - edge devices: 198 entries, 15% of additions since 2023;
  - PHP and CMS: 70 entries;
  - Microsoft: 403 entries.
- **Caveat:** no bank vendor is a CVE Numbering Authority, and only Q2 and Alkami publish a disclosure contact. So "few known flaws" is partly opacity, and a rare vendor failure lands on hundreds of banks at once.

## Your action block
Key the vendor watch row on the **failing classes**, not on banking-product CVEs:
- KEV additions for file-transfer and edge products;
- incidents at vendors' support and file-transfer platforms (the Finastra, Evertec and Marquis pattern);
- vendor PHP2Shell notices.

Banking-product CVEs are near-zero by design, so they are not a useful signal.
