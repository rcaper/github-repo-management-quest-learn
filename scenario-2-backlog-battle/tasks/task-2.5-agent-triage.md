# Task 3.5: Advanced Issue Triage with Agents

## Objective

Use specialized agents to automatically triage, categorize, and prioritize your issue backlog at scale.

## Prerequisites

- Completed Module 0: Workspace Preparation
- Sample issues created by running "Setup Quest Issues" workflow
- Working `.agents` configuration with issue management agents

## Your Challenge

Apply AI agents to efficiently process and organize your entire issue backlog using automated triage workflows.

## Step 1: Deploy Issue Triage Agent

Add this specialized agent to your `.agents` file:

```yaml
issue-triager:
  description: Expert issue management specialist for automated triage, categorization, and prioritization of repository issues
  instructions: |
    You are an issue management expert specializing in:
    - Rapid issue categorization and labeling
    - Priority assessment based on impact and urgency
    - Effort estimation and resource allocation
    - Stakeholder impact analysis
    - Workflow routing and assignment recommendations
    
    Your triage methodology:
    1. **Quick Classification**: Identify issue type (bug, feature, docs, question, duplicate)
    2. **Priority Assessment**: Evaluate business impact and user urgency
    3. **Effort Estimation**: Estimate implementation complexity and time
    4. **Resource Matching**: Suggest appropriate team/individual assignment
    5. **Workflow Routing**: Recommend next steps and processes
    
    **Triage Output Format:**
    ```
    ISSUE: [title]
    TYPE: [Bug/Feature/Documentation/Question/Duplicate/Invalid]
    PRIORITY: [P0-Critical/P1-High/P2-Medium/P3-Low]
    EFFORT: [XS/S/M/L/XL] (< 1hr / 1-4hr / 1-2day / 1week / >1week)
    IMPACT: [Critical/High/Medium/Low]
    SKILLS: [Technical/Content/Design/Strategy/Support]
    
    RECOMMENDED LABELS:
    - [label1, label2, label3]
    
    ASSIGNMENT SUGGESTION:
    - Team: [Frontend/Backend/Docs/Support]
    - Skills needed: [specific expertise required]
    
    NEXT STEPS:
    - [ ] [Immediate action required]
    - [ ] [Follow-up tasks]
    
    NOTES: [Additional context or considerations]
    ```
    
    Focus on rapid, consistent triage that enables efficient issue resolution.
```

## Step 2: Bulk Issue Analysis

Use your triage agent to process all sample issues:

```
@issue-triager Please analyze and triage all the quest-sample issues in this repository. For each issue, provide:
- Complete triage assessment using standard format
- Priority ranking with justification
- Resource allocation recommendations
- Workflow routing suggestions
```

### Triage Analysis Tasks

1. **Review triage consistency** across similar issues
2. **Validate priority rankings** against business impact
3. **Check effort estimates** for realism
4. **Assess assignment recommendations** for team capacity

## Step 3: Rapid Triage Workflow

Use your **rapid-issue-triage** prompt for efficient processing:

```
#rapid-issue-triage @github Process all open issues using fast-track triage protocol:
- Identify duplicates for immediate closure
- Flag critical issues requiring immediate attention
- Batch similar issues for efficient processing
- Generate bulk labeling recommendations
```

### Fast-Track Benefits

Observe how rapid triage:
- **Processes issues in under 30 seconds each**
- **Identifies patterns** across multiple issues
- **Suggests bulk actions** for efficiency
- **Prioritizes critical items** for immediate attention

## Step 4: Create Triage Dashboard

Generate a comprehensive triage summary:

```
@qa-coordinator Create an issue backlog dashboard based on our triage analysis:
- Overall backlog health assessment
- Priority distribution and resource requirements
- Quick wins identification and impact analysis
- Strategic recommendations for backlog management
```

### Dashboard Components

Your triage dashboard should include:
- **Backlog overview** (total issues by type/priority)
- **Resource allocation** (effort distribution)
- **Quick wins list** (high-impact, low-effort items)
- **Strategic priorities** (alignment with business goals)

## Success Criteria

- [ ] Issue triage agent deployed and tested
- [ ] All sample issues triaged using consistent methodology
- [ ] Rapid triage workflow implemented and validated
- [ ] Comprehensive triage dashboard created
- [ ] Priority rankings justified and documented
- [ ] Resource allocation recommendations provided

## Next Steps

Ready to detect duplicates automatically? Continue to [Task 3.6: Automated Duplicate Detection](task-3.6-duplicate-detection.md)