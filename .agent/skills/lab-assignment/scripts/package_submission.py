#!/usr/bin/env python3
"""
package_submission.py - Verify and package assignment submissions according to Policies.md
Structure:
  StudentID_WXX/
  ├── README.md (AI Usage Declaration & summary)
  ├── Git Commit Log.md
  ├── Exercise01/
  ├── Exercise02/
  ...
Compresses into: StudentID_WXX_YY.zip (where YY = count of completed exercises)
"""

import sys
import os
import re
import shutil
import zipfile
import subprocess
from pathlib import Path

# Add scripts directory to path to import render_html
script_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(script_dir))
try:
    from render_html import render_markdown_file
except ImportError:
    render_markdown_file = None

FORBIDDEN_DIRS = {"node_modules", "bin", "obj", ".venv", "venv", "__pycache__", ".git", ".vs", ".idea"}

def get_git_commit_log(repo_root, since=None, until=None):
    cmd = ["git", "log", "--graph", "--all", "--stat"]
    if since:
        cmd.append(f"--since={since}")
    if until:
        cmd.append(f"--until={until}")
    try:
        res = subprocess.run(cmd, cwd=repo_root, capture_output=True, text=True, check=True)
        return res.stdout
    except Exception as e:
        return f"# Git Commit Log\n\nError executing git log: {e}\n"

def validate_and_package(submission_dir, output_dir=None, auto_render=True, auto_git_log=True, since=None, until=None):
    sub_path = Path(submission_dir).resolve()
    if not sub_path.is_dir():
        print(f"[ERROR] Directory does not exist: {sub_path}")
        return False

    folder_name = sub_path.name
    match = re.match(r'^(\d+)_W(\d+)$', folder_name, re.IGNORECASE)
    if not match:
        print(f"[WARNING] Folder name '{folder_name}' does not strictly match 'StudentID_WXX' format (e.g., 25125048_W01).")
        student_id = "StudentID"
        week_num = "WXX"
    else:
        student_id = match.group(1)
        week_num = f"W{match.group(2).zfill(2)}"

    print(f"=== Validating Submission: {folder_name} ===")

    # 1. Check / auto-generate Git Commit Log.md if needed
    git_log_file = sub_path / "Git Commit Log.md"
    if auto_git_log and (not git_log_file.exists() or git_log_file.stat().st_size == 0):
        print(f"[INFO] Generating '{git_log_file.name}' from git repository...")
        repo_root = sub_path.parent
        log_content = get_git_commit_log(repo_root, since=since, until=until)
        formatted_log = f"# Git Commit Log for Week {week_num}\n\n**Student ID:** {student_id}\n\n```text\n{log_content.strip()}\n```\n"
        git_log_file.write_text(formatted_log, encoding='utf-8')
        print(f"[OK] Wrote {git_log_file.name}")

    # 2. Check README.md
    readme_file = sub_path / "README.md"
    if not readme_file.exists():
        print(f"[WARNING] 'README.md' (with AI Usage Declaration) is missing in {sub_path.name}.")
    else:
        print(f"[OK] Found README.md")

    # 3. Discover Exercise folders
    exercise_dirs = sorted([d for d in sub_path.iterdir() if d.is_dir() and re.match(r'^Exercise\d+$', d.name, re.IGNORECASE)])
    yy_count = len(exercise_dirs)
    yy_str = f"{yy_count:02d}"
    print(f"[INFO] Detected {yy_count} Exercise folders: {[d.name for d in exercise_dirs]}")

    if yy_count == 0:
        print("[WARNING] No 'ExerciseXX' folders found! Please ensure exercises are placed inside Exercise01, Exercise02, etc.")

    # 4. Check exercise contents & forbidden items
    total_files = 0
    clean = True

    for ex_dir in exercise_dirs:
        print(f"\nChecking {ex_dir.name}:")
        files = [f for f in ex_dir.iterdir() if f.is_file()]
        dirs = [d for d in ex_dir.iterdir() if d.is_dir()]

        for d in dirs:
            if d.name in FORBIDDEN_DIRS:
                print(f"  [DANGER] Forbidden directory found: {d.name} (Policy: do not submit build/virtualenv artifacts!)")
                clean = False

        md_files = [f for f in files if f.suffix.lower() == '.md']
        pdf_files = [f for f in files if f.suffix.lower() == '.pdf']

        for md in md_files:
            expected_pdf = md.with_suffix('.pdf')
            if expected_pdf.exists():
                print(f"  [OK] Found PDF companion: {expected_pdf.name}")
            else:
                print(f"  [NOTICE] Missing PDF for {md.name} -> Export using 'yzane.markdown-pdf' in VS Code (Markdown PDF: Export (pdf)).")

        # Recount files
        files = [f for f in ex_dir.iterdir() if f.is_file()]
        for f in files:
            print(f"  - {f.name} ({f.stat().st_size / 1024:.1f} KB)")
            total_files += 1

    # Add root files
    root_files = [f for f in sub_path.iterdir() if f.is_file()]
    total_files += len(root_files)
    print(f"\nRoot files count: {len(root_files)}")
    print(f"Total files in submission: {total_files}")

    if total_files > 20:
        print(f"[WARNING] Total files ({total_files}) exceeds Moodle link maximum of 20 files!")

    # 5. Create zip archive: StudentID_WXX_YY.zip
    target_zip_name = f"{student_id}_{week_num}_{yy_str}.zip"
    out_dir = Path(output_dir).resolve() if output_dir else sub_path.parent
    zip_target_path = out_dir / target_zip_name

    print(f"\n[INFO] Creating archive: {zip_target_path} ...")
    with zipfile.ZipFile(zip_target_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in sub_path.rglob('*'):
            # skip forbidden files/folders
            rel_path = file_path.relative_to(sub_path.parent)
            parts = rel_path.parts
            if any(p in FORBIDDEN_DIRS for p in parts):
                continue
            if file_path.is_file():
                zipf.write(file_path, arcname=rel_path)

    zip_size_mb = zip_target_path.stat().st_size / (1024 * 1024)
    print(f"[OK] Archive successfully created: {zip_target_path.name} ({zip_size_mb:.2f} MB)")

    if zip_size_mb > 20.0:
        print(f"[ALERT] Archive size ({zip_size_mb:.2f} MB) exceeds Moodle 20MB limit! Please split the archive.")
    else:
        print(f"[COMPLIANT] Size is within Moodle limit (< 20 MB).")

    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python package_submission.py <submission_folder> [output_dir]")
        sys.exit(1)

    sub_dir = sys.argv[1]
    out_d = sys.argv[2] if len(sys.argv) > 2 else None
    validate_and_package(sub_dir, out_d)
