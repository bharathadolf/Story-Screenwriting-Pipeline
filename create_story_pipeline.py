import os
import argparse

def create_structure(project_name, base_dir="."):
    project_root = os.path.join(base_dir, f"{project_name}_STORY")
    
    # List of directories to create based on the specified structure
    directories = [
        "00_ADMIN/contracts",
        "00_ADMIN/schedules/department_timelines",
        "00_ADMIN/meeting_notes/development",
        "00_ADMIN/meeting_notes/production",
        "00_ADMIN/meeting_notes/post",
        "00_ADMIN/approvals/gate_signoffs",
        "00_ADMIN/approvals/change_requests",
        "00_ADMIN/contacts",
        
        "01_DEVELOPMENT/01_ideas/brainstorm_sessions",
        "01_DEVELOPMENT/01_ideas/concept_cards",
        "01_DEVELOPMENT/01_ideas/pitch_documents",
        "01_DEVELOPMENT/02_research/genre_analysis",
        "01_DEVELOPMENT/02_research/comparable_titles",
        "01_DEVELOPMENT/02_research/audience_research",
        "01_DEVELOPMENT/02_research/technical_feasibility",
        "01_DEVELOPMENT/02_research/reference_materials",
        "01_DEVELOPMENT/03_synopsis/v01_initial",
        "01_DEVELOPMENT/03_synopsis/v02_revision",
        "01_DEVELOPMENT/03_synopsis/LOCKED",
        "01_DEVELOPMENT/04_bibles/world_bible/geography",
        "01_DEVELOPMENT/04_bibles/world_bible/history",
        "01_DEVELOPMENT/04_bibles/world_bible/culture",
        "01_DEVELOPMENT/04_bibles/world_bible/rules_systems",
        "01_DEVELOPMENT/04_bibles/world_bible/visual_references",
        "01_DEVELOPMENT/04_bibles/character_bible/protagonists",
        "01_DEVELOPMENT/04_bibles/character_bible/antagonists",
        "01_DEVELOPMENT/04_bibles/character_bible/supporting",
        "01_DEVELOPMENT/04_bibles/character_bible/relationship_maps",
        "01_DEVELOPMENT/04_bibles/theme_bible",
        "01_DEVELOPMENT/05_approvals/story_approval",
        "01_DEVELOPMENT/05_approvals/design_approval",
        "01_DEVELOPMENT/05_approvals/greenlight_documents",
        
        "02_PREPROD/01_outlines/beat_sheets",
        "02_PREPROD/01_outlines/step_outlines",
        "02_PREPROD/01_outlines/structure_analysis/pacing_charts",
        "02_PREPROD/02_treatments/v01_rough",
        "02_PREPROD/02_treatments/v02_polished",
        "02_PREPROD/02_treatments/LOCKED",
        "02_PREPROD/03_beatboards/act_one",
        "02_PREPROD/03_beatboards/act_two_a",
        "02_PREPROD/03_beatboards/act_two_b",
        "02_PREPROD/03_beatboards/act_three",
        "02_PREPROD/03_beatboards/sequence_breakdowns",
        "02_PREPROD/04_characters/passports",
        "02_PREPROD/04_characters/arc_charts",
        "02_PREPROD/04_characters/voice_samples",
        "02_PREPROD/05_previs/storyboard_sketches",
        "02_PREPROD/05_previs/sequence_tests",
        "02_PREPROD/05_previs/pacing_experiments",
        
        "03_PRODUCTION/01_drafts/v01_first_draft",
        "03_PRODUCTION/01_drafts/v02_revision",
        "03_PRODUCTION/01_drafts/v03_polish",
        "03_PRODUCTION/01_drafts/v04_production",
        "03_PRODUCTION/01_drafts/DAILIES",
        "03_PRODUCTION/02_notes/internal/dailies_feedback",
        "03_PRODUCTION/02_notes/internal/department_notes",
        "03_PRODUCTION/02_notes/external/producer_notes",
        "03_PRODUCTION/02_notes/external/studio_notes",
        "03_PRODUCTION/02_notes/external/test_screening",
        "03_PRODUCTION/03_locked",
        "03_PRODUCTION/04_scene_cards/by_act",
        "03_PRODUCTION/04_scene_cards/by_character",
        "03_PRODUCTION/05_qc_reports/logic_checks",
        "03_PRODUCTION/05_qc_reports/emotional_beat_analysis",
        "03_PRODUCTION/05_qc_reports/consistency_reports",
        
        "04_POST/01_shooting_script/final_shooting",
        "04_POST/01_shooting_script/scene_breakdown",
        "04_POST/01_shooting_script/character_sides",
        "04_POST/02_rewrites/on_set",
        "04_POST/02_rewrites/adr_scripts",
        "04_POST/02_rewrites/pickup_notes",
        "04_POST/03_deliverables",
        "04_POST/04_archive/all_versions",
        "04_POST/04_archive/deprecated",
        
        "05_ASSETS/templates",
        "05_ASSETS/reference/scripts",
        "05_ASSETS/reference/books",
        "05_ASSETS/reference/visual",
        "05_ASSETS/tools",
        
        "PIPELINE_CONFIG"
    ]
    
    # Placeholder files to instantiate
    files = {
        "00_ADMIN/schedules/master_schedule.xlsx": "",
        "00_ADMIN/schedules/milestone_tracker.xlsx": "",
        "00_ADMIN/contacts/team_directory.xlsx": "",
        
        "01_DEVELOPMENT/01_ideas/logline_library.txt": "Logline Library\n\n",
        f"01_DEVELOPMENT/03_synopsis/LOCKED/{project_name}_synopsis_FINAL.pdf": "",
        "01_DEVELOPMENT/04_bibles/theme_bible/thematic_questions.txt": "Thematic Questions\n\n",
        "01_DEVELOPMENT/04_bibles/theme_bible/emotional_arc_guide.pdf": "",
        
        f"02_PREPROD/01_outlines/beat_sheets/{project_name}_beat_v01.xlsx": "",
        f"02_PREPROD/01_outlines/beat_sheets/{project_name}_beat_LOCKED.xlsx": "",
        f"02_PREPROD/01_outlines/step_outlines/{project_name}_step_v01.docx": "",
        f"02_PREPROD/02_treatments/LOCKED/{project_name}_treatment_FINAL.pdf": "",
        "02_PREPROD/04_characters/passports/CHARNAME_passport.pdf": "",
        f"02_PREPROD/04_characters/arc_charts/{project_name}_arcs.xlsx": "",
        "02_PREPROD/04_characters/voice_samples/CHARNAME_voice.txt": "Voice Samples\n\n",
        "02_PREPROD/04_characters/relationship_matrix.xlsx": "",
        
        f"03_PRODUCTION/01_drafts/v01_first_draft/{project_name}_v01_ACT1.fdx": "",
        f"03_PRODUCTION/01_drafts/v01_first_draft/{project_name}_v01_ACT2A.fdx": "",
        f"03_PRODUCTION/01_drafts/v01_first_draft/{project_name}_v01_ACT2B.fdx": "",
        f"03_PRODUCTION/01_drafts/v01_first_draft/{project_name}_v01_ACT3.fdx": "",
        "03_PRODUCTION/02_notes/internal/revision_tracking.xlsx": "",
        "03_PRODUCTION/02_notes/integration_log.xlsx": "",
        f"03_PRODUCTION/03_locked/{project_name}_LOCKED_WHITE.fdx": "",
        f"03_PRODUCTION/03_locked/{project_name}_LOCKED_BLUE.fdx": "",
        f"03_PRODUCTION/03_locked/{project_name}_LOCKED_PINK.fdx": "",
        
        "04_POST/03_deliverables/final_script.pdf": "",
        "04_POST/03_deliverables/production_bible.pdf": "",
        "04_POST/03_deliverables/style_guide.pdf": "",
        "04_POST/04_archive/project_wrap_report.pdf": "",
        
        "05_ASSETS/templates/character_passport_template.docx": "",
        "05_ASSETS/templates/beat_sheet_template.xlsx": "",
        "05_ASSETS/templates/scene_card_template.docx": "",
        "05_ASSETS/templates/qc_checklist_template.xlsx": "",
        
        "05_ASSETS/tools/naming_validator.py": "# Naming validator script\n",
        "05_ASSETS/tools/beat_analyzer.py": "# Beat analyzer script\n",
        "05_ASSETS/tools/consistency_checker.py": "# Consistency checker script\n",
        
        "PIPELINE_CONFIG/project_config.yaml": f"# Configuration for {project_name}\nproject_name: {project_name}\n",
        "PIPELINE_CONFIG/department_assignments.xlsx": "",
        "PIPELINE_CONFIG/approval_thresholds.yaml": "# Approval thresholds\n",
        "PIPELINE_CONFIG/version_control_policy.txt": "Version Control Policy\n\n"
    }
    
    # Status subfolders for working directories
    status_folders = ["WIP", "REVIEW", "REVISION", "APPROVED", "LOCKED", "DEPRECATED"]
    working_directories = [
        "01_DEVELOPMENT/01_ideas",
        "01_DEVELOPMENT/03_synopsis",
        "01_DEVELOPMENT/04_bibles/world_bible",
        "01_DEVELOPMENT/04_bibles/character_bible",
        "01_DEVELOPMENT/04_bibles/theme_bible",
        "02_PREPROD/01_outlines",
        "02_PREPROD/02_treatments",
        "02_PREPROD/03_beatboards",
        "02_PREPROD/04_characters",
        "03_PRODUCTION/01_drafts",
        "03_PRODUCTION/04_scene_cards"
    ]
    
    # 1. Create main directories
    for d in directories:
        dir_path = os.path.join(project_root, d)
        os.makedirs(dir_path, exist_ok=True)
        
    # 2. Create status subfolders inside key working directories
    for wd in working_directories:
        for status in status_folders:
            os.makedirs(os.path.join(project_root, wd, status), exist_ok=True)
            
    # 3. Create placeholder files
    for f, content in files.items():
        file_path = os.path.join(project_root, f)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as fh:
            fh.write(content)
            
    print(f"Successfully created pipeline structure for project '{project_name}' at '{os.path.abspath(project_root)}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Story-to-Screenwriting Pipeline Folder Structure")
    parser.add_argument("project_name", help="Name of the project (e.g., MIDNIGHT)")
    parser.add_argument("--dir", default=".", help="Base directory to create the structure in")
    
    args = parser.parse_args()
    create_structure(args.project_name, args.dir)
