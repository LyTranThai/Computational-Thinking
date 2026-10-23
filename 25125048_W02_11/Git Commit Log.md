# Git Commit Log for Week 02

- **Student ID:** 25125048
- **Author:** Lý Trần Thái
- **Repository:** https://github.com/LyTranThai/Computational-Thinking
- **Extracted Period:** October 18, 2026 to October 23, 2026

---

```text
* commit 3346e6555b07861e0c5fa0e6f6bf7dd9634d3c69
| Author: LyTranThai <lytranthai1234@gmail.com>
| Date:   Fri Oct 23 18:11:27 2026 +0700
| 
|     Complete initial exercises and local execution verification for Week 2 Basic Python
| 
|  25125048_W02_11/Exercise01/AC.png              | Bin 0 -> 5890 bytes
|  25125048_W02_11/Exercise01/LocalRun.png        | Bin 0 -> 76122 bytes
|  25125048_W02_11/Exercise01/input.txt           |   1 +
|  25125048_W02_11/Exercise01/solve.py            |  40 +++++++++
|  25125048_W02_11/Exercise02/LocalRun.png        | Bin 0 -> 95591 bytes
|  25125048_W02_11/Exercise02/input.txt           |   4 +
|  25125048_W02_11/Exercise02/solve.py            |  72 +++++++++++++++++
|  25125048_W02_11/Exercise03/AC.png              | Bin 0 -> 14861 bytes
|  25125048_W02_11/Exercise03/LocalRun.png        | Bin 0 -> 95315 bytes
|  25125048_W02_11/Exercise03/input.txt           |   2 +
|  25125048_W02_11/Exercise03/solve.py            |  98 +++++++++++++++++++++++
|  25125048_W02_11/Exercise04/AC.png              | Bin 0 -> 5484 bytes
|  25125048_W02_11/Exercise04/LocalRun.png        | Bin 0 -> 94877 bytes
|  25125048_W02_11/Exercise04/input.txt           |   1 +
|  25125048_W02_11/Exercise04/solve.py            |  43 ++++++++++
|  25125048_W02_11/Exercise05/AC.png              | Bin 0 -> 6127 bytes
|  25125048_W02_11/Exercise05/LocalRun.png        | Bin 0 -> 89119 bytes
|  25125048_W02_11/Exercise05/input.txt           |   7 ++
|  25125048_W02_11/Exercise05/solve.py            |  48 +++++++++++
|  25125048_W02_11/Exercise06/AC.png              | Bin 0 -> 5815 bytes
|  25125048_W02_11/Exercise06/LocalRun.png        | Bin 0 -> 95629 bytes
|  25125048_W02_11/Exercise06/input.txt           |   4 +
|  25125048_W02_11/Exercise06/solve.py            |  58 ++++++++++++++
|  25125048_W02_11/Exercise07/input.txt           |   7 ++
|  25125048_W02_11/Exercise07/solve.py            |  75 +++++++++++++++++
|  25125048_W02_11/Exercise11/TeamContribution.md |   0
|  Requirement/Lab02-Basic Python.md              |  56 +++++++++++++
|  27 files changed, 516 insertions(+)
| 
* commit 1b0b68e6e9e654712f80e03847198b78e6fb8b1f
| Author: LyTranThai <lytranthai1234@gmail.com>
| Date:   Thu Oct 22 14:46:36 2026 +0700
| 
|     Implement validation scripts and rubric engine for lab compliance auditing
| 
|  .agent/skills/check-lab-assignment/SKILL.md       | 165 +++++
|  .../references/compliance_checklist.md            | 108 ++++
|  .../references/remediation_guide.md               | 105 ++++
|  .../references/strict_rubric_engine.md            |  69 +++
|  .../scripts/verify_submission.py                  | 646 ++++++++++++++++++++
|  .agent/skills/lab-assignment/SKILL.md             |  26 +-
|  .../lab-assignment/scripts/package_submission.py  |  62 +-
|  25125048_W01/Git Commit Log.md                    |  69 ++-
|  8 files changed, 1205 insertions(+), 45 deletions(-)
| 
* commit 17a25ec236e483a4598673cee21ef0029ffd875d
| Author: LyTranThai <lytranthai1234@gmail.com>
| Date:   Sat Oct 17 10:44:52 2026 +0700
| 
|     Finalize and organize Week 01 submission deliverables per course policy
| 
|  .agent/skills/lab-assignment/SKILL.md             | 167 +++++++
|  .../lab-assignment/references/policies_summary.md |  55 +++
|  .../lab-assignment/scripts/package_submission.py  | 160 +++++++
|  .../skills/lab-assignment/scripts/render_html.py  | 469 ++++++++++++++++++++
|  .../templates/Git_Commit_Log_template.md          |  12 +
|  .../lab-assignment/templates/README_template.md   |  37 ++
|  .gitignore                                        |   9 +
|  .../Exercise01/Exercise01_Team_Formation.md       |  89 ++++
|  .../Exercise02/Exercise02_Team_Contract.md        |  65 +++
|  .../Exercise03_Individual_Proposal.md             | 104 +++++
|  25125048_W01/Exercise04/Exercise04_Git.md         |  84 ++++
|  .../Exercise05/Exercise05_Responsible_AI.md       |  87 ++++
|  25125048_W01/Git Commit Log.md                    |  19 +
|  25125048_W01/README.md                            |  41 ++
|  .../Lab01-Team Formation-Responsible AI Usage.md  | 116 +++++
|  Requirement/Policies.md                           | 149 +++++++
|  Week1/Exercise01/Exercise01_Team_Formation.md     |  89 ++++
|  Week1/Exercise01/Exercise01_Team_Formation.pdf    | Bin 0 -> 124248 bytes
|  Week1/Exercise02/Exercise02_Team_Contract.md      |  65 +++
|  Week1/Exercise02/Exercise02_Team_Contract.pdf     | Bin 0 -> 100577 bytes
|  .../Exercise03_Individual_Proposal.md             | 104 ++++
|  .../Exercise03_Individual_Proposal.pdf            | Bin 0 -> 81890 bytes
|  Week1/Exercise04/Exercise04_Git.md                |  84 +++
|  Week1/Exercise04/Exercise04_Git.pdf               | Bin 0 -> 130444 bytes
|  Week1/Exercise05/Exercise05_Responsible_AI.md     |  87 +++
|  Week1/Exercise05/Exercise05_Responsible_AI.pdf    | Bin 0 -> 127116 bytes
|  Week1/Git Commit Log.md                           |  19 +
|  Week1/README.md                                   |  41 ++
|  28 files changed, 2152 insertions(+)
```
