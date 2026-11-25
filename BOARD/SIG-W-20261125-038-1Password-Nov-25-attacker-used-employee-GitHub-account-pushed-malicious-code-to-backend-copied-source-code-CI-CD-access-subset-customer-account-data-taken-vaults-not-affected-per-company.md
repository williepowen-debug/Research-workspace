---
signal_id: "SIG-W-20261125-038"
date: "2026-11-25"
timestamp: "2026-11-25T22:05:17Z"
dispatched: "2026-11-25T22:05:17Z"
source: "1password.com/blog/update-on-nov-2026-security-incident; bleepingcomputer.com and techcrunch.com articles of 2026-11-25; X bookmark 2125686942897463547"
origin: ["@exec_sum 15:23 ET 11/25", "1Password official post 11/25 (read by helper)", "BleepingComputer 11/25 16:33 (zone not stated), TechCrunch 11/25 13:49 ET (read by helper)"]
action: ["CYPHER"]
info: ["REGINALD", "SHADE", "VULCAN", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "indicator"
confidence: 0.9
confidence_language: "reports: company post read; unaffected claims are the company's own"
resources: 1
safety_net: "clear"
cluster: "CYBER"
domain: "CYBER"
entities: ["1Password", "GitHub"]
word_count: 270
dispatch_note: "Will-originated bookmark; CYBER row. PRIORITY: supply-chain compromise at a credential vendor, no named bank, core vendor or payment system hit. RED, PROME by BOARD diff."
event_window: "open"
---
# 1Password (company post, Nov 25): an attacker used an employee's GitHub account to push malicious code to its backend and copy source code; account data of a subset of customers was taken; the company says vaults, vault keys and apps were not affected

# 1Password backend breach, read Wed Nov 25

| Point | Fact | Basis |
|---|---|---|
| Post | Official 1Password post dated 2026-11-25; investigating since **November 19** | 1password.com/blog/update-on-nov-2026-security-incident, read by a Rule 9 helper |
| Path | An employee's corporate GitHub account; source code accessed and copied from private repositories; **malicious code pushed to backend services**; access gained to the CI/CD (build and release) system | official post |
| Data taken | Names, emails, account and user IDs, creation and last sign-in times, public keys, SRP parameters, invitation, provisioning and recovery tokens, other metadata, for 'a subset of our customers'. No count given | official post |
| Tokens | Post: a token alone cannot open an account; a 'small number of users' with exposed tokens were notified | official post; BleepingComputer's 'small number of users were affected' is broader than the post |
| Not affected, per the company | vault data and keys, account recovery keys, apps and browser extensions | company statement, not independently verified |
| Not stated | how long the malicious code ran, attribution, customer count, any enterprise named, how the GitHub account was taken | all three texts |

- **Bookmark check:** 'has been hacked' is right as a fact and incomplete as a reading: no vault access is claimed or shown.
- **So what:** 1Password is widely used by businesses (TechCrunch: more than 200,000). The open point is build-system access at a credential vendor; the company says infrastructure secrets were rotated. No named bank, vendor or market effect was found. CYPHER owns the event and any escalation row.
