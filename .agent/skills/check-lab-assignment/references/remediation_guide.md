# Remediation Guide: Resolving Lab Submission Audit Issues

This guide provides immediate instructions to resolve warnings and errors detected during submission compliance checks.

---

## 1. Missing PDF Companions in `ExerciseXX/`

**Error:** `Report 'ExerciseXX.md' is missing companion rendered PDF 'ExerciseXX.pdf'!`  
**Policy:** *"Submit both of the Markdown file and a rendered version (.pdf / .html) that displays the Markdown file correctly and attractively."*

### Resolution Steps:
1. Open the Markdown file in VS Code (e.g., `Exercise01_Team_Formation.md`).
2. Press `Ctrl+Shift+P` (Windows) to open the Command Palette.
3. Type: `Markdown PDF: Export (pdf)` and press Enter.
4. The extension (`yzane.markdown-pdf`) compiles the Markdown file using the configured Microsoft Edge headless binary and saves `Exercise01_Team_Formation.pdf` in the same directory.
5. Verify that the generated `.pdf` is placed in the respective `ExerciseXX/` folder alongside its `.md` source.

---

## 2. Invalid Zip Archive Structure / Incorrect Internal Root Folder

**Error:** `Root folder inside archive is 'Week1', but policy requires 'StudentID_WXX' (e.g. '25125048_W01')`  
**Policy:** The archive must unpack into `StudentID_WXX/`, not a generic name like `Week1/`.

### Resolution Steps:
1. Ensure your local folder is renamed to `StudentID_WXX` (e.g., `25125048_W01`).
2. Run the packaging helper script from the workspace root:
   ```powershell
   python .agent/skills/lab-assignment/scripts/package_submission.py 25125048_W01
   ```
3. This creates `StudentID_WXX_YY.zip` preserving the correct internal root folder path `StudentID_WXX/` and stripping any forbidden artifacts.

---

## 3. Missing or Incomplete AI Usage Declaration

**Error:** `README.md does not contain an 'AI Usage Declaration' section`  
**Policy:** Every submission must document AI assistance to maintain academic integrity.

### Resolution Steps:
Add the following Markdown table to `README.md`:

```markdown
## AI Usage Declaration

In compliance with the HCMUS FIT course academic integrity policy (CS252), the table below documents all AI tools, prompts, and student verifications utilized for this assignment:

| Exercise / Task | Tool Used | Purpose / Prompt Description | Student Verification & Refinement |
| :--- | :--- | :--- | :--- |
| **Overall Organization** | Antigravity AI / Gemini 3.8 Flash | Organizing files into ExerciseXX directories and checking policy rules. | Inspected directory layout against Policies.md and verified formatting. |
| **Exercise 01** | Tool Name | Prompt description | Verified facts, refined responses, confirmed calculations. |
| ... | ... | ... | ... |

### Academic Integrity Pledge
I certify that the deliverables submitted herein represent my own genuine work, ideas, and verification. External tools and AI assistants were used strictly for guidance and formatting in accordance with course policies.
```

---

## 4. Missing or Generic Git Commit Log

**Error:** `'Git Commit Log.md' appears empty` or `Detected generic commit message(s) ('update', 'test')`  
**Policy:** *"Each assignment requires at least one commit with a meaningful commit message, made before the deadline. Include git commit log in the submission."*

### Resolution Steps:
1. Make a substantive commit in your private repository with a clear description:
   ```bash
   git add .
   git commit -m "Complete Lab 01: Finalize team contract, proposals, and Git config"
   ```
2. Extract the formatted log for the week:
   ```powershell
   git log --graph --all --stat --since="YYYY-MM-DD 00:00:00" --until="YYYY-MM-DD 23:59:59" > "StudentID_WXX/Git Commit Log.md"
   ```
3. Wrap the content in a Markdown code block with student header information.

---

## 5. Forbidden Build Artifacts or Dependencies

**Error:** `Found forbidden files or folders: node_modules, bin, obj, .venv`  
**Policy:** *"Submit the source code needed to build and run the program. Do not include build artifacts or dependency folders (e.g., node_modules/, bin/, obj/, virtual environments)."*

### Resolution Steps:
1. Delete or exclude forbidden folders from the submission directory:
   ```powershell
   Remove-Item -Recurse -Force 25125048_W01/**/node_modules, 25125048_W01/**/bin, 25125048_W01/**/obj, 25125048_W01/**/.venv
   ```
2. Re-run `verify_submission.py` to confirm the submission directory is completely clean.

---

## 6. Archive Exceeds Moodle 20 MB Limit

**Error:** `Archive size exceeds Moodle 20 MB limit!`  
**Policy:** *"This Moodle submission link accepts a maximum of 20 files, with a size limit of 20 MB per file. If your submission exceeds 20 MB, please do not submit a Google Drive link. Instead, use the 'zip and split' feature."*

### Resolution Steps:
1. Verify large assets (e.g., uncompressed videos, large raw screenshots). Optimize images to PNG/JPG.
2. If total size remains $> 20\text{ MB}$, split into multi-part zip volumes using 7-Zip or PowerShell:
   ```powershell
   # 7-Zip CLI example (splits into 19MB parts):
   7z a -v19m StudentID_WXX_YY.zip StudentID_WXX/
   ```
