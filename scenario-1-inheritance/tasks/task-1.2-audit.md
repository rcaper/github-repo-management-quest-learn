# Task 1.2: Content Quality Audit with GitHub Copilot

**Duration:** 15 minutes
**Difficulty:** Intermediate
**GitHub Copilot Features:** @workspace, Copilot Chat, inline suggestions

## Objective

Identify specific content quality issues in the Microsoft Learn training modules repository using GitHub Copilot's workspace-wide analysis capabilities.

## Context

Now that you understand the repository structure (from Task 1.1), it's time to dig deeper and find concrete quality issues. For Microsoft Learn content, these could be outdated `ms.date` values, inconsistent metadata, formatting problems, missing accessibility attributes, or content inconsistencies across modules.

GitHub Copilot's @workspace agent can analyze all YAML and markdown files simultaneously to find patterns and issues that would take hours to discover manually.

## Setup

Ensure you're in the learn-pr content with Copilot Chat open:

```bash
cd learn-pr/wwl
code .
```

Press `Ctrl+Shift+I` (Cmd+Shift+I on Mac) to open Copilot Chat.

## Tasks

### 1. Check for Broken Links and References

**GitHub Copilot Chat Prompt:**

```text
@workspace Analyze all markdown and YAML files for broken links and references:
1. Internal links to files or includes that don't exist
2. Image references in media/ folders that may be missing
3. [!include[]] references that point to non-existent files
4. Cross-module references that may be broken
5. External URLs to learn.microsoft.com that may be outdated

List each issue with:
- Module folder and file name
- The reference or link
- Why it's potentially broken
- Suggested fix
```

**What Copilot Does:**

- Scans all .yml and .md files in workspace
- Checks if linked files exist
- Validates include references
- Identifies potentially outdated external URLs

**Follow-up Prompts:**

```text
@workspace Check if all the media files referenced in get-started-lakehouses actually exist
```

```text
@workspace Are there any includes/ files that reference images not present in media/?
```

**Deliverable:** Create `quality-audit.md` with a "Broken Links & References" section

---

### 2. Identify Outdated Content and Metadata

**GitHub Copilot Chat Prompt:**

```text
@workspace Review all module index.yml files for outdated information:
1. Find ms.date values older than 6 months from today (December 2025)
2. Identify deprecated ms.service values or product names
3. Check for inconsistent author metadata patterns
4. Find modules referencing features that may have changed
5. Identify old iconUrl paths or badge references

For each issue, provide:
- Module folder and file name
- What's outdated (current value)
- Why it matters
- Suggested update
```

**What Copilot Does:**

- Searches for date patterns across index.yml files
- Identifies older timestamps
- Compares metadata patterns across modules
- Flags inconsistencies

**Follow-up Prompts:**

```text
@workspace List all modules with ms.date values from 2023 or earlier
```

```text
@workspace What are all the different ms.service values used across modules?
```

**Deliverable:** Add "Outdated Content & Metadata" section to `quality-audit.md`

---

### 3. Check YAML and Markdown Formatting Consistency

**GitHub Copilot Chat Prompt:**

```text
@workspace Analyze formatting consistency across all modules:
1. Check YAML syntax consistency (indentation, quoting, line breaks)
2. Find markdown code blocks without language specifiers in includes/
3. Identify inconsistent heading levels in markdown files
4. Check for inconsistent metadata field ordering in YAML
5. Find inconsistent use of single vs double quotes in YAML

Present findings grouped by issue type with specific file examples.
```

**What Copilot Does:**

- Parses YAML and markdown structure in all files
- Identifies formatting patterns and violations
- Compares formatting across modules
- Highlights inconsistencies

**Using Inline Copilot:**

Once you find issues, you can fix them inline:

1. Open the file with issues
2. Select the problematic text
3. Press `Ctrl+I` (Cmd+I on Mac)
4. Ask: "Fix this YAML formatting to match Microsoft Learn standards"

**Deliverable:** Add "Formatting Issues" section to `quality-audit.md`

---

### 4. Find Incomplete Content and Missing Elements

**GitHub Copilot Chat Prompt:**

```text
@workspace Search all module files for incomplete content:
1. TODO, FIXME, or placeholder markers in content
2. Knowledge check questions that seem incomplete or missing
3. Exercises without proper instructions
4. Module summaries that don't match learning objectives
5. Modules missing expected units (intro, knowledge-check, summary)
6. Empty or stub markdown files in includes/ folders

List each with module, file location, and what's missing.
```

**What Copilot Does:**

- Searches for common placeholder patterns
- Identifies structural issues (missing units)
- Flags suspiciously short content
- Compares module structures for completeness

**Follow-up Prompts:**

```text
@workspace Do all modules have a knowledge-check.yml or knowledge-check unit?
```

```text
@workspace Which modules are missing summary units?
```

**Deliverable:** Add "Incomplete Content" section to `quality-audit.md`

---

### 5. Check for Content Contradictions and Inconsistencies

**GitHub Copilot Chat Prompt:**

```text
@workspace Compare content across Microsoft Learn modules to find contradictions:
1. Conflicting explanations of the same concept across modules
2. Inconsistent terminology (different terms for same Fabric feature)
3. Prerequisite modules that don't align
4. Different recommended approaches for similar tasks
5. Inconsistent UI references or navigation instructions

Focus on Microsoft Fabric modules where concepts overlap.
```

**What Copilot Does:**

- Cross-references content across modules
- Identifies terminology variations
- Finds conflicting information
- Highlights prerequisite mismatches

**Advanced Prompt:**

```text
@workspace Compare how "lakehouse" is described in get-started-lakehouses vs describe-medallion-architecture - are they consistent?
```

**Deliverable:** Add "Contradictions & Inconsistencies" section

---

### 6. Assess Accessibility and Clarity

**GitHub Copilot Chat Prompt:**

```text
@workspace Evaluate Microsoft Learn modules for accessibility and clarity:
1. Find images referenced without proper alt text descriptions
2. Identify complex jargon used without explanation or definition
3. Check if prerequisites in index.yml match actual requirements
4. Find overly complex explanations that could be simplified
5. Check for proper use of note/tip/warning callouts

Provide specific examples with suggestions for improvement.
```

**What Copilot Does:**

- Checks image syntax for alt attributes
- Identifies technical terms needing explanation
- Reviews prerequisite alignment
- Evaluates content complexity

**For Specific Modules:**

```text
@workspace Is the introduction-to-copilot-fabric module clear for beginners? What concepts need more explanation?
```

**Deliverable:** Add "Accessibility & Clarity" section

---

## Generate Summary Statistics

**GitHub Copilot Chat Prompt:**

```text
@workspace Based on all the issues we've found in the Microsoft Learn modules, generate summary statistics:
- Total issues by category (broken links, outdated dates, formatting, etc.)
- Severity breakdown (critical, high, medium, low)
- Modules with most issues
- Estimated time to fix each category
- Quick wins (high impact, low effort)

Present as tables and bullet points.
```

**Deliverable:** Add "Summary Statistics" section

---

## Output Format

Your `quality-audit.md` should look like this:

```markdown
# Microsoft Learn Content Quality Audit

**Generated with:** GitHub Copilot @workspace
**Audit Date:** [Date]
**Audited By:** [Your Name]

## Executive Summary
[Copilot-generated overview: X total issues found across Y modules]

---

## Issues by Category

### 1. Broken Links & References (Count: X)

| Module | File | Reference | Issue | Severity |
|--------|------|-----------|-------|----------|
| get-started-lakehouses | 3-work-lakehouse.yml | includes/missing-file.md | File not found | High |
| administer-fabric | index.yml | ../deprecated-module | Module removed | Medium |

**Copilot Notes:** [Any additional context from Copilot]

---

### 2. Outdated Metadata (Count: X)

| Module | File | Issue | Current Value | Severity |
|--------|------|-------|---------------|----------|
| fabric-data-governance | index.yml | ms.date from 2023 | 03/15/2023 | Critical |
| get-started-data-warehouse | index.yml | Old author format | wwlpublish | Medium |

---

### 3. Formatting Issues (Count: X)

| Module | File | Issue | Example |
|--------|------|-------|---------|
| describe-medallion-architecture | includes/2-describe.md | Code block no language | ``` without python |
| introduction-to-copilot-fabric | includes/3-copilot.md | Inconsistent heading levels | Jumps from H2 to H4 |

---

### 4. Incomplete Content (Count: X)

| Module | Unit | Issue | Severity |
|--------|------|-------|----------|
| implement-fabric-data-agents | knowledge-check.yml | Only 2 questions | Medium |
| explore-event-streams | includes/4-exercise.md | TODO marker present | High |

---

### 5. Contradictions & Inconsistencies (Count: X)

| Modules Affected | Issue | Severity |
|-----------------|-------|----------|
| get-started-lakehouses, describe-medallion | Different lakehouse definitions | High |
| administer-fabric, manage-copilot-fabric | Inconsistent admin terminology | Medium |

---

### 6. Accessibility & Clarity (Count: X)

| Module | Issue | Suggestion | Severity |
|--------|-------|-----------|----------|
| get-started-data-science | Images missing alt text | Add descriptive alt="" | Medium |
| introduction-to-copilot-fabric | Jargon: "OneLake" unexplained | Add definition in intro | Medium |

---

## Summary Statistics

**Generated by Copilot:**

- **Total Issues:** X
- **Critical:** X (fix immediately)
- **High:** X (fix this week)
- **Medium:** X (fix this month)
- **Low:** X (backlog)

### Issues by Module
1. get-started-lakehouses: X issues
2. administer-fabric: X issues
3. describe-medallion-architecture: X issues

### Issues by Category
- Broken links: X
- Outdated metadata: X
- Formatting: X
- Incomplete: X
- Contradictions: X
- Accessibility: X

---

## Quick Wins (High Impact, Low Effort)

[Copilot-generated list of issues that can be fixed in <1 hour each]

1. Update ms.date in 5 modules (30 min)
2. Add language specifiers to code blocks (15 min)
3. Fix broken include reference in get-started-lakehouses (10 min)

**Total Quick Win Time:** ~2 hours
**Impact:** Fixes 30% of high-severity issues

---

## Top Priority Issues

[Copilot's prioritized list of most critical fixes]

1. **[Critical] Fix broken prerequisites** - blocks learner progression
2. **[Critical] Update deprecated Fabric terminology** - confuses learners
3. **[High] Align lakehouse definitions across modules** - ensures consistency

---

## Recommendations

[Copilot-generated recommendations based on patterns found]

**Process Improvements:**
- Add automated YAML validation in CI/CD
- Implement markdownlint for formatting
- Create module review checklist
- Set up quarterly freshness reviews

**Immediate Actions:**
- Fix all critical issues (estimated X hours)
- Update all ms.date values
- Validate all include references

---

*Audit completed with GitHub Copilot @workspace assistance*
```

---

## GitHub Copilot Tips for This Task

### Iterative Analysis

Don't try to find everything in one prompt. Build up:
1. Start with one category (broken links)
2. Ask Copilot to find them
3. Ask follow-ups for details
4. Move to next category

### Verify Copilot's Findings

Copilot is powerful but not perfect. Spot-check:
- Do the files it mentions exist?
- Are the line numbers accurate?
- Is the issue really a problem?

**How to verify:**
```
@workspace Show me line 23 of getting-started.md
```

### Use Context Commands

```
@workspace /explain    - Explain what you found
@workspace /fix        - Suggest how to fix an issue
@workspace /tests      - Are there tests for this?
```

### Progressive Detail

Start broad, then narrow:
```
@workspace Find all broken links
  → @workspace Show me the broken links in getting-started.md specifically
    → @workspace Show me line 23 of that file
```

---

## Success Criteria

You've completed this task when you:

- ✅ Identified at least 15 specific issues across all categories
- ✅ Categorized each issue by type and severity
- ✅ Provided specific file names and line numbers
- ✅ Included enough detail to make issues actionable
- ✅ Used GitHub Copilot's @workspace for efficient analysis
- ✅ Generated summary statistics and priorities
- ✅ Created a professional audit document

---

## Time Management

- **Minutes 0-3:** Broken links and outdated content (2 prompts)
- **Minutes 4-7:** Formatting and incomplete content (2 prompts)
- **Minutes 8-10:** Contradictions and accessibility (2 prompts)
- **Minutes 11-13:** Summary statistics and prioritization
- **Minutes 14-15:** Compile findings into quality-audit.md

---

## What's Next?

After completing your audit, you'll use these findings in **Task 1.3** to create an executive report with GitHub Copilot's help, transforming technical findings into actionable business recommendations.

---

**Ready for the next step?** Continue to [Task 1.3: Generate Audit Report](task-1.3-report.md).
