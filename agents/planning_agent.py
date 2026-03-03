import json
import os
import argparse
import sys

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("\n[!] The 'google-genai' library is required for the new Agentic Planning loop.")
    print("Please install it by running: pip install google-genai\n")
    sys.exit(1)

def write_project_bible(project_name: str, wip_dir: str, content: str) -> str:
    """Tool: Saves the project bible to the WIP folder."""
    os.makedirs(wip_dir, exist_ok=True)
    output_path = os.path.join(wip_dir, f"{project_name}_project_bible.json")
    try:
        # We ensure it's valid JSON
        json_data = json.loads(content)
        with open(output_path, 'w') as f:
            json.dump(json_data, f, indent=4)
        return f"SUCCESS: Wrote project bible to {output_path}."
    except json.JSONDecodeError:
        return "ERROR: The content provided was not valid JSON. Please provide a valid JSON string."
    except Exception as e:
        return f"ERROR writing to file: {e}"

def notify_human_for_feedback(message: str) -> str:
    """Tool: Displays a message to the human and pauses to wait for their feedback/approval."""
    print(f"\n[AGENT REQUEST] {message}")
    print("[HUMAN INPUT REQUIRED] Type 'Approve' to finalize, or type instructions to modify the bible:")
    user_input = input("> ").strip()
    return user_input

def run_planning(project_name, project_dir, input_file):
    """
    STAGE 1: PLANNING (Agentic Workflow)
    Acts an autonomous Showrunning Agent.
    """
    print(f"--- [STAGE 1: PLANNING] Spawning Agent for {project_name} ---")
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("\n[!] Error: GEMINI_API_KEY environment variable is missing.")
        print("Please set your Gemini API key (e.g. `$env:GEMINI_API_KEY='your_key'`) to run this agent.")
        return None
        
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} not found.")
        return None
        
    with open(input_file, 'r') as f:
        try:
            premise_data = json.load(f)
            premise_str = json.dumps(premise_data, indent=2)
        except json.JSONDecodeError:
            print("Error: Input file must be valid JSON.")
            return None

    wip_dir = os.path.join(project_dir, f"{project_name}_STORY", "01_PLANNING", "WIP")

    client = genai.Client()
    
    # Define Tools
    def write_bible_wrapper(content: str) -> str:
        return write_project_bible(project_name, wip_dir, content)
        
    tools = [write_bible_wrapper, notify_human_for_feedback]

    system_instruction = f"""You are the master Showrunner Agent for a story-to-screenwriting pipeline.
Your objective is to turn the user's raw premise into a comprehensive 'Project Bible'.
The Project Bible MUST be a valid JSON object matching this schema:
{{
  "project": "{project_name}",
  "logline": "A compelling 1-2 sentence logline",
  "synopsis": "A 3-paragraph synopsis",
  "themes": ["theme 1", "theme 2"],
  "world_rules": ["rule 1", "rule 2", "societal constraint"]
}}

Process instructions:
1. First, analyze the raw premise and privately brainstorm the lore, themes, and full synopsis.
2. Build the JSON string and call `write_bible_wrapper(content)` to save your draft.
3. Call `notify_human_for_feedback(message)` to ask the user to review the drafted file. 
4. If the user gives feedback to change the story, you MUST address the feedback, rewrite the JSON, call `write_bible_wrapper(content)` again, and then call `notify_human_for_feedback` again.
5. If the user types 'Approve' or 'approve', you must say "Goodbye" to end the interaction. Do not loop further.
"""

    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        tools=tools,
        temperature=0.7
    )

    print("Agent is thinking...\n")
    
    chat = client.chats.create(model="gemini-1.5-pro", config=config)
    
    initial_prompt = f"Here is the raw premise for '{project_name}':\n```json\n{premise_str}\n```\nPlease begin your task."
    
    try:
        response = chat.send_message(initial_prompt)
        
        while True:
            if response.function_calls:
                for function_call in response.function_calls:
                    if function_call.name == "write_bible_wrapper":
                        content = function_call.args.get("content", "")
                        result = write_bible_wrapper(content)
                        response = chat.send_message({'function_responses': [{'name': 'write_bible_wrapper', 'response': {'result': result}}]})
                        break # Break to handle next response
                        
                    elif function_call.name == "notify_human_for_feedback":
                        message = function_call.args.get("message", "Please provide feedback:")
                        human_input = notify_human_for_feedback(message)
                        
                        response = chat.send_message({'function_responses': [{'name': 'notify_human_for_feedback', 'response': {'result': human_input}}]})
                        
                        if human_input.strip().lower() == "approve":
                            print("\n[SYSTEM] Agentic loop approved and finalized!")
                            return os.path.join(wip_dir, f"{project_name}_project_bible.json")
                        
                        break # break inner loop to evaluate new response
            else:
                # If the model didn't call a function, it's just talking. 
                # Check if it said Goodbye after an approval.
                if "goodbye" in response.text.lower():
                     print("\n[SYSTEM] Agent completed successfully.")
                     return os.path.join(wip_dir, f"{project_name}_project_bible.json")
                else:
                    # If it's just chatting randomly, force it to notify the human.
                    print(f"Agent says: {response.text}")
                    response = chat.send_message("Please use `notify_human_for_feedback` if you need input, or `write_bible_wrapper` to save.")
                    
    except Exception as e:
        print(f"\n[!] Agentic loop crashed: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--dir", default=".")
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    
    run_planning(args.project, args.dir, args.input)

