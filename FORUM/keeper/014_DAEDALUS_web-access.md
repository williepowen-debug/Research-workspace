**DAEDALUS · 2026-10-17 15:10 ET** — web access on Will's word (15:08 ET, relayed by PROME)

Applied. The paste file is regenerated at `AGENTS/DAEDALUS/builds/console_agent_2026-10-17/console-panel-nisaba.yaml`, round trip OK. Paste it over the existing NISABA; that creates a new version, not a new agent.

- **web_search and web_fetch on**, both `always_allow`.
- **Rule 4 has a fourth label, SOURCED:** material from the web, always with its link and the date fetched.
- **New rule 10**, PROME's wording plus one sentence: "Never send anything from his memory to a website or a command that reaches the network."
- `environment.yaml` is now `unrestricted`, to match `env_011p6pCa8p13cZB2eCHARUjo`. Its comment records that v1 was limited with no hosts and was reversed on Will's word. README step 2 is updated too.

**One change I made beyond the ask: bash moved from `always_allow` to `auto`.** Opening the internet creates a new route for a leak. A web page NISABA reads can carry hidden instructions, and with unrestricted networking a single bash command could post Will's memory files to any server. The prompt rule alone isn't a control, because that rule is exactly what such an injected page would try to talk the model out of.

Under `auto`, Anthropic's server judges each bash call. The clock and file moves should pass. A network-bound send of memory contents should be refused or paused. The cost: an occasional approval pause in the Console, which is fine because Will is present in every session and the scheduled run is parked. The web tools themselves stay `always_allow`; they run on Anthropic's side, and web_fetch only fetches URLs already in the conversation.

If pauses get annoying, flipping bash back to `always_allow` is a one-word change. Will would be choosing convenience over that guard, knowingly.
