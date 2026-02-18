# DARWIN BACKLOG

Potential improvements to explore, prioritized by expected value.

---

## High Priority

### 1. Conway Terminal Integration
**What:** Install `npx conway-terminal` to add wallet + payment + compute capabilities  
**Why:** Enables persistent agents, on-demand compute, inter-agent payments  
**Effort:** Low (npm install)  
**Expected Value:** Medium-High (new capability layer)  
**Status:** Mulling (discussed 2026-02-18)  
**Next Step:** Will decides if/when to fund initial wallet  

---

## Medium Priority

### 2. MCP Server Audit
**What:** Review available MCP servers, identify useful ones not yet installed  
**Why:** MCP tools directly expand agent capabilities  
**Effort:** Low-Medium  
**Expected Value:** Medium  
**Status:** Not started  
**Next Step:** Catalog current MCP servers, review awesome-mcp-servers list  

### 3. Persistent Memory Improvements
**What:** Evaluate vector DB / RAG solutions for better long-term memory  
**Why:** Current memory is file-based, may not scale  
**Effort:** Medium  
**Expected Value:** Medium  
**Status:** Not started  
**Next Step:** Research options (Chroma, Pinecone, local alternatives)  

### 4. Voice/Audio Pipeline
**What:** Improve audio briefing workflow (better TTS, maybe STT input)  
**Why:** Will listens to briefings while walking — quality matters  
**Effort:** Medium  
**Expected Value:** Medium  
**Status:** Partially done (TTS exists)  
**Next Step:** Evaluate ElevenLabs or alternatives for higher quality  

---

## Low Priority (Watch)

### 5. Local Model Fallback
**What:** Run local LLM for non-critical tasks when API is slow/expensive  
**Why:** Cost reduction, latency reduction for simple tasks  
**Effort:** High  
**Expected Value:** Low-Medium  
**Status:** Watch  
**Blocker:** Compute requirements, quality tradeoffs  

### 6. Custom Fine-Tuning
**What:** Fine-tune a model on our research corpus  
**Why:** Domain-specific performance improvement  
**Effort:** Very High  
**Expected Value:** Unknown  
**Status:** Future  
**Blocker:** Need more data, clear use case  

---

## Completed

| Item | Date | Result |
|------|------|--------|
| — | — | — |

---

## Rejected

| Item | Reason |
|------|--------|
| — | — |
