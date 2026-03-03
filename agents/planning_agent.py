import json
import os
import argparse

def run_planning(project_name, project_dir, input_file):
    """
    STAGE 1: PLANNING
    Simulates the Brainstorm, Worldbuilding, and Theme agents.
    Takes user's raw inspirational data/ideas and structures them into a Project Bible.
    """
    print(f"--- [STAGE 1: PLANNING] Processing Inspiration for {project_name} ---")
    
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} not found.")
        return None
        
    with open(input_file, 'r') as f:
        try:
            raw_data = json.load(f)
        except json.JSONDecodeError:
            print("Error: Input file must be valid JSON.")
            return None
            
    # Mock behavior of specialized agents:
    # BrainstormAgent extracts logline
    # ThemeAgent extracts themes
    # WorldbuildingAgent extracts rules
    
    project_bible = {
        "project": project_name,
        "logline": raw_data.get("logline", "A story about..."),
        "themes": raw_data.get("themes", []),
        "world_rules": raw_data.get("world_rules", [])
    }
    
    wip_dir = os.path.join(project_dir, f"{project_name}_STORY", "01_PLANNING", "WIP")
    os.makedirs(wip_dir, exist_ok=True)
    
    output_path = os.path.join(wip_dir, f"{project_name}_project_bible.json")
    with open(output_path, 'w') as f:
        json.dump(project_bible, f, indent=4)
        
    print(f"WIP Project Bible created: {output_path}")
    print("Action Required: Review the WIP Project Bible and execute `publish` to push it to the APPROVED folder.")
    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--dir", default=".")
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    run_planning(args.project, args.dir, args.input)
