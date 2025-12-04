# Task 3.4: Draft Responses and Action Plan

**Duration:** 20 minutes
**Difficulty:** Intermediate to Advanced

## Objective

Draft professional responses for representative issues, finalize your action plan, and prepare to execute on your backlog strategy.

## Context

You've categorized, prioritized, identified relationships, and created systems. Now it's time to take action:
- Close issues that should be closed
- Request information where needed
- Draft thoughtful responses
- Create a final execution roadmap

This task brings together everything you've learned and produces immediately actionable outputs.

## Your Challenge

Write responses for 7-10 representative issues covering different scenarios, then finalize your comprehensive backlog action plan.

## Tasks

### 1. Draft Closure Responses (Duplicates)

**For each duplicate issue:**
- Link to the original
- Thank the reporter
- Invite them to subscribe to the original

**Example AI Prompt:**
```
For these duplicate issues from my analysis:

[List duplicate pairs]

Draft professional closure responses following this template:
- Thank the reporter
- Acknowledge the issue
- Link to original issue being tracked
- Invite them to subscribe/contribute there
- Be warm and appreciative

Keep responses 2-3 sentences, friendly and professional.
```

**Deliverable:** Add "Duplicate Closures" section to `issue-responses.md`

### 2. Draft Closure Responses (Out of Scope)

**For wont-fix issues:**
- Thank them sincerely
- Explain why (briefly)
- Suggest alternatives
- Be empathetic

**Example AI Prompt:**
```
For these out-of-scope issues:

Issue #X: [Description]
Reason out of scope: [Your reasoning]

Draft polite closure responses that:
- Thank them for the suggestion
- Briefly explain why it's out of scope (2-3 sentences)
- Suggest alternatives if applicable
- Keep the door open (they can still contribute in other ways)
- Maintain positive relationship
```

**Deliverable:** Add "Out of Scope Closures" section

### 3. Draft Information Requests

**For unclear issues:**
- Thank them
- Ask specific questions
- Set expectation for response
- Make it easy to reply

**Example AI Prompt:**
```
For these issues needing more information:

Issue #X: [Vague description]

Draft responses that:
- Thank the reporter
- Explain what information is needed to help
- Ask 2-3 specific, clear questions
- Explain why you need this info
- Set expectation (will follow up, may close if no response in 30 days)
```

**Deliverable:** Add "Information Requests" section

### 4. Draft Acknowledgment Responses (High Priority)

**For issues you'll fix:**
- Acknowledge importance
- Explain priority
- Give timeline
- Thank them

**Example AI Prompt:**
```
For these high-priority issues we'll address:

Issue #X: [Critical bug]
Issue #Y: [Important feature request]

Draft acknowledgment responses that:
- Thank them enthusiastically
- Acknowledge the importance/impact
- Explain priority level and why
- Give realistic timeline
- Show we're taking it seriously
```

**Deliverable:** Add "High Priority Acknowledgments" section

### 5. Draft Invitation Responses (Good First Issues)

**For issues perfect for contributors:**
- Acknowledge the issue
- Invite them to contribute
- Provide guidance
- Offer support

**Example AI Prompt:**
```
For these good-first-issue items:

Issue #X: [Simple typo fix]
Issue #Y: [Straightforward enhancement]

Draft responses that:
- Thank them for reporting
- Note it's a good opportunity to contribute
- Ask if they'd like to submit a fix
- Link to CONTRIBUTING guide
- Offer to help if they contribute
- Note we'll add to backlog if not
```

**Deliverable:** Add "Contribution Invitations" section

### 6. Create Implementation Roadmap

**Prompt your AI to:**
- Organize responses by timing
- Create execution checklist
- Sequence the work

**Example AI Prompt:**
```
Based on all my categorization, priorities, and responses:

Create a day-by-day implementation plan for the next 2 weeks:

Day 1:
- Close all duplicates (X issues)
- Close out-of-scope issues (X issues)
- Send information requests (X issues)

Day 2:
- Complete quick wins (specific issues)
- Acknowledge high-priority items

Week 2:
- Start on critical fixes
- [Continue...]

Make this concrete and actionable.
```

**Deliverable:** Add "Implementation Roadmap" section

### 7. Create Success Metrics

**Define how you'll measure progress:**
- Backlog reduction
- Response time
- Issue resolution
- Quality improvements

**Example AI Prompt:**
```
Create success metrics for this backlog cleanup:

Current state:
- 25 total issues
- 0 labeled
- Avg age: X days
- 0 responses

Define metrics for:
1. Week 1 goals (quick wins)
2. Week 4 goals (critical items)
3. Week 8 goals (medium priority)
4. Ongoing health metrics

Include specific, measurable targets.
```

**Deliverable:** Add "Success Metrics" section

## Output Format

### issue-responses.md

```markdown
# Issue Response Drafts

**Created:** [Date]
**Total Responses:** [Count]
**Ready for:** Immediate execution

---

## Duplicate Closures

### Issue #17: Can't install - link returns 404

```markdown
Thanks for reporting this! This is a duplicate of #3 which we're actively tracking.

I'm closing this issue to consolidate discussion, but please subscribe to #3 for updates. If you have additional details that aren't covered there, feel free to add them.

Thanks for helping us improve the documentation!
```

**Action:** Close as duplicate, apply `duplicate` label

---

### Issue #[X]: [Title]

[Similar format...]

---

## Out of Scope Closures

### Issue #12: Add video tutorials for every feature

```markdown
Thanks for the suggestion! We appreciate you thinking about ways to improve our documentation.

After team discussion, we've decided video tutorials are outside our current scope because:
- Our small team focuses on written documentation
- Videos require significant ongoing maintenance
- We rely on community video creators for this content

However, check out these community resources:
- [YouTube Channel X] has great video walkthroughs
- [Blog Y] has video tutorials

We're closing this as won't-fix, but we appreciate the suggestion! If you're interested in creating video content, we'd be happy to link to it.
```

**Action:** Close as wont-fix, apply `wont-fix` label

---

## Information Requests

### Issue #8: Docs are confusing

```markdown
Thanks for the feedback! We definitely want to improve any confusing documentation.

To help us address this, could you provide some specifics:

1. Which documentation pages are confusing? (Links would be helpful)
2. What specifically is unclear? (terminology, organization, missing steps, etc.)
3. What were you trying to accomplish when you got confused?
4. What would make it clearer for you?

We'll follow up once we have this information. If we don't hear back within 30 days, we'll close this issue, but you're welcome to reopen it anytime with the details.

Thanks!
```

**Action:** Apply `needs-info` label, set reminder for 30 days

---

## High Priority Acknowledgments

### Issue #3: Installation link broken - returns 404

```markdown
Thanks for reporting this! You're absolutely right - this is blocking new users from getting started.

I've labeled this as P0-critical and am fixing it right now. The correct link should be [URL].

Expected fix: Within 2 hours
I'll update this issue when it's deployed.

Thanks for catching this quickly!
```

**Action:**
- Apply labels: `bug`, `P0-critical`, `area:installation`
- Self-assign
- Fix within 2 hours
- Update issue when complete

---

### Issue #7: Missing authentication tutorial

```markdown
Thanks for this suggestion! Authentication is definitely a key topic we should cover better.

I've labeled this as P1-high because it's a frequent question from new users. We're planning to add a comprehensive authentication tutorial covering:
- Basic authentication setup
- OAuth integration
- API key management
- Security best practices

Expected timeline: 2-3 weeks
We'll update this issue as we make progress.

Thanks for helping us identify this gap!
```

**Action:**
- Apply labels: `enhancement`, `P1-high`, `area:tutorials`
- Add to next sprint
- Update in 1 week with progress

---

## Contribution Invitations

### Issue #15: Typo in quick start guide

```markdown
Thanks for catching this typo! Good eye.

This looks like a great opportunity for a first contribution if you're interested! Here's how to submit a fix:

1. Check our [CONTRIBUTING.md](link) for guidelines
2. Fork the repository
3. Make the typo fix
4. Submit a pull request

It should only take a few minutes! We're here to help if you have questions.

If you'd prefer not to contribute, no worries - I've labeled this as `good-first-issue` and we'll fix it soon.

Thanks for the report!
```

**Action:**
- Apply labels: `typo`, `P2-medium`, `good-first-issue`
- Wait 1 week for contributor response
- If no response, fix internally

---

## Quick Win Responses

For quick wins (small effort, clear action):

### Issue #22: Update Python version in examples

```markdown
Good catch! You're right that our examples still reference Python 3.8 when 3.12 is current.

I'm updating all the version references now. Should be done within the hour.

Thanks for keeping our docs current!
```

**Action:**
- Fix immediately (30 min)
- Update issue when complete
- Close

---

## Implementation Roadmap

### Day 1: Clear the Deck (2 hours)

**Morning (1 hour):**
- [ ] Close 3 duplicate issues with responses
- [ ] Close 2 out-of-scope issues with responses
- [ ] Label all issues with type/priority/component

**Afternoon (1 hour):**
- [ ] Send 4 information requests
- [ ] Post acknowledgments on 5 high-priority issues
- [ ] Update project board with categories

**Result:** Backlog down to 16 actionable issues

---

### Days 2-5: Quick Wins (4-5 hours)

**Each day: 1 hour**
- [ ] Day 2: Fix issues #15, #22, #28 (typos, minor fixes)
- [ ] Day 3: Fix issues #4, #11 (broken links)
- [ ] Day 4: Fix issues #19, #31 (quick updates)
- [ ] Day 5: Fix issues #25, #30 (add missing content)

**Result:** 8 issues closed, quick improvements shipped

---

### Week 2: Critical Priorities (10-15 hours)

- [ ] Issue #3: Fix installation (P0) - 2h
- [ ] Issue #9: Update API docs (P0) - 3h
- [ ] Issue #7: Authentication tutorial (P1) - 5h
- [ ] Issue #14: Navigation fix (P1) - 3h
- [ ] Issue #21: Error handling docs (P1) - 2h

**Result:** No critical or high-priority issues remaining

---

### Weeks 3-6: Medium Priority (25-35 hours)

Spread across multiple sprints:
- [ ] Features and enhancements (8 issues)
- [ ] Documentation expansions
- [ ] Structural improvements

**Result:** Comprehensive, polished documentation

---

### Ongoing: Process Maintenance

**Weekly:**
- [ ] Triage new issues within 48h
- [ ] Review `needs-info` issues, close stale ones
- [ ] Update roadmap based on progress

**Monthly:**
- [ ] Review open issue count
- [ ] Close stale issues (>90 days, no activity)
- [ ] Adjust priorities based on user feedback

---

## Success Metrics

### Week 1 Targets

- ✅ **Backlog size:** 25 → 16 → 8
- ✅ **Labeled issues:** 0% → 100%
- ✅ **Response rate:** 0% → 100% (all issues acknowledged)
- ✅ **Quick wins closed:** 8 issues

### Month 1 Targets

- ✅ **Critical issues:** 0 remaining
- ✅ **High priority issues:** 0 remaining
- ✅ **Avg issue age:** Reduce from 50 days to 20 days
- ✅ **Issue response time:** <24h first response

### Quarter 1 Targets

- ✅ **Backlog size:** <5 open issues
- ✅ **Documentation coverage:** All key topics covered
- ✅ **User feedback:** "Documentation helped" rating >80%
- ✅ **Process:** Triage workflow established and running smoothly

### Ongoing Health Metrics

Track monthly:
- **New issues per week:** Target <5
- **Closed issues per week:** Target >5
- **Avg time to close:** Target <14 days
- **Backlog trend:** Decreasing or stable
- **Duplicate rate:** Target <10%

---

## Execution Checklist

Ready to execute? Follow this checklist:

### Setup (30 min)
- [ ] Import label configuration: `gh label sync -f labels.yml`
- [ ] Add issue templates to `.github/ISSUE_TEMPLATE/`
- [ ] Create saved responses in GitHub
- [ ] Set up project board with columns (Triage, Quick Win, In Progress, Done)

### Day 1 Execution (2 hours)
- [ ] Label all issues
- [ ] Post all prepared responses
- [ ] Close duplicates and out-of-scope
- [ ] Send information requests

### Daily Standup Questions (5 min/day)
- What issues did I close yesterday?
- What will I work on today?
- Are any issues blocked?
- Do I need help with anything?

### Weekly Review (30 min)
- Review backlog size trend
- Check response times
- Adjust priorities if needed
- Celebrate progress!

---

## Tips for Execution

1. **Batch similar work:** Respond to all duplicates at once, fix all typos together
2. **Use templates:** Customize rather than write from scratch
3. **Track time:** Note how long things actually take vs estimates
4. **Celebrate wins:** Closing issues feels good - acknowledge progress
5. **Stay organized:** Update project board as you work
6. **Be responsive:** Answer contributor questions quickly
7. **Iterate:** Adjust the plan based on what you learn

---

## What You've Accomplished

By completing this task, you've:

✅ Drafted professional responses for all issue types
✅ Created a realistic, actionable execution plan
✅ Defined success metrics
✅ Built a sustainable process
✅ Transformed chaos into organized work

**You're ready to execute!**

---

*This completes Scenario 3. You now have all the skills and tools for effective issue management.*
```

## Success Criteria

- ✅ Drafted 7-10 professional issue responses
- ✅ Covered all scenarios (closures, requests, acknowledgments)
- ✅ Created day-by-day implementation roadmap
- ✅ Defined specific success metrics
- ✅ Responses are professional and empathetic
- ✅ Plan is realistic and actionable

## Hints

<details>
<summary>Hint 1: Tone Matters</summary>

Every response should:
- Thank the reporter (they took time to help you)
- Be professional but warm
- Set clear expectations
- End positively

Never be dismissive or defensive.
</details>

<details>
<summary>Hint 2: Be Specific</summary>

Vague: "We'll look into this"
Specific: "I'm fixing this today, should be deployed by 5pm"

Specific responses build trust.
</details>

<details>
<summary>Hint 3: Close Aggressively</summary>

It's okay to close issues! Reasons to close:
- Duplicates
- Out of scope
- Already fixed
- Can't reproduce after asking for info
- Stale (no response in 30 days)

A clean backlog is healthy.
</details>

<details>
<summary>Hint 4: Make Roadmap Realistic</summary>

Better to under-promise and over-deliver.
Add buffer time for unexpected issues.
Don't commit to more than you can actually do.
</details>

## Time Management

- **Minutes 0-8:** Draft responses for different issue types
- **Minutes 9-14:** Create implementation roadmap
- **Minutes 15-18:** Define success metrics
- **Minutes 19-20:** Review and finalize

## Quest Complete!

Congratulations! You've completed all three scenarios of the GitHub Repository Management Quest.

You now have practical skills in:
- ✅ Repository exploration and auditing
- ✅ PR review workflows
- ✅ Issue triage and management
- ✅ Template and process creation
- ✅ AI-assisted documentation work

### Apply Your Learning

Take these skills and apply them to your own repositories:
1. Audit your current documentation
2. Establish review processes
3. Implement issue templates
4. Use AI to work more efficiently

---

🎉 **Congratulations!** You've completed Scenario 2 - Issue Triage. Ready to continue? Move to **[Scenario 3: The Big Merge](../../scenario-3-big-merge/README.md)** to learn PR review techniques!
