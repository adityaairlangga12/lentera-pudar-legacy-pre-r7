import os
import glob

skills_dir = 'D:/GodotProjects/Lentera-Pudar/.agents/skills'
skill_files = glob.glob(f"{skills_dir}/**/SKILL.md", recursive=True)

out = [
    "# Laporan Audit 15 Skill Proyek (.agents/skills/)",
    f"Total Skills: {len(skill_files)}\n",
    "| No | Folder / Skill Name | Name di Frontmatter | Deskripsi Trigger | Baris | Status Format |",
    "|---|---|---|---|---|---|"
]

all_details = []

for idx, path in enumerate(sorted(skill_files)):
    rel_path = os.path.relpath(path, skills_dir)
    skill_name = os.path.dirname(rel_path)
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    has_frontmatter = content.startswith('---')
    desc = ""
    name_in_fm = ""
    if has_frontmatter:
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm = parts[1]
            for line in fm.strip().split('\n'):
                if line.startswith('name:'):
                    name_in_fm = line.split('name:', 1)[1].strip()
                elif line.startswith('description:'):
                    desc = line.split('description:', 1)[1].strip()
    
    status = "OK" if (has_frontmatter and name_in_fm and desc) else "WARNING (No valid FM)"
    desc_short = (desc[:60] + '...') if len(desc) > 60 else desc
    out.append(f"| {idx+1} | `{skill_name}` | `{name_in_fm}` | {desc_short} | {len(lines)} | {status} |")
    
    all_details.append(f"## {idx+1}. Skill: `{skill_name}`\n- **Path**: `{path}`\n- **Frontmatter Name**: `{name_in_fm}`\n- **Description**: {desc}\n\n```markdown\n" + "\n".join(lines[:30]) + "\n...\n```\n\n---\n")

full_report = "\n".join(out) + "\n\n" + "\n".join(all_details)

with open('hasil diskusi/skills_audit_report.md', 'w', encoding='utf-8') as f:
    f.write(full_report)

print(f"Skills audit report generated at hasil diskusi/skills_audit_report.md ({len(skill_files)} skills audited)")
