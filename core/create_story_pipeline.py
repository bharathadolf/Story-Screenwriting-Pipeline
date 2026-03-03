import os
import argparse

def create_structure(project_name, base_dir="."):
    """
    Creates the updated 5-stage directory structure.
    Each of the 5 stages has a WIP, REVIEW, APPROVED, and LOCKED status folder
    to govern the flow of data through the pipeline via publishing.
    """
    project_root = os.path.join(base_dir, f"{project_name}_STORY")
    
    # The 5 Core Stages
    stages = [
        "01_PLANNING",
        "02_CHARACTER_DEVELOPMENT",
        "03_OUTLINING",
        "04_DRAFTING",
        "05_REFINING"
    ]
    
    # Subdirectories for dataflow gates
    status_folders = ["WIP", "REVIEW", "APPROVED", "LOCKED"]
    
    # 1. Create Stage Directories with Status Subfolders
    for stage in stages:
        for status in status_folders:
            os.makedirs(os.path.join(project_root, stage, status), exist_ok=True)
            
    # 2. Add structural folders for Admin and Assets
    admin_folders = [
        "00_ADMIN/meeting_notes",
        "00_ADMIN/schedules",
        "PIPELINE_CONFIG"
    ]
    for admin_dir in admin_folders:
        os.makedirs(os.path.join(project_root, admin_dir), exist_ok=True)
        
    # 3. Create Placeholder Configs
    config_file = os.path.join(project_root, "PIPELINE_CONFIG", "project_config.yaml")
    if not os.path.exists(config_file):
         with open(config_file, 'w') as fh:
              fh.write(f"# Configuration for {project_name}\nproject_name: {project_name}\n")
              
    print(f"Successfully created 5-Stage Pipeline structure for '{project_name}' at '{os.path.abspath(project_root)}'")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate the 5-Stage Story Pipeline Folder Structure")
    parser.add_argument("project_name", help="Name of the project (e.g., MIDNIGHT)")
    parser.add_argument("--dir", default=".", help="Base directory to create the structure in")
    
    args = parser.parse_args()
    create_structure(args.project_name, args.dir)
