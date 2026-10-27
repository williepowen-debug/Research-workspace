# Browser-source verification — October 26, 2026

Gartner's October 26 publisher page was browser-readable; direct requests returned HTTP 403. No raw Gartner HTML snapshot is claimed. August fieldwork (1,004 US respondents) supports an intention/affordability finding, not current sales or CARL's assumed population split. URL: https://www.gartner.com/en/newsroom/press-releases/2026-10-26-gartner-marketing-survey-finds-nearly-60-percent-of-us-consumers-have-less-to-spend-this-holiday-season

Edmunds' October 21 primary was read from its publisher insights link. Direct requests returned HTTP 403; no raw HTML snapshot claimed. Its Q3 financed-new-trade-in population and underwater rollover subset are distinct from an all-loan default measure and Cox's negative-equity component. URL: https://www.edmunds.com/car-news/Q3-2026-negative-equity-report.html

CRS browser access failed, but direct original-host requests returned HTTP 200 with PDF magic confirmed. Installed pdfplumber extracted all three pages and identified October 23, 2026, IF13335 VERSION 1 NEW. That retrieval resolves the initial browser-access limit. Original: https://www.congress.gov/crs_external_products/IF/PDF/IF13335/IF13335.1.pdf

pdftotext and fitz/PyMuPDF are missing locally. Installed .venv pdfplumber extracted the saved PDFs successfully. No install or Claude-native tool assumed. SOURCE_MANIFEST.json retains source/derived-file hashes and request times; browser verification and direct downloads remain distinguished.
