---
description: >
  Execute HR operations: draft-job-description, plan-interview, create-onboarding,
  performance-review, compensation-analysis, or validate-cvs.
argument-hint: "<operation> [options]"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# proagent-hr Run

Execute human resources and talent management operations based on the specified mode.

## Variables

mode: $1
target: $2 (optional - role title, employee name, team name, Google Drive folder path, or file path depending on mode)
options: $3 (optional - additional configuration such as scoring weights or batch size)

## Instructions

Read the `mode` variable and execute the corresponding workflow below.

---

### Mode: draft-job-description

Draft a comprehensive job description for an open role.

1. **Gather Role Requirements**
   - If `target` is provided, use it as the role title (e.g., "Senior Backend Engineer")
   - Ask the hiring manager for: team context, reporting structure, key responsibilities, must-have vs. nice-to-have qualifications, and budget range
   - Identify the seniority level and map to the company's career ladder framework

2. **Research Market Context**
   - Reference industry benchmarks for similar roles at comparable companies
   - Identify competitive differentiators to highlight in the description
   - Determine appropriate compensation range based on level, location, and market data

3. **Draft the Job Description**
   Structure the document with these sections:
   - **Role Summary**: 2-3 sentence overview of the position and its impact
   - **About the Team**: Team mission, size, tech stack or domain focus
   - **Key Responsibilities**: 5-8 bullet points describing primary duties
   - **Required Qualifications**: Must-have skills, experience, and credentials
   - **Preferred Qualifications**: Nice-to-have skills that strengthen a candidacy
   - **What Success Looks Like**: Measurable outcomes for the first 6-12 months
   - **Compensation & Benefits**: Salary range, equity, benefits summary
   - **Equal Opportunity Statement**: Standard EEO language

4. **Validate and Output**
   - Review for bias-free, inclusive language (remove gendered terms, unnecessary jargon)
   - Ensure compliance with salary transparency requirements
   - Output the job description as a formatted document ready for Google Docs publishing
   - If Google Docs MCP is available, create the document directly in the designated hiring folder

---

### Mode: plan-interview

Design a structured interview process for a specific role.

1. **Define Interview Stages**
   - If `target` is provided, use it as the role title to tailor the process
   - Design a multi-stage pipeline appropriate for the role level:
     - **Recruiter Screen** (30 min): Role fit, salary expectations, availability
     - **Hiring Manager Interview** (45 min): Experience deep-dive, team alignment
     - **Technical Assessment** (60 min): Role-specific skills evaluation
     - **Behavioral Interview** (45 min): Collaboration, problem-solving, values alignment
     - **Final Panel** (60 min): Cross-functional stakeholder evaluation

2. **Generate Question Banks**
   For each stage, create 8-12 questions covering:
   - Technical competency aligned to job description requirements
   - Problem-solving approach and critical thinking
   - Collaboration style and conflict resolution
   - Growth mindset and learning orientation
   - Leadership potential (for senior roles)
   - Include follow-up probes for each question

3. **Build Evaluation Scorecards**
   - Create a scorecard for each interview stage
   - Define 4-6 evaluation criteria per stage with weighted scoring (1-5 scale)
   - Include behavioral anchors for each score level (what a 1, 3, and 5 looks like)
   - Add a section for red flags and green flags

4. **Coordinate Scheduling**
   - Generate a suggested timeline from posting to offer (target: 3-4 weeks)
   - If Google Calendar MCP is available, create calendar holds for panel members
   - Draft candidate communication templates for each stage transition
   - Include rejection and advancement email templates

5. **Output**
   Deliver the complete interview kit:
   - Interview stage overview with owners and durations
   - Question banks per stage (formatted for interviewer use)
   - Evaluation scorecards per stage
   - Scheduling timeline and communication templates

---

### Mode: create-onboarding

Create a comprehensive onboarding plan for a new hire.

1. **Gather New Hire Context**
   - If `target` is provided, use it as the new hire's role or name
   - Determine: start date, role, team, manager, location (remote/hybrid/onsite)
   - Identify role-specific tools, systems, and access requirements

2. **Generate Day-One Checklist**
   - Equipment and workspace setup (laptop, monitors, peripherals)
   - Account provisioning (email, Slack, GitHub/GitLab, cloud services, HR systems)
   - Policy acknowledgments (code of conduct, security policy, NDA, benefits enrollment)
   - Welcome meeting with manager and buddy introduction
   - Office tour or virtual workspace orientation

3. **Build 30/60/90-Day Plan**
   **First 30 Days - Learn:**
   - Complete all mandatory training modules
   - Shadow team members on key workflows
   - Attend team meetings and learn recurring ceremonies
   - Have 1:1s with each direct team member
   - Complete first small deliverable or contribution

   **Days 31-60 - Contribute:**
   - Take ownership of defined work items independently
   - Participate actively in team planning and retrospectives
   - Begin building cross-functional relationships
   - Complete role-specific certifications or training
   - Receive and act on first informal feedback from manager

   **Days 61-90 - Own:**
   - Lead a project or initiative independently
   - Contribute to process improvements or documentation
   - Establish personal development goals with manager
   - Complete 90-day review with formal feedback
   - Transition from onboarding to ongoing performance cadence

4. **Schedule Milestones**
   - If Google Calendar MCP is available, create recurring check-in events
   - Schedule buddy meetings (weekly for first month, biweekly thereafter)
   - Schedule manager 1:1s (weekly)
   - Set reminders for 30-day, 60-day, and 90-day review conversations

5. **Generate Welcome Communications**
   - Draft welcome email from manager with first-day logistics
   - Create team introduction message for Slack with new hire bio
   - Prepare onboarding resources packet with links to key documentation
   - If Gmail MCP is available, send welcome email directly

---

### Mode: performance-review

Facilitate a performance review cycle for an individual or team.

1. **Set Up Review Cycle**
   - If `target` is provided, use it as the employee name or team scope
   - Determine review type: annual, mid-year, quarterly check-in, or probationary
   - Identify review participants: self, peers (3-5), manager, skip-level (optional)
   - Set timeline with deadlines for each phase

2. **Generate Review Templates**
   Create structured templates covering:
   - **Self-Assessment**: Goal achievement, key accomplishments, challenges faced, development areas, career aspirations
   - **Peer Feedback**: Collaboration effectiveness, technical contributions, communication quality, areas for growth
   - **Manager Evaluation**: Performance against objectives, competency assessment, potential rating, promotion readiness
   - Align all templates to the company competency framework and role-level expectations

3. **Synthesize Feedback**
   - Aggregate feedback across all sources into a unified narrative
   - Identify consistent themes in strengths and development areas
   - Flag discrepancies between self-assessment and peer/manager feedback
   - Quantify goal achievement against defined OKRs or KPIs

4. **Draft Review Narrative**
   Structure the review document:
   - **Summary**: Overall performance level and key achievements
   - **Strengths**: 3-5 demonstrated strengths with specific examples
   - **Development Areas**: 2-3 areas for improvement with actionable guidance
   - **Goal Achievement**: Status of each objective with evidence
   - **Development Plan**: Recommended actions for the next review period
   - **Compensation Recommendation**: If applicable, include merit increase or promotion rationale

5. **Prepare Calibration Materials**
   - Generate calibration summary with performance distribution across the team
   - Create comparison view of similar-level employees for consistency
   - If Google Docs MCP is available, publish review documents to the HR folder

---

### Mode: compensation-analysis

Analyze compensation for a role, individual, or team.

1. **Define Analysis Scope**
   - If `target` is provided, use it as the role title, individual name, or team name
   - Determine analysis type: market benchmarking, internal equity audit, or adjustment modeling

2. **Research Market Data**
   - Identify comparable roles at peer companies based on level, function, and location
   - Gather compensation data points: base salary, bonus target, equity grants, total compensation
   - Note data sources and freshness (flag data older than 6 months)

3. **Analyze Internal Position**
   - Map the role to internal pay bands and salary grades
   - Calculate compa-ratio (actual pay / midpoint of pay band)
   - Compare against peers at the same level within the organization
   - Identify any pay equity concerns across demographics or tenure

4. **Build Compensation Report**
   Structure the analysis:
   - **Market Positioning**: Where the role/individual sits relative to market (25th, 50th, 75th percentile)
   - **Internal Equity**: Compa-ratio analysis and peer comparison
   - **Total Compensation Breakdown**: Base, bonus, equity, benefits valued in total
   - **Gap Analysis**: Difference between current and target positioning
   - **Recommendations**: Specific adjustment proposals with budget impact
   - **Risk Assessment**: Retention risk if compensation is below market

5. **Model Scenarios**
   - Create adjustment scenarios (e.g., move to 50th percentile, match competitor offer)
   - Calculate budget impact for each scenario
   - Provide timeline recommendation for implementing adjustments

---

### Mode: validate-cvs

Validate candidate CVs against a job description using a multi-agent orchestration pipeline with blind review.

1. **Gather Inputs**
   - If `target` is provided, use it as the Google Drive folder path containing CVs
   - Ask for:
     - **Job Description source**: Google Drive path or local file path to the JD
     - **CV folder**: Google Drive folder containing candidate CV PDFs (if not provided as `target`)
     - **Scoring weights** (optional): Custom weights for Skills/Experience/Education/Certifications (default: 35/35/15/15)
     - **Batch size** (optional): Number of CVs to process per batch (default: all)
   - Use Google Drive MCP to list files in the CV folder and confirm the count with the user

2. **Extract Job Requirements**
   - Read the job description from Google Drive via MCP
   - Parse into a structured requirements rubric:
     - **Must-Have Requirements**: Minimum qualifications (pass/fail)
     - **Should-Have Requirements**: Strong preferences
     - **Nice-to-Have Requirements**: Bonus qualifications
   - Extract scoring dimensions: skills, experience level, education, certifications, industry alignment
   - Present the extracted rubric to the user and **STOP for confirmation** before proceeding

3. **Parse CVs (Sequential — cv-parser agent)**
   - For each CV in the folder, dispatch the `cv-parser` agent via the Task tool
   - The parser extracts structured data and separates PII into an identity envelope
   - Store parsed profiles with anonymized candidate IDs (Candidate #001, #002, etc.)
   - Track progress: "Parsed X of Y CVs"
   - If a CV cannot be parsed, log the failure and continue with remaining CVs

4. **Analyze Candidates (Parallel Fan-Out)**
   For each parsed candidate, dispatch these agents in parallel via the Task tool:
   - **cv-skills-matcher**: Score technical and professional skill match against JD
   - **cv-experience-validator**: Validate work history timeline, progression, and relevance
   - **cv-red-flag-detector**: Check for factual inconsistencies and integrity concerns

   Each agent receives ONLY the anonymized profile (no PII) plus the JD rubric.
   All three agents run simultaneously for each candidate.

5. **Aggregate Scores (Fan-In — cv-scoring-aggregator agent)**
   - Dispatch the `cv-scoring-aggregator` agent via the Task tool
   - Aggregator collects all parallel results and produces:
     - Per-candidate composite scorecards
     - Candidate comparison matrix ranked by overall score
     - Tier classifications (Tier 1-4)
     - Batch summary statistics
   - Write results to a Markdown file and optionally to Google Sheets via MCP

6. **Recruiter Review Gate — STOP**
   - Present the comparison matrix and batch summary to the user
   - **STOP and wait for recruiter approval** before generating recommendations
   - Options:
     - **[A]pprove**: Proceed to recommendation generation
     - **[E]dit**: Adjust weights, re-score specific candidates, or modify tier thresholds
     - **[R]edo**: Re-run analysis with different parameters

7. **Generate Recommendations (cv-recommendation-generator agent)**
   - Only after recruiter approval, dispatch the `cv-recommendation-generator` agent
   - Produces:
     - Ranked shortlist with per-candidate advancement rationale
     - Interview focus areas for each advancing candidate
     - Pipeline summary with scheduling recommendations
     - Action items for hiring manager, recruiter, and interviewers
   - Reunite candidate numbers with names from the identity envelope in the final output
   - If Gmail MCP is available, draft outreach emails for advancing candidates
   - If Slack MCP is available, post completion notification to the hiring channel

8. **Persist Session State**
   Throughout the pipeline, maintain a session state file (`cv_validation_session.json`):
   ```json
   {
     "started_at": "ISO timestamp",
     "job_description": "source path",
     "cv_folder": "source path",
     "weights": { "skills": 35, "experience": 35, "education": 15, "certifications": 15 },
     "total_cvs": 0,
     "parsed_cvs": [],
     "scored_cvs": [],
     "current_step": "parsing|analyzing|aggregating|reviewing|recommending",
     "status": "in_progress|paused_for_review|completed|failed"
   }
   ```
   - Update after each candidate is fully processed
   - If the session is interrupted, resume from the last completed candidate on restart

## Error Handling

- If required context is missing (role title, employee name), prompt the user with specific questions before proceeding
- If Google Docs or Gmail MCP is unavailable, output documents as formatted Markdown for manual publishing
- If market compensation data cannot be retrieved, note the limitation and use available internal data with caveats
- If a CV file cannot be read or parsed, log the error and continue with remaining candidates — do not abort the batch
- If a parallel analysis agent fails for a candidate, note the gap in the aggregation and proceed with available results
- If the Google Drive MCP is unavailable, fall back to reading local file paths
- All outputs include a "Next Steps" section with clear action items and owners
