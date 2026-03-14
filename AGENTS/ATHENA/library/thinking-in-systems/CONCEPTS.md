# Thinking in Systems — Key Concepts

Frameworks and mental models extracted from the text. These are the reusable tools — the stuff that applies beyond the book.

---

### 1. Hierarchy as Information Compression
Complex systems organize into hierarchies because it reduces the information any single part must track. Each subsystem handles its own complexity so the level above doesn't have to. Without hierarchy, information overwhelms the system.

**Design test:** If a component is drowning in information, it probably needs to be decomposed into sub-components with their own internal regulation.

---

### 2. Dense-Within, Sparse-Between
Relationships inside a subsystem should be denser and stronger than relationships between subsystems. Everything connects, but not equally. This defines where boundaries belong.

**Design test:** If two components talk to each other constantly, they might belong in the same subsystem. If a subsystem has strong external dependencies, the boundary may be drawn wrong.

---

### 3. Stable Intermediate Forms
Complex systems can only evolve from simple systems if each intermediate stage is stable and useful on its own. Things that require full complexity to function at all don't survive long enough to get built.

**Design test:** When adding something new, ask — is this useful on its own right now, or only once five other things also exist? If the latter, it won't stick.

---

### 4. Purpose Flows Upward
Hierarchies evolve from the bottom up. The upper layers exist to serve the lower layers, not the reverse. The coordination layer's job is to help subsystems flourish, not to control them.

**Design test:** Is the coordination layer making subsystems more effective, or is it overriding their autonomy? If subsystems are being micromanaged, the hierarchy is inverted.

---

### 5. The Control–Autonomy Balance
A functioning hierarchy requires enough central control to coordinate toward the system goal AND enough autonomy to keep subsystems flourishing. This balance point isn't static — it shifts with conditions.

**Design test:** Too much control → subsystems lose self-regulation, become brittle. Too little → subsystems drift, no synthesis occurs. Watch for both failure modes.

---

### 6. Resilience + Self-Organization + Hierarchy Are Mutually Reinforcing
These aren't separate system properties. Hierarchy enables resilience (one subsystem failing doesn't kill others). Resilience enables self-organization (safe to experiment). Self-organization produces hierarchy (structure emerges from complexity).

---

### 8. Events → Behavior → Structure (Three Depths of Understanding)
Events are surface outputs — dramatic, visible, no predictive value. Behavior is patterns over time — correlations, trends. Structure is the interlocking stocks, flows, and feedback loops that CAUSE the behavior that PRODUCES the events. Most analysis stops at events or behavior. Structural understanding is where prediction and intervention become possible.

**Design test:** When analyzing something, ask — am I explaining an event with another event? (useless) Am I finding a behavioral pattern? (better) Or am I identifying the structural mechanism that makes this behavior inevitable? (actual understanding)

---

### 7. Partial Decomposability
Hierarchical systems can be taken apart along subsystem boundaries and the pieces still function. When hierarchies break down, they split along these same boundaries. This is a feature — graceful degradation rather than catastrophic collapse.
