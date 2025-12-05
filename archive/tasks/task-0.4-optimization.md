# Task 0.4: Testing and Optimization

## Objective

Test your agents and prompts thoroughly, then optimize them for better performance and reliability.

## Your Challenge

Ensure your workspace configuration is robust, consistent, and ready for real-world use.

## Step 1: Comprehensive Testing

### Test Agent Consistency

Run the same query with different agents and compare results:

```
@documentation-auditor Analyze the structure of learn-pr/wwl/get-started-lakehouses
```

```
@style-enforcer Analyze the structure of learn-pr/wwl/get-started-lakehouses
```

```
@link-checker Analyze the structure of learn-pr/wwl/get-started-lakehouses
```

**Questions to consider:**
- Do agents stay focused on their specialization?
- Are responses consistently helpful?
- Do agents complement each other well?

### Test Prompt Reliability

Use the same prompt on different content types:

```
#content-audit learn-pr/wwl/get-started-lakehouses/index.yml
```

```
#content-audit learn-pr/wwl/describe-medallion-architecture/index.yml
```

```
#content-audit learn-pr/wwl/introduction-to-copilot-fabric/index.yml
```

**Questions to consider:**
- Do prompts work consistently across different content?
- Is the output format stable and useful?
- Are the results actionable?

## Step 2: Performance Optimization

### Refine Agent Instructions

Based on your testing, improve your agents:

1. **Add specific examples** of good vs. bad responses
2. **Clarify scope and boundaries** - what should the agent focus on?
3. **Improve output formatting** - make results more actionable
4. **Add context awareness** - help agents understand their role in larger workflows

Example optimization:
```yaml
documentation-auditor:
  description: Specialized agent for analyzing documentation repositories and identifying content gaps, inconsistencies, and improvement opportunities
  instructions: |
    You are a documentation auditor with expertise in technical content analysis.
    
    **Your Primary Focus:**
    - Content completeness and logical structure
    - Information gaps that impact user success
    - Consistency across related documents
    - Alignment with user journey and needs
    
    **Analysis Framework:**
    1. Structural Assessment: Organization, navigation, discoverability
    2. Content Quality: Accuracy, clarity, completeness
    3. User Experience: Flow, prerequisites, examples
    4. Maintenance: Currency, link validity, consistency
    
    **Output Format:**
    Always structure responses as:
    - Executive Summary (2-3 sentences)
    - Key Findings (prioritized list)
    - Specific Recommendations (actionable items)
    - Quick Wins (immediate improvements)
    
    **Scope Boundaries:**
    Focus on content strategy and user experience, not code quality or technical implementation details.
```

### Optimize Prompt Templates

Improve your prompts for better results:

1. **Add specific output formats** to ensure consistency
2. **Include examples** of desired responses
3. **Specify scope clearly** to avoid off-topic responses
4. **Add quality criteria** for self-assessment

Example optimization:
```yaml
content-audit:
  description: Comprehensive analysis of repository content and structure with actionable recommendations
  prompt: |
    Perform a comprehensive content audit following this structured approach:
    
    **Analysis Areas (required):**
    1. **Content Architecture**: Structure, organization, findability
    2. **Quality Assessment**: Accuracy, completeness, clarity
    3. **User Experience**: Flow, prerequisites, examples, accessibility
    4. **Maintenance Status**: Currency, broken links, consistency
    
    **Required Output Format:**
    
    ## Executive Summary
    [2-3 sentences summarizing overall state and priority areas]
    
    ## Key Findings
    ### High Priority Issues
    - [Issue 1]: [Impact] - [Location]
    - [Issue 2]: [Impact] - [Location]
    
    ### Opportunities for Improvement
    - [Opportunity 1]: [Benefit] - [Effort estimate]
    
    ## Specific Recommendations
    1. **[Action Item]**: [Description] - Priority: [High/Medium/Low]
    2. **[Action Item]**: [Description] - Priority: [High/Medium/Low]
    
    ## Quick Wins (Can be implemented in <1 hour)
    - [ ] [Quick fix 1]
    - [ ] [Quick fix 2]
    
    **Quality Check**: Ensure all recommendations are specific, actionable, and prioritized.
```

## Step 3: Documentation and Best Practices

Create documentation for your workspace setup:

### Create Agent Documentation

Create `module-0-workspace-prep/my-agents-config.md`:

```markdown
# My Custom Agents Configuration

## Agent Roster

### documentation-auditor
**Purpose**: Content analysis and improvement recommendations
**Best Used For**: Repository overviews, content gap analysis, strategic planning
**Sample Query**: `@documentation-auditor Analyze the overall content strategy for this repository`

### style-enforcer
**Purpose**: Style consistency and quality assurance
**Best Used For**: Content review, style guide enforcement, quality checks
**Sample Query**: `@style-enforcer Review this document for style consistency and clarity`

### link-checker
**Purpose**: Link validation and management
**Best Used For**: Link audits, reference validation, maintenance planning
**Sample Query**: `@link-checker Find and validate all links in this directory`

## Usage Guidelines

1. **Combine agents** for comprehensive analysis
2. **Use specific queries** for better results
3. **Provide context** about your goals
4. **Follow up** with clarifying questions

## Optimization Notes

[Document what you learned during testing and what improvements you made]
```

### Create Prompt Library Documentation

Create `module-0-workspace-prep/my-prompts-library.md`:

```markdown
# My Prompt Library

## Content Analysis Prompts

### #content-audit
**Purpose**: Comprehensive repository analysis
**Best Used With**: @workspace for full context
**Expected Output**: Structured report with executive summary and action items

### #quick-fixes
**Purpose**: Identify immediate improvements
**Best Used With**: Specific files or directories
**Expected Output**: Prioritized list of easy wins

## Workflow Prompts

### #issue-analysis
**Purpose**: GitHub issue triage and categorization
**Best Used With**: Issue lists or individual issues
**Expected Output**: Categorization and priority recommendations

### #pr-review-guide
**Purpose**: Generate comprehensive PR feedback
**Best Used With**: PR diffs or changed files
**Expected Output**: Structured review comments

## Usage Tips

1. **Combine with agents** for specialized analysis
2. **Use @workspace** for full repository context
3. **Specify scope** in your queries for better results
4. **Follow prompt structure** for consistent outputs
```

## Step 4: Final Validation

Run a complete test of your workspace:

1. **Test all agents** with the same content
2. **Test all prompts** with different content types
3. **Combine agents and prompts** in realistic workflows
4. **Document any remaining issues** for future improvement

## Success Criteria

- [ ] All agents tested and optimized
- [ ] All prompts provide consistent, useful output
- [ ] Documentation created for your configuration
- [ ] Workspace ready for use in Scenarios 1-4
- [ ] Performance meets your quality standards

## Congratulations!

You've successfully created a customized GitHub Copilot workspace! Your agents and prompts will now enhance your productivity throughout the rest of the quest.

## Next Steps

Ready to use your new workspace configuration? Continue to [Scenario 1: The Inheritance](../../scenario-1-inheritance/README.md) where you'll put your custom agents and prompts to work!

---

**Pro Tip**: Keep iterating on your agents and prompts as you use them. The best configurations evolve based on real-world usage and feedback.