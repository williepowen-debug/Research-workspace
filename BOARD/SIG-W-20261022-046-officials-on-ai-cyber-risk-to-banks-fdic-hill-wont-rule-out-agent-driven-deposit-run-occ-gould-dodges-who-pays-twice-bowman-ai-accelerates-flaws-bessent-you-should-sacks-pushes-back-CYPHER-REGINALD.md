---
signal_id: "SIG-W-20261022-046"
date: "2026-10-22"
timestamp: "2026-10-23T01:05:22Z"
dispatched: "2026-10-23T01:05:22Z"
source: "WALTER"
origin: "WALTER search on Will's ask (20:57 ET: 'anyone in the Trump admin or surrounding individuals discussing AI/cyber threats on banks'); Will said route it (21:04 ET). Read at the outlet before dispatch: Banking Dive 10/21 (Hill), American Banker 10/22 (Gould), PYMNTS 9/29-30 (Bowman), PYMNTS 5/3 (Bessent). Others from search summaries."
domain: "CYBER"
cluster: "BANK_COLLATERAL"
action: ["CYPHER", "REGINALD"]
info: ["GIBBS", "CARL", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.75
confidence_language: "four statements read at the reporting outlet; Hill's 10/1 bank-run line is a Bloomberg video headline; Sacks and the joint regulator inquiry are weak secondaries"
resources: 9
safety_net: "clear"
word_count: 420
entities: ["Travis-Hill", "FDIC", "Jonathan-Gould", "OCC", "Michelle-Bowman", "Federal-Reserve", "Scott-Bessent", "Treasury", "Jerome-Powell", "David-Sacks", "Andrew-Bailey", "Mythos", "Reg-E"]
event_window: "closed"
dispatch_note: "None of these statements was on the BOARD (grep -i on each name with AI/cyber/agent, Aug-Oct). The open policy gap is liability: who pays when an AI agent moves a customer's money."
---
# What US officials are saying about AI and cyber risk to banks: the bank supervisors treat it as live this fall, and the FDIC chair won't rule out AI agents speeding a deposit run. The OCC head twice declined to say who pays when an agent moves a customer's money, and the White House AI adviser is pushing back on the alarm

| When | Who | What they said | Basis |
|---|---|---|---|
| 10/20 (and 10/1) | **FDIC Chair Travis Hill** | AI agents moving deposits are "the big thing that we're thinking about"; "to what extent are depositors going to delegate that type of decision-making authority to these types of agents?" On 10/1 he **would not rule out agentic-AI bank-run risk** | Banking Dive 10/21, read; 10/1 = Bloomberg video headline |
| 10/22 week | **Comptroller Jonathan Gould** (Fox Business) | "The banks have been all over this for months now, fortifying their defenses"; "Banks are some of the most fortified parts of our system". **Asked twice whether customers get their funds back after an unauthorized agent transfer: no answer** | American Banker 10/22, read |
| 10/22 | **David Sacks** (White House AI and crypto adviser; current role unclear) | Customers delegating credentials to agents is not a cyberattack; linking the two needlessly alarms the public | weak secondary of an X post |
| Oct | **Fed, OCC, FDIC** | Reportedly asking banks about Chinese-built AI, AI agents in cyber defense, and kill switches; all declined comment | weak secondary |
| 9/29 | **Fed Vice Chair for Supervision Michelle Bowman** (Denver community-bank cyber workshop) | AI can "accelerate vulnerability identification, create sophisticated social engineering campaigns"; the Fed will "tailor our approach to IT examinations" | PYMNTS, read |
| 5/3 | **Treasury Secretary Scott Bessent** (Fox) | Should Americans worry about AI hacking their bank accounts? **"You should."** "a step change in the power of one large language model" | PYMNTS, read |
| 4/7 | **Bessent and Fed Chair Powell** | Unannounced Treasury meeting with Citi, Morgan Stanley, BofA, Wells, Goldman CEOs on Anthropic's Mythos | several outlets |

**Why it matters:**
- **REGINALD:** Hill names the deposit-flight mechanism (agents moving deposits), the same channel as 036's "Fear 3". The live question is size, not existence.
- **CYPHER:** the liability gap is a candidate marker for Will's "bank money problem" prediction (packet d9b5c12d9). Under Reg E an agent the customer authorized mostly leaves the loss with the customer; a regulator moving it onto banks would change that.
- **The split:** bank supervisors are warning, while the White House AI adviser frames agent access as customer choice. If that framing holds, it argues against new bank liability.

**Do not relay as:** "the FDIC warns of an AI bank run" (he would not rule it out; he called its size an open question) · "Bessent says banks will be hacked" (he answered a question about worry).

**ACTION:** CYPHER (ledger as regulator-stance context; your row 5 fires only on supervisory-concern statements, and none of these is one) · REGINALD (deposit-flight channel). **INFO:** GIBBS (large banks named at the April meeting), CARL (consumer liability under Reg E). RED and PROME by BOARD. No trade is implied.
