#!/usr/bin/env python3
"""Fixture tests for absee_office_screen.py. Run: python3 test_absee_office_screen.py"""
import datetime as dt
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import absee_office_screen as s  # noqa: E402

XML = """<?xml version="1.0" encoding="utf-8"?>
<assetData xmlns="http://www.sec.gov/edgar/document/absee/cmbs/assetdata">
 <assets>
  <assetNumber>1</assetNumber>
  <originationDate>03-01-2019</originationDate>
  <originalLoanAmount>50000000.0</originalLoanAmount>
  <maturityDate>03-06-2029</maturityDate>
  <hyperAmortizingDate>03-06-2027</hyperAmortizingDate>
  <loanStructureCode>A1</loanStructureCode>
  <property>
   <propertyName>One Test Plaza</propertyName>
   <propertyCity>Los Angeles</propertyCity>
   <propertyState>CA</propertyState>
   <propertyZip>2141</propertyZip>
   <propertyTypeCode>OF</propertyTypeCode>
   <netRentableSquareFeetNumber>100000</netRentableSquareFeetNumber>
   <largestTenant>Acme &amp; Co</largestTenant>
   <squareFeetLargestTenantNumber>60000</squareFeetLargestTenantNumber>
   <leaseExpirationLargestTenantDate>12-31-2026</leaseExpirationLargestTenantDate>
   <mostRecentAnnualLeaseRolloverReviewDate>12-31-2025</mostRecentAnnualLeaseRolloverReviewDate>
   <mostRecentDebtServiceCoverageNetCashFlowpercentage>1.10</mostRecentDebtServiceCoverageNetCashFlowpercentage>
   <mostRecentPhysicalOccupancyPercentage>.85</mostRecentPhysicalOccupancyPercentage>
   <valuationSecuritizationAmount>100000000</valuationSecuritizationAmount>
   <DefeasedStatusCode>N</DefeasedStatusCode>
  </property>
  <reportPeriodEndActualBalanceAmount>49000000.0</reportPeriodEndActualBalanceAmount>
  <paymentStatusLoanCode>0</paymentStatusLoanCode>
 </assets>
 <assets>
  <assetNumber>2</assetNumber>
  <maturityDate>01-06-2030</maturityDate>
  <property><propertyName>Paid Off</propertyName><propertyTypeCode>OF</propertyTypeCode></property>
  <reportPeriodEndActualBalanceAmount>.00000000</reportPeriodEndActualBalanceAmount>
 </assets>
</assetData>"""

FILING = (
    "ABS ASSET CLASS:             \tCommercial mortgages\n<DOCUMENT>\n<TYPE>ABS-EE\n<TEXT>x</TEXT>\n"
    "</DOCUMENT>\n<DOCUMENT>\n<TYPE>EX-102\n<SEQUENCE>2\n<FILENAME>exh_102.xml\n<TEXT>\n<XML>\n"
    + XML
    + "\n</XML>\n</TEXT>\n</DOCUMENT>\n"
)
PERIOD = dt.date(2026, 10, 13)


def row(**over):
    asset = next(s.parse_assets(XML))
    base = s.loan_record(asset, "T1", PERIOD)
    base.update(over)
    return base


class Parsing(unittest.TestCase):
    def test_header_class(self):
        self.assertEqual(s.header_value(FILING, "ABS ASSET CLASS"), s.CMBS_CLASS)

    def test_extract_and_entity(self):
        assets = list(s.parse_assets(s.extract_ex102(FILING)))
        self.assertEqual(len(assets), 2)
        self.assertEqual(assets[0]["properties"][0]["largestTenant"], "Acme & Co")

    def test_zero_balance_dropped(self):
        assets = list(s.parse_assets(XML))
        self.assertIsNone(s.loan_record(assets[1], "T1", PERIOD))

    def test_zip_restores_leading_zero(self):
        self.assertEqual(row()["zip"], "02141")

    def test_blank_stays_blank(self):
        self.assertIsNone(s.parse_num(""))
        self.assertIsNone(s.parse_date(""))
        self.assertIsNone(s.parse_date("13-45-2026"))


class Maturity(unittest.TestCase):
    def test_ard_beats_contract(self):
        self.assertEqual(
            s.effective_maturity({"maturityDate": "03-06-2029", "hyperAmortizingDate": "03-06-2027"}),
            (dt.date(2027, 3, 6), "ARD"),
        )

    def test_modified_replaces_contract(self):
        self.assertEqual(
            s.effective_maturity(
                {"maturityDate": "03-06-2027", "postModificationMaturityDate": "03-06-2029"}
            ),
            (dt.date(2029, 3, 6), "MOD"),
        )

    def test_ard_after_legal_does_not_count(self):
        self.assertEqual(
            s.effective_maturity({"maturityDate": "03-06-2027", "hyperAmortizingDate": "03-06-2029"}),
            (dt.date(2027, 3, 6), "CONTRACT"),
        )


class Status(unittest.TestCase):
    def test_delinquent_codes(self):
        for code in "1235":
            self.assertTrue(s.is_delinquent_status(code))
        for code in ("0", "A", "B", "4", "", None):
            self.assertFalse(s.is_delinquent_status(code))

    def test_open_special_servicing(self):
        d1, d2 = dt.date(2026, 1, 1), dt.date(2026, 6, 1)
        self.assertTrue(s.in_special_servicing({"ss_transfer": d1, "ss_return": None}))
        self.assertTrue(s.in_special_servicing({"ss_transfer": d2, "ss_return": d1}))
        self.assertFalse(s.in_special_servicing({"ss_transfer": d1, "ss_return": d2}))
        self.assertFalse(s.in_special_servicing({"ss_transfer": None, "ss_return": None}))


class Pieces(unittest.TestCase):
    def test_same_loan_two_trusts_groups_and_adds(self):
        a, b = row(trust="T1", balance=40e6), row(trust="T2", balance=60e6)
        groups = s.piece_groups([a, b])
        self.assertEqual(len(groups), 1)
        self.assertEqual(sum(r["balance"] for r in groups[0]), 100e6)

    def test_nra_key_joins_when_origination_differs(self):
        a = row(origination=dt.date(2019, 3, 1))
        b = row(origination=dt.date(2019, 3, 4))
        self.assertEqual(len(s.piece_groups([a, b])), 1)

    def test_two_buildings_one_origination_stay_apart(self):
        a, b = row(nra=179604.0), row(nra=70040.0)
        self.assertEqual(len(s.piece_groups([a, b])), 2)

    def test_merge_takes_freshest_tenant_and_adds_dollars(self):
        old = row(balance=40e6, lease_end=dt.date(2023, 9, 30), review=dt.date(2023, 1, 1))
        new = row(balance=60e6, lease_end=dt.date(2035, 2, 28), review=dt.date(2025, 12, 31))
        merged = s.merge_group([old, new])
        self.assertEqual(merged["balance"], 100e6)
        self.assertEqual(merged["lease_end"], dt.date(2035, 2, 28))
        self.assertTrue(merged["lease_disagreed"])

    def test_blank_lease_never_overrides(self):
        blank = row(lease_end=None, review=dt.date(2026, 6, 30))
        dated = row(review=dt.date(2025, 12, 31))
        self.assertEqual(s.merge_group([blank, dated])["lease_end"], dated["lease_end"])

    def test_one_bad_piece_marks_the_loan(self):
        merged = s.merge_group([row(status="0"), row(status="3")])
        self.assertEqual(s.status_resolved(merged), "DELINQUENT")
        self.assertFalse(s.is_performing(merged))

    def test_special_servicing_on_one_piece_marks_the_loan(self):
        merged = s.merge_group([row(), row(ss_transfer=dt.date(2026, 5, 1))])
        self.assertFalse(s.is_performing(merged))


class DuplicateTapes(unittest.TestCase):
    def tape(self, trust, n=10, year=2021, offset=0):
        out = []
        for i in range(n):
            out.append(row(trust=trust, asset=str(i), balance=1e6 + i + offset, name=f"L{i}",
                           origination=dt.date(year, 1, 1)))
        return out

    def test_full_match_flags_the_trust_whose_year_outruns_the_tape(self):
        rows = self.tape("BANK 2021-BNK36") + self.tape("BANK 2022-BNK40")
        self.assertEqual(s.find_duplicate_tapes(rows), {"BANK 2022-BNK40": "BANK 2021-BNK36"})

    def test_a_few_shared_notes_do_not_flag(self):
        rows = self.tape("Deal 2021-A") + self.tape("Deal 2021-B", offset=500)
        rows += [row(trust="Deal 2021-B", asset="0", balance=1e6, name="L0")]
        self.assertEqual(s.find_duplicate_tapes(rows), {})


class StatusResolution(unittest.TestCase):
    def test_blank_code_current_when_paid_up(self):
        self.assertEqual(s.status_resolved(row(status="", paid_through=dt.date(2026, 10, 11))), "CURRENT")

    def test_blank_code_unknown_when_paid_long_ago(self):
        got = s.status_resolved(row(status="", paid_through=dt.date(2024, 6, 6)))
        self.assertEqual(got, "UNKNOWN")
        self.assertFalse(s.is_performing(row(status="", paid_through=dt.date(2024, 6, 6))))

    def test_blank_code_and_no_date_is_unknown(self):
        self.assertEqual(s.status_resolved(row(status="", paid_through=None)), "UNKNOWN")

    def test_partial_defeasance_code_is_ip(self):
        self.assertTrue(s.is_defeased(row(defeased="IP")))
        self.assertFalse(s.is_defeased(row(defeased="X")))

    def test_different_loans_stay_apart(self):
        a = row()
        b = row(zip="90071", origination=dt.date(2018, 1, 1), nra=5.0)
        self.assertEqual(len(s.piece_groups([a, b])), 2)

    def test_two_loans_on_one_building_stay_apart(self):
        a = row(origination=dt.date(2016, 12, 30), contract_maturity=dt.date(2027, 1, 6))
        b = row(origination=dt.date(2020, 8, 6), contract_maturity=dt.date(2030, 8, 6))
        self.assertEqual(len(s.piece_groups([a, b])), 2)

    def test_blank_zip_never_joins(self):
        self.assertEqual(len(s.piece_groups([row(zip=""), row(zip="")])), 2)


class Screen(unittest.TestCase):
    def test_hit_uses_ard_and_reports_share(self):
        flags = s.screen_row(row())
        self.assertTrue(flags["before_maturity"])
        self.assertAlmostEqual(flags["share"], 0.6)
        self.assertTrue(flags["thin_dscr"])
        self.assertFalse(flags["thin_occ"])
        self.assertTrue(flags["fresh"])

    def test_ard_can_clear_a_contract_hit(self):
        # Lease ends 2028: before the 2029 legal date but after the 2027 ARD.
        flags = s.screen_row(row(lease_end=dt.date(2028, 1, 1)))
        self.assertFalse(flags["before_maturity"])

    def test_blank_dscr_is_not_thin(self):
        self.assertFalse(s.screen_row(row(dscr=None))["thin_dscr"])

    def test_stale_review(self):
        self.assertFalse(s.screen_row(row(review=dt.date(2024, 1, 1)))["fresh"])
        self.assertFalse(s.screen_row(row(review=None))["fresh"])

    def test_summary_counts_every_row_once_at_top(self):
        rows = [row(), row(lease_end=None), row(maturity=dt.date(2026, 1, 1), lease_end=dt.date(2025, 1, 1))]
        out = s.summarize(rows)
        self.assertEqual(out["book"][0], 3)
        self.assertEqual(out["not testable"][0], 1)
        self.assertEqual(out["already past maturity"][0], 1)
        self.assertEqual(out["forward book"][0], 1)
        self.assertEqual(out["share>50"][0], 1)
        self.assertEqual(out["hit 2027"][1], row()["balance"])
        self.assertEqual(out["share>30 thin 2027"][0], 1)

    def test_refi_window_is_separate_from_the_hit(self):
        just_after = row(lease_end=dt.date(2027, 9, 1))  # effective maturity 2027-03-06
        flags = s.screen_row(just_after)
        self.assertFalse(flags["before_maturity"])
        self.assertTrue(flags["refi_window"])
        out = s.summarize([just_after])
        self.assertEqual(out["window share>30 thin 2027"][0], 1)
        self.assertNotIn("hit", out)

    def test_lease_far_past_maturity_is_in_neither_cut(self):
        flags = s.screen_row(row(lease_end=dt.date(2039, 1, 1)))
        self.assertFalse(flags["before_maturity"] or flags["refi_window"])

    def test_stale_tenant_data_never_reaches_the_hit_count(self):
        out = s.summarize([row(review=dt.date(2023, 1, 1))])
        self.assertEqual(out["stale tenant data"][0], 1)
        self.assertNotIn("hit", out)


if __name__ == "__main__":
    unittest.main()
