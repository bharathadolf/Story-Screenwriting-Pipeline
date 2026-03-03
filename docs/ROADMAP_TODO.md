# 🚀 Story Pipeline Future Roadmap & TODO

The following is an architectural roadmap documenting the future potential implementations of the Agentic Story Pipeline. It outlines the transition from a single generative department (Planning) into a fully-fledged, production-ready multi-agent virtual studio.

---

### [ ] 1. Activate Remaining Agentic Departments

Currently, only **Stage 1 (Planning)** has a generative LLM active. The immediate next steps are to integrate the `google-genai` loop into the remaining stages:

- [ ] **Stage 2 (Character):** Design prompts to autonomously read the Project Bible and generate unique, flawed characters with interweaving relationship dynamics. Implement the interactive terminal QA.
- [ ] **Stage 3 (Outlining):** Design prompts to strictly pace character arcs alongside plot sequences into a scene-by-scene beat sheet.
- [ ] **Stage 4 (Drafting - The Holy Grail):** Instead of writing a whole script at once and hallucinating, prompt the drafter to read the Master Outline and write **one scene at a time** (saving to WIP incrementally), ensuring tight continuity.
- [ ] **Stage 5 (Refining):** Upgrade the basic linter to an LLM evaluator to scan for plot holes and voice consistency.

### [ ] 2. Multi-Agent Debate (The "Writers Room")

In **Stage 5: Refining**, implement an interactive multi-agent debate system where multiple distinct persona prompts evaluate the draft concurrently:

- [ ] **Agent A (The Director):** Scans the `HTML`/JSON drafts to flag if the scenes lack visual intrigue.
- [ ] **Agent B (The Actor):** Evaluates dialogue to rewrite "robotic" exposition into natural subtext.
- [ ] **Agent C (The Showrunner):** Analyzes the Master Outline vs. Drafts to flag continuity plot holes.
- [ ] Generate a unified `linter_errors.json` report containing the aggregated agent feedback for the user to fix.

### [ ] 3. Long-Term Memory (RAG Vector Databases)

As the Project Bible and scripts grow massive (100+ pages), the agents might "forget" early constraints by the time they reach Stage 4.

- [ ] Integrate a Vector Database (e.g., `ChromaDB` or `Pinecone`).
- [ ] Slice the `project_bible.json`, `character_bible.json`, and `master_outline.json` into semantic chunks.
- [ ] Implement an autonomous RAG query step: Before the Drafter writes a scene set in the "Ice Kingdom", it queries the database (_"Fetch the climate rules for the Ice Kingdom"_) and only loads that specific contextual chunk into its prompt, preventing token context saturation.

### [ ] 4. Direct Production Integration (The Studio Level)

Once the script is approved in Stage 5, automate the pipeline to export deliverables tailored for film production crews:

- [ ] **Screenplay Export:** Convert the JSON/HTML scenes directly into standard industry `.fdx` (Final Draft) format or Fountain format.
- [ ] **Production Breakdowns:** Parse the approved script to automatically generate **Shot Lists**, **Prop Lists**, and **Location Lists**.
- [ ] **VFX Pipeline Sync:** Implement Python scripts to push those CSV/JSON lists directly via API into VFX management software like **ShotGrid**, **Kitsu**, or **Notion**.
