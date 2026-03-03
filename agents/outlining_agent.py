import json
import os
import argparse

def run_outlining(project_name, project_dir, project_bible_path, character_bible_path, raw_outline_input):
    """
    STAGE 3: OUTLINING
    Simulates PlottingAgent, SceneCardAgent, and PacingQC.
    Takes APPROVED bibles and user plot points to map out the scene cards.
    """
    print(f"--- [STAGE 3: OUTLINING] Mapping the Story for {project_name} ---")
    
    if not os.path.exists(project_bible_path) or not os.path.exists(character_bible_path):
        print("Error: APPROVED Bibles not found. You must publish Stages 1 and 2.")
        return None
        
    if not os.path.exists(raw_outline_input):
        print(f"Error: User outline input {raw_outline_input} not found.")
        return None
        
    with open(raw_outline_input, 'r') as f:
        master_outline = json.load(f)
        
    scenes = master_outline.get("scenes", [])
    
    # PacingQC Agent simulation: Check for climax/midpoint structure
    qc_passed = True
    if len(scenes) < 3:
        print("QC WARN: Outline has fewer than 3 scenes. Pacing Agent flags this as too short.")
        qc_passed = False
        
    master_outline["project"] = project_name
    
    wip_dir = os.path.join(project_dir, f"{project_name}_STORY", "03_OUTLINING", "WIP")
    os.makedirs(wip_dir, exist_ok=True)
    
    output_path = os.path.join(wip_dir, f"{project_name}_master_outline.json")
    with open(output_path, 'w') as f:
        json.dump(master_outline, f, indent=4)
        
    print(f"WIP Master Outline created: {output_path}")
    print("Action Required: Review the WIP Outline and execute `publish` to push it to the APPROVED folder.")
    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--dir", default=".")
    parser.add_argument("--bible", required=True)
    parser.add_argument("--chars", required=True)
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    run_outlining(args.project, args.dir, args.bible, args.chars, args.input)
