import json
import os
import argparse

def run_refining(project_name, project_dir, drafts_dir, character_bible_path):
    """
    STAGE 5: REFINING & EDITING
    Simulates ContinuityAgent and StyleAgent.
    Lints the approved drafts from Stage 4 against the DB from Stage 2.
    """
    print(f"--- [STAGE 5: REFINING] Continual Revision for {project_name} ---")
    
    if not os.path.exists(drafts_dir) or not os.path.exists(character_bible_path):
        print("Error: APPROVED inputs not found. Ensure drafts are published.")
        return None
        
    with open(character_bible_path, 'r') as f:
        characters_data = json.load(f)
        characters_list = characters_data.get('characters', [])
        character_map = {c['name']: c for c in characters_list}

    wip_dir = os.path.join(project_dir, f"{project_name}_STORY", "05_REFINING", "WIP")
    os.makedirs(wip_dir, exist_ok=True)
    
    linter_errors = []
    
    for filename in os.listdir(drafts_dir):
        if filename.endswith(".html"):
            filepath = os.path.join(drafts_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Scan for character tags
            lines = content.split("\n")
            for i, line in enumerate(lines):
                if '<p class="character">' in line:
                    char_name = line.replace('<p class="character">', '').replace('</p>', '').strip()
                    if char_name not in character_map and not char_name.startswith("("):
                        linter_errors.append({
                            "scene_file": filename,
                            "line_num": i+1,
                            "error": "Continuity Error",
                            "severity": "HIGH",
                            "message": f"Character '{char_name}' is speaking, but does not exist in the Character Cast."
                        })
                        
    report_path = os.path.join(wip_dir, f'{project_name}_linter_errors.json')
    with open(report_path, 'w') as f:
         json.dump({"total_errors": len(linter_errors), "errors": linter_errors}, f, indent=4)
         
    if len(linter_errors) == 0:
        print("REFINING SUCCESS: 0 Linter Errors Found. Script is clean.")
    else:
        print(f"REFINING FAILURE: {len(linter_errors)} Errors Found. See {report_path}")

    return report_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--dir", default=".")
    parser.add_argument("--drafts", required=True)
    parser.add_argument("--chars", required=True)
    args = parser.parse_args()
    run_refining(args.project, args.dir, args.drafts, args.chars)
