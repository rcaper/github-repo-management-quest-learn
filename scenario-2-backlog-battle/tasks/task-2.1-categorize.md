# Task 3.1: Bulk Issue Categorization with GitHub Copilot

**Duration:** 20 minutes
**Difficulty:** Intermediate
**GitHub Copilot Features:** @github for issue analysis, @workspace for repository files, bulk analysis, pattern recognition

## Objective

Use GitHub Copilot to quickly categorize, prioritize, and analyze a backlog of GitHub issues, identifying patterns, priorities, and relationships that would take hours to identify manually.

## Context

You've inherited a backlog of unorganized GitHub issues for the Microsoft Learn Fabric training modules with:
- No labels or categories
- Mixed priority levels (Copilot features, lakehouse content, medallion architecture)
- Unclear relationships between module issues
- No clear ownership

Manually categorizing issues would take 1-2 hours. GitHub Copilot can analyze all of them in minutes, identifying:
- Issue types (content bug, feature request, accessibility, broken links)
- Priority levels (P0-P3 based on learner impact)
- Effort estimates (small typo fix to major content rewrite)
- Common themes across Fabric modules
- Duplicate or related module issues

This task shows you how to use Copilot's bulk analysis capabilities to bring order to chaos.

## Setup

### Prerequisites

**Before starting this task:** Ensure you have run the "Setup Quest Issues" workflow to create the sample issues in your repository.

1. Go to your repository's **Actions** tab
2. Select "Setup Quest Issues" workflow
3. Click "Run workflow"
4. Navigate to the **Issues** tab to find the created issues (labeled with `quest-sample`)

### For This Task You'll Use:

1. **The Sample Issues on GitHub:**
   - Filter issues by the `quest-sample` label
   - 12 issues covering various Microsoft Learn content challenges

2. **VS Code with Copilot Chat:**
   - Open your repository in VS Code
   - Press `Ctrl+Shift+I` (Cmd+Shift+I on Mac)
   - Use @github to analyze issues in the repository
   - Use @workspace to analyze files in the repository

## Tasks

### 1. Generate Complete Issue Overview

**GitHub Copilot Chat Prompt:**

```
@github Analyze all open issues in this repository with the quest-sample label.

Provide a complete overview:

1. **Total Issue Count:** How many issues?

2. **By Type** (categorize each):
   - Bugs (something broken)
   - Features (new functionality requested)
   - Documentation (docs issues)
   - Questions (user asking how-to)
   - Discussions (proposals, ideas)

3. **By Current State:**
   - How many have labels?
   - How many have assignees?
   - How many have detailed descriptions?
   - How many are vague or incomplete?

4. **Common Themes:**
   - What topics come up multiple times?
   - Are there patterns in the issues?

Present as a summary with counts and percentages.
```

**What Copilot Does:**
- Reads all issues with the quest-sample label
- Categorizes each one
- Identifies patterns
- Provides statistical overview

**Deliverable:** Create `issue-analysis.md` with "Overview" section

---

### 2. Categorize and Label All Issues

**GitHub Copilot Chat Prompt:**

```
@github Categorize all issues with the quest-sample label into a detailed table.

For each issue, determine:

1. **Type:**
   - content-bug (incorrect information, broken code examples)
   - content-update (outdated ms.date, stale screenshots)
   - broken-link (missing includes, broken references)
   - accessibility (missing alt text, heading issues)
   - enhancement (improve clarity, add examples)
   - new-content (request for new topics)

2. **Priority** (P0-P3):
   - P0: Critical, blocks users, needs immediate fix
   - P1: Important, affects many users, fix soon
   - P2: Normal, standard feature/bug, schedule normally
   - P3: Low, nice-to-have, fix when possible

3. **Effort** (estimation):
   - XS: < 1 hour (typos, simple fixes)
   - S: 1-4 hours (small features, simple bugs)
   - M: 1-2 days (medium complexity)
   - L: 3-5 days (complex features)
   - XL: 1+ weeks (major features, refactoring)

4. **Suggested Labels:**
   - Appropriate GitHub labels for this issue

Present as a markdown table:
| Issue # | Title | Type | Priority | Effort | Suggested Labels |

Sort by priority (P0 first), then by effort (smallest first within each priority).
```

**What Copilot Does:**
- Analyzes all issues simultaneously
- Applies consistent categorization criteria
- Estimates complexity
- Prioritizes by business value
- Suggests appropriate labels

**Follow-up to Refine:**

```
@github For the P0 issues, explain WHY you rated them as critical priority.
```

```
@github For the XL effort issues, explain what makes them complex.
```

**Deliverable:** Add "Complete Issue Categorization" section with comprehensive table

---

### 3. Identify Quick Wins

**GitHub Copilot Chat Prompt:**

```
@github From the issues with the quest-sample label, identify "quick wins" - issues that:
- Are high value (user-facing problems or popular requests)
- Require low effort (XS or S)
- Have clear solutions
- Can be fixed quickly to show progress

For each quick win:
1. Issue number and title
2. Why it's valuable
3. What needs to be done
4. Estimated time to fix
5. Could it be automated or assigned to Copilot?

Rank by value/effort ratio (biggest bang for buck first).
```

**What Copilot Does:**
- Filters for low-effort, high-value issues
- Identifies clear, actionable items
- Prioritizes by impact-to-effort ratio
- Suggests automation opportunities

**Deliverable:** Add "Quick Wins" section with prioritized list

---

### 4. Group Issues by Theme

**GitHub Copilot Chat Prompt:**

```
@github Group all issues with the quest-sample label by common themes or topics.

Examples of themes:
- Copilot for Fabric content gaps
- Lakehouse module issues
- Medallion architecture examples need updating
- PySpark code examples broken/outdated
- ms.date freshness across modules
- Screenshot currency for Fabric portal
- Accessibility compliance gaps

For each theme:
1. Theme name
2. Issues in this theme (by number)
3. Summary of what users are asking for
4. Potential unified solution (could one fix address multiple issues?)
5. Priority of this theme overall

This helps identify if we should focus on specific areas rather than tackling issues individually.
```

**What Copilot Does:**
- Identifies common topics across issues
- Groups related requests
- Finds opportunities for combined solutions
- Highlights focus areas

**Deliverable:** Add "Issues by Theme" section

---

### 5. Identify Duplicate and Related Issues

**GitHub Copilot Chat Prompt:**

```
@github Find duplicate and closely related issues in the backlog.

Look for:

1. **Exact Duplicates:**
   - Same problem reported by different users
   - Should be closed as duplicate

2. **Related Issues:**
   - Different aspects of the same underlying problem
   - Could be solved together
   - Should reference each other

3. **Conflicting Requests:**
   - Issues asking for opposite things
   - Need discussion to resolve
   - Example: Issue A wants feature X, Issue B wants X removed

For each set of related issues:
- List issue numbers
- Relationship type (duplicate/related/conflicting)
- Recommended action
- Which issue should be the "main" one (most detailed/complete)
```

**What Copilot Does:**
- Compares all issues for similarity
- Identifies duplicates
- Finds related issues
- Flags conflicts

**Example Output:**
```markdown
### Duplicates Found

**Issue #1 and #13: API Key Authentication Problems**
- Both report same issue: API key authentication failing
- Issue #13 has more detail and error logs
- **Action:** Close #1 as duplicate of #13, ask reporter to add info to #13

### Related Issues (Could Solve Together)

**Issues #3, #7, #15: Windows Installation Problems**
- All Windows-specific installation issues
- Common root cause likely
- **Action:** Create epic issue combining all three, fix together

### Conflicting Requests

**Issues #8 vs #20:**
- #8 wants automatic updates
- #20 wants to disable auto-updates
- **Action:** Need discussion - make auto-update optional?
```

**Deliverable:** Add "Duplicates and Relationships" section

---

### 6. Flag Issues Needing More Information

**GitHub Copilot Chat Prompt:**

```
@github Identify issues that are incomplete or vague and need more information before they can be worked on.

Flag issues that are missing:
1. Clear problem description (what's wrong?)
2. Steps to reproduce (how to see the problem?)
3. Expected vs actual behavior
4. Environment details (OS, version, etc.)
5. Error messages or logs
6. Clear acceptance criteria

For each flagged issue:
- Issue number and title
- What information is missing
- Template questions to ask the reporter
- Whether to label as "needs-info" or "incomplete"
```

**What Copilot Does:**
- Identifies vague or incomplete issues
- Determines what's missing
- Generates questions to ask reporters
- Helps improve issue quality

**Deliverable:** Add "Issues Needing Information" section

---

### 7. Create Priority Action Plan

**GitHub Copilot Chat Prompt:**

```
@github Based on all the categorization and analysis, create an action plan for tackling this backlog.

Provide a prioritized plan:

**Week 1 Focus (Immediate):**
- P0 critical issues (list them)
- Quick wins that show progress (list top 5)
- Issues needing info (send requests)

**Week 2-3 Focus (Important):**
- P1 high-priority issues
- Themed groups that can be solved together

**Month 1-2 Focus (Standard):**
- P2 normal priority
- Feature requests with clear value

**Backlog (Low Priority):**
- P3 nice-to-haves
- Consider closing very old low-priority items

For each phase, provide:
- Issue numbers
- Estimated total effort
- Expected outcomes/impact
- Who should work on these (if roles clear)
```

**What Copilot Does:**
- Creates realistic, phased action plan
- Balances quick wins with important work
- Estimates capacity needed
- Provides clear roadmap

**Deliverable:** Add "Priority Action Plan" section

---

### 8. Generate Label Recommendations

**GitHub Copilot Chat Prompt:**

```
@github Based on the issues analyzed, recommend a labeling system for this repository.

Suggest:

1. **Label Categories Needed:**
   - Type labels (bug, feature, docs, question)
   - Priority labels (P0-critical, P1-high, P2-normal, P3-low)
   - Status labels (needs-info, in-progress, blocked, ready)
   - Component labels (api, cli, docs, installer)
   - Effort labels (effort/XS, effort/S, effort/M, effort/L)

2. **Color Coding:**
   - Suggested colors for each label
   - Why (make them scannable)

3. **Label Descriptions:**
   - Clear description for each label

4. **Bulk Labeling Commands:**
   - GitHub CLI commands to label all issues appropriately

Format as:
- Label definitions (for GitHub settings)
- Bulk labeling script
- Before/after view showing current mess → organized system
```

**What Copilot Does:**
- Analyzes issue types to determine needed labels
- Creates consistent label system
- Provides implementation commands
- Shows impact of labeling

**Deliverable:** Add "Label System Recommendations" section

## Next Steps

### LLA Live Session

- [Scenario 2: Automated Fixes](scenario-2-backlog-battle/tasks/task-2.4-automated-fixes.md)


### Self-paced and want to explore

**Ready for the next step?** Continue to [Task 2.2: Find Duplicates and Relationships](task-2.2-duplicates.md).
