# Thinking in Systems — Connections to Our Work

How Meadows' frameworks map to the agent network, trading thesis, and system design.

---

### Hierarchy as Information Compression → Context Optimization
The 31KB→13KB context reduction IS Meadows' principle applied to LLM token limits. Each agent's context window is its information budget. The hierarchy (domain agents → NEXUS → PROME) exists to compress information so no single level is overwhelmed. CARL turns 50 consumer credit signals into one STATUS line. PROME acts on that without knowing every input.

---

### Dense-Within, Sparse-Between → Agent Boundary Validation
CARL's internal links (subprime auto ↔ savings rate ↔ gas prices ↔ DQ rates) are dense — constant mutual reference. CARL↔SAM is sparse — maybe one signal a week. This confirms the boundary is drawn correctly. **Potential issue:** BROCK handles both BDCs and Apollo/Athene insurance plumbing — two subsystems with different internal densities. SHADE was created to resolve this, which is the system self-organizing to fix a boundary problem.

---

### Stable Intermediate Forms → Build History
Codex/Scrolls → single agent → specialized agents → full network with HERMES/NEXUS. Each stage was useful before the next was added. **Live example of misfit:** SHADE — intermediate form not yet stable enough to self-sustain. Needs a minimal viable version that's useful tomorrow.

---

### Purpose Flows Upward → PROME's Role
PROME exists so agents can do their jobs better, not so agents can serve PROME. NEXUS exists to synthesize what agents produce, not to direct what they research. When PROME directly edits agent files → hierarchy inversion → subsystem breaks (see LESSONS.md).

---

### Control–Autonomy Balance → Daily Operations
Too much PROME intervention: agent files overwritten, inbox signals skipped ("already handled it"), agents lose self-regulation. Too little: agents drift (DARWIN stale since Feb 18), RED frozen for a month, no synthesis. The balance shifts constantly. Rule of thumb: PROME coordinates via inbox signals, not direct file edits.

---

### Partial Decomposability → Agent Isolation
Spawning CARL in isolation produces useful work. It doesn't need HAWK or LIQUID to function. When the system degrades, it degrades by subsystem (agents going stale), not by central collapse. This is graceful degradation — a design feature, not an accident.

---

### Open Question: Is NEXUS a Hierarchy Flaw?
Meadows suggests hierarchy should naturally produce synthesis through its information flows. The fact that NEXUS must be spawned periodically to do a separate synthesis pass might mean the between-subsystem communication isn't quite right. Or NEXUS might be the legitimate coordination layer every hierarchy needs. TBD — watch for Meadows on coordination costs.
