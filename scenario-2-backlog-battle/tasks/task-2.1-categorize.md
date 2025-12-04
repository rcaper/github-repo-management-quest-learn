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

---

## Output Format

Your `issue-analysis.md` should include:

```markdown
# Issue Backlog Analysis

**Analyst:** [Your Name]
**Date:** [Date]
**Analyzed with:** GitHub Copilot @github
**Total Issues:** 12

---

## Overview

### Summary Statistics

| Metric | Count | Percentage |
|--------|-------|------------|
| Total Issues | 27 | 100% |
| With Labels | 0 | 0% |
| With Assignees | 0 | 0% |
| Detailed Descriptions | 12 | 44% |
| Vague/Incomplete | 15 | 56% |

### By Type

| Type | Count | % |
|------|-------|---|
| Bugs | 8 | 30% |
| Features | 7 | 26% |
| Documentation | 5 | 19% |
| Questions | 4 | 15% |
| Discussions | 3 | 11% |

### Common Themes

1. **Windows Installation Issues** (5 issues) - 19%
2. **API Documentation Problems** (4 issues) - 15%
3. **Authentication/Security** (3 issues) - 11%
4. **Error Messages Unclear** (3 issues) - 11%

---

## Complete Issue Categorization

| Issue # | Title (truncated) | Type | Priority | Effort | Suggested Labels |
|---------|-------------------|------|----------|--------|------------------|
| #13 | API key authentication failing | bug | P0 | S | bug, P0-critical, api, security |
| #3 | Installation on Windows fails | bug | P0 | M | bug, P0-critical, installer, windows |
| #17 | Docs site returning 404 | bug | P0 | XS | bug, P0-critical, docs |
| #5 | Add Python 3.11 support | feature | P1 | M | feature, P1-high, compatibility |
| #9 | Error messages not helpful | enhancement | P1 | L | enhancement, P1-high, UX |
[Continue for all issues]

### Priority Distribution

- **P0 (Critical):** 3 issues | 11% | ~2-3 days total effort
- **P1 (High):** 7 issues | 26% | ~2 weeks total effort
- **P2 (Normal):** 12 issues | 44% | ~3-4 weeks total effort
- **P3 (Low):** 5 issues | 19% | ~1 week total effort

### Effort Distribution

- **XS (<1hr):** 4 issues | Quick wins!
- **S (1-4hrs):** 8 issues | Good for new contributors
- **M (1-2 days):** 10 issues | Standard work
- **L (3-5 days):** 4 issues | Complex, need planning
- **XL (1+ weeks):** 1 issue | Major initiative

---

## Quick Wins (High Value, Low Effort)

### Top 5 Quick Wins

1. **Issue #17: Docs site 404 error** (P0, XS)
   - **Value:** Users can't access docs (critical)
   - **Fix:** Update broken link in README
   - **Time:** 15 minutes
   - **Automate:** Yes - Copilot could fix this!

2. **Issue #23: Typo in getting started** (P2, XS)
   - **Value:** First impression for new users
   - **Fix:** Correct spelling error
   - **Time:** 5 minutes
   - **Automate:** Yes - perfect for Copilot

3. **Issue #11: Missing import in example** (P1, XS)
   - **Value:** Example doesn't work (frustrating)
   - **Fix:** Add missing import statement
   - **Time:** 10 minutes
   - **Automate:** Yes - Copilot can generate complete example

[Continue for top 5]

**Total Quick Wins Effort:** ~2 hours
**Total Quick Wins Value:** Fixes 3 critical issues, improves user experience

**Recommendation:** Tackle all 5 this week!

---

## Issues by Theme

### Theme 1: Windows Installation (5 issues)

**Issues:** #3, #7, #15, #19, #24

**Summary:** Users on Windows can't install or run the tool due to:
- Path separator issues (3 issues)
- PowerShell vs CMD differences (2 issues)
- Missing Windows-specific instructions (all 5)

**Unified Solution:**
- Create comprehensive Windows setup guide
- Fix path handling in installer
- Add Windows-specific examples
- Test on Windows 10 and 11

**Priority:** P0/P1 (affects significant user base)
**Estimated Effort:** 5-7 days (fix all together)

### Theme 2: API Documentation (4 issues)

**Issues:** #2, #6, #13, #16

**Summary:** API docs are:
- Incomplete (missing endpoints)
- Incorrect (wrong parameter names)
- Outdated (old API version shown)

**Unified Solution:**
- Full API documentation audit
- Generate docs from code (consider automation)
- Add examples for each endpoint

**Priority:** P0/P1
**Estimated Effort:** 3-4 days

[Continue for other themes]

---

## Duplicates and Relationships

### Exact Duplicates

**Issues #1 and #13: API Authentication**
- Both report API key auth failing with same error
- #13 has more detail (error logs, environment)
- **Action:** Close #1 as duplicate of #13
- **Comment for #1:** "This is a duplicate of #13 which has more detail. Please add any additional information to #13."

**Issues #10 and #22: Dark mode request**
- Both asking for dark theme in docs
- Identical request
- **Action:** Close #22 as duplicate of #10 (opened first)

### Related Issues (Solve Together)

**Windows Install Theme:**
- Issues #3, #7, #15 (path issues)
- **Relationship:** Same root cause (Windows path handling)
- **Action:** Create epic issue, fix together

**API Documentation:**
- Issues #2, #6, #16 (incomplete docs)
- **Relationship:** All same API docs problems
- **Action:** One comprehensive API docs update fixes all

### Conflicting Requests

**Issues #8 vs #20:**
- #8: "Add automatic updates"
- #20: "Disable automatic updates - they're annoying"
- **Conflict:** Users want opposite things
- **Action:** Need discussion → Make auto-updates optional (default on, can disable)
- **Create:** New discussion issue to propose solution

---

## Issues Needing More Information

### High Priority (Can't Fix Without Info)

**Issue #4: "Tool crashes sometimes"**
- **Missing:** Steps to reproduce, error message, when it crashes
- **Questions to ask:**
  ```
  Thanks for reporting! To help fix this, could you provide:
  1. What were you doing when it crashed?
  2. Does it crash every time or randomly?
  3. What error message do you see (if any)?
  4. What OS and version are you using?
  ```
- **Label:** needs-info
- **Action:** Add comment, label, check back in 7 days

**Issue #12: "Performance is slow"**
- **Missing:** What's slow? How slow? Compared to what?
- **Questions:** [similar template]

[Continue for all incomplete issues]

**Summary:** 8 issues need more info before they can be worked on.
**Action:** Send info requests this week, close if no response in 14 days.

---

## Priority Action Plan

### Week 1: Critical Issues + Quick Wins

**P0 Critical (Must Fix):**
- [ ] #13: API authentication (2-3 hours)
- [ ] #3: Windows install (1 day)
- [ ] #17: Docs 404 link (15 min)

**Quick Wins (Show Progress):**
- [ ] #23: Typo fix (5 min) - **Assign to Copilot!**
- [ ] #11: Missing import (10 min) - **Assign to Copilot!**
- [ ] #25: Broken link (10 min) - **Assign to Copilot!**
- [ ] #14: Add code example (30 min)
- [ ] #18: Update outdated screenshot (20 min)

**Admin Tasks:**
- [ ] Send "needs-info" requests (8 issues)
- [ ] Close duplicates (2 issues)
- [ ] Set up label system

**Total Effort:** ~2-3 days
**Impact:** 3 critical bugs fixed, 5 improvements shipped, backlog organized

### Week 2-3: High Priority Themes

**Windows Installation Theme (P0/P1):**
- [ ] Fix all Windows path issues (#3, #7, #15)
- [ ] Create Windows setup guide
- [ ] Test on Windows 10/11

**API Documentation Update (P1):**
- [ ] Audit API docs (#2, #6, #16)
- [ ] Add missing endpoints
- [ ] Update examples

**Total Effort:** ~2 weeks
**Impact:** Major pain points resolved

### Month 1-2: Standard Priority

**P2 Normal Issues:**
- Feature requests with clear value
- Documentation improvements
- UX enhancements

**Total:** 12 issues | ~3-4 weeks effort

### Backlog: Low Priority

**P3 Nice-to-Have:**
- #8: Auto-updates (controversial, needs discussion)
- #21: Color scheme options
- #26: Minor UI tweaks

**Action:** Keep in backlog, tackle during slower periods

---

## Label System Recommendations

### Proposed Label System

#### Type Labels

| Label | Color | Description |
|-------|-------|-------------|
| `bug` | #d73a4a | Something isn't working |
| `feature` | #0075ca | New feature or request |
| `enhancement` | #a2eeef | Improvement to existing feature |
| `docs` | #0075ca | Documentation improvement |
| `question` | #d876e3 | Further information requested |
| `discussion` | #cc317c | Ideas and proposals |

#### Priority Labels

| Label | Color | Description |
|-------|-------|-------------|
| `P0-critical` | #b60205 | Blocking issue, fix immediately |
| `P1-high` | #d93f0b | Important, fix soon |
| `P2-normal` | #fbca04 | Standard priority |
| `P3-low` | #c2e0c6 | Nice to have |

#### Status Labels

| Label | Color | Description |
|-------|-------|-------------|
| `needs-info` | #d876e3 | Waiting for more information |
| `duplicate` | #cfd3d7 | Duplicate of another issue |
| `ready` | #0e8a16 | Ready to be worked on |

#### Component Labels

| Label | Color | Description |
|-------|-------|-------------|
| `lakehouse` | #1d76db | Lakehouse module content |
| `medallion` | #1d76db | Medallion architecture |
| `copilot` | #1d76db | Copilot for Fabric |
| `data-warehouse` | #1d76db | Data warehouse content |
| `real-time` | #5319e7 | Real-time analytics |
| `yaml` | #5319e7 | Module metadata issues |

### Bulk Labeling Script

```bash
# Issue #13
gh issue edit 13 --add-label "bug,P0-critical,api"

# Issue #3
gh issue edit 3 --add-label "bug,P0-critical,installer,windows"

# Issue #17
gh issue edit 17 --add-label "bug,P0-critical,docs"

[Continue for all issues]
```

### Before/After View

**Before:**
- Unlabeled issues
- No clear priorities
- Can't filter or organize
- Overwhelming to look at

**After:**
- Every issue labeled by type, priority, component
- Can filter: "Show me P0 bugs in API"
- Can see at a glance: "3 critical, 7 high priority"
- Clear action plan

---

## Key Insights from Analysis

1. **Windows support is biggest pain point** (5 issues)
   - Should be top priority
   - Could be fixed together efficiently

2. **Quick wins available** (5 issues under 1 hour)
   - Can be automated/assigned to Copilot
   - Show quick progress

3. **Documentation needs work** (9 issues docs-related)
   - API docs incomplete
   - Setup guides unclear
   - Examples broken

4. **Issue quality varies widely**
   - 8 need more info before work can start
   - Good opportunity to improve issue template

5. **Some coordination possible**
   - Themes can be solved together (more efficient)
   - Duplicates should be consolidated

---

## Recommendations

### Immediate Actions (This Week)

1. **Fix P0 criticals** (3 issues, ~2 days)
2. **Knock out quick wins** (5 issues, ~2 hours) - **Use Copilot!**
3. **Request missing info** (8 issues, ~30 min)
4. **Close duplicates** (2 issues, ~10 min)
5. **Implement label system** (~1 hour setup)

### Short Term (Next 2-3 Weeks)

1. **Windows installation sprint** (5 issues together)
2. **API documentation update** (4 issues together)
3. **Work through P1 high priority items**

### Longer Term (Next 1-2 Months)

1. **Create issue template** (prevent vague issues)
2. **Set up automated link checking** (prevent broken links)
3. **Work through P2 standard priority**
4. **Discuss and decide on P3 items**

### Process Improvements

1. **Use GitHub Copilot for simple fixes**
   - Assign typos, broken links, simple bugs to Copilot
   - Let it create PRs automatically
   - Review and merge quickly

2. **Create issue templates**
   - Bug report template (with required fields)
   - Feature request template
   - Question template

3. **Set up automation**
   - Auto-label by keywords
   - Stale issue management
   - Link checking in CI

---

## Copilot Queries Used

Most helpful queries:

1. `@github Analyze all issues with quest-sample label and categorize by type, priority, and effort`
2. `@github Find duplicate or related issues in the backlog`
3. `@github Group issues by common themes`
4. `@github Identify quick wins - low effort, high value issues`
5. `@github Which issues are incomplete and need more info?`
6. `@github Create a prioritized action plan for the backlog`

---

*Analysis complete! Ready to tackle the backlog strategically with GitHub Copilot's help.*
```

---

## GitHub Copilot Tips for This Task

### Bulk Analysis

**Use @github for analyzing many items:**

```
@github Analyze all issues with the quest-sample label...
```

This is much faster than asking about issues one by one.

### Ask for Patterns

```
@github What patterns do you see across these issues?
@github What themes emerge?
@github What's the root cause appearing in multiple issues?
```

### Get Specific Recommendations

```
@github Which of these should I work on first and why?
@github Which can be automated?
@github Which should be closed?
```

### Use for Bulk Operations

```
@github Generate GitHub CLI commands to label all issues appropriately
```

---

## Success Criteria

You've completed this task when you:

- ✅ Analyzed all issues with Copilot
- ✅ Categorized each by type, priority, and effort
- ✅ Identified quick wins for immediate action
- ✅ Grouped issues by theme
- ✅ Found duplicates and related issues
- ✅ Flagged incomplete issues
- ✅ Created prioritized action plan
- ✅ Designed label system

---

## Time Management

- **Minutes 0-4:** Generate overview and categorization
- **Minutes 5-8:** Identify quick wins and themes
- **Minutes 9-12:** Find duplicates and relationships
- **Minutes 13-16:** Flag issues needing info
- **Minutes 17-19:** Create action plan and label system
- **Minutes 19-20:** Final review and summary

---

## What's Next?

After categorizing issues, move to **Task 2.2** where you'll use GitHub Copilot to find duplicate and related issues in more detail, and create a plan for consolidation.

---

**Ready for the next step?** Continue to [Task 2.2: Find Duplicates and Relationships](task-2.2-duplicates.md).
