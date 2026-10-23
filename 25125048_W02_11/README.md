# Lab Assignment - Week 02: Basic Python

- **Course:** Computational Thinking (25A01 - CS252)
- **Student ID:** 25125048
- **Full Name:** Lý Trần Thái
- **Personal Repository:** https://github.com/LyTranThai/Computational-Thinking
- **Group Repository:** https://github.com/callmelucian/cs252-final-project
- **Submission Date:** October 23, 2026

---

## Completed Exercises Summary

| Exercise | Topic / Problem | Author / Assistance | Deliverables |
| :--- | :--- | :--- | :--- |
| **Exercise 01** | [Codeforces 1A - Theatre Square](https://codeforces.com/problemset/problem/1/A) | Student (Independent Work) | `solve.py`, `input.txt`, `LocalRun.png`, `AC.png` |
| **Exercise 02** | [Codeforces 2A - Winner](https://codeforces.com/problemset/problem/2/A) | **AI Assisted (Requested by Student)** | `solve.py`, `input.txt`, `LocalRun.png` |
| **Exercise 03** | [Codeforces 3A - Shortest path of the king](https://codeforces.com/problemset/problem/3/A) | Student (Independent Work) | `solve.py`, `input.txt`, `LocalRun.png`, `AC.png` |
| **Exercise 04** | [Codeforces 4A - Watermelon](https://codeforces.com/problemset/problem/4/A) | Student (Independent Work) | `solve.py`, `input.txt`, `LocalRun.png`, `AC.png` |
| **Exercise 05** | [Codeforces 5A - Chat server's outgoing traffic](https://codeforces.com/problemset/problem/5/A) | Student (Independent Work) | `solve.py`, `input.txt`, `LocalRun.png`, `AC.png` |
| **Exercise 06** | [Codeforces 6B - President's Office](https://codeforces.com/problemset/problem/6/B) | Student (Independent Work) | `solve.py`, `input.txt`, `LocalRun.png`, `AC.png` |
| **Exercise 07** | [Codeforces 7B - Memory Manager](https://codeforces.com/problemset/problem/7/B) | **AI Assisted (Requested by Student)** | `solve.py`, `input.txt` |
| **Exercise 08** | [Codeforces 8B - Obsession with Robots](https://codeforces.com/problemset/problem/8/B) | **AI Assisted (Requested by Student)** | `solve.py` |
| **Exercise 09** | [Codeforces 9B - Running Student](https://codeforces.com/problemset/problem/9/B) | **AI Assisted (Requested by Student)** | `solve.py` |
| **Exercise 10** | [Codeforces 10B - Cinema Cashier](https://codeforces.com/problemset/problem/10/B) | **AI Assisted (Requested by Student)** | `solve.py` |
| **Exercise 11** | Group Project Contribution & Git Commit Log | Student (Assisted by AI for brief summary) | `TeamContribution.md`, `git_log.txt` |

> **Note on Directives & Scope of AI Assistance:**
> As explicitly instructed by the student, the AI assistant was tasked **ONLY** with providing source code solutions for **Exercise 2, Exercise 7, Exercise 8, Exercise 9, and Exercise 10**. No image files were generated or modified by AI. All other exercises (1, 3, 4, 5, 6, 11) were independently solved and prepared by the student.

---

## AI Usage Declaration

In compliance with the HCMUS FIT course academic integrity policy (CS252), the table below documents all AI tools, prompts, and student verifications utilized for this assignment:

| Task / Exercise | Tool Used | Purpose / Prompt Description | Student Verification & Refinement |
| :--- | :--- | :--- | :--- |
| **Scope Delegation** | Antigravity AI (Gemini 3.8 Flash) | Explicit instruction: *"Complete exercise 2, 7, 8, 9, 10 ONLY. Do not do other exercise that are not listed. You do not need to provide image as required, only provide the source code."* | Confirmed that only the specified exercises were modified/created and all other student work was preserved. |
| **Exercise 02 (CF 2A: Winner)** | Antigravity AI (Gemini 3.8 Flash) | Refactor competitive programming logic to track maximum final score, filter candidates, and identify earliest round reaching $\ge \text{max\_score}$. | Reviewed `solve.py`, verified tie-breaker rule and test input against problem specification. |
| **Exercise 07 (CF 7B: Memory Manager)** | Antigravity AI (Gemini 3.8 Flash) | Implement simulation for memory operations: first-fit contiguous block allocation (`alloc`), ID validation and cleanup (`erase`), and compaction shifting (`defragment`). | Inspected linear memory bounds ($m \le 100$), verified sample cases (`alloc 5`, `alloc 3`, `erase 1`, `alloc 6`, `defragment`, `alloc 6`). |
| **Exercise 08 (CF 8B: Obsession with Robots)** | Antigravity AI (Gemini 3.8 Flash) | Check if robot trajectory could represent a shortest path by verifying coordinate uniqueness and adjacency of non-consecutive steps. | Verified 4-neighborhood step check logic, confirmed edge cases with loops and adjacent cell shortcuts. |
| **Exercise 09 (CF 9B: Running Student)** | Antigravity AI (Gemini 3.8 Flash) | Calculate minimal total transit time combining bus travel $x_i / v_b$ and running distance $\text{dist} / v_s$ for stops $i \ge 2$, with Euclidean tie-breaking. | Validated floating-point tolerance ($\varepsilon = 10^{-9}$), confirmed that stop 1 is disallowed per problem rules. |
| **Exercise 10 (CF 10B: Cinema Cashier)** | Antigravity AI (Gemini 3.8 Flash) | Implement $K \times K$ cinema seating simulation minimizing Manhattan centrality cost to center $((K+1)/2, (K+1)/2)$ with row/column tie-breakers. | Verified 2D grid allocation, consecutive seat availability checks, and edge cases where request cannot be fulfilled (output `-1`). |
| **Exercise 11 (Group Contribution)** | Antigravity AI (Gemini 3.8 Flash) | Prompted to briefly refine and structure the weekly group project contribution summary and git log export. | Verified alignment with student's assigned project role (Core Developer & Data Integration) and weekly deliverables. |

---

## Academic Integrity Pledge

I certify that the deliverables submitted herein represent my own genuine work, ideas, and verification. External tools and AI assistants were used strictly for algorithmic guidance, implementation refinement, and structuring in accordance with course policies.

---
*Generated and verified for HCMUS FIT CS252 - Computational Thinking (Class 25A01).*
