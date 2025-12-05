# Part 1: GitHub Copilot Fundamentals for Repository Management

## Overview

Welcome to **Part 1** of the GitHub Copilot Repository Management Quest! This 60-minute lab introduces you to the core GitHub Copilot features for managing documentation repositories efficiently.

**Duration:** ~60 minutes  
**Difficulty:** Beginner to Intermediate  
**Prerequisites:** VS Code with GitHub Copilot extension, GitHub account

## What You'll Learn

By completing Part 1, you will:

1. **Configure your workspace** with custom agents and prompts for documentation tasks
2. **Explore unfamiliar repositories** using GitHub Copilot's @workspace agent
3. **Audit content quality** with AI-assisted analysis and reporting
4. **Triage issues efficiently** using AI-powered categorization and prioritization

## Lab Structure

| Module | Duration | Focus |
|--------|----------|-------|
| **Quick Setup** | 5 min | Fork repo, run setup workflows |
| **Module 0.1: Workspace Basics** | 10 min | Introduction to agents and prompts |
| **Scenario 1: Repository Exploration** | 25 min | Understand and audit a repository |
| **Scenario 2: Issue Triage Basics** | 15 min | AI-assisted issue categorization |
| **Wrap-up** | 5 min | Reflection and next steps |

---

## Quick Setup (5 minutes)

### 1. Fork and Clone the Repository

```bash
# Fork via GitHub UI first, then:
git clone https://github.com/[your-username]/github-repo-management-quest.git
cd github-repo-management-quest
code .
```

### 2. Run Setup Workflows

In your forked repository on GitHub:

1. Go to **Actions** tab
2. Run **"Setup Quest Issues"** workflow (creates sample issues for Scenario 2)
3. Run **"Setup Quest PR"** workflow (creates sample PR for Part 2)

### 3. Verify Setup

- ✅ Repository open in VS Code
- ✅ GitHub Copilot icon visible in status bar
- ✅ Sample issues visible in Issues tab (labeled `quest-sample`)

---

## Module 0.1: Workspace Basics (10 minutes)

Learn the fundamentals of GitHub Copilot workspace customization.

### What Are Agents and Prompts?

- **Agents** (`.agents` file): Specialized AI assistants with specific roles
- **Prompts** (`.prompts` file): Reusable templates for common tasks

### Quick Start Configuration

Create a `.agents` file in your repository root:

```yaml
documentation-auditor:
  description: Analyzes documentation for gaps and improvements
  instructions: |
    You are a documentation auditor. Focus on:
    - Content completeness and structure
    - Broken links and outdated information
    - Clarity and user experience
    
    Provide actionable recommendations with specific examples.

style-enforcer:
  description: Reviews content for style consistency
  instructions: |
    You are a style guide enforcer. Check for:
    - Grammar and spelling consistency
    - Formatting standards (headings, lists, code blocks)
    - Terminology standardization
    
    Suggest specific corrections with explanations.
```

Create a `.prompts` file:

```yaml
content-audit:
  description: Comprehensive analysis of repository content
  prompt: |
    Analyze this repository's documentation for:
    1. Structure and organization
    2. Content gaps or missing sections
    3. Outdated information
    4. Link validity
    
    Provide: Executive summary, Key findings, Quick wins

quick-fixes:
  description: Identify immediate improvement opportunities
  prompt: |
    Find quick fixes that can be implemented immediately:
    - Broken links
    - Typos or grammar issues
    - Formatting inconsistencies
    - Missing headings
    
    List by priority with estimated effort.
```

### Test Your Configuration

Open Copilot Chat (`Ctrl+Shift+I` / `Cmd+Shift+I`) and try:

```
@documentation-auditor Analyze the structure of the learn-pr/wwl folder
```

```
#content-audit @workspace Perform a content audit learn-pr/wwl folder
```

**Full Task Details:** [module-0-workspace-prep/tasks/task-0.1-intro.md](../module-0-workspace-prep/tasks/task-0.1-intro.md)

---

## Scenario 1: Repository Exploration (25 minutes)

### The Story

You've just been assigned to take over a documentation repository containing Microsoft Learn training modules. Your mission: understand what you've inherited and create an improvement plan.

### Task 1.1: Explore the Repository (10 min)

Use @workspace to map the repository structure:

```
@workspace Give me an overview of this repository. What types of content does it contain? How is it organized?
```

```
@workspace What Microsoft Learn modules are in the learn-pr/wwl folder? List them with their topics.
```

**Key Skills:**
- Using @workspace for repository-wide context
- Understanding folder structures and content types
- Mapping relationships between files

**Full Task Details:** [scenario-1-inheritance/tasks/task-1.1-explore.md](../scenario-1-inheritance/tasks/task-1.1-explore.md)

### Task 1.2: Identify Issues (10 min)

Use Copilot to find problems:

```
@workspace Analyze the learn-pr/wwl modules for potential issues like outdated ms.date values, broken includes, or inconsistent metadata.
```

```
@documentation-auditor Review the get-started-lakehouses module for content quality issues.
```

**Key Skills:**
- Targeted issue detection
- Pattern recognition across files
- Using custom agents for specialized analysis

**Full Task Details:** [scenario-1-inheritance/tasks/task-1.2-identify.md](../scenario-1-inheritance/tasks/task-1.2-identify.md)

### Task 1.3: Generate Audit Report (5 min)

Create a comprehensive report:

```
#content-audit @workspace Create an audit report for the learn-pr/wwl folder focusing on the Fabric-related modules.
```

**Key Skills:**
- Generating structured reports
- Prioritizing findings
- Creating actionable recommendations

**Full Task Details:** [scenario-1-inheritance/tasks/task-1.3-audit.md](../scenario-1-inheritance/tasks/task-1.3-audit.md)

---

## Scenario 2: Issue Triage Basics (15 minutes)

### The Story

Your Microsoft Learn documentation repository has accumulated open issues. They range from broken images to outdated content to accessibility concerns. Your challenge: efficiently categorize and prioritize these issues.

### Task 2.1: Issue Categorization (15 min)

Open the Issues tab in your forked repository. You should see 12 sample issues with the `quest-sample` label.

Use Copilot to analyze and categorize:

```
@workspace Analyze the GitHub issues in this repository with the quest-sample label. For each issue, identify:
1. Type (bug, content, accessibility, enhancement)
2. Priority (P0-Critical, P1-High, P2-Medium, P3-Low)
3. Effort estimate (XS, S, M, L)
4. Quick win? (Yes/No)
```

**Identify Quick Wins:**
```
@workspace From the quest-sample issues, which ones are quick wins that can be fixed in under 30 minutes? List them with the specific fix needed.
```

**Key Skills:**
- Bulk issue analysis with AI
- Consistent categorization frameworks
- Priority-based triage
- Identifying quick wins for immediate action

**Full Task Details:** [scenario-2-backlog-battle/tasks/task-2.1-categorize.md](../scenario-2-backlog-battle/tasks/task-2.1-categorize.md)

---

## Wrap-up (5 minutes)

### What You Accomplished

- ✅ Configured workspace with custom agents and prompts
- ✅ Explored and mapped a repository using @workspace
- ✅ Identified content issues with AI assistance
- ✅ Generated an audit report
- ✅ Triaged issues using AI-powered categorization

### Key Takeaways

1. **@workspace provides repository-wide context** - essential for understanding unfamiliar repos
2. **Custom agents specialize Copilot's expertise** - focus on specific tasks
3. **Prompts ensure consistent output** - reusable templates for common workflows
4. **AI accelerates triage but doesn't replace judgment** - validate findings

### Reflection Questions

1. How would you customize the agents for your team's specific needs?
2. What patterns did Copilot help you identify faster than manual review?
3. How will you apply these skills to your actual documentation work?

---

## Continue to Part 2

Ready to tackle advanced workflows? **Part 2: Advanced Copilot Workflows** covers:

- Advanced agent creation and customization
- Pull request review with multiple agents
- Agent orchestration for complex workflows
- Enterprise-scale automation

**Next:** [Part 2: Advanced Copilot Workflows](../part-2-advanced/README.md)

---

## Quick Reference

### Essential Commands

| Command | Purpose |
|---------|---------|
| `@workspace [query]` | Query with full repository context |
| `@documentation-auditor [query]` | Use your custom audit agent |
| `#content-audit @workspace` | Run your audit prompt |
| `Ctrl+Shift+I` / `Cmd+Shift+I` | Open Copilot Chat |

### Files to Reference

- **Module 0 Tasks:** `module-0-workspace-prep/tasks/`
- **Scenario 1 Tasks:** `scenario-1-inheritance/tasks/`
- **Scenario 2 Tasks:** `scenario-2-backlog-battle/tasks/`
- **Learn Content:** `learn-pr/wwl/` (Microsoft Fabric modules)

### Need Help?

- Check solution guides in each scenario's `solutions/` folder
- Review `resources/copilot-prompts.md` for more examples
- See `resources/best-practices.md` for tips
