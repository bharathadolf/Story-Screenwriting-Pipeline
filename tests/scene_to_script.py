import json
import os
import argparse

# ANSI Color Codes
class Colors:
    HEADER = '\033[95m'      # Magenta
    SCENE_HEADING = '\033[94m' # Blue
    CHARACTER = '\033[92m'   # Green
    PARENTHETICAL = '\033[93m' # Yellow
    DIALOGUE = '\033[97m'    # White
    ACTION = '\033[96m'      # Cyan
    ENDC = '\033[0m'         # Reset color

def generate_script_from_scene(scene_file_path, output_dir="."):
    """
    Simulates the 'Drafting Department' agentic workflow.
    Takes a structured scene data packet and renders it into a script format.
    """
    print(f"Loading scene data from {scene_file_path}...")
    with open(scene_file_path, 'r') as f:
        scene_data = json.load(f)
        
    scene_number = scene_data.get("scene_number", 0)
    location = scene_data.get("location", "UNKNOWN LOCATION")
    time = scene_data.get("time", "DAY")
    
    # Render the fountain/script text format with ANSI colors for terminal
    terminal_content = f"{Colors.HEADER}SCENE START{Colors.ENDC}\n\n"
    terminal_content += f"{Colors.SCENE_HEADING}EXT/INT. {location} - {time}{Colors.ENDC}\n\n"

    # Render HTML content for the saved file
    html_content = f"""
    <html>
    <head>
    <style>
        body {{ font-family: 'Courier New', Courier, monospace; background-color: #1e1e1e; color: #d4d4d4; padding: 40px; white-space: pre-wrap; }}
        .header {{ color: #d16969; font-weight: bold; }}
        .scene {{ color: #569cd6; font-weight: bold; }}
        .action {{ color: #4ec9b0; }}
        .character {{ color: #b5cea8; margin-left: 20%; }}
        .parenthetical {{ color: #d7ba7d; font-style: italic; margin-left: 15%; }}
        .dialogue {{ color: #ce9178; margin-left: 10%; margin-right: 20%; }}
    </style>
    </head>
    <body>
    <div class='header'>SCENE START</div><br/>
    <div class='scene'>EXT/INT. {location} - {time}</div><br/>
    """
    
    for action in scene_data.get("action_lines", []):
        terminal_content += f"{Colors.ACTION}{action}{Colors.ENDC}\n\n"
        html_content += f"<div class='action'>{action}</div><br/>\n"
        
    for line in scene_data.get("dialogue", []):
        char = line.get("character")
        paren = line.get("parenthetical", "")
        text = line.get("text")
        
        terminal_content += f"{Colors.CHARACTER}          {char}{Colors.ENDC}\n"
        html_content += f"<div class='character'>{char}</div>\n"
        
        if paren:
            terminal_content += f"{Colors.PARENTHETICAL}        ({paren}){Colors.ENDC}\n"
            html_content += f"<div class='parenthetical'>({paren})</div>\n"
            
        terminal_content += f"{Colors.DIALOGUE}    {text}{Colors.ENDC}\n\n"
        html_content += f"<div class='dialogue'>{text}</div><br/>\n"
        
    html_content += "</body></html>"
        
    output_filename = f"scene_{scene_number}.fbx.html"
    output_path = os.path.join(output_dir, output_filename)
    
    with open(output_path, 'w') as out_f:
        out_f.write(html_content)
        
    print(f"\n+++ Successfully generated script file: {output_path} +++\n")
    print("--- PREVIEW OF COMPILED FBX SCENE ---")
    print(terminal_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert scene JSON to script FBX.")
    parser.add_argument("--input", type=str, help="Path to scene JSON file", default="scene_demo.json")
    parser.add_argument("--output_dir", type=str, help="Directory to save the script", default=".")
    
    args = parser.parse_args()
    
    # Ensure relative paths are handled correctly if run from outside the directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, args.input) if not os.path.isabs(args.input) else args.input
    output_dir = os.path.join(current_dir, args.output_dir) if not os.path.isabs(args.output_dir) else args.output_dir
    
    if os.path.exists(input_path):
        generate_script_from_scene(input_path, output_dir)
    else:
        print(f"Error: Demo scene file not found at {input_path}")
