# Policies Compliance Checklist for Lab Assignments

*HCMUS FIT - Computational Thinking (CS252 / Class 25A01)*  
*Source Document: `Requirement/Policies.md`*

---

## 1. Naming & Packaging Rules

| Item | Requirement Specification | Strictness | Check Method |
| :--- | :--- | :--- | :--- |
| **Directory Name** | Must match `StudentID_WXX` (e.g., `25125048_W01`). | **MANDATORY** | Regex `^\d{8}_W\d{2}$` |
| **Archive Name** | Must match `StudentID_WXX_YY.zip` (e.g., `25125048_W01_05.zip`). `XX` = 2-digit week, `YY` = 2-digit count of completed exercises. | **MANDATORY** | Regex `^\d{8}_W\d{2}_\d{2}\.zip$` |
| **Zip Root Folder** | Top-level folder inside `.zip` MUST be `StudentID_WXX/`, matching the archive prefix. Never `Week1/` or unnested loose files. | **MANDATORY** | Archive header inspection |
| **Moodle File Limit** | Total files in submission link $\le 20$ files. | **MANDATORY** | File count check |
| **Moodle Size Limit** | Maximum **20 MB** per file. If $> 20\text{ MB}$, use zip split (`part1.zip`, `part2.zip`). | **MANDATORY** | File size check |
| **No Cloud Links** | Submitting Google Drive, OneDrive, or Dropbox links instead of files is strictly forbidden. | **MANDATORY** | Link audit |

---

## 2. Root Level Deliverables

Only two files are permitted at the root of `StudentID_WXX/`:

### A. `README.md`
- [ ] Contains Student ID, Full Name, Class (25A01), and Course (CS252).
- [ ] Contains links to Personal Private Repository and Group Repository.
- [ ] Summary of completed exercises with topics and deliverables.
- [ ] **AI Usage Declaration** (Strict Requirement):
  - Structured Markdown table detailing:
    1. Exercise / Task
    2. Tool Used (e.g., ChatGPT, Claude, Antigravity AI)
    3. Purpose / Prompts used
    4. Student Verification & Refinement statement
- [ ] **Academic Integrity Pledge**: Explicit statement certifying answers submitted represent the student's own verified understanding.

### B. `Git Commit Log.md`
- [ ] Extracted using official command:
  ```bash
  git log --graph --all --stat --since="YYYY-MM-DD 00:00:00" --until="YYYY-MM-DD 23:59:59"
  ```
- [ ] Contains at least one commit made before the deadline.
- [ ] Commit messages must be meaningful (flags: "update", "asdf", "test", "commit").
- [ ] Commit author matches student's identity.

---

## 3. Directory Organization

```text
StudentID_WXX/
├── README.md               # AI Usage Declaration, overview, repo links
├── Git Commit Log.md       # Extracted Git commit history
├── Exercise01/             # All files for Exercise 1
├── Exercise02/             # All files for Exercise 2
├── ...
└── ExerciseYY/             # All files for Exercise YY
```

- [ ] Every completed exercise has a dedicated directory: `Exercise01/`, `Exercise02/`, ..., `ExerciseYY/`.
- [ ] Zero loose exercise files at root level.
- [ ] Total number of `ExerciseXX` subdirectories equals `YY` in `StudentID_WXX_YY.zip`.

---

## 4. Forbidden Artifacts & Directory Cleanliness

The submission **MUST NOT** include build artifacts, virtual environments, or system caches:
- [ ] `node_modules/`
- [ ] `bin/`, `obj/`
- [ ] `.venv/`, `venv/`, `env/`
- [ ] `__pycache__/`, `*.pyc`
- [ ] `.vs/`, `.idea/`
- [ ] `.git/` (do not zip the actual `.git` folder)
- [ ] `.DS_Store`, `Thumbs.db`, `desktop.ini`
- [ ] Executable binaries: `*.exe`, `*.dll`, `*.so`, `*.dylib`

---

## 5. Deliverable Specifics by Exercise Type

### Type A: Reporting Assignments
- [ ] Written in clean Markdown (`.md`).
- [ ] High visual presentation quality: clear headings, Markdown tables, code blocks.
- [ ] **Both formats required**: Must submit BOTH `.md` report AND rendered `.pdf` file.
  - Exported using VS Code extension `yzane.markdown-pdf`.
  - Both `.md` and `.pdf` files reside together in the respective `ExerciseXX/` folder.

### Type B: Coding Assignments
- [ ] Source code required to build and run the program included.
- [ ] No compiled binaries or dependency folders.
- [ ] Environment and build/run instructions included:
  - Operating system
  - Language and compiler version
  - External dependencies
  - Exact command lines to install, build, and run
- [ ] Screenshots showing:
  - Program running on the student's machine
  - Command line entered
  - Program output resulting from execution

---

## 6. Academic Integrity & Anti-Cheating

- [ ] Submissions must represent the student's genuine personal work.
- [ ] Internet and AI hints/instructions are permitted, but direct copying is prohibited.
- [ ] Similar submissions receive 0 points for all lab results and are reported to the lecturer.
