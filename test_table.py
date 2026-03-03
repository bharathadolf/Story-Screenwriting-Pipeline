def print_custom_help():
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    magenta = '\033[95m'
    reset = '\033[0m'

    print(f"\n{magenta}===================================================================================================================={reset}")
    print(f"{magenta}                                        STORY-TO-SCREENWRITING PIPELINE CLI                                         {reset}")
    print(f"{magenta}===================================================================================================================={reset}\n")
    print(f"Usage: {cyan}python main.py <command> [options]{reset}\n")
    
    general_cmds = [
        ("init", "Initialize 5-stage project structure. Args: project_name, [--dir]", "python main.py init MY_MOVIE"),
        ("publish", "Publish WIP artifacts to APPROVED folder. Args: --input, --destination", "python main.py publish --input ... --dest ...")
    ]
    
    dept_cmds = [
        ("plan", "Stage 1: Planning. Extracts Lore & Theme. Args: project_name, --input", "python main.py plan MY_MOVIE --input concept.json"),
        ("character", "Stage 2: Character Dev. Generates bibles. Args: project_name, --bible, --input", "python main.py character MY... --bible... --input..."),
        ("outline", "Stage 3: Outlining. Maps story beats. Args: project_name, --bible, --chars, --input", "python main.py outline MY... --bible... --chars..."),
        ("draft", "Stage 4: Drafting. Auto-writes scenes. Args: project_name, --chars, --outline", "python main.py draft MY... --chars... --outline..."),
        ("refine", "Stage 5: Refining. QA checks. Args: project_name, --drafts, --chars", "python main.py refine MY... --drafts... --chars...")
    ]
    
    def print_table(title, rows):
        print(f"{yellow}{title}{reset}")
        
        headers = ["Command", "Description", "Example Usage"]
        
        col_widths = [len(h) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                if len(cell) > col_widths[i]:
                    col_widths[i] = len(cell)
                    
        col_widths = [w + 2 for w in col_widths]
        
        def print_separator():
            sep = "+" + "+".join("-" * w for w in col_widths) + "+"
            print(f"{green}{sep}{reset}")
            
        print_separator()
        
        header_str = "|" + "|".join(f" {headers[i].ljust(col_widths[i]-1)}" for i in range(len(headers))) + "|"
        print(f"{green}{header_str}{reset}")
        print_separator()
        
        for row in rows:
            row_str = f"{green}|{reset}"
            for i, cell in enumerate(row):
                if i == 0:
                    row_str += f" {cyan}{cell.ljust(col_widths[i]-1)}{reset}{green}|{reset}"
                elif i == 2:
                    row_str += f" {yellow}{cell.ljust(col_widths[i]-1)}{reset}{green}|{reset}"
                else:
                    row_str += f" {cell.ljust(col_widths[i]-1)}{green}|{reset}"
            print(row_str)
            
        print_separator()
        print()
        
    print_table("General Operations:", general_cmds)
    print_table("Department Operations:", dept_cmds)

if __name__ == '__main__':
    print_custom_help()
