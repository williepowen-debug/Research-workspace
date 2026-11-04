> Final parent disposition: ACCEPT of bounded implementation at exact hashes in `runs/2026-11-04_CATCHUP_FIRETIME_REVIEW.md`. Earlier pending/HOLD text below records review sequence; remaining scope limits survive.

# L757 firetime repair — November 4, 2026

Authority: Will's catch-up assignment; parent bounded this work to L757. No owner documents, allowlist, gate registrations or consumer code may change. Runtime Codex/OpenAI, child /root/firetime_repair; exact model UNKNOWN. No Claude tools assumed. Git root /home/willi/Research-workspace. Parent owns pull/commit/push and shared-register delivery.

## Acceptance written before implementation

1. Full slash dates keep their explicit year and cannot be re-parsed as a partial M/D token (production DEWEY Nano report 1/18/2022 and 01/01/2025).
2. Explicit quantity grammar (fraction followed by `of`/`the size`; explicit score label; ratio/rate assignment) is not a date. Same-line independent due dates still alert. Unqualified ambiguous short dates remain eligible.
3. MM/YY and Mon-YY period syntax overlaps real date syntax, including brackets and paired ranges. Leave this part UNIMPLEMENTED rather than guessing from financial words or punctuation. Bracketed/paired and bare short dates remain eligible. L757 cannot be closed whole by this repair.
4. Dated path templates containing the literal YYYY-MM-DD marker are not filesystem assertions; concrete missing paths retain DEAD POINTER. Negated path claims skip only the directly negated token, not an independent missing path beside it. Unquoted extensionless `docs/handoffs` is ambiguous and remains a finding rather than weakening directory coverage.
5. An explicit hexadecimal commit:path artifact is read from its Git blob; its relative pointers resolve in the same historical tree. Missing commit/path remains UNREADABLE. A historical blob cannot be cleared by a similarly named live file. Date drift and current-canon ordering cannot reframe an immutable historical object as a current claim; disclose this scope in output.
6. Existing CLI rc 0/1/2, flag headers and footer grammar stay compatible with PROME/tools/firetime_delta.py. At least one clean and one defective CLI output must be observed. No allowlist rows added.
7. Dedicated tests fail against the original checker and pass against repair. Production false-positive input excerpts and actual Git object inputs exercised. Independent review required before parent publication; this record is not that review.

REVIEW: required — changes date/pointer interpretation and artifact source boundary; scope scripts/firetime_check.py and dedicated tests; reader PENDING; disposition UNVERIFIED-REMEDY.


## Independent review 1 — HOLD, original iteration retained

Parent /root reproduced three counterexamples: pinned operative letter lost its current date/canon checks; repeated relative path after one directly negated occurrence was skipped by line.find; `rate 1/17` silently read as a ratio without assignment. Added all three tests before fixing: 17 tests ran, exactly 3 failures. Initial seven-day observation (74 to 69 flags) belongs to this rejected iteration and is not final acceptance.

POST-REVIEW changes: retain date/current-canon checking for Git blobs, with artifact timestamp drawn from named revision; preserve each quoted-path occurrence through negation handling; require `:` or `=` on rate/ratio/score quantities. These changes await fresh independent acceptance. Original acceptance item 5's historical-only claim is REFUTED: a pinned address does not establish historical-only semantics.


## Result and scope limits

Implemented: slash dates are parsed as complete tokens with their written year; directly attached fraction/assignment grammar is separated from dates; literal date-template paths and directly negated path occurrences are separated from filesystem assertions; hexadecimal Git object artifact references load blobs and resolve relative pointers in the named tree. Date drift still compares pinned content to the current docket, and current canon is compared to the artifact's revision-specific timestamp. No domain source or allowlist changed.

Remaining L757 residue: unqualified `1/5` scores, ambiguous `12/23`, `[12/25]`, `(12/24 → 6/26)` and `Dec-25`, plus extensionless prose `docs/handoffs`. These forms overlap real deadlines/directory references. Tests explicitly preserve their flags. The existing whole-line historical/URL exclusions remain unchanged and retain their old limits; this is not a general parser rewrite. No claim that every date flag is wrong, that all existing dead pointers are fixed, or that L757 is fully complete.

### Reproducible validation

`python3 -m unittest AGENTS.DAEDALUS.scripts.test_firetime_l757 -v`: 17 methods PASS. Includes genuine future dates, unrelated due date beside a quantity, concrete absent paths, repeated relative quoted claims after negation, absent Git path, historical-tree vs working-tree disagreement, and operative dates in a pinned blob. Original implementation (`/tmp/daedalus-firetime-l757-original.py`, with REPO restored to the real root) fails 16 assertions/subtests in the same 17-method suite, rc 1. Temporary Git-tree fixtures never touch the repository index or references.

Real clean CLI: `python3 scripts/firetime_check.py 778ef6a38:PROME/inbox/2026-10-12_from-MIDAS_news-sweep.md 55ee66731:AGENTS/MIDAS/analysis/2026-10-12_MIDAS-news-sweep.md` printed two clean headers and the pinned-scope note, rc 0. Missing-path control `778ef6a38:scripts/L757-absent.md` printed UNREADABLE, one-flag footer, rc 1.

Production full-artifact comparison at October 21 reproduction date against a December 31 control docket: CREED VLY property-comparable report flags 2 → 1 (the directly stated 1/16 fraction removed); DEWEY Nano primary-documents report 11 → 5 (historical M/D/Y fragments removed; real full future 11/30/2026 and 1/12/2027 still candidates); PROME charter 2 → 1 (date template removed, prose directory retained); NEXUS charter 1 → 0 (directly negated invalid PROME home removed). Sources are current working-tree artifacts, not an asserted frozen October 21 source snapshot. The three parent-review changes preserve these specific outcomes; whole-window results below are separately qualified.

### Consumers and read coverage

Consumers inspected: PROME/tools/firetime_delta.py (whole parse/validation functions 1–150) consumes artifact headers, indented flag lines and footer counts; PROME/tools/fleet_dashboard.py:1090–1132 reads nonzero rc. PROME/tools/prome_gate.py:1600 notes retirement from routine boot/closeout and on-demand use. No rc or flag/footer grammar changed. Full-year token cores can now differ: old date-fragment baseline entries must be dispositioned/pruned by PROME using its existing baseline process, not rewritten here. Consumer parser compatibility is checked against the final log below; this is not whole-dashboard certification.

Read coverage: root CLAUDE.md 1–122, AGENTS.md 1–61, USER.md 1–103; DAEDALUS CLAUDE.md 1–138, OPERATIONS.md 1–110; CHECK_STANDARD.md 1–128 (initial truncated prefix recovered at 1–42); UPGRADE_PROTOCOL.md 72–80 review rules; scripts/firetime_check.py 1–522 before edit; PROME/reports/2026-10-21_firetime-boot-flags-disposition.md whole; DOCKET physical L757. Production example line ranges returned and compared to their named text. Root/local AGENTS absence was established by the parent startup; no independent whole-fleet/inbox/profile audit by this repair worker.

Final implementation hashes before independent re-review: scripts/firetime_check.py `41f6554ec59d7374955660f0d11d7f096b34821992c72d7b00dbd8b010ecd092`; dedicated test `3b7e014956597997bf3542c6780c2c42fa8b90912f941248c706aba292d63574`. No source changes after these hashes. REVIEW remains required/PENDING for the POST-REVIEW revision; parent owns acceptance, CHECKS update, packet and publication.


### Final seven-day production comparison

68 cited artifact targets, current working tree and November 4 clock. Original rc 1 / 74 flags; repair rc 1 / 69 flags. Input hashes unchanged across the two runs (68 target locators plus DOCKET/allowlist; Git locators are immutable rather than working-tree files). Consumer firetime_delta.parse parsed 69/69 flag lines and validate returned None (complete consistent rc-1 log). Remaining 69 flags are not individually adjudicated here.

Removed flag cores:
- ('AGENTS/CREED/analysis/2026-09-27_VLY_property_comparable_challenge.md', 'DATE DRIFT', "artifact says 2027-01-16 ('1/16')")
- ('AGENTS/DEWEY/output/2026-10-22_screwworm-cattle-beef-food-cpi.md', 'DATE DRIFT', "artifact says 2027-01-05 ('1/5')")
- ('AGENTS/FLG/reports/2026-09-27_WQ312_Q2_workout_rows.md', 'DATE DRIFT', "artifact says 2027-01-19 ('1/19')")
- ('AGENTS/OTTO/STATUS.md', 'DATE DRIFT', "artifact says 2027-01-25 ('1/25')")
- ('AGENTS/REGINALD/reports/2026-09-27_VLY_CRE_transmission.md', 'DATE DRIFT', "artifact says 2027-01-06 ('1/6')")
- ('PROME/CLAUDE.md', 'DEAD POINTER', '`memory/YYYY-MM-DD.md`')

Added flag cores:
- ('AGENTS/OTTO/STATUS.md', 'DATE DRIFT', "artifact says 2027-01-25 ('1/25/27')")

Input snapshot SHA256 values (working-tree files; NOT_WORKTREE_FILE marks Git object or absent locators):

```json
{
  "AGENTS/BOND/STATUS.md": "b78c31efb748039dafdece13cefb8421bcd9b42b7d14ef0883a98f7e58ad567f",
  "AGENTS/BOND/analysis/2026-08-23_MIDAS-8-19-gold-rates-rederivation.md": "cb53824e7700aabb89f23e6a0dad09be9f78a45af9c0e5fd179a6e168837bba8",
  "AGENTS/BOND/analysis/2026-09-17_PREPRINT_TIPS-R_91282CRE3_SEP-grade_F2-carrier.md": "face4d93d3c6a9245125ce7a38ed2160317de35ea730b6e2cfb10737098da143",
  "AGENTS/CARL/research/2026-10-26_L786/RESULT.md": "abfe426ca1b5b352eab83fc85292ff0355c0a99321d2e560bf9c95dad9fddc98",
  "AGENTS/CORAL/MEMORY.md": "e39aefb66e5bf39bde182bdae30e53d89867f9a36df7181ecb9205424a799049",
  "AGENTS/CORAL/STATUS.md": "018732f6bcdbe5c15ba1c109b77d9b131c7325feeb5a4508fe6ade0cce638692",
  "AGENTS/CREED/analysis/2026-09-27_VLY_property_comparable_challenge.md": "3166c4b6728e09102c4a9b5e87259ad2fecbc04d11f17155e5bf1a61176ffa83",
  "AGENTS/CRUISE/WATCHLIST_NCLH_Q3.md": "a23e3769bd63130b9b0d65910204e5fc55c4918d4737e8d5360840b0c316342c",
  "AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md": "a326afd037cc5e037cd9673a011ad7c21bc5990156f9ae645af6f66576cf90a8",
  "AGENTS/DAEDALUS/profiles/CREED.md": "14d99ac2d62d0aa9820929d9583b528f95d340e531851a05d637daf3c655ab40",
  "AGENTS/DAEDALUS/profiles/FALCON.md": "f748b3672c44d02e0a9d4134067bcb9bc86a7690c251730e737001a718a59a64",
  "AGENTS/DAEDALUS/runs/2026-09-25_INBOX_DISPOSITIONS.md": "ece18c846ef954c23b1e8bac380a8d1c25fa9fd17953521077c9c84676905403",
  "AGENTS/DAEDALUS/runs/2026-10-30_CREED_REFRESH.md": "9cf667ec0143051c98f0f435d72bda9388a96d3b8df42b0fa8fb8ecd60f5a806",
  "AGENTS/DAEDALUS/runs/2026-10-30_FALCON_REFRESH.md": "bf49363738f92aabefcc8215a1851cdd453022593e7f7d46c440f2ecbe71fbec",
  "AGENTS/DAEDALUS/runs/2026-10-30_WIRING_SWEEP_17_RUN4.md": "f578f9c6c3275b2afd6d5478b8e4194ef4f54d948be03a773f8d4dbc03833a15",
  "AGENTS/DEWEY/output/2026-10-22_screwworm-cattle-beef-food-cpi.md": "a7e53adbfae3a6d466ad88e5e096339ae440cd54ac0802a91d2b888a3b34129c",
  "AGENTS/DEWEY/output/2026-10-23_dewey-research-history-meta-review.md": "eb8ba2c4945d22609934acc444d45e2850ad335a6f033a3c0de543c2c0ad1cee",
  "AGENTS/FLG/reports/2026-09-27_WQ312_Q2_workout_rows.md": "1f6a8d44a0a9bdf2a8cbea4e01e6e10bcf20e7a3fcc0cd2d2d41759583cd6979",
  "AGENTS/GIBBS/research/2026-10-21_five-things-regional-question.md": "224970d8dd10fd1b2c0232b9b4680ef24d67f02be756a4636771f857524d552a",
  "AGENTS/HENRY/domain/ECON_CALENDAR.md": "e0d9d6bbca59f8f1cfa7ff58bcc42529aaa07ccb9d189f03920f0aa1d8ec1500",
  "AGENTS/LABOR/docket/GRADING_CARD_20261105_Challenger.md": "8aaf45e47b2c9c35bbcb0a754cb3519e280f9999c02cc9e3cffad5838c9a76ef",
  "AGENTS/LABOR/docket/GRADING_CARD_20261106_NFP.md": "e3b582f96e6b4cd303494c103397c5fbc292580e381622c032fada4423ee1558",
  "AGENTS/MIDAS/gold/research/2026-10-23_WQ451-decomposition-letter.md": "c41c635417f40e66b963ce33a903ab6b5225a93e59977e3a84c8f7df62e316ea",
  "AGENTS/NEXUS/PREDICTIONS_MONITOR.md": "b8163aab7fab62aaa5a0e3f890243e9c50fa1eeaa64a93af672c151bd12cff79",
  "AGENTS/NEXUS/STATUS.md": "0e6f8f0bc4dfbc5a0aa3fda3249149240c04415bbe13b14bd021653bffae9f9f",
  "AGENTS/NEXUS/research/2026-10-08_disc-J_letters.md": "3e8f80f221bcd1f4680ade778b00fcc87326064b26e6a98718d5417b310116d4",
  "AGENTS/NEXUS/research/2026-10-19_WQ459_guarded_HY_letter.md": "478005fe1018a99928fb03bc160fcf52a7253fdcbd3bbbcebaa188b1c5935843",
  "AGENTS/ORACLE/SCHEDULED_RUNS.md": "0bc8c9856ec57aab039cb4e433fc75ce8cff691d40fa5abff19d7b7b9891f6f9",
  "AGENTS/OTTO/STATUS.md": "73bc8e2064b5d156e7bc3b0ce41c806bf8de2d5c2b8b1c754c543c2a531011ea",
  "AGENTS/OZK/CALENDAR.md": "eece32024831e884474f4926fb7b0dc04b12f786244cfde8d12512514f2ba4f6",
  "AGENTS/OZK/reports/2026-10-21_self-sweep.md": "1680ad6775d7d64a9b14d186b7fb1499a1af790362fe879c8abffcc455594e4c",
  "AGENTS/OZK/research/threads/2026-10-01_SUBNOTES_RESET.md": "843cffeb575c7d16310b01367db4a6da5179051d6bad96fc9653647ed4f18c27",
  "AGENTS/REGINALD/CALENDAR.md": "122917ad6a6c584e0250fbec8e287a326284fd02108e1ca8f4355fffce143b14",
  "AGENTS/REGINALD/registry/NOTES.md": "a948f6710fb5b1f8b70c4c8ce84aa3cb5d2bdcc5840008eb9e0f54841a058586",
  "AGENTS/REGINALD/reports/2026-09-27_VLY_CRE_transmission.md": "09758fb2938b4ea603bc13c9e0d04121626de4deaa32bd32cea41bd45061e4ed",
  "AGENTS/REGINALD/reports/2026-10-31_L857/REPORT.md": "8b1822ab88650ca12bee15e27e807b371db4afd4f28b9874fa79a6d1ff7e3191",
  "AGENTS/TERRY/setups/UNG_jan15-10-12C_polar-vortex-break_2026-10-31.md": "21573e3d3828555e46ef11fdc505a07d8551735cd4ffad4ced5f1e3f7cbd6d42",
  "AGENTS/VULCAN/workbook/GPU_INSTRUMENT_SPEC.md": "7455a4b14f99efcefbf632c9cd69d088ddb641b1d44ad4769b854418f1736e14",
  "AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md": "31b519e21600ef145130be11d08634026cce9b82ba7e4775b01821f42c70e06c",
  "AGENTS/WATT/reports/2026-10-29_WATT_SWEEP.md": "8f205b8fa57b5a3c146aca345e363e0ef39735e095a1d82fcce4d8b0e3ec4924",
  "AGENTS/_NETWORK.md": "3ec35c767c6252a52db4ab1317c944767292c644993cd10e03276d2131389702",
  "AGENTS/{VULCAN,HAWK}/inbox/2026-09-18_from-ZHAO_the-other-half-of-the-clock-chinas-own-restraint-expires-11-10.md": "NOT_WORKTREE_FILE",
  "FORUM/2026-08-07_system-review/08_dissent/05_TERRY_capitals-case.md": "f30271ec8bb65851160713f43f4fd90d38c88f596ce8f8fb953f48cd846ee501",
  "PROME/CLAUDE.md": "8ed66e427d264a0f212c42cc1fa220f95bffd752301952a47b379d819cb34e27",
  "PROME/MACHINE_LOCAL.md": "a8b7a2f44801ad5c02cd68942c35cb8ad539b246c7751a1687e546bb85b38a01",
  "PROME/ROSTER.md": "95fac42caf9b350ffe75be78e66eaa3a010a7d688a602551c044f58f06aa18a1",
  "PROME/WILL_QUEUE.md": "40558337bfb22fdcde0d413c786b8635cd2e9a19295c1d07a3c83b850599488f",
  "PROME/inbox/2026-10-01_from-NEXUS_resolver-grades-and-wake-dates.md": "e4b42a426069a7297380a70201e0b97da4edd4cb5ebf791cdf18c98b53952953",
  "PROME/inbox/processed/2026-09-25_from-DAEDALUS_L290-render-4-inbox-drain-wq295-doorbell-close.md": "96e147fd6f2bcdfb734d8ef4ba83b06357d4349649d9056b6f6971c37b5e35b2",
  "PROME/inbox/processed/2026-10-01_from-FERT_wake-coverage-ask-ride-alongs-plus-CF-Q3-row.md": "2f1eadb2049e18a482eb37371e1e0aca0efaf0d1c1020095ca4998090e526cf7",
  "PROME/inbox/processed/2026-10-01_from-NEXUS_charter-fix-ef23c5351-and-L572-redate.md": "3fe42945278a24c19ae9bfca39b76b02351dee754f7756a3a03bdbedd7e4611f",
  "PROME/inbox/processed/2026-10-08_from-VULCAN_L250-graded-compute-futures-not-trading.md": "f292f988b611488617a5b67c24727058a30974ac0e29c3df3c102bd6ef0ea24b",
  "PROME/inbox/processed/2026-10-21_from-MARCO_catchup-wave3.md": "9426d648b6f85240ee818687304ff7285c2b5fb7ab5c4256e3ff5666cdb6f434",
  "PROME/inbox/processed/2026-10-30_from-DAEDALUS_creed-profile-refresh.md": "56f7f064847ada821449d6047959d57983a963ec52809495f336fa768b8cb07b",
  "PROME/inbox/processed/2026-10-30_from-DAEDALUS_falcon-profile-refresh.md": "9d1a7237275c17e12adbd5fd43ed925a8528a494dae2a9d153e05c253fadad33",
  "PROME/inbox/processed/2026-10-30_from-DAEDALUS_wiring4-wal-check10.md": "2924fab47699034069c08be4f3e693d1c69d3b5fc45bf932a16eb8585ce70faf",
  "PROME/inbox/processed/2026-10-31_from-REGINALD_L857-shortlist-rerun.md": "4ac20185becbd80112ba7d35e9378945717d2b3566befba4f18e0896fa590eb4",
  "PROME/inbox/processed/2026-11-02_from-BROCK_L794-crmt-ninth-bridge-drain7.md": "dbba6ad563105a9a7b8aef9e8153270637e71ccf44ba5dad8eec8473ba4f4aa8",
  "PROME/proposals/2026-09-03_codex-workspace-audit-RECORD.md": "4b5fae1d9d88f7abac8a8eadde3fab9d6d4d2c61d152928096f8bfd3c4702799",
  "PROME/proposals/2026-10-23_wq513-516-RULED.md": "e07e7dfa3d7f65271863c3d1d3f94bbfaab29387758ec1b4fed8d14f171a8a93",
  "PROME/proposals/2026-10-30_wq560-RULED.md": "81e3baf6a2e6c752822e4d6cbbad562696d32d8ff606b45b3629df6e1d17616d",
  "PROME/proposals/2026-11-02_wq559-RULED.md": "005116a89dc94065ffbdbbfdfa9cbcd9530acd2efbeb39a4dcb25b0b5d71d6e1",
  "PROME/proposals/2026-11-02_wq589-RULED.md": "e328f4823402b0d46bbccf882552bdc50c2741090c40e49a22e0ace72db8172c",
  "PROME/reports/2026-10-24_L796-pin-counterexample-read3.md": "f9f3fc97c77bdfc1b77baec5f74d96144d05e1b1d61fdfa48c1d4c4ddc0fed05",
  "PROME/themes/ellison/theses/2026-10-22_ellison-collateral-loop.md": "bec02795f2384450ce1ef287070c0d47cb3da5de889d29bd6da4798451f507f5",
  "PROME/tools/tests/ACCEPTANCE_claim_check_glued_2026-10-30.md": "93c03b41c13787177c80bb5636afe796c257b06489c02ddfa83f4f7ef1812f75",
  "PROME/tools/tests/ACCEPTANCE_closeout_gate_perimeter_pin_2026-10-24.md": "72c2ed47fbb37953256a62cf6ab7b00b618db16490bd6f522b52f1bed502c5f2",
  "scripts/AGENT_LAUNCHER.md": "a7a36b4dbd24150a3d56207caa965300e2d5036f3cd6cfe56aa59bd40470f9dc",
  "PROME/DOCKET.tsv": "fbb29fd302aea0e754763c520df82590cca22f58b6bcf7d011354cd992acdc59",
  "scripts/firetime_allowlist.tsv": "ebf56e8691daa0e915c26eb67e82d7920fdcc3aebea159ae55cf50680f38bfde"
}
```
