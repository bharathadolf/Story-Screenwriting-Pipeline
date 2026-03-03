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
python run_pipeline.py init MY_MOVIE
```

---

## Step 1: Planning

Write down your raw ideas, themes, and worldbuilding concepts into a JSON file, e.g., `concept.json`.

```bash
python run_pipeline.py plan MY_MOVIE --input concept.json
```

It will process this into a `MY_MOVIE_project_bible.json` located in `01_PLANNING/WIP`.

**Review and Publish:**
Once you check this WIP file and approve it, "publish" it to the approved folder so Stage 2 can access it:

```bash
python run_pipeline.py publish --input MY_MOVIE_STORY/01_PLANNING/WIP/MY_MOVIE_project_bible.json --destination MY_MOVIE_STORY/01_PLANNING/APPROVED/MY_MOVIE_project_bible.json
```

---

## Step 2: Character Development

With your approved concept, write down your raw character profiles in a JSON file, e.g., `characters.json`.

```bash
python run_pipeline.py character MY_MOVIE --bible MY_MOVIE_STORY/01_PLANNING/APPROVED/MY_MOVIE_project_bible.json --input characters.json
```

It will output the formatted `MY_MOVIE_character_bible.json` in `02_CHARACTER_DEVELOPMENT/WIP`.

**Review and Publish:**
Ensure the character flaws and arcs look correct.

```bash
python run_pipeline.py publish --input MY_MOVIE_STORY/02_CHARACTER_DEVELOPMENT/WIP/MY_MOVIE_character_bible.json --destination MY_MOVIE_STORY/02_CHARACTER_DEVELOPMENT/APPROVED/MY_MOVIE_character_bible.json
```

---

## Step 3: Outlining

Now map out your specific scene-by-scene script beats in a JSON file, e.g., `outline.json`.

```bash
python run_pipeline.py outline MY_MOVIE --bible MY_MOVIE_STORY/01_PLANNING/APPROVED/MY_MOVIE_project_bible.json --chars MY_MOVIE_STORY/02_CHARACTER_DEVELOPMENT/APPROVED/MY_MOVIE_character_bible.json --input outline.json
```

It creates a `MY_MOVIE_master_outline.json` in `03_OUTLINING/WIP`.

**Review and Publish:**

```bash
python run_pipeline.py publish --input MY_MOVIE_STORY/03_OUTLINING/WIP/MY_MOVIE_master_outline.json --destination MY_MOVIE_STORY/03_OUTLINING/APPROVED/MY_MOVIE_master_outline.json
```

---

## Step 4: Drafting

You don't need any new input files for this! The Drafting Agent takes your approved characters and approved outline and writes the scenes for you.

```bash
python run_pipeline.py draft MY_MOVIE --chars MY_MOVIE_STORY/02_CHARACTER_DEVELOPMENT/APPROVED/MY_MOVIE_character_bible.json --outline MY_MOVIE_STORY/03_OUTLINING/APPROVED/MY_MOVIE_master_outline.json
```

The drafted HTML script files will populate in the `04_DRAFTING/WIP` folder.

**Review and Publish:**
Publish the _entire folder_:

```bash
python run_pipeline.py publish --input MY_MOVIE_STORY/04_DRAFTING/WIP --destination MY_MOVIE_STORY/04_DRAFTING/APPROVED
```

---

## Step 5: Refining & QA

Run the continuity checker and syntax linters to make sure everything matches.

```bash
python run_pipeline.py refine MY_MOVIE --drafts MY_MOVIE_STORY/04_DRAFTING/APPROVED --chars MY_MOVIE_STORY/02_CHARACTER_DEVELOPMENT/APPROVED/MY_MOVIE_character_bible.json
```

It will generate a `MY_MOVIE_linter_errors.json` report in `05_REFINING/WIP`. If it reports `0 Linter Errors`, your script is completely production-ready.
