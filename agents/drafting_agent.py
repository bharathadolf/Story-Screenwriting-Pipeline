import json
import os
import argparse
import sys

# Add the project directory to sys.path so we can import tests
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
if project_dir not in sys.path:
    sys.path.append(project_dir)

from tests.scene_to_script import generate_script_from_scene

def run_drafting(project_name, project_dir, character_bible_path, master_outline_path):
    """
    STAGE 4: DRAFTING
    Simulates DraftingAgent and LocationAgent.
    Drafts the actual scenes by cross-referencing Stage 2 (Characters) and Stage 3 (Outline).
    """
    print(f"--- [STAGE 4: DRAFTING] Writing the Story for {project_name} ---")
    
    if not os.path.exists(master_outline_path) or not os.path.exists(character_bible_path):
        print("Error: APPROVED inputs not found. You must publish Stages 2 and 3.")
        return None
        
    with open(master_outline_path, 'r') as f:
        outline_data = json.load(f)
        scenes = outline_data.get('scenes', [])

    wip_dir = os.path.join(project_dir, f"{project_name}_STORY", "04_DRAFTING", "WIP")
    os.makedirs(wip_dir, exist_ok=True)
    
    generated_scenes = []

    for outline_scene in scenes:
        scene_num = outline_scene.get('scene_number', 0)
        print(f"Drafting Scene {scene_num} to WIP...")
        
        # In full version, LLM agent looks at character voices and location rules here
        # For now, we mock the generated output based on the outline payload
        mock_scene_data = {
            "scene_number": scene_num,
            "location": outline_scene.get('location'),
            "time": outline_scene.get('time'),
            "action_lines": outline_scene.get('action_beats', []),
            "dialogue": outline_scene.get('dialogue_beats', [])
        }
        
        temp_scene_path = os.path.join(wip_dir, f"temp_scene_{scene_num}.json")
        with open(temp_scene_path, 'w') as f:
            json.dump(mock_scene_data, f, indent=4)
            
        generate_script_from_scene(temp_scene_path, wip_dir)
        generated_scenes.append(os.path.join(wip_dir, f"scene_{scene_num}.html"))
        
        if os.path.exists(temp_scene_path):
             os.remove(temp_scene_path)
             
    print(f"Drafted {len(generated_scenes)} scenes in {wip_dir}")
    print("Action Required: Review drafted scenes. Use `publish` to push them to APPROVED for Refining.")
    return wip_dir

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--dir", default=".")
    parser.add_argument("--chars", required=True)
    parser.add_argument("--outline", required=True)
    args = parser.parse_args()
    run_drafting(args.project, args.dir, args.chars, args.outline)
