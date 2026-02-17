---
description: >
  Review HR artifacts: job descriptions, interview process, onboarding plans,
  team composition, and cv-screening results.
argument-hint: "[target]"
allowed-tools: Read, Glob, Grep, Bash, Task
---

# proagent-hr Review

Review and assess HR processes, documents, and organizational health.

## Variables

mode: $1 (one of: "review job descriptions", "interview process", "onboarding plans", "team composition", "cv-screening")
target: $2 (optional - specific document, role, team, screening batch, or scope to review)

## Instructions

Read the `mode` variable and execute the corresponding review workflow below.

---

### Mode: review job descriptions

Audit existing job descriptions for quality, compliance, and effectiveness.

1. **Locate Job Descriptions**
   - If `target` is provided, review the specified job description file or document
   - Otherwise, scan the workspace for job description documents (docs/, hiring/, roles/ directories)
   - Identify all active job descriptions awaiting review

2. **Assess Content Quality**
   - Verify all required sections are present: role summary, responsibilities, qualifications, compensation, EEO statement
   - Check that responsibilities are specific and measurable (not vague filler like "other duties as assigned")
   - Validate that required qualifications reflect genuine needs (flag excessive years-of-experience requirements or unnecessary degree requirements)
   - Confirm preferred qualifications are clearly separated from required ones
   - Verify success criteria are included and tied to measurable outcomes

3. **Check Language and Inclusivity**
   - Scan for gendered language (he/she instead of they, "manpower," "chairman")
   - Identify unnecessarily aggressive terms ("rockstar," "ninja," "crushing it") that may discourage diverse applicants
   - Check for jargon or acronyms that could confuse external candidates
   - Verify the tone matches the company brand and culture
   - Flag any language that could create legal risk (age preferences, disability assumptions)

4. **Evaluate Market Alignment**
   - Compare the role scope against similar positions in the market
   - Assess whether the compensation range is competitive for the requirements listed
   - Check if the seniority level matches the expected responsibilities

5. **Report**
   Provide a structured review:
   - Overall job description quality score (1-10)
   - List of identified issues with severity (critical, warning, suggestion)
   - Specific rewrite recommendations with before/after examples
   - Compliance checklist with pass/fail status for each requirement

---

### Mode: interview process

Evaluate the interview workflow for a role or across the organization.

1. **Gather Process Details**
   - If `target` is provided, scope the review to that specific role's interview process
   - Map the current interview stages: what happens at each step, who is involved, how long it takes
   - Identify the evaluation criteria and scoring methodology in use

2. **Assess Stage Coverage**
   - Verify the process covers all critical dimensions: technical skills, behavioral competencies, culture alignment, and role-specific requirements
   - Check for redundancy between stages (same questions asked by multiple interviewers)
   - Identify gaps where critical competencies are not being assessed
   - Evaluate the balance between structured (scorecard-based) and unstructured (conversational) interviews

3. **Evaluate Candidate Experience**
   - Assess total process duration from application to offer (benchmark: 2-4 weeks)
   - Count the number of touchpoints and total interview hours required of candidates
   - Check for clear communication at each stage transition
   - Evaluate whether the process is accessible (remote options, scheduling flexibility, accommodations)

4. **Review Question Quality**
   - Check that questions are behavioral and situational (not hypothetical or trivia)
   - Verify questions are legal and do not probe protected characteristics
   - Assess whether questions differentiate between good and great candidates
   - Check for consistency in scoring criteria across interviewers

5. **Report**
   Provide a process assessment:
   - Process efficiency score (1-10) based on time-to-hire and candidate experience
   - Coverage gap analysis showing which competencies are under or over-assessed
   - Specific recommendations for process improvements
   - Suggested question replacements for weak or problematic questions
   - Benchmark comparison against industry best practices

---

### Mode: onboarding plans

Review onboarding plan completeness and effectiveness.

1. **Locate Onboarding Materials**
   - If `target` is provided, review the specified onboarding plan
   - Otherwise, identify the current onboarding template or most recent onboarding plan
   - Gather feedback data from recent new hires if available

2. **Assess Completeness**
   - Verify the plan covers all phases: pre-boarding, day one, week one, 30/60/90 days
   - Check for essential elements:
     - Equipment and access provisioning checklist
     - Mandatory training and policy acknowledgments
     - Team introductions and buddy assignment
     - Role-specific onboarding tasks
     - Milestone check-ins with manager
     - 90-day review and transition to regular performance cadence

3. **Evaluate Quality**
   - Check that milestones have clear owners and deadlines
   - Verify onboarding goals are specific and measurable (not just "learn the codebase")
   - Assess whether the ramp-up timeline is realistic for the role level
   - Evaluate the social integration plan (team events, buddy program, cross-functional introductions)
   - Check for remote/hybrid-specific accommodations if applicable

4. **Identify Gaps**
   - Compare against onboarding best practices: structured programs reduce time-to-productivity by 50%
   - Flag missing elements that are standard for the role type
   - Identify areas where new hires commonly report confusion or lack of support
   - Check whether feedback loops exist to improve the onboarding process iteratively

5. **Report**
   Provide an onboarding assessment:
   - Onboarding readiness score (1-10)
   - Completeness checklist with pass/fail per element
   - Gap list with priority ranking and recommended additions
   - New hire satisfaction indicators (if feedback data is available)
   - Estimated impact on time-to-productivity

---

### Mode: team composition

Analyze team structure, skills distribution, and organizational health.

1. **Map Team Structure**
   - If `target` is provided, scope the analysis to that specific team
   - Identify team members, roles, levels, and reporting structure
   - Map tenure distribution across the team
   - Note open positions and planned headcount changes

2. **Analyze Skills Distribution**
   - Inventory technical and domain skills across team members
   - Identify skill concentrations (single points of failure) and skill gaps
   - Map skill coverage against team objectives and upcoming project needs
   - Assess the team's collective growth trajectory based on development plans

3. **Evaluate Team Health Indicators**
   - Analyze tenure distribution and turnover risk (flag teams with high concentration of new or long-tenure employees)
   - Assess level distribution (healthy pyramid vs. top-heavy or flat structures)
   - Evaluate diversity of experience backgrounds and perspectives
   - Check manager-to-IC ratio against organizational benchmarks (target: 5-8 ICs per manager)
   - Review meeting behavioral patterns if transcript data is available (derived from meeting-insights-analyzer)

4. **Succession Planning**
   - Identify critical roles with no backup coverage
   - Assess promotion readiness across the team
   - Flag flight risks based on tenure, compensation positioning, and growth trajectory
   - Recommend development actions to build bench strength

5. **Report**
   Provide a team composition assessment:
   - Team structure visualization (org chart with levels and tenure)
   - Skills matrix showing coverage and gaps
   - Health indicators dashboard (tenure, turnover risk, level distribution)
   - Succession risk summary with mitigation recommendations
   - Hiring priorities based on current gaps and planned work
   - Comparison against organizational benchmarks

---

### Mode: cv-screening

Audit a completed CV screening batch for quality, consistency, and bias.

1. **Locate Screening Results**
   - If `target` is provided, use it as the path to the screening batch output (comparison matrix, scorecards, recommendations)
   - Otherwise, look for the most recent `cv_validation_session.json` and associated output files
   - Identify all components: parsed profiles, individual scorecards, comparison matrix, batch summary, recommendations

2. **Assess Scoring Consistency**
   - Verify that the same scoring weights were applied to all candidates in the batch
   - Check for score distribution anomalies:
     - Are all scores clustered in a narrow range? (may indicate rubric is too broad)
     - Are scores bimodal? (may indicate a clear dividing line in candidate quality)
     - Are there outlier scores that deviate significantly from the batch mean?
   - Verify that must-have pass/fail was applied consistently (no candidates in Tier 1-2 with must-have failures)
   - Cross-check tier assignments against the defined thresholds

3. **Bias Audit**
   - After reuniting candidate IDs with identity data, check for statistical patterns:
     - Are rejection rates correlated with any demographic indicators? (name patterns, university regions, graduation years as age proxy)
     - Are tier distributions uniform across demographic groups?
     - Were employment gaps flagged as red flags? (they should not be)
   - Review red flag analysis for any flags that could serve as proxies for protected characteristics
   - Verify the blind review protocol was followed (no PII in scoring rationale)
   - Flag any scoring rationale that references non-job-relevant criteria

4. **Coverage Assessment**
   - Verify all JD requirements were evaluated for every candidate
   - Check that each scoring dimension has supporting evidence cited
   - Identify requirements that no candidate satisfied (may indicate unrealistic JD)
   - Identify skills that many candidates had but were not in the JD (may indicate market shift)

5. **Report**
   Provide a screening quality assessment:
   - **Screening Quality Score** (1-10): Overall quality of the screening process
   - **Consistency Check**: Pass/fail on weight application, tier thresholds, must-have gating
   - **Bias Risk Assessment**: Low/Medium/High with specific findings
   - **Coverage Report**: Requirements evaluated vs. total, evidence citation rate
   - **Score Distribution Analysis**: Mean, median, std dev, tier breakdown
   - **Recommendations**:
     - Process improvements for future screenings
     - JD adjustments if requirements appear miscalibrated
     - Candidates to re-evaluate if bias concerns are identified
   - **Compliance Checklist**:
     - [ ] Blind review protocol followed
     - [ ] No PII in scoring rationale
     - [ ] No protected characteristic references in red flags
     - [ ] Employment gaps not penalized
     - [ ] Consistent weights across all candidates
     - [ ] Must-have gate applied uniformly
     - [ ] All scores have evidence citations
