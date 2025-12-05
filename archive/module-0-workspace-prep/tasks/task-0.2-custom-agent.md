# Task 0.2: Creating Your First Agent

## Objective

Build a custom agent tailored to your specific documentation needs.

## Your Challenge

Create a "link-checker" agent that specializes in finding and validating links in documentation.

## Step 1: Design Your Agent

Add this agent to your `.agents` file:

```yaml
link-checker:
  description: Specialized agent for finding, validating, and managing links in documentation
  instructions: |
    You are a link validation specialist with expertise in:
    - Identifying all types of links (internal, external, relative, absolute)
    - Checking link validity and accessibility
    - Finding broken or outdated references
    - Suggesting link organization improvements
    - Recommending link maintenance strategies
    
    When analyzing links:
    1. Catalog all links found in the content
    2. Identify potentially broken or problematic links
    3. Check for consistency in link formatting
    4. Suggest improvements for link organization
    5. Recommend maintenance procedures
    
    Always provide actionable recommendations with specific examples and prioritization.
```

## Step 2: Test Your Agent

Try your new agent with these commands:

```
@link-checker Please analyze all links in the learn-pr/wwl/get-started-lakehouses directory
```

```
@link-checker Check this file for link issues: learn-pr/wwl/introduction-to-copilot-fabric/index.yml
```

## Step 3: Refine and Optimize

Based on the results:
1. **Adjust the instructions** if the agent isn't focusing on what you need
2. **Add more specific guidance** for better results
3. **Test with different content** to ensure consistency

## Your Task

Create one additional custom agent of your choice. Consider:
- **Tutorial validator** - Tests step-by-step instructions
- **Accessibility checker** - Reviews content for accessibility compliance
- **Content planner** - Helps plan documentation roadmaps
- **User journey mapper** - Analyzes user flows through documentation

## Success Criteria

- [ ] Link-checker agent created and tested
- [ ] Custom agent of your choice created
- [ ] Both agents provide useful, actionable feedback
- [ ] Agents respond consistently across different content

## Next Steps

Ready to build reusable prompts? Continue to [Task 0.3: Building a Prompt Library](task-0.3-prompt-library.md)