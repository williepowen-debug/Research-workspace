# Oracle FQ2 FY27 date — bounded source check, October 25, 2026

TERRY. PRD1 follow-through requested in the committed PROME packet of October 24.
The approved WQ-514 verified-date condition remains binding.

| Source/read method | Observed result | What it establishes |
|---|---|---|
| [Oracle IR FAQ](https://investor.oracle.com/faq/default.aspx), web search index, October 25 | Index identifies December 14, 2026 as the FQ2 FY27 announcement date | An issuer-domain indexed lead; publication time and current rendered answer unverified |
| Same FAQ, direct web open | Navigation and FAQ heading, no dated answer | Direct rendered-text verification failed; no absence claim |
| Same FAQ, direct curl | HTTP 403; 5,425-byte Cloudflare challenge | Access failed; not the FAQ answer |
| [Oracle IR events](https://investor.oracle.com/events-and-presentations/default.aspx), direct web open | Featured/upcoming/archived headings, no dated event | No date verified from this read |
| Search restricted to investor.oracle.com and oracle.com, FQ2 FY27 and December 14 | FAQ lead repeated; returned results did not independently establish a current dated issuer announcement | SEARCH-NOT-FOUND for corroboration, not proof none exists |

Conclusion: **date remains unverified under the card's condition**. December 10
from third-party calendars remains unconfirmed; December 14 remains an indexed
lead. The two saved historical release intervals of about eight days do not bound
other issuer channels and cannot establish that verification must await December.
No waiver, entry, approval expansion or change to the November 20 window or
December 4 time stop. Recheck the issuer at the next card touch.

Local access diagnostic: `/tmp/terry-oracle-faq-20261025.html` (challenge, not
source evidence of the date). Web source/method observations are recorded above;
no screenshot or full browser DOM was available in this runtime.
