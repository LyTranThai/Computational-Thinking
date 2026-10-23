# Group 05 - Task Distribution

## 1. Contribution Summary

All 7 members contributed equally to the brainstorming, research, report writing, and presentation preparation for the Project Proposal phase.

| Student ID | Full Name | GitHub Username | Project Role | Slide & Presentation Responsibilities | Contribution |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 25125027 | Nguyễn Tấn Minh | [callmelucian](https://github.com/callmelucian) | Team Leader | Motivation & limitations of existing tools, presentation delivery & submission packaging (`Group05.zip`) | $\approx 14.29\%$ |
| 25125014 | Nguyễn Đức Huy | [SpheraXX](https://github.com/SpheraXX) | Front-end Developer | Problem definition, inputs, outputs, goal & lead Beamer slide deck design & visual styling | $\approx 14.29\%$ |
| 25125048 | Lý Trần Thái | [LyTranThai](https://github.com/LyTranThai) | Developer | Scope, future integration, success criteria & slide formatting, layout review, XeLaTeX compilation | $\approx 14.29\%$ |
| 25125084 | Trần Gia Huy | [FubuGold](https://github.com/FubuGold) | Main System Design | Decomposition, Pattern Recognition, Abstraction & TikZ pipeline flowchart | $\approx 14.29\%$ |
| 25125050 | Bùi Đỗ Thiên Ân | [Gasmask-Chan](https://github.com/Gasmask-Chan) | Algorithm & Logic Developer | Algorithm Design: 3-stage pipeline & Baseline for comparison: *LetsJustMeet* | $\approx 14.29\%$ |
| 25125056 | Trần Đăng Khoa | [trankhoa8581](https://github.com/trankhoa8581) | Backend Developer | Subsystem annotations (LLM extraction & routing rules) & Technical feasibility & classmate testing | $\approx 14.29\%$ |
| 23125054 | Ngô Tấn Đạt | [diamondzone1](https://github.com/diamondzone1) | Security & Data | Data feasibility: OSM & 200–300 places, project risks & compliance documentation (`ai-usage.md`, `task_distribution.md`) | $\approx 14.29\%$ |
| **Total** | | | | | **$100\%$** |

---

## 2. Detailed Breakdown of Tasks
- **Nguyễn Tấn Minh – Motivation & Existing Tools:**
  - ***My own problem: Finding a meeting place?*:** Formulated the student meeting scenario with realistic constraints ($\le 10\text{ km}$ travel limit, $\le 50.000\text{ VND}$ budget, 5-hour study duration) and highlighted the failure of manual guessing and single-point search.
  - ***Why Existing Tools Fall Short*:** Evaluated current tools across three categories (Map tools like Google Maps + Gemini, Midpoint finders like *LetsJustMeet*, and social media), identifying the gap in multi-origin planning with group preferences.

- **Nguyễn Đức Huy – Problem Definition & Visual Identity:**
  - ***Problem Definition*:** Formalized target users (university students in HCMC), structured input fields (origins, group size, budget, diet, meeting time, style), expected outputs (ranked candidates, travel times, rationales), and the core goal (feasible & fair recommendations).
  - **Visual Design:** Designed the presentation visual layout, custom Beamer theme styling, color palette (`fitblue`, `accent`, `fitlight`), typography, and university logo integration.

- **Lý Trần Thái – Scope & Evaluation Criteria:**
  - ***Scope and Success Criteria*:** Established the bounded project scope (HCMC road network, curated café/eatery dataset, hard constraints vs. soft style tags), future integration scope (traffic, weather, booking, transit), and defined the 5 preliminary success criteria.
  - **Presentation Engineering:** Handled slide layout alignment, XeLaTeX compilation workflow, and presentation rendering.

- **Trần Gia Huy – System Pillars & Pipeline Architecture:**
  - ***Decomposition*:** Structured the solution into resources collection (streetmap, POIs), solution phases (filtering, scoring, responses), and architecture (database & query handling).
  - ***Pattern Recognition*:** Identified spatial clustering near the group centroid, shared request schemas, and repeated shortest-path reuse.
  - ***Abstraction*:** Formulated the Abstraction comparison table (Real world vs. Our model vs. Left out for Streetmap, Member, Place, and Request).
  - ***Planned Pipeline*:** Programmed the 7-stage flowchart in LaTeX TikZ ($\text{Request} \rightarrow \text{Understand} \rightarrow \text{Route} \rightarrow \text{Compute} \rightarrow \text{Rank} \rightarrow \text{Verify} \rightarrow \text{Respond}$).

- **Bùi Đỗ Thiên Ân – Algorithm Design & Baseline Benchmark:**
  - ***Algorithm Design*:** Structured the 3-stage recommendation algorithm: Stage 1 (Spatial bounding & shortlist via straight-line distance and hard constraints), Stage 2 (Travel-time scoring combining fairness, travel time, and style match), and Stage 3 (Multi-objective ranking).
  - ***Baseline for Comparison*:** Structured the baseline comparison around *LetsJustMeet*, analyzing its midpoint search behavior in HCMC and demonstrating its inability to filter by budget, diet, or hours.

- **Trần Đăng Khoa – Processing Subsystems & Technical Feasibility:**
  - ***Pipeline Annotations*:** Defined subsystem logic for the pipeline diagram: LLM query extraction with fixed schema, deterministic routing rules (search, ask, or refuse), constraint verification, and template responses.
  - ***Technical Feasibility*:** Specified the algorithmic feasibility of shortest-path computation on road graphs (one run per origin member) and the evaluation approach using university classmates.

- **Ngô Tấn Đạt – Data Feasibility & Risk Analysis:**
  - ***Data Feasibility & Risks*:** Defined the data acquisition strategy (free road data from OpenStreetMap, hand-curated dataset of 200–300 places) and articulated project risks (scope suitability for Computational Thinking skills, dataset collection challenges).
  - **Compliance Documentation:** Maintained academic integrity logs (`ai-usage.md`), contribution tracking (`task_distribution.md`).

---

## 3. Technical Artifacts & Deliverables

Each member delivered a concrete, essential supporting artifact directly tied to the slide deck:

- **Nguyễn Tấn Minh:** Team leadership, meeting facilitation, oral presentation delivery, slide review, and submission packaging (`Group05.zip`).
- **Nguyễn Đức Huy:** Beamer slide deck architecture, visual theme design, color palette, and university branding.
- **Lý Trần Thái:** Slide formatting, typography review, XeLaTeX compilation pipeline, and PDF rendering.
- **Trần Gia Huy:** Pipeline architecture design and LaTeX TikZ vector flowchart implementation.
- **Bùi Đỗ Thiên Ân:** Algorithmic ranking logic design and *LetsJustMeet* baseline comparative analysis.
- **Trần Đăng Khoa:** Subsystem routing rules, query extraction schema specification, and graph algorithmic runtime assessment.
- **Ngô Tấn Đạt:** OpenStreetMap data extraction strategy, venue curation protocol, and academic compliance records (`ai-usage.md`, `task_distribution.md`).

---

## 4. Shared Team Activities

In addition to individual assignments, all 7 members actively collaborated in:
1. Brainstorming candidate topics and selecting the fair meeting-point planner through group consensus.
2. Reviewing and proofreading the slide content to ensure technical accuracy, clear terminology, and visual consistency.
3. Conducting rehearsal runs, presentation timing checks, and Q&A defense preparation for the live presentation session.
4. Participating in peer review of each member's contributions and post-presentation refinement.