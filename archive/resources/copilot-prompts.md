# GitHub Copilot Prompts for Repository Management

This guide contains effective GitHub Copilot prompts specifically designed for repository management tasks. All prompts use Copilot's features like @workspace, inline suggestions, and GitHub.com integration.

**Key Copilot Features Used:**
- `@workspace` - Repository-wide context awareness
- Inline Copilot (`Ctrl+I` / `Cmd+I`) - Quick edits and suggestions
- Copilot Chat (`Ctrl+Shift+I` / `Cmd+Shift+I`) - Conversational assistance
- GitHub.com PR summaries - Native PR analysis
- Issue-to-PR workflow - Automated fix generation

## Table of Contents

1. [Repository Exploration](#repository-exploration)
2. [Content Auditing](#content-auditing)
3. [PR Review](#pr-review)
4. [Issue Management](#issue-management)
5. [Documentation Writing](#documentation-writing)
6. [Automated Fixes](#automated-fixes)
7. [Quick Reference](#quick-reference)

---

## Repository Exploration

### 1. Understanding Repository Structure

**Use @workspace for complete analysis:**

```
@workspace Analyze this repository structure and provide:
1. A tree diagram showing main directories and key files
2. The purpose of each directory
3. The types of content in each section
4. Overall organization pattern
5. What type of project this appears to be

Format as markdown for easy copying.
```

**Why it works:** @workspace sees the entire repository, not just open files.

---

### 2. Mapping Content by Topic

```
@workspace Categorize all markdown files in this repository by:
- Content type (tutorial, guide, reference, API docs, etc.)
- Topic area (getting started, advanced features, API, troubleshooting)
- Intended audience (beginners, developers, administrators)
- Completeness (complete, in-progress, has TODOs)

Present as a table with columns: File, Type, Topic, Audience, Status
```

**Follow-up for summaries:**
```
@workspace Summarize the categorization - how many of each type?
```

---

### 3. Identifying Documentation Gaps

```
@workspace Based on the documentation files present, what essential documentation is missing for a complete documentation set?

Consider:
- Getting started guides
- Contributing guidelines
- Architecture documentation
- Troubleshooting guides
- FAQ
- Code of conduct
- License
- Changelog

What's here and what's missing?
```

---

### 4. Finding Utility Scripts

```
@workspace I see Python files in the utils/ directory. For each script:
1. What does it do?
2. When would you use it?
3. What are its dependencies?
4. Is it well-documented?
5. Could it help with documentation quality checks?
```

---

### 5. Creating Visual Repository Map

```
@workspace Create a visual map of this documentation repository using Mermaid diagram syntax showing:
1. The main documentation sections as nodes
2. How they relate to each other (arrows)
3. The typical user journey through the docs
4. Entry points for different user types (beginner, advanced, API user)
```

---

## Content Auditing

### 1. Finding Broken Links

**Repository-wide link analysis:**

```
@workspace Analyze all markdown files and find broken links. Check for:
1. Internal links to files that don't exist
2. Internal links with incorrect paths
3. Anchor links (#section) that don't match headings
4. Suspicious external URLs (old domains, deprecated endpoints)

List each broken link with:
- File name and line number
- The link text and URL
- Why it's broken
- Suggested fix
```

**For specific file:**
```
@workspace In docs/getting-started.md, there's a link to "../guides/setup". Verify this path is correct and the file exists.
```

---

### 2. Checking for Outdated Content

```
@workspace Review all documentation files for outdated content.

Look for:
- Old version numbers (e.g., "Python 2.7", "Node 10")
- Deprecated features or APIs
- References to old tools or services
- Dates more than 6 months old
- Code examples using outdated syntax

For each issue found, specify:
- File and location
- What's outdated
- Recommended update
- Priority (critical/normal/low)
```

---

### 3. Verifying Code Examples

```
@workspace Extract all code examples from these documentation files:

[List files]

For each code example:
1. Language (Python, JavaScript, etc.)
2. Is it syntactically correct?
3. Can it run as-is or needs context?
4. Does it follow best practices?
5. Are dependencies/imports included?
6. Error handling present?

Flag any problematic examples.
```

---

### 4. Checking Formatting Consistency

```
@workspace Review all markdown files for formatting consistency:

**Heading Issues:**
- Files should have exactly one H1
- No skipped heading levels (H1 → H3)
- Consistent heading capitalization

**Code Block Issues:**
- All code blocks use ``` fences
- All specify language
- Consistent indentation

**List Formatting:**
- Consistent bullet style
- Proper nesting

Report any inconsistencies found.
```

---

### 5. Finding TODO/FIXME Markers

```
@workspace Search all files for TODO, FIXME, or XXX markers.

For each:
- File and line number
- The TODO text
- Context (what section/function)
- Priority estimate
- Whether it's critical or can wait

Present as a prioritized list.
```

---

## PR Review

### 1. High-Level PR Analysis (Use @workspace)

```
@workspace I'm reviewing a pull request with these changes:

[Paste PR description and file list]

Provide:
1. A 2-3 sentence summary of what this PR accomplishes
2. The main categories of changes
3. Why this change is needed
4. Whether the scope seems appropriate
5. Overall complexity level (low/medium/high)

Format as a structured summary.
```

**For GitHub.com:**
- Use the native PR summary button in GitHub's PR interface
- Click "Copilot Summary" for automatic analysis

---

### 2. Assessing Change Scope

```
@workspace For this PR, analyze the file changes:

New Files:
[List]

Modified Files:
[List with line changes]

Deleted Files:
[List]

Categorize changes and identify:
1. What types of changes (new content, updates, refactoring, fixes)
2. Which changes are high-risk
3. Is this PR appropriately scoped?
4. What areas need the most careful review?
```

---

### 3. Quality Spot Check

```
@workspace Perform a quality spot check on these files from the PR:

[Share 2-3 files]

Check for:
1. Writing quality (clarity, grammar, style)
2. Formatting consistency
3. Obvious technical errors
4. Completeness
5. Code examples (correct and well-documented)

What's your overall quality assessment?
```

---

### 4. Validating Cross-References

```
@workspace This PR modifies several files and deletes [filename].

Check for cross-reference issues:
1. Find all internal links in the changed files
2. Verify each link points to an existing file
3. Check if any links point to deleted files
4. Verify anchor links match actual headings

List all broken or potentially broken references.
```

---

### 5. Style Consistency Check

```
@workspace Compare the style in these changed files to the existing documentation style. What's inconsistent?

Specifically check:
- Heading capitalization
- Code block formatting patterns
- Use of second person ("you") vs third person
- Terminology and technical terms
- Example structure
```

---

### 6. Checking for Cross-File Impacts

```
@workspace This PR changes these files: [list]

Find all files in the ENTIRE repository (not just those in the PR) that:
1. Link to any of these changed or deleted files
2. Reference content that might have changed
3. Include these files in navigation/menus
4. Depend on code/content in these files

List each dependency with file and line number.
```

---

## Issue Management

### 1. Bulk Issue Categorization

```
@workspace Analyze all issues in this file/repository and categorize each by:

1. Type (bug, feature, enhancement, docs, question, discussion)
2. Priority (P0-critical, P1-high, P2-normal, P3-low)
3. Effort (XS/<1hr, S/1-4hrs, M/1-2days, L/3-5days, XL/1+weeks)
4. Suggested labels

Present as a table: Issue #, Title, Type, Priority, Effort, Labels

Sort by priority then effort.
```

---

### 2. Finding Duplicate Issues

```
@workspace Find duplicate and closely related issues.

Look for:
1. Exact duplicates (same problem, different reporters)
2. Related issues (different aspects of same problem)
3. Conflicting requests (users want opposite things)

For each set:
- List issue numbers
- Relationship type
- Which issue should be primary
- Recommended action
```

---

### 3. Identifying Quick Wins

```
@workspace From these issues, identify "quick wins" - issues that:
- Are high value (user-facing or popular)
- Require low effort (XS or S)
- Have clear solutions
- Can be fixed quickly

For each:
1. Issue number and title
2. Why it's valuable
3. What needs to be done
4. Estimated time
5. Could it be automated or assigned to Copilot?

Rank by value/effort ratio.
```

---

### 4. Grouping Issues by Theme

```
@workspace Group all issues by common themes or topics.

Examples:
- Installation/setup problems
- API documentation issues
- Feature requests for specific functionality
- Error handling/messages
- Platform-specific (Windows, macOS, Linux)

For each theme:
1. Theme name
2. Issues in this theme (by number)
3. Summary of what users are asking for
4. Potential unified solution
5. Overall priority of this theme
```

---

### 5. Issues Needing More Information

```
@workspace Identify issues that are incomplete or vague.

Flag issues missing:
1. Clear problem description
2. Steps to reproduce
3. Expected vs actual behavior
4. Environment details
5. Error messages
6. Acceptance criteria

For each:
- Issue number
- What information is missing
- Template questions to ask the reporter
```

---

## Documentation Writing

### 1. Generating Content from Prompts

```
@workspace Create a getting started guide for [feature/tool] that includes:
1. Prerequisites
2. Installation steps
3. Basic usage example
4. Common tasks
5. Next steps

Target audience: [beginners/developers/admins]
Tone: [professional but approachable]
```

---

### 2. Improving Clarity (Inline Copilot)

**Use Ctrl+I / Cmd+I:**
1. Select text that needs improvement
2. Press `Ctrl+I` (inline Copilot)
3. Prompt: "Make this clearer and more concise"
4. Review and accept changes

---

### 3. Creating Code Examples

```
@workspace Generate a code example showing how to [task].

Requirements:
- Language: [Python/JavaScript/etc.]
- Include all necessary imports
- Add error handling
- Include inline comments
- Show expected output
- Make it copy-paste ready
```

---

### 4. Expanding Sections

**Inline Copilot method:**
1. Place cursor where content should be added
2. Press `Ctrl+I`
3. Prompt: "Add a detailed explanation of [concept] with examples"

---

### 5. Creating Templates

```
@workspace Create a template for [type of doc: tutorial/API reference/troubleshooting guide] that includes:
- Required sections
- Optional sections
- Example structure
- When to use this template

Format as copy-paste ready markdown.
```

---

## Automated Fixes

### 1. Fixing Simple Issues (Issue-to-PR Workflow)

**For typos:**
```
@workspace Issue #23 reports a typo in docs/getting-started.md.

Issue description: "The word 'experiance' on line 12 should be 'experience'"

Please:
1. Find the file and typo
2. Show me the current line
3. Provide the corrected line
4. Generate a PR description for this fix
```

---

### 2. Fixing Broken Links

```
@workspace Issue #25 reports a broken link.

Issue: "Link on line 45 of README.md points to http://old-docs.example.com which no longer exists. Should link to https://docs.example.com"

Please:
1. Find the broken link
2. Show current vs corrected
3. Check for other references to old domain
4. Generate the fix
```

---

### 3. Adding Missing Imports

```
@workspace Issue #11: Code example missing import

Issue description: "The code example at line 45-52 in tutorials/api-guide.md uses `Client` but doesn't import it."

Please:
1. Find the code example
2. Identify what import is needed
3. Show current vs corrected code
4. Verify the import is correct for our project
```

---

### 4. Generating Missing Examples

```
@workspace Issue #14 reports missing code example.

Issue: "In docs/api-reference.md, the Authentication section mentions error handling but doesn't provide an example."

Generate a complete code example showing:
- Successful authentication
- Error handling for failed authentication
- Best practices
- Inline comments

Make it beginner-friendly and copy-paste ready.
```

---

### 5. Batch Processing Similar Issues

```
@workspace I want to fix multiple typos at once:

1. docs/quick-start.md line 23: "seperate" → "separate"
2. docs/api-reference.md line 105: "recieve" → "receive"
3. tutorials/advanced.md line 89: "occured" → "occurred"

For each:
1. Verify the typo exists
2. Provide corrected text
3. Generate a single PR description fixing all

Should these be one PR or separate?
```

---

## Quick Reference

### Most Useful Copilot Prompts

**Repository Exploration:**
```
@workspace Analyze this repository and explain its structure
```

**Find Issues:**
```
@workspace Find all [broken links/TODOs/outdated content] in the documentation
```

**PR Review:**
```
@workspace Summarize this PR and identify potential issues
```

**Issue Triage:**
```
@workspace Categorize all issues by type, priority, and effort
```

**Generate Fix:**
```
@workspace Issue #X: [paste issue description]. Generate a fix.
```

---

### Keyboard Shortcuts

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Open Copilot Chat | `Ctrl+Shift+I` | `Cmd+Shift+I` |
| Inline Copilot | `Ctrl+I` | `Cmd+I` |
| Trigger suggestion | `Alt+\` | `Alt+\` |
| Accept suggestion | `Tab` | `Tab` |
| Dismiss suggestion | `Esc` | `Esc` |

---

### Copilot Agents

| Agent | When to Use | Example |
|-------|-------------|---------|
| `@workspace` | Repository-wide analysis | `@workspace Find all broken links` |
| `@terminal` | Terminal command help | `@terminal How do I grep for...` |
| `@vscode` | VS Code help | `@vscode How to enable...` |

---

## Advanced Techniques

### 1. Iterative Refinement

Don't expect perfection on first try:

1. **Initial prompt:** `@workspace Analyze this repository`
2. **Refine:** "Tell me more about the Python utilities"
3. **Drill down:** "What's in the docs/ directory specifically?"
4. **Specific question:** "Are there any broken links?"

---

### 2. Using Context Effectively

**Good context:**
```
@workspace I'm reviewing PR #127 which changes 18 files. [Share PR description]
```

**Not enough context:**
```
Review this PR ❌
```

---

### 3. Asking for Specific Formats

```
@workspace [query] and present as:
- a markdown table
- a bullet list
- a Mermaid diagram
- a JSON structure
```

---

### 4. Validation Prompts

Always verify Copilot's findings:

```
@workspace Are you sure this link is broken? Check again.
```

```
@workspace Does this code example actually work? Test the syntax.
```

---

### 5. Combining Features

**Use inline + @workspace together:**

1. Use @workspace to understand the issue
2. Navigate to the file
3. Use inline Copilot (`Ctrl+I`) to fix
4. Use @workspace to verify no other impacts

---

## GitHub.com Native Features

### 1. PR Summary

**On GitHub.com PR page:**
- Look for "Copilot" or "Summary" button
- Click for AI-generated PR summary
- Use for quick understanding

**What it shows:**
- Main changes
- Files modified by category
- Potential issues
- Testing suggestions

---

### 2. Issue Assignment to Copilot

**With GitHub Copilot Business/Enterprise:**

```
Assign issue to @copilot
```

**Copilot will:**
- Analyze the issue
- Generate a fix
- Create a branch
- Open a PR

**Best for:**
- Typos
- Broken links
- Simple formatting
- Missing imports
- Version updates

---

### 3. Inline PR Review Suggestions

**On GitHub.com:**
- Add review comments
- Copilot suggests improvements
- Click to insert suggested code
- Author can accept with one click

---

## Tips for Better Results

### Do:
- ✅ Use `@workspace` for repository-wide queries
- ✅ Be specific (file names, line numbers)
- ✅ Ask for formats (tables, diagrams)
- ✅ Request examples
- ✅ Verify Copilot's findings
- ✅ Iterate and refine

### Don't:
- ❌ Forget `@workspace` (limits context)
- ❌ Be vague ("fix the docs")
- ❌ Accept first response without validation
- ❌ Skip spot-checking
- ❌ Use for complex judgment calls

---

## Common Patterns

### Pattern: Comprehensive Audit

```
@workspace Audit all documentation for:
1. [Check type 1]
2. [Check type 2]
3. [Check type 3]

For each issue found:
- File and line number
- What's wrong
- Suggested fix
- Priority

Present as a prioritized table.
```

---

### Pattern: Impact Analysis

```
@workspace If we [change/delete/add] [X], what will be affected?

Check:
- Files that link to/from X
- Files that depend on X
- Navigation that includes X
- Related features

List all impacts with file references.
```

---

### Pattern: Generation + Refinement

```
Step 1: @workspace Generate [content type]
Step 2: Make this [more concise/clearer/friendlier]
Step 3: Add [specific element]
Step 4: Review for [quality aspect]
```

---

## Troubleshooting Copilot

### Problem: @workspace not available

**Solution:**
- Ensure GitHub Copilot extension installed
- Open folder in VS Code (not just files)
- Update to latest VS Code version
- Check Copilot is activated

---

### Problem: Responses too generic

**Solution:** Be more specific:
- Reference specific files/directories
- Ask for file names and line numbers
- Request examples
- Provide more context

---

### Problem: Copilot missed something

**Solution:** Ask directly:
```
@workspace I see a utils/ directory. What's in there?
@workspace Are there any Python files you didn't mention?
```

---

### Problem: Wrong information

**Solution:** Verify and correct:
```
@workspace You said X, but I see Y. Can you check again?
```

---

## Best Practices

1. **Start broad, then narrow**
   - Overview → Theme → Specific issue

2. **Always use @workspace for repo tasks**
   - It sees the full context

3. **Verify critical findings**
   - Spot-check files
   - Test code examples
   - Confirm links

4. **Iterate conversationally**
   - Build on previous responses
   - Ask follow-ups
   - Refine understanding

5. **Document useful prompts**
   - Save what works
   - Create templates
   - Share with team

---

## Resources

**Official Documentation:**
- [GitHub Copilot Docs](https://docs.github.com/copilot)
- [Copilot Chat Features](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)
- [@workspace Agent](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide#using-agents)

**Quest Resources:**
- [Copilot Features Guide](copilot-features-guide.md)
- [Best Practices](best-practices.md)
- [Setup Guide](../COPILOT_SETUP_GUIDE.md)

---

*These prompts are specifically designed for GitHub Copilot's capabilities. Adjust based on your specific repository and needs!*
