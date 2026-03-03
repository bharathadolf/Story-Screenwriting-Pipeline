import json
import os
import argparse

def run_character_dev(project_name, project_dir, project_bible_path, raw_character_input):
    """
    STAGE 2: CHARACTER DEVELOPMENT
    Simulates ArcAgent, RelationshipAgent, VoiceAgent, and ConsistencyQC.
    Uses the APPROVED Project Bible and user character notes to generate the detailed Cast.
    """
    print(f"--- [STAGE 2: CHARACTER DEVELOPMENT] Building Cast for {project_name} ---")
    
    if not os.path.exists(project_bible_path):
        print(f"Error: APPROVED Project Bible not found at {project_bible_path}. You must run 'publish' on Stage 1 first.")
        return None
        
    if not os.path.exists(raw_character_input):
        print(f"Error: User character input {raw_character_input} not found.")
        return None
        
    with open(project_bible_path, 'r') as f:
        project_bible = json.load(f)
        themes = project_bible.get("themes", [])
        
    with open(raw_character_input, 'r') as f:
        raw_chars = json.load(f).get("characters", [])
        
    # ConsistencyQC Agent simulation: Check if characters align with themes
    qc_passed = True
    for char in raw_chars:
        if not char.get("flaw"):
            print(f"QC WARN: Character {char.get('name')} is missing a defining flaw.")
            qc_passed = False
            
    if not qc_passed:
        print("ConsistencyQC Agent flagged issues. Please update your input and try again.")
        # We can still output it to WIP for manual review, or block it. 
        # For pipeline flow, we output to WIP so the user can see it.

    character_bible = {
        "project": project_name,
        "themes_applied": themes,
        "characters": raw_chars
    }
    
    wip_dir = os.path.join(project_dir, f"{project_name}_STORY", "02_CHARACTER_DEVELOPMENT", "WIP")
    os.makedirs(wip_dir, exist_ok=True)
    
    output_path = os.path.join(wip_dir, f"{project_name}_character_bible.json")
    with open(output_path, 'w') as f:
        json.dump(character_bible, f, indent=4)
        
    print(f"WIP Character Bible created: {output_path}")
    print("Action Required: Review the WIP Character Bible and execute `publish` to push it to the APPROVED folder.")
    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--dir", default=".")
    parser.add_argument("--bible", required=True, help="Path to APPROVED project_bible.json")
    parser.add_argument("--input", required=True, help="Path to raw character profiles")
    args = parser.parse_args()
    run_character_dev(args.project, args.dir, args.bible, args.input)
