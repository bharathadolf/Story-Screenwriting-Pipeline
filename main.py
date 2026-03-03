import sys
import os
import argparse
import shutil

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.planning_agent import run_planning
from agents.character_agent import run_character_dev
from agents.outlining_agent import run_outlining
from agents.drafting_agent import run_drafting
from agents.refining_agent import run_refining
from core.create_story_pipeline import create_structure

def init_project(args):
    print(f"Initializing project: {args.project_name}")
    create_structure(args.project_name, args.dir)

def plan(args):
    print(f"Running STAGE 1 (Planning) for: {args.project_name}")
    run_planning(args.project_name, args.dir, args.input)

def character(args):
    print(f"Running STAGE 2 (Character Development) for: {args.project_name}")
    run_character_dev(args.project_name, args.dir, args.bible, args.input)

def outline(args):
    print(f"Running STAGE 3 (Outlining) for: {args.project_name}")
    run_outlining(args.project_name, args.dir, args.bible, args.chars, args.input)

def draft(args):
    print(f"Running STAGE 4 (Drafting) for: {args.project_name}")
    run_drafting(args.project_name, args.dir, args.chars, args.outline)

def refine(args):
    print(f"Running STAGE 5 (Refining) for: {args.project_name}")
    run_refining(args.project_name, args.dir, args.drafts, args.chars)

def publish(args):
    print(f"Publishing artifact: {args.input} to {args.destination}")
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found.")
        return
        
    os.makedirs(os.path.dirname(args.destination), exist_ok=True)
    
    # If it's a directory, copy tree, else copy file
    if os.path.isdir(args.input):
        shutil.copytree(args.input, args.destination, dirs_exist_ok=True)
    else:
        shutil.copy2(args.input, args.destination)
        
    print(f"Successfully published '{args.input}' to '{args.destination}'. Ready for next stage.")

def print_custom_help():
    try:
        from rich.console import Console
        from rich.table import Table
    except ImportError:
        print("\n[!] The 'rich' library is required for the new CLI help menu.")
        print("Please install it by running: pip install rich\n")
        return

    console = Console()
    
    console.print("\n[bold magenta]" + "="*116)
    console.print("[bold magenta]" + "                                        STORY-TO-SCREENWRITING PIPELINE CLI                                         ".center(116))
    console.print("[bold magenta]" + "="*116 + "\n")
    console.print("Usage: [bold cyan]python main.py <command> [options][/bold cyan]\n")
    
    # GENERAL COMMANDS TABLE
    gen_table = Table(title="General Operations", title_style="bold yellow", title_justify="left", header_style="bold green", show_lines=True)
    gen_table.add_column("Command", style="bold cyan", no_wrap=True)
    gen_table.add_column("Description")
    gen_table.add_column("Example Usage", style="yellow")
    
    gen_table.add_row("init", "Initialize 5-stage project structure. Args: project_name, [--dir]", "python main.py init MY_MOVIE")
    gen_table.add_row("publish", "Publish WIP artifacts to APPROVED folder. Args: --input, --destination", "python main.py publish --input ... --dest ...")
    
    console.print(gen_table)
    console.print()
    
    # DEPARTMENT COMMANDS TABLE
    dept_table = Table(title="Department Operations", title_style="bold yellow", title_justify="left", header_style="bold green", show_lines=True)
    dept_table.add_column("Command", style="bold cyan", no_wrap=True)
    dept_table.add_column("Description")
    dept_table.add_column("Example Usage", style="yellow")
    
    dept_table.add_row("plan", "Stage 1: Planning. Extracts Lore & Theme. Args: project_name, --input", "python main.py plan MY_MOVIE --input examples/concept_input.json")
    dept_table.add_row("character", "Stage 2: Character Dev. Generates bibles. Args: project_name, --bible, --input", "python main.py character MY... --bible... --input...")
    dept_table.add_row("outline", "Stage 3: Outlining. Maps story beats. Args: project_name, --bible, --chars, --input", "python main.py outline MY... --bible... --chars...")
    dept_table.add_row("draft", "Stage 4: Drafting. Auto-writes scenes. Args: project_name, --chars, --outline", "python main.py draft MY... --chars... --outline...")
    dept_table.add_row("refine", "Stage 5: Refining. QA checks. Args: project_name, --drafts, --chars", "python main.py refine MY... --drafts... --chars...")

    console.print(dept_table)
    console.print()

if __name__ == "__main__":
    if "-h" in sys.argv or "--help" in sys.argv:
        print_custom_help()
        sys.exit(0)
        
    parser = argparse.ArgumentParser(description="5-Stage Story Pipeline CLI")
    subparsers = parser.add_subparsers(dest="command", help="Pipeline staging commands")
    subparsers.required = True
    
    # Init
    parser_init = subparsers.add_parser("init", help="Initialize 5-stage project structure")
    parser_init.add_argument("project_name", help="Name of the project")
    parser_init.add_argument("--dir", default=".", help="Base directory")
    parser_init.set_defaults(func=init_project)
    
    # Stage 1: Planning
    parser_plan = subparsers.add_parser("plan", help="Execute Stage 1: Planning")
    parser_plan.add_argument("project_name", help="Name of the project")
    parser_plan.add_argument("--input", required=True, help="Path to raw ideas/inspiration JSON")
    parser_plan.add_argument("--dir", default=".", help="Base directory")
    parser_plan.set_defaults(func=plan)
    
    # Stage 2: Character
    parser_char = subparsers.add_parser("character", help="Execute Stage 2: Character Development")
    parser_char.add_argument("project_name", help="Name of the project")
    parser_char.add_argument("--bible", required=True, help="Path to APPROVED project_bible.json (From Stage 1)")
    parser_char.add_argument("--input", required=True, help="Path to raw character profiles JSON")
    parser_char.add_argument("--dir", default=".", help="Base directory")
    parser_char.set_defaults(func=character)
    
    # Stage 3: Outline
    parser_outline = subparsers.add_parser("outline", help="Execute Stage 3: Outlining")
    parser_outline.add_argument("project_name", help="Name of the project")
    parser_outline.add_argument("--bible", required=True, help="Path to APPROVED project_bible.json (From Stage 1)")
    parser_outline.add_argument("--chars", required=True, help="Path to APPROVED character_bible.json (From Stage 2)")
    parser_outline.add_argument("--input", required=True, help="Path to raw outline/beat sheet JSON")
    parser_outline.add_argument("--dir", default=".", help="Base directory")
    parser_outline.set_defaults(func=outline)
    
    # Stage 4: Draft
    parser_draft = subparsers.add_parser("draft", help="Execute Stage 4: Drafting")
    parser_draft.add_argument("project_name", help="Name of the project")
    parser_draft.add_argument("--chars", required=True, help="Path to APPROVED character_bible.json (From Stage 2)")
    parser_draft.add_argument("--outline", required=True, help="Path to APPROVED master_outline.json (From Stage 3)")
    parser_draft.add_argument("--dir", default=".", help="Base directory")
    parser_draft.set_defaults(func=draft)
    
    # Stage 5: Refine
    parser_refine = subparsers.add_parser("refine", help="Execute Stage 5: Refining/Editing")
    parser_refine.add_argument("project_name", help="Name of the project")
    parser_refine.add_argument("--drafts", required=True, help="Path to APPROVED drafts directory (From Stage 4)")
    parser_refine.add_argument("--chars", required=True, help="Path to APPROVED character_bible.json (From Stage 2)")
    parser_refine.add_argument("--dir", default=".", help="Base directory")
    parser_refine.set_defaults(func=refine)
    
    # Publish
    parser_publish = subparsers.add_parser("publish", help="Publish a WIP artifact to an APPROVED folder")
    parser_publish.add_argument("--input", required=True, help="Path to the WIP file/folder")
    parser_publish.add_argument("--destination", required=True, help="Path to the APPROVED destination")
    parser_publish.set_defaults(func=publish)
    
    args = parser.parse_args()
    args.func(args)
