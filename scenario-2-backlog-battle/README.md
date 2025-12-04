# Scenario 2: The Backlog Battle

## The Story

It's Friday, and you're reviewing the documentation repository's issue tracker. Your heart sinks:

> **25 open issues**
> Oldest: 147 days ago
> Newest: 2 days ago
> Labels: None
> Milestones: None
> Assignments: None

The issues range from simple typo fixes to complex requests for new documentation sections. Some are duplicates. Some contradict each other. Many lack enough information to act on.

Your manager walks by:

> "Hey, I noticed we have a lot of open documentation issues. The product team is asking about them. Can you triage the backlog and create a plan? We need to show we're on top of this. Also, let's set up some templates and processes so this doesn't happen again."

**Your mission:** Efficiently triage and categorize the issues, create response strategies, establish templates and processes, and develop a sustainable issue management workflow.

## Scenario Overview

**Duration:** 45-60 minutes
**Difficulty:** Intermediate to Advanced
**Focus:** AI-assisted issue triage and backlog management

## Learning Objectives

By completing this scenario, you will:

1. Learn to efficiently triage large issue backlogs using AI
2. Categorize and prioritize issues systematically
3. Identify duplicates, related issues, and dependencies
4. Create effective issue templates and labels
5. Draft professional, helpful responses at scale
6. Establish sustainable issue management processes
7. Balance quick wins with long-term improvements

## The Issue Backlog

Before starting this scenario, ensure the sample issues have been created by running the **Setup Quest Issues** workflow (`.github/workflows/setup-quest-issues.yml`). This creates 12 realistic GitHub issues representing common Microsoft Learn content challenges:

- **Content bugs** - Broken images, broken cross-reference links, non-working code samples
- **Metadata issues** - Outdated ms.date values, YAML syntax errors
- **Enhancement requests** - Requests for new troubleshooting content
- **Consistency issues** - Terminology inconsistencies across modules
- **Accessibility issues** - Missing alt text on images
- **Questions** - Unclear prerequisites or requirements
- **Duplicates** - Same issue reported differently
- **Vague issues** - Need more information to act on

> **Note:** Look for issues with the `quest-sample` label in your repository's Issues tab.

## Your Tasks

### Task 2.1: Issue Categorization and Prioritization (15 minutes)
**File:** [tasks/task-2.1-categorize.md](tasks/task-2.1-categorize.md)

Use AI to quickly categorize all issues by:
- Type (bug, feature, question, discussion, typo)
- Priority (critical, high, medium, low)
- Effort (quick-win, medium, large)
- Status (actionable, needs-info, wont-fix, duplicate)

**Outcome:** A prioritized, categorized backlog

### Task 2.2: Identify Relationships and Duplicates (10 minutes)
**File:** [tasks/task-2.2-relationships.md](tasks/task-2.2-relationships.md)

Find connections between issues:
- Duplicate issues (same problem, different reporters)
- Related issues (should be worked on together)
- Conflicting issues (mutually exclusive requests)
- Dependencies (issue A blocks issue B)

**Outcome:** A relationship map showing issue connections

### Task 2.3: Create Issue Templates and Labels (15 minutes)
**File:** [tasks/task-2.3-templates.md](tasks/task-2.3-templates.md)

Establish systems to prevent future backlog chaos:
- Issue templates for common request types
- Label system for categorization
- Issue triage process documentation
- Response templates for common scenarios

**Outcome:** Reusable templates and processes

### Task 2.4: Draft Responses and Action Plan (20 minutes)
**File:** [tasks/task-2.4-responses.md](tasks/task-2.4-responses.md)

Create responses for issues and an execution plan:
- Draft responses for 5-7 representative issues
- Close duplicates and wont-fix items
- Request more info where needed
- Create action plan for remaining issues

**Outcome:** Issue responses and remediation roadmap

## How to Approach This Scenario

### Step 0: Set Up the Scenario

Run the **Setup Quest Issues** workflow to create the sample issues:

1. Go to Actions tab in your repository
2. Select "Setup Quest Issues" workflow
3. Click "Run workflow"
4. Wait for the issues to be created
5. Navigate to the Issues tab to see them

### Step 1: Load and Scan

Quickly scan all issues to understand the variety and volume.

### Step 2: Use AI for Bulk Analysis
Don't read every issue in detail. Use AI to:
- Categorize all issues at once
- Find patterns and duplicates
- Generate summaries

### Step 3: Apply the 80/20 Rule
- 20% of issues probably represent 80% of user pain
- Find and prioritize those high-impact issues
- Quick wins can clear out 30-40% of backlog fast

### Step 4: Think Systematically
Don't just process this backlog - create systems to prevent the next one:
- Templates prevent low-quality issues
- Labels enable quick triage
- Processes ensure nothing falls through cracks

### Step 5: Batch Similar Work
Group similar issues and handle them together:
- All typos in one session
- All duplicates closed at once
- Related feature requests combined

## Success Criteria

You've successfully completed this scenario when you:

- ✅ Categorized all issues by type, priority, and effort
- ✅ Identified at least 2 duplicates or related issue groups
- ✅ Created 3-5 issue templates for common types
- ✅ Established a label system and triage process
- ✅ Drafted responses for representative issues
- ✅ Created an actionable roadmap for the backlog
- ✅ Closed or responded to at least 10 issues
- ✅ Reduced "unlabeled" issues to zero

## Tips for Success

1. **Categorize first, prioritize second**: Understanding what you have comes before deciding what to do
2. **Look for patterns**: Similar issues suggest documentation gaps
3. **Be decisive**: Not every issue deserves implementation
4. **Communicate clearly**: Good responses prevent follow-up questions
5. **Create systems, not solutions**: Templates and processes scale better than individual responses
6. **Celebrate quick wins**: Closing 10 easy issues feels good and clears the board

## Time Management

- **Task 2.1 (Categorize)**: 15 minutes - Use AI to bulk categorize
- **Task 2.2 (Relationships)**: 10 minutes - Find duplicates and connections
- **Task 2.3 (Templates)**: 15 minutes - Create reusable systems
- **Task 2.4 (Responses)**: 20 minutes - Draft and plan
- **Buffer**: 10 minutes for review and final plan

## What's Different from Scenario 1?

**Scenario 1** - You audited content (what's wrong in the repo?)
**Scenario 2** - You manage requests (what should we do?)

This scenario is about:
- Prioritization and decision-making
- Stakeholder communication
- Process creation
- Sustainable workflows

## Real-World Application

Every documentation repository eventually faces backlog challenges:
- Issues pile up during busy periods
- Contributors get overwhelmed
- Users get frustrated by no responses
- Team morale suffers from endless backlog

Learning to triage effectively is a crucial skill for documentation maintainers.

## What's Next?

After completing this scenario, you'll be ready for **Part 2** which covers:
- Advanced PR review with multiple agents (Scenario 3)
- Agent orchestration for complex workflows (Scenario 4)
- Enterprise-scale automation patterns

## Need Help?

- **Stuck on a task?** Check the hints section in each task file
- **Want to see solutions?** Review the solution guides in `solutions/`
- **Questions about issue management?** See `../../resources/best-practices.md`

---

**Ready to begin?** Start with [Task 2.1: Issue Categorization and Prioritization](tasks/task-2.1-categorize.md)
