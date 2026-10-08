# Jev opportunities for the research system

October 8, 2026. CATO advice for Will; research and brainstorming authorized. Recommendation: investigate assistance for WALTER's existing novelty/relevance decisions first, with document passage selection second. The benefit sought is less repetitive reading or better coverage at the same effort. Integration and live API testing have not been commissioned.

## Evidence

[TypeSafe's specifications](https://docs.typesafe.ai/models) list Jev 1.13.0 at $0.042 per million input tokens, free output, and text-only input. It returns predefined choices, scores and probabilities. At an assumed 2,000 total billed input tokens per item, 10,000 items cost $0.84 in Jev charges; collection, extraction, retrieval, downstream models and review are additional. This is illustrative arithmetic, not measured system cost.

The [launch post](https://typesafe.ai/blog/introducing-system-one-models-and-jev) describes schema guarantees, which do not establish factual correctness. Its workflow reference answers come from other models. Headline savings should not be projected onto this system.

An [independent September 29 preprint](https://arxiv.org/abs/2609.37647), abstract inspected, reports 346,009 requests across 37 datasets for under $10. It reports weaker fine-grained/noisy labels and rubric judgments, and task-dependent binary thresholds. This is reported external evidence, not CATO replication or a financial-news test. The [vendor's limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13) include numerical/date weaknesses, context distraction, adversarial input and option-order effects. Keep exact comparisons in code and validate each question locally.

## Existing mechanisms

Starting HEAD: `dbc40d0c438298d78a8267228e3e6227500cbedf`, master, initially clean. Relevant sources inspected: `PROME/ROSTER.md` owner rows; WALTER `CLAUDE.md` identity and intake sections; `design/FILTER_SPEC.md` novelty/relevance rules; routing-table ownership. WALTER already owns these judgments. Its rules preserve new developments, changed figures, contradiction and stronger-source confirmation. Existing critical-alert bypasses and owner-state checks must survive.

Local `/home/willi/Research-Intake/scripts/fetch_newsweep.py` and `newsweep_config.py` show headline deduplication and configured queries/keywords. This checkout was not refreshed or certified as live production. Jev cannot recover articles never collected. Source bodies and prior evidence must be supplied for novelty assessment; a headline alone supports preliminary tagging.

## Candidate uses

| Candidate | Proposed behavior | Benefit and limit |
|---|---|---|
| WALTER novelty assistance | Compare an article with retrieved prior signals; separately flag same event, added information, correction, contradiction and stronger source. Suggest recipients independently. | Reduce repeated reading while preserving meaningful updates. No automatic kill or dispatch in a first test. |
| Better document retrieval | Ordinary search selects passages; Jev ranks them against the actual question and returns existing passage IDs. | Shorter exploratory reads with source text preserved. Cannot recover absent candidates or bypass mandatory reads. |
| Filing section triage | Label extracted passages as guidance, liquidity, covenant, refinancing or capex. | Direct DEWEY/domain attention into long documents. Extend existing retrieval; preserve exact numeric parsing. |
| Evidence warnings | Given a claim and cited passage, suggest supported, contradicted or insufficient support. | Flag attribution errors. Cannot authenticate sources or establish external truth; avoid a universal extra review stage. |
| Entity matching | Disambiguate candidate company/ticker/product matches after exact lookup. | Reduce name collisions, retaining unresolved cases. |
| Model/tool routing | Classify bounded requests as lookup, extraction, synthesis or complex investigation. | Secondary candidate; requires repeat work and measured downstream savings. Does not grant authority or launch agents. |
| Research features | Label a fixed public corpus for narrowly defined mentions of financing stress or other evidence. | Exploratory extension. Text labels are not event probabilities or demonstrated predictive signals. |

These are hypotheses, not demonstrated performance. Vendor recipes: [entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment), [reranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe), [citation checking](https://docs.typesafe.ai/cookbooks/citation_check), [intent routing](https://docs.typesafe.ai/patterns/intent-routing). The citation example uses eight constructed cases with four planted failures. The reranking example reports top-ten retrieval improving from 38% to 62% on 40 legal queries; design evidence, not reliable financial-source retrieval established here.

## Proposed first experiment

Use about 150 historical items with only information available at original arrival. Retain public source bodies and short candidate sets of prior signals. Split tuning and held-out evaluation before adjusting questions. Include ordinary items plus difficult cases: repeated headline with a new figure, correction, stronger source, ticker collision, multi-desk relevance, missing body and an important repeated alert. Review historical dispositions rather than treating every past route/kill as truth.

Compare existing rules, Jev suggestions and a small general model on identical inputs. Measure important updates missed, false duplicate suggestions, missing recipients, reviewer reading/time and total downstream effort. A small sample can reject a poor design; it cannot certify rare-miss safety. Pin the model version and retain exact inputs/questions. Failures or abstentions preserve the item for the existing workflow.

Illustrative case: an anonymous refinery-disruption report receives company confirmation. Same event should not mean discard: a separate stronger-source flag should preserve the update for WALTER. Code owns timestamps and known routing constraints; WALTER owns final disposition and transmission implications.

Success means less net review effort while preserving important held-out updates. A critical false duplicate blocks automated suppression. Stop if review/correction effort consumes the saving. Next discussion: select one candidate and refine its test before changing production.

## Verification and delivery limits

No API calls, installations, credentials, owner edits, launches or messages. External results were read, not reproduced. WALTER/TERRY became dirty during the session and were preserved. A startup pull attempt was refused by Git because intervening owner edits existed; no integration occurred. Future pulls require a new separate dirty-tree check.

Verification: weekday checker passed on the readable PROME DOCKET/GATES/WILL_QUEUE, CATO CONTINUITY and this report. Six startup files were readable and below 32,550 bytes: CATO AGENTS 6,465; CHARTER 9,921; CONTINUITY 23,800; root CLAUDE 24,961; USER 5,200; AGENTS 5,313. Generic read-cap returned CANNOT-EVALUATE because CATO has no local CLAUDE.md; direct measurements are separate evidence. Orphan advisory showed only concurrent WALTER paths outside CATO at closeout, left untouched. No ledger, auto-memory or superseded numerical consumer claim changed. Final Git receipt is delivered in-session. No reduced usage, independently validated model performance or trading benefit is claimed.
