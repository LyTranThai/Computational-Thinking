#!/usr/bin/env python3
"""
verify_submission.py - Comprehensive Lab Assignment Checker for Computational Thinking (HCMUS FIT)
Audits and grades student submission directories strictly in READ-ONLY mode against Policies.md
and dynamically parsed weekly requirement documents (LabYY...md).
"""

import sys
import os
import re
import argparse
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# --- Forbidden Items per Policies.md ---
FORBIDDEN_DIRS = {
    "node_modules", "bin", "obj", ".venv", "venv", "env",
    "__pycache__", ".git", ".vs", ".idea", ".gradle", "build", "dist"
}

FORBIDDEN_FILES = {
    ".ds_store", "thumbs.db", "desktop.ini"
}

FORBIDDEN_EXTENSIONS = {
    ".exe", ".dll", ".so", ".dylib", ".o", ".obj", ".class", ".pyc"
}

GENERIC_COMMIT_MESSAGES = {
    "update", "updates", "fixed", "fix", "done", "asdf", "test", "commit",
    "first commit", "initial commit", "wip", "upload files", "add files"
}

class ProblemItem:
    def __init__(self, code, severity, location, policy_clause, impact_pts, details, fix):
        self.code = code
        self.severity = severity # "CRITICAL", "MAJOR", "MINOR", "ADVISORY"
        self.location = location
        self.policy_clause = policy_clause
        self.impact_pts = impact_pts
        self.details = details
        self.fix = fix


class ExerciseAudit:
    def __init__(self, number, title, folder_name, max_pts):
        self.number = number
        self.title = title
        self.folder_name = folder_name
        self.max_pts = max_pts
        self.coverage_score = 0.0 # max 0.50 * max_pts
        self.deliverable_score = 0.0 # max 0.30 * max_pts
        self.quality_score = 0.0 # max 0.20 * max_pts
        self.findings = []
        self.traceability = []

    @property
    def total_earned(self):
        return round(self.coverage_score + self.deliverable_score + self.quality_score, 2)

    @property
    def status(self):
        if self.total_earned >= self.max_pts * 0.95:
            return "✅ Pass"
        elif self.total_earned > 0:
            return "⚠️ Partial"
        return "❌ Missing"


def resolve_requirement_path(req_path, target_dir):
    """
    Intelligently resolves requirement file path across multiple potential relative root locations.
    """
    if not req_path:
        return None
    p = Path(req_path)
    if p.exists():
        return p.resolve()

    target = Path(target_dir).resolve()
    # Check relative to target folder
    if (target / req_path).exists():
        return (target / req_path).resolve()
    # Check relative to target's parent (e.g. Lab\Week1 -> Lab\Requirement\...)
    if (target.parent / req_path).exists():
        return (target.parent / req_path).resolve()
    # Check relative to target's parent's parent
    if (target.parent.parent / req_path).exists():
        return (target.parent.parent / req_path).resolve()

    # Search by filename in target and ancestor directories
    file_name = p.name
    search_roots = [target.parent, target, target.parent.parent]
    for root in search_roots:
        if root.exists():
            matches = list(root.rglob(file_name))
            if matches:
                return matches[0].resolve()

    return None


def parse_weekly_requirement(resolved_req_path):
    """
    Dynamically reads and parses the weekly requirement document (LabYY...md).
    Returns a list of exercises and extracted prompts/sub-tasks.
    """
    if not resolved_req_path or not Path(resolved_req_path).exists():
        return None

    content = Path(resolved_req_path).read_text(encoding='utf-8', errors='ignore')
    exercises = []

    # Match headers like '## Exercise 1 - Team Formation' or '## Exercise01'
    pattern = re.compile(r'^(#{1,3})\s+Exercise\s*(\d+)[:\s\-–—]*(.*)$', re.IGNORECASE | re.MULTILINE)
    matches = list(pattern.finditer(content))

    for idx, match in enumerate(matches):
        ex_num = int(match.group(2))
        title = match.group(3).strip() or f"Exercise {ex_num}"
        start_pos = match.end()
        end_pos = matches[idx + 1].start() if idx + 1 < len(matches) else len(content)
        ex_body = content[start_pos:end_pos].strip()

        # Extract sub-tasks or bullet prompts
        sub_prompts = []
        for line in ex_body.splitlines():
            clean_line = line.strip()
            if clean_line.lower().startswith('### references') or clean_line.lower() == 'references':
                continue
            if clean_line.startswith('-') or clean_line.startswith('*') or clean_line.startswith('###') or clean_line.endswith('?'):
                prompt_text = re.sub(r'^[#\-\*\s]+', '', clean_line).strip()
                # Exclude purely reference links or short non-prompt tokens
                if len(prompt_text) > 5 and not prompt_text.lower().startswith(('http', '<u>http', 'references')):
                    sub_prompts.append(prompt_text)

        exercises.append({
            "number": ex_num,
            "title": title,
            "folder_name": f"Exercise{ex_num:02d}",
            "body": ex_body,
            "sub_prompts": sub_prompts
        })

    return exercises


def audit_submission(target_dir, requirement_path=None):
    target = Path(target_dir).resolve()
    problems = []
    policy_penalties = 0.0

    if not target.exists() or not target.is_dir():
        print(f"[FATAL] Target directory does not exist or is not a folder: {target}")
        sys.exit(1)

    # 1. Folder naming check (StudentID_WXX)
    folder_name = target.name
    match = re.match(r'^(\d+)_W(\d+)$', folder_name, re.IGNORECASE)
    student_id = match.group(1) if match else "StudentID"
    week_num = f"W{match.group(2).zfill(2)}" if match else "WXX"

    if not match:
        problems.append(ProblemItem(
            code="CRIT-NAME",
            severity="CRITICAL",
            location=folder_name,
            policy_clause="Policies.md - Submission folder structure: StudentID_WXX",
            impact_pts=0.0, # Structural naming flag
            details=f"Folder name '{folder_name}' does not strictly follow 'StudentID_WXX' format (e.g., 25125048_W01).",
            fix="Rename folder to match your 8-digit Student ID and 2-digit week (e.g. 25125048_W01)."
        ))

    # 2. Check for CRITICAL FLAW: Loose files at root
    root_files = [f for f in target.iterdir() if f.is_file()]
    allowed_root_names = {"readme.md", "git commit log.md"}
    loose_files = [f.name for f in root_files if f.name.lower() not in allowed_root_names]
    loose_penalty = 0.0

    if loose_files:
        loose_penalty = 2.00
        policy_penalties += loose_penalty
        problems.append(ProblemItem(
            code="CRIT-01",
            severity="CRITICAL",
            location=f"{folder_name}/",
            policy_clause="Policies.md - Submission folder structure: Only README.md and Git Commit Log.md at root",
            impact_pts=loose_penalty,
            details=f"CRITICAL STRUCTURAL FLAW: Found {len(loose_files)} loose work file(s) at root ({', '.join(loose_files)}). All exercise deliverables must be inside ExerciseXX/ subdirectories.",
            fix="Move all loose files into their corresponding ExerciseXX/ subfolders."
        ))

    # 3. Check for CRITICAL FLAW: Forbidden build artifacts & dependencies
    all_files = list(target.rglob('*'))
    forbidden_found = []
    for f in all_files:
        rel = f.relative_to(target)
        parts_lower = [p.lower() for p in rel.parts]
        for part in parts_lower:
            if part in FORBIDDEN_DIRS:
                forbidden_found.append(str(rel))
                break
        if f.is_file():
            if f.name.lower() in FORBIDDEN_FILES or f.suffix.lower() in FORBIDDEN_EXTENSIONS:
                forbidden_found.append(str(rel))

    artifact_penalty = 0.0
    if forbidden_found:
        artifact_penalty = 3.00
        policy_penalties += artifact_penalty
        problems.append(ProblemItem(
            code="CRIT-02",
            severity="CRITICAL",
            location=f"{folder_name}/",
            policy_clause="Policies.md - Coding assignments: Do not include build artifacts or dependency folders",
            impact_pts=artifact_penalty,
            details=f"Found forbidden files/directories:\n    " + "\n    ".join(forbidden_found[:5]),
            fix="Delete all build, virtualenv, and system cache folders (e.g., node_modules, bin, obj, .venv, __pycache__)."
        ))

    # 4. Check total files count (Moodle informational advisory, NOT a grading penalty)
    file_count = len([f for f in all_files if f.is_file()])
    if file_count > 20:
        problems.append(ProblemItem(
            code="ADV-01",
            severity="ADVISORY",
            location=f"{folder_name}/",
            policy_clause="Policies.md - Moodle submission link accepts a maximum of 20 files",
            impact_pts=0.00,
            details=f"Total file count is {file_count}, which exceeds Moodle's 20-file limit. (Informational only: No grading penalty).",
            fix="Ensure files are packaged appropriately when submitting to Moodle."
        ))

    # 5. Check Root README.md & AI Usage Declaration
    readme_path = target / "README.md"
    readme_penalty = 0.0
    if not readme_path.exists():
        readme_penalty = 2.00
        policy_penalties += readme_penalty
        problems.append(ProblemItem(
            code="CRIT-03",
            severity="CRITICAL",
            location=f"{folder_name}/README.md",
            policy_clause="Policies.md - Root deliverables: README.md (file)",
            impact_pts=readme_penalty,
            details="Root 'README.md' is missing entirely.",
            fix="Create 'README.md' at the root with student details, exercise overview, and AI Usage Declaration."
        ))
    else:
        readme_content = readme_path.read_text(encoding='utf-8', errors='ignore')
        # Check AI Usage Declaration
        has_ai_decl = re.search(r'AI\s+Usage\s+Declaration', readme_content, re.IGNORECASE)
        has_table = "|" in readme_content and re.search(r'Tool|Prompt|Verification', readme_content, re.IGNORECASE)
        has_pledge = re.search(r'Academic\s+Integrity\s+Pledge|own\s+genuine\s+work|own\s+work', readme_content, re.IGNORECASE)

        if not has_ai_decl or not has_table:
            ai_penalty = 1.50
            policy_penalties += ai_penalty
            problems.append(ProblemItem(
                code="MAJ-01",
                severity="MAJOR",
                location=f"{folder_name}/README.md",
                policy_clause="Policies.md - README.md: AI Usage Declaration",
                impact_pts=ai_penalty,
                details="Missing or non-tabular 'AI Usage Declaration' in README.md. Policy requires documenting tools, prompts/purposes, and verification in a table.",
                fix="Add a Markdown table under '## AI Usage Declaration' listing Tool Used, Purpose/Prompt, and Student Verification."
            ))

        if not has_pledge:
            pledge_penalty = 0.50
            policy_penalties += pledge_penalty
            problems.append(ProblemItem(
                code="MIN-02",
                severity="MINOR",
                location=f"{folder_name}/README.md",
                policy_clause="Policies.md - Collaboration and cheating policy",
                impact_pts=pledge_penalty,
                details="Missing explicit Academic Integrity Pledge certifying submitted answers represent student's own verified understanding.",
                fix="Add an Academic Integrity Pledge certifying that external AI tools were used ethically and work is verified personal understanding."
            ))

    # 6. Check Root Git Commit Log.md
    git_log_path = target / "Git Commit Log.md"
    git_penalty = 0.0
    if not git_log_path.exists():
        git_penalty = 1.50
        policy_penalties += git_penalty
        problems.append(ProblemItem(
            code="CRIT-04",
            severity="CRITICAL",
            location=f"{folder_name}/Git Commit Log.md",
            policy_clause="Policies.md - Root deliverables: Git Commit Log.md",
            impact_pts=git_penalty,
            details="Root 'Git Commit Log.md' is missing.",
            fix="Extract git commit history using 'git log --graph --all --stat' and save to 'Git Commit Log.md'."
        ))
    else:
        git_content = git_log_path.read_text(encoding='utf-8', errors='ignore')
        if len(git_content.strip()) < 40 or not ("commit " in git_content.lower() or "author:" in git_content.lower()):
            log_fmt_penalty = 1.00
            policy_penalties += log_fmt_penalty
            problems.append(ProblemItem(
                code="MAJ-02",
                severity="MAJOR",
                location=f"{folder_name}/Git Commit Log.md",
                policy_clause="Policies.md - Git commit log command: git log --graph --all --stat",
                impact_pts=log_fmt_penalty,
                details="'Git Commit Log.md' is empty or does not contain standard git log graph/stat output.",
                fix="Run: git log --graph --all --stat --since='YYYY-MM-DD 00:00:00' --until='YYYY-MM-DD 23:59:59' and save output in the file."
            ))

        # Check for generic commit messages
        flagged_messages = []
        for line in git_content.splitlines():
            cleaned = line.strip().lower()
            if cleaned in GENERIC_COMMIT_MESSAGES:
                flagged_messages.append(line.strip())

        if flagged_messages:
            msg_penalty = 0.50
            policy_penalties += msg_penalty
            problems.append(ProblemItem(
                code="MIN-01",
                severity="MINOR",
                location=f"{folder_name}/Git Commit Log.md",
                policy_clause="Policies.md - At least one commit with a meaningful commit message",
                impact_pts=msg_penalty,
                details=f"Detected generic commit message(s) in git history: {', '.join(set(flagged_messages[:3]))}. Policy mandates meaningful commit messages.",
                fix="Use descriptive commit messages detailing completed features/exercises in your repository."
            ))

    # 7. Dynamic Exercise-Driven Quality Audit & Rubric Scoring
    resolved_req_path = resolve_requirement_path(requirement_path, target)
    raw_exercises = parse_weekly_requirement(resolved_req_path) if resolved_req_path else None

    if requirement_path and not resolved_req_path:
        problems.append(ProblemItem(
            code="WARN-REQ-PATH",
            severity="ADVISORY",
            location=str(requirement_path),
            policy_clause="Requirement Document Resolution",
            impact_pts=0.00,
            details=f"Requirement file '{requirement_path}' could not be found at target/relative paths. Auditing based on discovered Exercise folders.",
            fix="Provide the path to the weekly LabYY Markdown requirement file."
        ))

    # Fallback to directory-based exercise discovery if no requirement file provided or found
    if not raw_exercises:
        discovered_dirs = sorted([d for d in target.iterdir() if d.is_dir() and re.match(r'^Exercise\d+$', d.name, re.IGNORECASE)])
        if discovered_dirs:
            raw_exercises = []
            for d in discovered_dirs:
                m = re.match(r'^Exercise(\d+)$', d.name, re.IGNORECASE)
                num = int(m.group(1)) if m else len(raw_exercises) + 1
                raw_exercises.append({
                    "number": num,
                    "title": f"Exercise {num:02d}",
                    "folder_name": d.name,
                    "body": "",
                    "sub_prompts": []
                })

    exercise_audits = []

    if raw_exercises:
        num_ex = len(raw_exercises)
        weight_per_ex = round(10.0 / num_ex, 2)
        total_assigned_weights = weight_per_ex * num_ex

        for raw_ex in raw_exercises:
            ex_num = raw_ex["number"]
            ex_title = raw_ex["title"]
            folder_target_name = raw_ex["folder_name"]
            audit = ExerciseAudit(ex_num, ex_title, folder_target_name, weight_per_ex)

            # Discover folder
            matched_folder = None
            for d in target.iterdir():
                if d.is_dir() and re.match(rf'^Exercise0?{ex_num}$', d.name, re.IGNORECASE):
                    matched_folder = d
                    break

            if not matched_folder:
                audit.findings.append(f"Folder '{folder_target_name}/' is MISSING.")
                problems.append(ProblemItem(
                    code="CRIT-EX-MISSING",
                    severity="CRITICAL",
                    location=f"{folder_name}/{folder_target_name}/",
                    policy_clause=f"Policies.md - Submission folder structure: {folder_target_name}/",
                    impact_pts=weight_per_ex,
                    details=f"Exercise {ex_num} ({ex_title}) directory '{folder_target_name}' is missing.",
                    fix=f"Create folder '{folder_target_name}/' and add all required deliverables for Exercise {ex_num}."
                ))
                exercise_audits.append(audit)
                continue

            # Audit files inside ExerciseXX
            ex_files = list(matched_folder.iterdir())
            md_files = [f for f in ex_files if f.is_file() and f.suffix.lower() == '.md']
            pdf_files = [f for f in ex_files if f.is_file() and f.suffix.lower() == '.pdf']
            code_files = [f for f in ex_files if f.is_file() and f.suffix.lower() in {'.py', '.cpp', '.c', '.h', '.java', '.js', '.ts', '.html', '.css', '.sh'}]
            img_files = [f for f in ex_files if f.is_file() and f.suffix.lower() in {'.png', '.jpg', '.jpeg', '.gif'}]

            # Deliverables Scoring (30% of exercise weight)
            deliv_max = round(weight_per_ex * 0.30, 2)
            has_deliv_error = False

            if not ex_files:
                audit.findings.append(f"Folder '{folder_target_name}/' is empty.")
                problems.append(ProblemItem(
                    code="CRIT-EMPTY",
                    severity="CRITICAL",
                    location=f"{folder_name}/{folder_target_name}/",
                    policy_clause="Policies.md - All submitted files for ExXX",
                    impact_pts=weight_per_ex,
                    details=f"Directory '{folder_target_name}' contains no files.",
                    fix=f"Add deliverables for Exercise {ex_num} into '{folder_target_name}/'."
                ))
            else:
                # Reporting check: Every .md must have a companion .pdf
                for md in md_files:
                    companion_pdf = md.with_suffix('.pdf')
                    if companion_pdf.exists():
                        audit.findings.append(f"Found Markdown and companion PDF: {md.name} & {companion_pdf.name}")
                    else:
                        has_deliv_error = True
                        problems.append(ProblemItem(
                            code="CRIT-DELIV",
                            severity="CRITICAL",
                            location=f"{folder_name}/{folder_target_name}/{md.name}",
                            policy_clause="Policies.md - Submit both of the Markdown file and a rendered version (.pdf / .html)",
                            impact_pts=deliv_max,
                            details=f"Report '{md.name}' is missing companion rendered PDF '{companion_pdf.name}'.",
                            fix=f"Open '{md.name}' in VS Code and run 'Markdown PDF: Export (pdf)' to generate the PDF companion."
                        ))

                if code_files:
                    if not img_files:
                        problems.append(ProblemItem(
                            code="MAJ-SCREENSHOT",
                            severity="MAJOR",
                            location=f"{folder_name}/{folder_target_name}/",
                            policy_clause="Policies.md - Coding assignments: include screenshots of the program running",
                            impact_pts=round(deliv_max * 0.5, 2),
                            details=f"Coding exercise detected in '{folder_target_name}', but no execution screenshots (.png/.jpg) found.",
                            fix="Add screenshots showing the commands run and program output on your machine."
                        ))
                    else:
                        audit.findings.append(f"Found source code and execution screenshot(s): {', '.join([i.name for i in img_files])}")

                if not has_deliv_error:
                    audit.deliverable_score = deliv_max

            # Content Coverage Scoring (50% of exercise weight)
            coverage_max = round(weight_per_ex * 0.50, 2)
            sub_prompts = raw_ex.get("sub_prompts", [])
            combined_md_text = ""
            for md in md_files:
                combined_md_text += md.read_text(encoding='utf-8', errors='ignore') + "\n"

            if combined_md_text:
                if sub_prompts:
                    matched_prompts = 0
                    for p in sub_prompts:
                        keywords = [w.lower() for w in re.findall(r'\b[A-Za-z]{4,}\b', p)]
                        match_count = sum(1 for kw in keywords if kw in combined_md_text.lower())
                        ratio = match_count / max(1, len(keywords))
                        if ratio >= 0.4:
                            matched_prompts += 1
                            audit.traceability.append((p, True))
                        else:
                            audit.traceability.append((p, False))

                    coverage_ratio = matched_prompts / len(sub_prompts)
                    audit.coverage_score = round(coverage_max * coverage_ratio, 2)
                    if coverage_ratio < 0.7:
                        problems.append(ProblemItem(
                            code="MAJ-COVERAGE",
                            severity="MAJOR",
                            location=f"{folder_name}/{folder_target_name}/",
                            policy_clause=f"Weekly Requirement: Exercise {ex_num} Prompts",
                            impact_pts=round(coverage_max - audit.coverage_score, 2),
                            details=f"Exercise {ex_num} answers only {matched_prompts}/{len(sub_prompts)} prompts from the requirement document.",
                            fix=f"Review '{Path(requirement_path).name}' and answer all unaddressed questions for Exercise {ex_num}."
                        ))
                else:
                    audit.coverage_score = coverage_max
                    audit.traceability.append((f"Exercise {ex_num} General Content", True))
            else:
                audit.coverage_score = 0.0

            # Quality Scoring (20% of exercise weight)
            quality_max = round(weight_per_ex * 0.20, 2)
            if len(combined_md_text.strip()) > 500 and ("|" in combined_md_text or "```" in combined_md_text or "###" in combined_md_text):
                audit.quality_score = quality_max
            elif len(combined_md_text.strip()) > 150:
                audit.quality_score = round(quality_max * 0.6, 2)
            else:
                audit.quality_score = 0.0

            exercise_audits.append(audit)

    # Calculate Totals
    content_subtotal = sum(ea.total_earned for ea in exercise_audits) if exercise_audits else 0.0
    final_grade = max(0.00, round(content_subtotal - policy_penalties, 2))

    return {
        "folder_name": folder_name,
        "student_id": student_id,
        "week_num": week_num,
        "requirement_file": resolved_req_path.name if resolved_req_path else (f"Not Found: {requirement_path}" if requirement_path else "Directory Fallback (No Requirement Specified)"),
        "file_count": file_count,
        "exercise_audits": exercise_audits,
        "content_subtotal": content_subtotal,
        "policy_penalties": policy_penalties,
        "final_grade": final_grade,
        "problems": problems
    }


def render_report(report_data):
    fn = report_data["folder_name"]
    rf = report_data["requirement_file"]
    grade = report_data["final_grade"]
    problems = report_data["problems"]
    ea_list = report_data["exercise_audits"]

    crit_problems = [p for p in problems if p.severity == "CRITICAL"]
    maj_problems = [p for p in problems if p.severity == "MAJOR"]
    min_problems = [p for p in problems if p.severity == "MINOR"]
    adv_problems = [p for p in problems if p.severity == "ADVISORY"]

    status_badge = "✅ FULLY COMPLIANT" if not crit_problems and not maj_problems and grade >= 9.5 else "⚠️ ACTION REQUIRED"

    print("\n" + "=" * 78)
    print(f"📋 LAB ASSIGNMENT COMPLIANCE & GRADING REPORT: {fn}")
    print("=" * 78)
    print(f"Target Directory:    {fn}")
    print(f"Requirement File:    {rf}")
    print(f"Auditor Mode:        🔒 STRICTLY READ-ONLY (No files modified)")
    print(f"Overall Final Grade: {grade:.2f} / 10.00")
    print(f"Status:              {status_badge}")
    print("=" * 78 + "\n")

    # 1. Executive Scorecard
    print("## 1. Executive Scorecard\n")
    print(f"{'Component / Exercise':<35} | {'Max':<5} | {'Earned':<6} | {'Status':<10} | {'Findings / Deductions'}")
    print("-" * 88)

    for ea in ea_list:
        deduction_note = f"Missing companion PDF (-{round(ea.max_pts * 0.3, 2)} pts)" if ea.deliverable_score == 0 and ea.max_pts > 0 else "All deliverables verified"
        print(f"Exercise {ea.number:02d}: {ea.title[:21]:<21} | {ea.max_pts:<5.2f} | {ea.total_earned:<6.2f} | {ea.status:<10} | {deduction_note}")

    print("-" * 88)
    print(f"{'Content Subtotal':<35} | 10.00 | {report_data['content_subtotal']:<6.2f} |            |")
    print("-" * 88)

    # Policy Penalties summary
    print(f"{'Policy Penalties':<35} |  0.00 | -{report_data['policy_penalties']:<5.2f} | {'⚠️ Penalties' if report_data['policy_penalties'] > 0 else '✅ Clean':<10} | Total policy deductions")
    print("=" * 88)
    print(f"{'FINAL GRADE':<35} | 10.00 | {report_data['final_grade']:<6.2f} | {status_badge:<10} | Final recalibrated score\n")

    # 2. Exhaustive Problem Ledger
    print("\n## 2. Exhaustive Problem Ledger\n")
    if not problems:
        print("  🎉 No policy violations, deliverable flaws, or prompt deficiencies detected!\n")
    else:
        if crit_problems:
            print("### 🚨 CRITICAL FLAWS & POLICY BLOCKERS")
            for idx, p in enumerate(crit_problems, 1):
                print(f"{idx}. [{p.code}] {p.policy_clause}")
                print(f"   • Location: {p.location}")
                print(f"   • Impact:   -{p.impact_pts:.2f} pts" if p.impact_pts > 0 else "   • Impact:   CRITICAL STRUCTURAL FLAG")
                print(f"   • Details:  {p.details}")
                print(f"   • Fix:      {p.fix}\n")

        if maj_problems:
            print("### ⚠️ MAJOR REQUIREMENT & CONTENT DEFICIENCIES")
            for idx, p in enumerate(maj_problems, 1):
                print(f"{idx}. [{p.code}] {p.policy_clause}")
                print(f"   • Location: {p.location}")
                print(f"   • Impact:   -{p.impact_pts:.2f} pts")
                print(f"   • Details:  {p.details}")
                print(f"   • Fix:      {p.fix}\n")

        if min_problems:
            print("### ℹ️ MINOR ADVISORIES & QUALITY WARNINGS")
            for idx, p in enumerate(min_problems, 1):
                print(f"{idx}. [{p.code}] {p.policy_clause}")
                print(f"   • Location: {p.location}")
                print(f"   • Impact:   -{p.impact_pts:.2f} pts")
                print(f"   • Details:  {p.details}")
                print(f"   • Fix:      {p.fix}\n")

        if adv_problems:
            print("### 📌 INFORMATIONAL ADVISORIES (No Grade Penalty)")
            for idx, p in enumerate(adv_problems, 1):
                print(f"{idx}. [{p.code}] {p.details}")
                print(f"   • Advice:   {p.fix}\n")

    # 3. Requirement Traceability Matrix
    print("## 3. Requirement Traceability Matrix\n")
    if ea_list:
        print(f"{'Exercise':<12} | {'Requirement Prompt / Sub-Task':<48} | {'Status'}")
        print("-" * 75)
        for ea in ea_list:
            for prompt_name, is_satisfied in ea.traceability:
                st = "✅ PASS" if is_satisfied else "❌ DEFICIENT"
                print(f"Ex {ea.number:02d}        | {prompt_name[:46]:<48} | {st}")
    else:
        print("  (Provide -r <LabYY.md> to view prompt-level requirement traceability matrix)\n")

    # 4. Remediation Action Plan
    print("\n## 4. Remediation Action Plan (Next Steps for Student)\n")
    if not crit_problems and not maj_problems and not min_problems:
        print("  ✅ All checks passed! The submission is ready for Moodle submission.")
    else:
        print("Follow these concrete steps to achieve a perfect 10.00 / 10.00:")
        step = 1
        for p in crit_problems + maj_problems + min_problems:
            print(f"  [ ] Step {step}: {p.fix}")
            step += 1
    print("\n" + "=" * 78 + "\n")


def main():
    parser = argparse.ArgumentParser(description="Audit and grade student submission folder in READ-ONLY mode")
    parser.add_argument("target_dir", help="Path to student submission folder (StudentID_WXX)")
    parser.add_argument("-r", "--requirement", help="Path to weekly requirement Markdown file (LabYY...md)", default=None)

    args = parser.parse_args()
    report_data = audit_submission(args.target_dir, args.requirement)
    render_report(report_data)

    # Return exit code: 0 if fully compliant (>= 9.5 and no critical issues), 1 if action required
    is_clean = len([p for p in report_data["problems"] if p.severity == "CRITICAL"]) == 0 and report_data["final_grade"] >= 9.5
    sys.exit(0 if is_clean else 1)


if __name__ == "__main__":
    main()
