# Task 0.3: Building a Prompt Library

## Objective

Create a comprehensive library of reusable prompts for documentation workflows.

## Your Challenge

Expand your `.prompts` file with templates for common documentation tasks.

## Step 1: Add Repository Management Prompts

Add these prompts to your `.prompts` file:

```yaml
quick-fixes:
  description: Identify and suggest quick wins for immediate improvement
  prompt: |
    Analyze the provided content and identify quick fixes that can be implemented immediately:
    
    **Priority Areas:**
    - Broken links or missing references
    - Simple grammar or spelling errors
    - Formatting inconsistencies
    - Missing or unclear headings
    - Incomplete code examples
    
    **Output Format:**
    1. Issue type and location
    2. Current state vs. desired state
    3. Estimated effort (Low/Medium/High)
    4. Implementation steps
    
    Focus on changes that provide maximum impact with minimal effort.

compare-versions:
  description: Compare different versions or sections of content
  prompt: |
    Compare the provided content and identify:
    
    **Key Differences:**
    - Content additions or removals
    - Structural changes
    - Style or tone variations
    - Technical accuracy differences
    
    **Assessment:**
    - Which version is more effective and why
    - Strengths and weaknesses of each
    - Recommendations for improvement
    - Merge suggestions if applicable
    
    Provide a clear comparison table and actionable recommendations.

create-checklist:
  description: Generate checklists for review or quality assurance
  prompt: |
    Create a comprehensive checklist based on the provided content or requirements:
    
    **Checklist Categories:**
    - Content completeness and accuracy
    - Style and formatting consistency
    - Technical requirements
    - User experience factors
    - Quality assurance items
    
    **Format:**
    - [ ] Checkable items with clear criteria
    - Organized by priority or workflow stage
    - Include brief explanations for complex items
    - Add relevant links or references
    
    Make the checklist actionable and easy to follow.
```

## Step 2: Create Workflow-Specific Prompts

Add prompts for specific scenarios you'll encounter:

```yaml
issue-analysis:
  description: Analyze GitHub issues for patterns and prioritization
  prompt: |
    Analyze the provided issues and create:
    
    **Categorization:**
    - Issue types (bug, feature, documentation, question)
    - Priority levels (critical, high, medium, low)
    - Effort estimates (quick win, moderate, complex)
    - Relationship mapping (duplicates, dependencies)
    
    **Insights:**
    - Common patterns or themes
    - Resource allocation suggestions
    - Quick wins for immediate action
    - Long-term strategic recommendations
    
    Present as an executive summary with actionable next steps.

pr-review-guide:
  description: Generate comprehensive PR review comments
  prompt: |
    Review the provided pull request changes and generate:
    
    **Technical Review:**
    - Code quality and best practices
    - Documentation accuracy and completeness
    - Consistency with existing patterns
    - Potential impact assessment
    
    **Constructive Feedback:**
    - Specific suggestions for improvement
    - Positive reinforcement for good practices
    - Questions for clarification
    - Additional resources or examples
    
    **Summary:**
    - Overall assessment and recommendation
    - Priority items to address
    - Optional enhancements
    
    Maintain a supportive, collaborative tone throughout.
```

## Step 3: Test Your Prompt Library

Test each prompt with relevant content:

1. **Quick fixes prompt:**
   ```
   #quick-fixes Please analyze: learn-pr/wwl/get-started-lakehouses/includes/1-introduction.md
   ```

2. **Issue analysis prompt:**
   ```
   #issue-analysis @workspace Look at the sample issues created by the setup workflow
   ```

3. **Create checklist prompt:**
   ```
   #create-checklist Create a documentation review checklist for Microsoft Learn modules based on the learn-pr/wwl structure
   ```

## Step 4: Create Your Own Prompts

Design 2-3 additional prompts for tasks specific to your workflow. Consider:
- Meeting note summarization
- Content planning and roadmapping
- User feedback analysis
- Competitive analysis
- Migration planning

## Success Criteria

- [ ] All provided prompts added and tested
- [ ] Custom prompts created for your specific needs
- [ ] Prompts generate consistent, useful output
- [ ] Prompt library covers your common workflows

## Next Steps

Ready to optimize your setup? Continue to [Task 0.4: Testing and Optimization](task-0.4-optimization.md)