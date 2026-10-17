# Policies Quick Reference for Computational Thinking (HCMUS FIT)

Source: `Policies.md` (Class: 25A01 / Course: CS252)

## 1. Directory Structure
```text
StudentID_WXX/
├── README.md               # Contains AI Usage Declaration & assignment overview
├── Git Commit Log.md       # Extracted Git commit history
├── Exercise01/             # All files for Exercise 1
├── Exercise02/             # All files for Exercise 2
├── ...
└── ExerciseYY/             # All files for Exercise YY
```
- `XX`: 2-digit week number (e.g. `01`, `02`).
- `YY`: 2-digit count of completed exercises (e.g. `05`).
- Final archive name: `StudentID_WXX_YY.zip` (e.g. `25125048_W01_05.zip`).

## 2. Deliverables by Assignment Type

### A. Reporting Assignments
- **Format**: Markdown (`.md`).
- **Rendered version**: Must submit BOTH `.md` file AND a rendered `.pdf` file (exported using the `yzane.markdown-pdf` extension).
- Store both side-by-side in the respective `ExerciseXX/` directory:
  - `Exercise01_Report.md`
  - `Exercise01_Report.pdf` (exported via `yzane.markdown-pdf`)

### B. Coding Assignments
- **Source code**: Only submit source code necessary to build and run the project.
- **Forbidden artifacts**: Do NOT include `node_modules/`, `bin/`, `obj/`, `.venv/`, `venv/`, `__pycache__/`, `.vs/`, or build binaries.
- **Instructions**: Submit instructions stating:
  - Execution environment (OS, language/compiler version, dependencies).
  - How to install/build the project.
  - Exact command lines to run the program.
- **Screenshots**: Include screenshots of the program running on student's machine showing commands run and output.

### C. Git Commit Log & Repositories
- Students must use a private repository on GitHub, Bitbucket, or GitLab.
- At least one commit with a meaningful commit message before the deadline.
- Extract git commit history:
  ```bash
  git log --graph --all --stat --since="YYYY-MM-DD 00:00:00" --until="YYYY-MM-DD 23:59:59"
  ```
- Store the output in `Git Commit Log.md` in the root of `StudentID_WXX/`.

### D. AI Usage Declaration
- Required in root `README.md`.
- Detail the AI tools used, purpose/prompts, and student verification.
- Answers submitted must represent the student's own verified understanding.

## 3. Moodle Submission Limits
- Maximum **20 files** per submission link.
- Maximum **20 MB** per file.
- If zip archive exceeds 20 MB, split into multiple zip parts (`part1.zip`, `part2.zip`).
- Cloud storage links (Google Drive, OneDrive, Dropbox) are strictly forbidden.
