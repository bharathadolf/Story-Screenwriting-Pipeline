<div align="center">
  <h1>🎬 Story-to-Screenwriting Pipeline</h1>
  <p><b>An Agentic, Production-Ready Workflow for Screenwriters</b></p>
</div>

Welcome to the **Story Pipeline CLI**. Inspired by the strict discipline and data-consistency of VFX studio pipelines, this tool uses **Gemini 1.5 Pro** agents to autonomously map your raw ideas into production-ready screenplays across five controlled stages.

---

### 🌟 Core Philosophy

1. **Agentic Automation:** Let specialized AI act as your Showrunner, Dramaturg, and Drafter.
2. **Interactive Development:** The AI pauses at key moments to ask for your creative direction.
3. **QA Gates ("Publish"):** No stage advances without human review. Work remains in `WIP` until explicitly published to `APPROVED`, preventing messy continuity errors.

---

## 🚀 The 5-Stage Workflow

### `[Step 0]` Init: Scaffolding the Studio

Generate the robust `WIP` and `APPROVED` folder structures.

```bash
python main.py init MY_MOVIE
```

### `[Step 1]` Planning: The Showrunner 🧠 (Gemini Agent)

Autonomously processes your raw idea (`concept_input.json`) to develop the world, themes, and master synopsis.

> **Note:** Requires Gemini API Key (`set GEMINI_API_KEY=your_key`)

```bash
python main.py plan MY_MOVIE --input examples/concept_input.json
```

⌨️ _The agent will pause mid-execution in your terminal to ask for feedback. Type instructions to rewrite the lore, or type **"Approve"** to finalize!_

### `[Step 2]` Characters: The Dramaturg 🎭

Builds deep, flawed character bibles using your approved project lore.

```bash
python main.py character MY_MOVIE --bible MY_MOVIE/.../APPROVED/MY_MOVIE_project_bible.json --input characters.json
```

### `[Step 3]` Outlining: The Mapper 🗺️

Transforms the master synopsis and characters into tight scene-by-scene script beats.

```bash
python main.py outline MY_MOVIE --bible [Path] --chars [Path] --input examples/outline_input.json
```

### `[Step 4]` Drafting: The Screenwriter ✍️

Auto-writes the actual screenplay scenes using your approved characters and outline. No manual input json required!

```bash
python main.py draft MY_MOVIE --chars [Path] --outline [Path]
```

### `[Step 5]` Refining: The Continuity Checker 🔎

Scans the final drafted scripts for character continuity or format breaks. `0 Linter Errors` means your script is production-ready!

```bash
python main.py refine MY_MOVIE --drafts [Path] --chars [Path]
```

---

## 🔒 Publishing (The Quality Gate)

Between _every_ stage, you must **review** the agent's work inside the `WIP` (Work-In-Progress) folder. If the output is flawless, you officially "Publish" it to the `APPROVED` folder for the next agent to use.

```bash
python main.py publish --input [WIP_FILE] --destination [APPROVED_FILE]
```
