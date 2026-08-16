import os
import re
import sys

WORKSPACE_ROOT = r"d:\GodotProjects\Lentera-Pudar"

FILE_MAPPING = {
    # 01-core
    "creative-vision.md": "01-core/creative-vision.md",
    "design-decisions.md": "01-core/design-decisions.md",
    "game-design-document.md": "01-core/game-design-document.md",
    "master-index.md": "01-core/master-index.md",
    "theory-reference.md": "01-core/theory-reference.md",
    
    # 02-gameplay
    "ambient-world-life.md": "02-gameplay/ambient-world-life.md",
    "enemy-design-balancing.md": "02-gameplay/enemy-design-balancing.md",
    "level-design-storytelling.md": "02-gameplay/level-design-storytelling.md",
    "sector-ability-progression.md": "02-gameplay/sector-ability-progression.md",
    "ui-ux-accessibility.md": "02-gameplay/ui-ux-accessibility.md",
    
    # 03-narrative
    "cinematics-cutscenes.md": "03-narrative/cinematics-cutscenes.md",
    "prologue-tutorial-script.md": "03-narrative/prologue-tutorial-script.md",
    "vocal-direction-dialogue.md": "03-narrative/vocal-direction-dialogue.md",
    
    # 04-art-3d
    "additional-techniques.md": "04-art-3d/additional-techniques.md",
    "anatomy-kinesiology.md": "04-art-3d/anatomy-kinesiology.md",
    "expert-3d-foundations.md": "04-art-3d/expert-3d-foundations.md",
    "human-facial-expressions.md": "04-art-3d/human-facial-expressions.md",
    "kena-art-research.md": "04-art-3d/kena-art-research.md",
    "reference-board-guide.md": "04-art-3d/reference-board-guide.md",
    "style-guide.md": "04-art-3d/style-guide.md",
    
    # 05-foundations
    "expert-art-creativity.md": "05-foundations/expert-art-creativity.md",
    "expert-mathematics.md": "05-foundations/expert-mathematics.md",
    "expert-physics.md": "05-foundations/expert-physics.md",
    "expert-psychology.md": "05-foundations/expert-psychology.md",
    
    # 06-pipeline-qc
    "api-cheat-sheet.md": "06-pipeline-qc/api-cheat-sheet.md",
    "emotional-playtesting.md": "06-pipeline-qc/emotional-playtesting.md",
    "expert-ai-methodology.md": "06-pipeline-qc/expert-ai-methodology.md",
    "few-shot-calibration.md": "06-pipeline-qc/few-shot-calibration.md",
    "qa-qc-framework.md": "06-pipeline-qc/qa-qc-framework.md",
    "qc-patterns.md": "06-pipeline-qc/qc-patterns.md",
    "sop-workflow.md": "06-pipeline-qc/sop-workflow.md",
    "tools-mcp-stack.md": "06-pipeline-qc/tools-mcp-stack.md",
}

def update_links_in_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    orig_content = content
    for old_name, new_subpath in FILE_MAPPING.items():
        # Pattern 1: references/old_name (not already prefixed by 0X-...)
        # e.g., references/master-index.md -> references/01-core/master-index.md
        # Negative lookahead/behind to avoid double replacement
        pattern = re.compile(rf"(references/)(?!0[1-6]-)({re.escape(old_name)})")
        content = pattern.sub(rf"references/{new_subpath}", content)

    if content != orig_content:
        with open(filepath, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        return True
    return False

def verify_all_links():
    sys.stdout.reconfigure(encoding='utf-8')
    print("\n--- AUDITING ALL MARKDOWN LINKS ---")
    broken = []
    total_checked = 0
    link_pattern = re.compile(r"\[([^\]]+)\]\((file:///[^\)]+|references/[^\)]+)\)")

    for root, dirs, files in os.walk(WORKSPACE_ROOT):
        # Skip git and cache
        if ".git" in root or "__pycache__" in root:
            continue
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    text = f.read()
                
                for match in link_pattern.finditer(text):
                    link_text = match.group(1)
                    raw_url = match.group(2)
                    total_checked += 1
                    
                    # Clean up url (strip anchors)
                    url_clean = raw_url.split("#")[0]
                    
                    if url_clean.startswith("file:///"):
                        # Extract local absolute path
                        local_path = url_clean.replace("file:///", "").replace("/", "\\")
                        if not os.path.exists(local_path):
                            broken.append((filepath, raw_url, local_path))
                    elif url_clean.startswith("references/"):
                        local_path = os.path.join(WORKSPACE_ROOT, url_clean.replace("/", "\\"))
                        if not os.path.exists(local_path):
                            broken.append((filepath, raw_url, local_path))

    print(f"Total Markdown Links Checked: {total_checked}")
    if broken:
        print(f"[FAIL] FOUND {len(broken)} BROKEN LINKS:")
        for source, raw, loc in broken:
            print(f"  In {source}:\n    Raw: {raw}\n    Target Not Found: {loc}")
        return False
    else:
        print("[SUCCESS] ALL LINKS VALIDATED: 0 Broken Links Found!")
        return True

def main():
    print("Starting automated link updates...")
    updated_files = 0
    
    for root, dirs, files in os.walk(WORKSPACE_ROOT):
        if ".git" in root:
            continue
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                if update_links_in_file(filepath):
                    print(f"Updated: {filepath}")
                    updated_files += 1

    print(f"\nTotal files updated: {updated_files}")
    success = verify_all_links()
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
