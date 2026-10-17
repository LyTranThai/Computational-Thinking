# Exercise 04: Git Repository Configuration & Collaboration Report

- **Course:** Computational Thinking (CS252 - Class 25A01)
- **Student ID:** 25125048
- **Student Name:** Lý Trần Thái
- **Personal GitHub Handle:** [@LyTranThai](https://github.com/LyTranThai)
- **Submission Date:** October 17, 2026

---

## 1. Task 1: Personal Repository Setup

In accordance with course policies, a private Git repository has been established on GitHub for managing all individual weekly lab assignments, exercises, and documentation for the Computational Thinking course.

### Personal Repository Details
- **Platform:** GitHub
- **Visibility:** Private
- **Repository URL:** [https://github.com/LyTranThai/Computational-Thinking](https://github.com/LyTranThai/Computational-Thinking)
- **Designated Git Username:** `LyTranThai`
- **Associated Email:** `25125048@student.hcmus.edu.vn` (and `145539003+LyTranThai@users.noreply.github.com`)

### Collaborator Access Verification
The course instructor and Teaching Assistant (TA) have been added as collaborators with read/write access to this private repository to facilitate continuous progress monitoring and grading:
- [x] Instructor added as collaborator
- [x] Teaching Assistant (TA) added as collaborator
- [x] Repository access verified

> **Commitment:** I confirm that my GitHub username (`LyTranThai`) will remain fixed and unchanged throughout the entire semester for all personal and group course submissions.

---

## 2. Task 2: Group Repository Setup & Team Roster

A dedicated private repository has been configured by the team on GitHub to host the source code, architecture specifications, sprint documentation, and deliverables for the CS252 Final Project.

### Group Repository Details
- **Platform:** GitHub
- **Visibility:** Private
- **Repository Name:** `cs252-final-project`
- **Repository URL:** [https://github.com/callmelucian/cs252-final-project](https://github.com/callmelucian/cs252-final-project)
- **Primary Owner / Administrator:** Nguyễn Tấn Minh ([@callmelucian](https://github.com/callmelucian))

### Team Member Roster & Git Identifiers
All seven team members have been added to the private repository with appropriate contributor permissions. The permanent Git usernames for all members are documented below:

| Student ID | Full Name | GitHub Username | Profile Link | Assigned Project Role |
| :--- | :--- | :--- | :--- | :--- |
| **25125027** | Nguyễn Tấn Minh | `callmelucian` | [github.com/callmelucian](https://github.com/callmelucian) | Team Leader |
| **25125084** | Trần Gia Huy | `FubuGold` | [github.com/FubuGold](https://github.com/FubuGold) | Main System Design |
| **25125050** | Bùi Đỗ Thiên Ân | `Gasmask-Chan` | [github.com/Gasmask-Chan](https://github.com/Gasmask-Chan) | Algorithm & Logic Developer |
| **25125014** | Nguyễn Đức Huy | `SpheraXX` | [github.com/SpheraXX](https://github.com/SpheraXX) | Front-end Developer |
| **25125048** | Lý Trần Thái | `LyTranThai` | [github.com/LyTranThai](https://github.com/LyTranThai) | Core Developer & Data Integration |
| **25125056** | Trần Đăng Khoa | `trankhoa8581` | [github.com/trankhoa8581](https://github.com/trankhoa8581) | Back-end Developer |
| **23125054** | Ngô Tấn Đạt | `diamondzone1` | [github.com/diamondzone1](https://github.com/diamondzone1) | Security & Data Engineer |

### Group Collaborator Access Checklist
- [x] All 7 team members added to repository permissions
- [x] Course Instructor invited as repository collaborator
- [x] Course Teaching Assistant invited as repository collaborator
- [x] Branch protection rule enabled on `main` branch (requires code review approval)

---

## 3. Git Environment & Local Configuration

To guarantee traceable and consistent commit history across all machines, the local Git environment has been verified:

```bash
# Verify Git global user configuration
git config --global user.name "LyTranThai"
git config --global user.email "145539003+LyTranThai@users.noreply.github.com"

# Check active remote connection
git remote -v
# Output:
# origin  https://github.com/LyTranThai/Computational-Thinking (fetch)
# origin  https://github.com/LyTranThai/Computational-Thinking (push)
```

### Git Workflow Standards
In alignment with `Exercise 02 (Team Contract)`:
1. **Branching Model:** Features are developed on dedicated branches (`feature/<name>`) branched from `dev`, then merged via Pull Request with peer review.
2. **Commit Conventions:** Structured messages using standardized prefixes (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`).
3. **Weekly Commit Audits:** Commit logs are systematically generated and verified prior to each weekly submission.
