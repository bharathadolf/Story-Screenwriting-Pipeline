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
    Takes a structured scene data packet and renders it into a perfectly calibrated HTML script format
    specifically optimized for "Save As PDF" / Print to US Letter margins.
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

    # Perfect Print Calibration Settings - US Letter
    html_content = [
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        "<meta charset=\"utf-8\">",
        f"<title>Scene {scene_number}</title>",
        "<style>",
        "    /* Base Reset */",
        "    * { box-sizing: border-box; margin: 0; padding: 0; }",
        "",
        "    /* Screen Setup (for previewing) */",
        "    body {",
        "        background-color: #525659;",
        "        display: flex;",
        "        justify-content: center;",
        "        padding: 2in 0;",
        "    }",
        "    ",
        "    .page {",
        "        background: white;",
        "        width: 8.5in;",             # US Letter width
        "        min-height: 11in;",         # US Letter height
        "        padding-top: 1in;",         # Top margin
        "        padding-bottom: 1in;",      # Bottom margin
        "        padding-left: 1.5in;",      # Left margin (binding)
        "        padding-right: 1in;",       # Right margin
        "        box-shadow: 0 0 0.5in rgba(0,0,0,0.5);",
        "        font-family: 'Courier Prime', 'Courier New', Courier, monospace;",
        "        font-size: 12pt;",
        "        line-height: 1.0;",
        "        position: relative;",
        "    }",
        "",
        "    /* Print Calibration */",
        "    @media print {",
        "        @page {",
        "            size: letter;",         # Force US Letter size
        "            margin: 0;",            # Remove browser default margins! Crucial.",
        "        }",
        "        body {",
        "            background-color: white;",
        "            padding: 0;",
        "            margin: 0;",
        "            display: block;",
        "        }",
        "        .page {",
        "            box-shadow: none;",
        "            width: 8.5in;",
        "            height: 11in;",
        "            margin: 0;",
        "            padding-top: 1in;",
        "            padding-bottom: 1in;",
        "            padding-left: 1.5in;",
        "            padding-right: 1in;",
        "            page-break-after: always;",
        "        }",
        "    }",
        "",
        "    /* Screenplay Elements Settings */",
        "    /* Margins align with true page edges (1.5in left padding on .page) */",
        "    p { margin-bottom: 12pt; } /* Default 1 line space after paragraphs */",
        "    ",
        "    .page-number {",
        "        position: absolute;",
        "        top: 0.5in;",
        "        right: 1in;",
        "        margin: 0;",
        "    }",
        "    ",
        "    .scene-heading {",
        "        margin-left: 0in; /* Total 1.5in */",
        "        text-transform: uppercase;",
        "    }",
        "    .action {",
        "        margin-left: 0in; /* Total 1.5in */",
        "    }",
        "    .character {",
        "        margin-left: 2.2in; /* Total 3.7in */",
        "        width: 1.8in; /* Ends at 5.5in */",
        "        text-transform: uppercase;",
        "        margin-bottom: 0; /* Character name touches parenthetical/dialogue */",
        "        page-break-after: avoid;",
        "    }",
        "    .dialogue {",
        "        margin-left: 1.0in; /* Total 2.5in */",
        "        width: 3.5in; /* Ends at 6.0in */",
        "    }",
        "    .parenthetical {",
        "        margin-left: 1.6in; /* Total 3.1in */",
        "        width: 2.5in; /* Ends at 5.6in */",
        "        margin-bottom: 0; /* Touches dialogue */",
        "        page-break-after: avoid;",
        "    }",
        "    .transition {",
        "        margin-left: 4.5in; /* Total 6.0in */",
        "        width: 1.5in; /* Ends at 7.5in */",
        "        text-transform: uppercase;",
        "    }",
        "</style>",
        "</head>",
        "<body>",
        "    <div class=\"page\">",
        "        <!-- Page Numbers usually hide on page 1, but added for template completeness -->"
    ]

    html_content.append(f"        <p class=\"scene-heading\">EXT/INT. {location} - {time}</p>")
    
    for action in scene_data.get("action_lines", []):
        terminal_content += f"{Colors.ACTION}{action}{Colors.ENDC}\n\n"
        html_content.append(f"        <p class=\"action\">{action}</p>")
        
    for line in scene_data.get("dialogue", []):
        char = line.get("character")
        paren = line.get("parenthetical", "")
        text = line.get("text")
        
        terminal_content += f"{Colors.CHARACTER}          {char}{Colors.ENDC}\n"
        html_content.append(f"        <p class=\"character\">{char}</p>")
        
        if paren:
            if not paren.startswith("("): paren = f"({paren})"
            if not paren.endswith(")"): paren = f"{paren})"
            terminal_content += f"{Colors.PARENTHETICAL}        {paren}{Colors.ENDC}\n"
            html_content.append(f"        <p class=\"parenthetical\">{paren}</p>")
            
        terminal_content += f"{Colors.DIALOGUE}    {text}{Colors.ENDC}\n\n"
        html_content.append(f"        <p class=\"dialogue\">{text}</p>")

    html_content.append("    </div>")
    html_content.append("</body>")
    html_content.append("</html>")

    output_filename = f"scene_{scene_number}.html"
    output_path = os.path.join(output_dir, output_filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(html_content))
        
    print(f"\n+++ Successfully generated script file: {output_path} +++\n")
    print("--- PREVIEW OF COMPILED SCENE ---")
    print(terminal_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert scene JSON to script HTML.")
    parser.add_argument("--input", type=str, required=True, help="Path to scene JSON file (required)")
    parser.add_argument("--output_dir", type=str, help="Directory to save the script", default=".")
    
    args = parser.parse_args()
    
    # Ensure relative paths are handled correctly if run from outside the directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, args.input) if not os.path.isabs(args.input) else args.input
    output_dir = os.path.join(current_dir, args.output_dir) if not os.path.isabs(args.output_dir) else args.output_dir
    
    if os.path.exists(input_path):
        generate_script_from_scene(input_path, output_dir)
    else:
        print(f"Error: Scene file not found at {input_path}")
