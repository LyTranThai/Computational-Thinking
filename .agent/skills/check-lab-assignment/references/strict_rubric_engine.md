# Strict Rubric Engine & Grading Reference

*HCMUS FIT - Computational Thinking (CS252 / Class 25A01)*  
*Auditor Mode:* **Strictly READ-ONLY (No modifications permitted)**

---

## 1. Operating Rules for the Auditor

> [!CAUTION]
> **READ-ONLY CONSTRAINT:**
> `/check-lab-assignment` is strictly an evaluator. It must **NEVER** edit, move, create, split, rename, or delete any files or directories in the student's submission directory. All modifications are the responsibility of the student or `/lab-assignment`.

### Dynamic Requirement-First Workflow:
1. **Re-Read Weekly Requirement Document (`LabYY...md`) First**:
   - The auditor must read the full Markdown requirement document for that week.
   - Enumerate all exercises (e.g. `Exercise 1`, `Exercise 2`, ... `Exercise N`).
   - Extract the specific questions, sub-tasks, prompts, and deliverable types for each exercise.
   - Dynamically build the expected file/folder manifest:
     - Root: `README.md` and `Git Commit Log.md` ONLY.
     - Subfolders: `Exercise01/` through `ExerciseYY/`.
2. **Audit Target**: The active working folder `StudentID_WXX` (e.g. `25125048_W01`).
3. **Zip Self-Check**: Archive packaging (`StudentID_WXX_YY.zip`) is self-checked by the student; the automated checker focuses directly on the folder.

---

## 2. 10.0-Point Base Scoring Rubric

The grade is calculated out of **10.00 points total**.

For $N$ exercises in the weekly requirement:
$$W_i = \frac{10.0}{N} \quad (\text{Base weight per exercise})$$
*(For Lab 01 with 5 exercises, each exercise is worth $2.00\text{ pts}$.)*

### Sub-Criteria per Exercise:
Every exercise $i$ is graded against 3 criteria:

| Sub-Criterion | Weight (% of Ex) | Lab 01 Weight ($2.0\text{ pts}$) | Evaluation Standard |
| :--- | :---: | :---: | :--- |
| **1. Prompt & Sub-task Coverage** | **50%** | **$1.00\text{ pt}$** | Itemized check against every explicit question, prompt, and required section in `LabYY`. Partial credit is proportional to the fraction of sub-tasks satisfied. |
| **2. Deliverable Pairing** | **30%** | **$0.60\text{ pt}$** | - **Reporting:** Companion rendered `.pdf` file present alongside `.md` report in `ExerciseXX/` (exported via `yzane.markdown-pdf`). Missing `.pdf` forfeits all deliverable points.<br>- **Coding:** Clean source code, execution guide (OS, compiler, commands), and actual execution screenshots with visible outputs. |
| **3. Depth, Rigor & Quality** | **20%** | **$0.40\text{ pt}$** | Substantive depth (no placeholder text, no one-sentence answers), clear Markdown structure (tables, headers), independent thinking. |

---

## 3. Global Course Policy Penalties (`Policies.md`)

These deductions are subtracted directly from the total score:

| Code | Violation Description | Severity | Impact | Policy Rationale |
| :--- | :--- | :---: | :---: | :--- |
| **CRIT-01** | **Loose files at root folder** | **CRITICAL FLAW** | **$-2.00\text{ pts}$** | Violates mandatory directory hierarchy. Only `README.md` and `Git Commit Log.md` allowed at root. All work must be inside `ExerciseXX/`. |
| **CRIT-02** | Forbidden build artifacts present (`node_modules`, `bin`, `obj`, `.venv`, `__pycache__`, `.vs`) | **CRITICAL FLAW** | **$-3.00\text{ pts}$** | Policy strictly forbids build artifacts and virtualenvs. |
| **CRIT-03** | Missing root `README.md` | **CRITICAL FLAW** | **$-2.00\text{ pts}$** | Root metadata and declaration missing. |
| **CRIT-04** | Missing root `Git Commit Log.md` | **CRITICAL FLAW** | **$-1.50\text{ pts}$** | Verification of individual version control missing. |
| **MAJ-01** | Missing or non-tabular AI Usage Declaration in `README.md` | **MAJOR** | **$-1.50\text{ pts}$** | Mandatory academic integrity compliance rule. |
| **MAJ-02** | Git Commit Log empty or missing `--graph --all --stat` format | **MAJOR** | **$-1.00\text{ pt}$** | Incomplete git log extraction. |
| **MIN-01** | Generic / non-descriptive commit messages (`"update"`, `"asdf"`, `"test"`) | **MINOR** | **$-0.50\text{ pt}$** | Policy requires meaningful commit messages before deadline. |
| **MIN-02** | Missing Academic Integrity Pledge in `README.md` | **MINOR** | **$-0.50\text{ pt}$** | Formal pledge statement omitted. |

*(Note: Total file count $> 20$ is strictly an informational advisory for Moodle, **never a grading penalty**).*

---

## 4. Final Grade Formula

$$\text{Content Score} = \sum_{i=1}^N \text{Score}(Ex_i) \quad (\text{Max } 10.0)$$
$$\text{Policy Penalties} = \sum \text{Deductions}$$
$$\text{Final Grade} = \max(0.00, \, \text{Content Score} - \text{Policy Penalties})$$
