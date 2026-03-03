# 5-Stage Story Pipeline Guide

This guide explains how to use the Agentic Story Pipeline from start to finish. The pipeline is designed around a stage-wise execution process with explicit QA gates ("Publish" steps) to ensure perfect data consistency before moving to the next stage.

## The 5 Stages

1. `plan`: Brainstorm, worldbuilding, and theme selection.
2. `character`: Defines character arcs, flaws, and constraints.
3. `outline`: Maps out the story beats and scene cards.
4. `draft`: Agent auto-writes the scenes based on the characters and outlines.
5. `refine`: Continuity checker scans the drafted script for inconsistencies.

---

## Step 0: Initialization

First, run the initialization command to generate the 5-stage scaffolding (`WIP` and `APPROVED` folders).

```bash
python main.py init MY_MOVIE
```

---

## Step 1: Planning (Agentic Loop)

The planning stage is a fully autonomous **Agentic Loop** powered by Gemini 1.5 Pro. The Showrunner Agent will read your raw concept, creatively brainstorm the themes and lore, write the Project Bible, and then pause to ask for your feedback interactively in the terminal!

**Prerequisite:** Ensure you have your Gemini API key set:

- **Windows CMD:** `set GEMINI_API_KEY=your_actual_key`
- **Windows PowerShell:** `$env:GEMINI_API_KEY="your_actual_key"`
- **Mac/Linux:** `export GEMINI_API_KEY="your_actual_key"`

Write down your raw ideas into a JSON file, e.g., `examples/concept_input.json`, then spawn the agent:

```bash
python main.py plan MY_MOVIE --input examples/concept_input.json
```

The Agent will spawn, think, and draft the `MY_MOVIE_project_bible.json` in `01_PLANNING/WIP`.
When it pauses and asks for human feedback, you can type instructions to redirect the story (e.g., _"Make the villain's motivations more sympathetic"_), and the agent will dynamically rewrite the lore file.
When you are happy with the generated Bible, type **"Approve"** in the terminal to end the loop.

**Review and Publish:**
Once approved and finalized, "publish" it to the approved folder so Stage 2 can access it:

```bash
python main.py publish --input MY_MOVIE_STORY/01_PLANNING/WIP/MY_MOVIE_project_bible.json --destination MY_MOVIE_STORY/01_PLANNING/APPROVED/MY_MOVIE_project_bible.json
```

---

## Step 2: Character Development

With your approved concept, write down your raw character profiles in a JSON file, e.g., `characters.json`.

```bash
python main.py character MY_MOVIE --bible MY_MOVIE_STORY/01_PLANNING/APPROVED/MY_MOVIE_project_bible.json --input characters.json
```

It will output the formatted `MY_MOVIE_character_bible.json` in `02_CHARACTER_DEVELOPMENT/WIP`.

**Review and Publish:**
Ensure the character flaws and arcs look correct.

```bash
python main.py publish --input MY_MOVIE_STORY/02_CHARACTER_DEVELOPMENT/WIP/MY_MOVIE_character_bible.json --destination MY_MOVIE_STORY/02_CHARACTER_DEVELOPMENT/APPROVED/MY_MOVIE_character_bible.json
```

---

## Step 3: Outlining

Now map out your specific scene-by-scene script beats in a JSON file, e.g., `examples/outline_input.json`.

```bash
python main.py outline MY_MOVIE --bible MY_MOVIE_STORY/01_PLANNING/APPROVED/MY_MOVIE_project_bible.json --chars MY_MOVIE_STORY/02_CHARACTER_DEVELOPMENT/APPROVED/MY_MOVIE_character_bible.json --input examples/outline_input.json
```

It creates a `MY_MOVIE_master_outline.json` in `03_OUTLINING/WIP`.

**Review and Publish:**

```bash
python main.py publish --input MY_MOVIE_STORY/03_OUTLINING/WIP/MY_MOVIE_master_outline.json --destination MY_MOVIE_STORY/03_OUTLINING/APPROVED/MY_MOVIE_master_outline.json
```

---

## Step 4: Drafting

You don't need any new input files for this! The Drafting Agent takes your approved characters and approved outline and writes the scenes for you.

```bash
python main.py draft MY_MOVIE --chars MY_MOVIE_STORY/02_CHARACTER_DEVELOPMENT/APPROVED/MY_MOVIE_character_bible.json --outline MY_MOVIE_STORY/03_OUTLINING/APPROVED/MY_MOVIE_master_outline.json
```

The drafted HTML script files will populate in the `04_DRAFTING/WIP` folder.

**Review and Publish:**
Publish the _entire folder_:

```bash
python main.py publish --input MY_MOVIE_STORY/04_DRAFTING/WIP --destination MY_MOVIE_STORY/04_DRAFTING/APPROVED
```

---

## Step 5: Refining & QA

Run the continuity checker and syntax linters to make sure everything matches.

```bash
python main.py refine MY_MOVIE --drafts MY_MOVIE_STORY/04_DRAFTING/APPROVED --chars MY_MOVIE_STORY/02_CHARACTER_DEVELOPMENT/APPROVED/MY_MOVIE_character_bible.json
```

It will generate a `MY_MOVIE_linter_errors.json` report in `05_REFINING/WIP`. If it reports `0 Linter Errors`, your script is completely production-ready.
