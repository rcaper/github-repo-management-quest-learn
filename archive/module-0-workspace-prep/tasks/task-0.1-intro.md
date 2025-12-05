# Task 0.1: Introduction to Agents and Prompts

## Objective

Learn the fundamentals of GitHub Copilot workspace customization using `.agents` and `.prompts` files.

## Background

GitHub Copilot's workspace features allow you to create:
- **Custom agents** (`.agents` file): Specialized AI assistants with specific roles and expertise
- **Reusable prompts** (`.prompts` file): Template prompts that can be easily invoked and customized

These features transform GitHub Copilot from a general-purpose assistant into a tailored toolkit for your specific workflows.

## What You'll Learn

1. **Agent fundamentals** - How agents work and their benefits
2. **Prompt engineering** - Creating effective, reusable prompts
3. **Workspace integration** - How these features work together
4. **Best practices** - Naming conventions and organization strategies

## Step 1: Explore Example Configurations

First, let's see what agents and prompts look like in action.

### Example .agents File

Create a file named `.agents` in the repository root with this content:

```yaml
documentation-auditor:
  description: Specialized agent for analyzing documentation repositories and identifying content gaps, inconsistencies, and improvement opportunities
  instructions: |
    You are a documentation auditor with expertise in:
    - Content gap analysis and identification
    - Style consistency checking across multiple files
    - Information architecture assessment
    - User experience evaluation for documentation
    - Technical accuracy validation
    
    When analyzing content:
    1. Look for completeness and logical flow
    2. Check for broken or outdated links
    3. Identify missing prerequisites or setup instructions
    4. Assess clarity and accessibility of language
    5. Suggest structural improvements
    
    Always provide actionable recommendations with specific examples.

style-enforcer:
  description: Agent focused on maintaining consistent writing style and documentation standards
  instructions: |
    You are a style guide enforcer for documentation teams. Your expertise includes:
    - Grammar, spelling, and punctuation consistency
    - Tone and voice alignment with brand guidelines
    - Formatting consistency (headings, lists, code blocks)
    - Terminology standardization
    - Accessibility compliance (alt text, heading structure)
    
    When reviewing content:
    1. Check adherence to established style guidelines
    2. Identify inconsistent terminology or phrasing
    3. Suggest improvements for readability and accessibility
    4. Ensure proper markdown formatting
    5. Maintain professional, helpful tone
    
    Provide specific corrections and explanations for suggested changes.
```

### Example .prompts File

Create a file named `.prompts` in the repository root:

```yaml
content-audit:
  description: Comprehensive analysis of repository content and structure
  prompt: |
    Please analyze this repository's documentation with focus on:
    
    **Content Analysis:**
    - Overall structure and organization
    - Completeness of information
    - Content gaps or missing sections
    - Outdated or inaccurate information
    
    **User Experience:**
    - Navigation and findability
    - Clarity of instructions
    - Appropriate depth for target audience
    - Logical flow and sequencing
    
    **Technical Quality:**
    - Link validity and accuracy
    - Code example functionality
    - Prerequisites and setup clarity
    - Cross-references and consistency
    
    Provide a structured report with:
    1. Executive summary
    2. Key findings (prioritized)
    3. Specific recommendations
    4. Quick wins for immediate improvement

style-check:
  description: Review content for style consistency and quality
  prompt: |
    Review the provided content for:
    
    **Style Consistency:**
    - Grammar, spelling, and punctuation
    - Consistent terminology usage
    - Appropriate tone and voice
    - Proper markdown formatting
    
    **Quality Factors:**
    - Clarity and conciseness
    - Logical organization
    - Accessibility compliance
    - Professional presentation
    
    **Output Format:**
    1. Overall assessment (1-10 score)
    2. Specific issues found (with line references if applicable)
    3. Suggested improvements
    4. Style guide recommendations

generate-summary:
  description: Create executive summaries of content or changes
  prompt: |
    Create a comprehensive summary of the provided content including:
    
    **Key Information:**
    - Main topics and themes
    - Important facts or data points
    - Key takeaways or conclusions
    
    **Structure:**
    - Logical organization of information
    - Relationships between topics
    - Priority or importance ranking
    
    **Actionable Items:**
    - Decisions that need to be made
    - Next steps or follow-up actions
    - Areas requiring attention
    
    Format as a clear, executive-level summary suitable for stakeholder review.
```

## Step 2: Test the Configuration

1. **Save both files** in your repository root
2. **Reload VS Code** (or restart GitHub Copilot extension)
3. **Open Copilot Chat** (Ctrl+Shift+I or Cmd+Shift+I)

### Test Your Agents

Try these commands in Copilot Chat:

```
@documentation-auditor Please analyze the structure of the learn-pr/wwl folder
```

```
@style-enforcer Review the learn-pr/wwl/get-started-lakehouses/index.yml file for style consistency
```

### Test Your Prompts

Try these commands in Copilot Chat:

```
#content-audit Analyze the learn-pr/wwl/analyze-devops-continuous-planning-intergration folder
```

```
#style-check Please review this file: learn-pr/wwl/analyze-devops-continuous-planning-intergration/index.yml
```

## Step 3: Understanding the Results

Notice how:
- **Agents respond with their specialized perspective** and expertise
- **Prompts provide structured, consistent output** following your templates
- **Workspace context (@workspace)** gives agents and prompts full repository awareness

## Reflection Questions

1. How do the agent responses differ from standard GitHub Copilot responses?
2. What makes the prompt-generated output more useful than ad-hoc queries?
3. How could you customize these agents and prompts for your specific needs?

## Next Steps

Ready to create your own agents? Continue to [Task 0.2: Creating Your First Agent](task-0.2-custom-agent.md)

---

**Key Takeaway:** Agents and prompts transform GitHub Copilot into a specialized toolkit tailored to your workflow, providing consistent, expert-level assistance across all your documentation tasks.
