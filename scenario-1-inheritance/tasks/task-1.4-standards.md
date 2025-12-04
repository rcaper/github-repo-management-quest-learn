# Task 1.4: Documentation Standards with GitHub Copilot

**Duration:** 15 minutes
**Difficulty:** Intermediate
**GitHub Copilot Features:** @workspace, Copilot Chat, template generation

## Objective

Create comprehensive documentation standards using GitHub Copilot to prevent future quality issues and ensure consistency across the Microsoft Learn training modules in the `learn-pr/wwl` repository.

## Context

You've identified numerous issues in the Fabric training modules, many of which could have been prevented with clear standards. GitHub Copilot can help you create professional standards documents by analyzing your audit findings and generating guidelines based on Learn authoring best practices.

This document will serve as:
- A guide for Learn content authors
- A checklist for module reviewers
- The basis for automated YAML and content validation
- The foundation for your Learn content quality culture

## Setup

Have your `quality-audit.md` and `audit-report.md` open for reference.
Open Copilot Chat: `Ctrl+Shift+I` (Cmd+Shift+I on Mac)

## Tasks

### 1. Generate Markdown Formatting Standards

**GitHub Copilot Chat Prompt:**
```
@workspace Based on the formatting issues found in my audit of the learn-pr/wwl modules:

[Paste formatting issues from your audit]

Create a "Learn Module Formatting Standards" section for our documentation that includes:
1. YAML metadata requirements (ms.date, author, ms.service fields)
2. Module structure rules (proper index.yml to unit .yml to includes/*.md flow)
3. Code block formatting (always use ``` with language specifiers like python, yaml, sql)
4. Cross-reference link formatting (proper [!include[]] syntax)
5. Image and media conventions (media/ folder structure, alt text requirements)

For each rule provide:
- The standard (what to do)
- Why it matters (rationale for Learn platform)
- ✅ Good example
- ❌ Bad example

Format as markdown suitable for LEARN_MODULE_STANDARDS.md file.
```

**What Copilot Does:**
- Analyzes issues found in your audit
- Generates specific standards to prevent those issues
- Provides rationale for each standard
- Creates clear examples (good vs bad)

**Follow-up to Refine:**
```
@workspace Add standards for heading capitalization (title case vs sentence case)
```

**Deliverable:** Create `DOCUMENTATION_STANDARDS.md` with formatting section

---

### 2. Create Content Structure Templates

**GitHub Copilot Chat Prompt:**
```
@workspace Create templates for different Microsoft Learn module content types:

1. Module index.yml template (module metadata and unit listing)
2. Learning unit .yml template (unit with knowledge check)
3. Exercise unit .yml template (hands-on activity)
4. Conceptual content template (includes/*.md understanding)
5. Tutorial content template (includes/*.md step-by-step)

For each template, define:
- Required YAML fields with descriptions
- Required content sections
- Example structure showing includes/ references
- When to use this template

Format as copy-paste ready templates following Learn authoring guidelines.
```

**What Copilot Does:**
- Generates professional documentation templates
- Based on documentation best practices (Diátaxis framework)
- Creates ready-to-use markdown structures
- Provides guidance on template selection

**Refine Templates:**
```
@workspace Add a frontmatter section to each template with metadata fields
```

**Deliverable:** Add "Document Templates" section with 4+ templates

---

### 3. Define Quality Requirements

**GitHub Copilot Chat Prompt:**
```
@workspace Based on quality issues from my Learn modules audit, create enforceable quality requirements:

[Reference your audit findings]

Include standards for:
1. ms.date freshness (maximum age, update triggers, automation)
2. Code example validation (PySpark/SQL examples must run in Fabric)
3. Include file references (all [!include[]] paths must resolve)
4. Images and media (alt text required, media/ folder organization, screenshot currency)
5. Prerequisites accuracy (Fabric capacity requirements, access needs)

Make each requirement:
- Specific and measurable for Learn publishing
- Enforceable through build validation or review
- Practical for content authors to follow

Provide implementation guidance for each.
```

**What Copilot Does:**
- Converts audit findings into preventive standards
- Creates measurable, testable requirements
- Suggests automation approaches
- Provides implementation steps

**Add Automation:**
```
@workspace For each quality requirement, suggest a tool or script that could automate the check
```

**Deliverable:** Add "Quality Requirements" section

---

### 4. Create Review Process Documentation

**GitHub Copilot Chat Prompt:**
```
@workspace Create a documentation review process that would catch the issues we found:

Define:
1. Who reviews documentation (peer, SME, tech writer roles)
2. Review workflow (branch → PR → review → merge)
3. Reviewer checklist (specific items to verify)
4. Merge criteria (what must pass before merging)
5. How to use GitHub Copilot during reviews

Make this practical - not overly bureaucratic but thorough enough to catch quality issues.

Include a copy-paste checklist reviewers can use.
```

**What Copilot Does:**
- Designs pragmatic review workflow
- Creates actionable checklist
- Balances thoroughness with efficiency
- Includes Copilot-assisted review steps

**Example Copilot-Enhanced Review Step:**
```markdown
### Using GitHub Copilot in Reviews

Before approving, reviewers should:
1. Use @workspace to check cross-references:
   ```
   @workspace Does this PR break any links in other files?
   ```

2. Verify technical accuracy:
   ```
   @workspace Are the code examples in this PR correct and up-to-date?
   ```

3. Check consistency:
   ```
   @workspace Compare the style in this PR to existing documentation
   ```
```

**Deliverable:** Add "Review and Approval Process" section

---

### 5. Define Style and Voice Guidelines

**GitHub Copilot Chat Prompt:**
```
@workspace Create style and voice guidelines for technical documentation:

1. Tone (professional but approachable, active voice)
2. Perspective (second person "you" for user docs)
3. Terminology standards (preferred vs deprecated terms)
4. Writing style (sentence structure, paragraph length)
5. Common pitfalls to avoid

Include:
- Before/after examples showing improvements
- Specific terms to use/avoid for our product
- How to explain technical concepts clearly

Make this practical with lots of examples.
```

**What Copilot Does:**
- Generates professional style guide
- Provides clear examples
- Creates terminology glossary
- Shows common improvements

**Refine for Your Product:**
```
@workspace Our content covers Microsoft Fabric. Add terminology standards specific to:
- Fabric workspaces, capacities, and lakehouses
- Copilot for Fabric features
- Medallion architecture (bronze, silver, gold)
- Real-time analytics and KQL
```

**Deliverable:** Add "Style and Voice Guidelines" section

---

### 6. Specify Tools and Automation

**GitHub Copilot Chat Prompt:**
```
@workspace Recommend specific tools and automation to enforce these standards:

1. Markdown linting (which tool, configuration)
2. Link checking (automated in CI/CD)
3. Spell checking (with custom dictionary)
4. Style enforcement (vale or similar)

For each tool provide:
- Tool name and purpose
- Installation command
- Basic configuration
- How to integrate with VS Code
- How to run in CI/CD

Include example configuration files.
```

**What Copilot Does:**
- Recommends specific, proven tools
- Generates configuration files
- Provides installation instructions
- Shows CI/CD integration

**Generate Configurations:**
```
@workspace Create a .markdownlint.json configuration file that enforces our formatting standards
```

```
@workspace Create a GitHub Actions workflow that runs these checks on every PR
```

**Deliverable:** Add "Tools and Automation" section with configs

---

### 7. Create Quick Reference Checklist

**GitHub Copilot Chat Prompt:**
```
@workspace From all the standards we've created, generate a one-page quick reference checklist that contributors can print or bookmark.

Include only the most important items:
- Top 10 formatting rules
- Must-have quality checks
- Review checklist
- Common mistakes to avoid

Format as a simple, scannable checklist.
```

**What Copilot Does:**
- Distills comprehensive standards into essentials
- Creates printer-friendly format
- Prioritizes most important items
- Makes standards accessible

**Deliverable:** Add "Quick Reference" section at top of document

---

## Generate Complete Standards Document

**Final Assembly Prompt:**
```
@workspace Review this complete DOCUMENTATION_STANDARDS.md file:

[Share your assembled document]

Check for:
1. Missing sections or incomplete areas
2. Inconsistent formatting
3. Unclear language
4. Missing examples
5. Sections that could be more practical

Suggest improvements to make this a professional, usable standards document.
```

**Polish with Inline Copilot:**
1. Select any unclear section
2. Press `Ctrl+I` (Cmd+I)
3. Ask: "Make this clearer and more concise"
4. Review and accept changes

---

## Output Format

Your `LEARN_MODULE_STANDARDS.md` should follow this structure (Copilot-generated):

```markdown
# Microsoft Learn Module Standards

**Created with:** GitHub Copilot @workspace
**Version:** 1.0
**Last Updated:** [Date]
**Owner:** Learn Content Team

## Quick Reference

[One-page checklist for content authors - print this!]

**Before submitting Learn module changes:**
- [ ] index.yml has current ms.date and complete metadata
- [ ] All unit .yml files reference valid includes/*.md files
- [ ] All code blocks have language specifiers (python, yaml, sql, kusto)
- [ ] All [!include[]] references resolve correctly
- [ ] Images have descriptive alt text and are in media/ folder
- [ ] ms.date updated to reflect actual content changes
- [ ] Reviewed by peer content author
- [ ] Passes Learn build validation

**Most Important Rules:**
1. Use relative paths for internal links
2. Always specify code block language
3. Start files with H1 heading
4. Use second person ("you") in user docs
5. Test all code examples

---

## 1. Markdown Formatting Standards

[Copilot-generated comprehensive formatting rules]

### 1.1 Headings

**Standard:** Use proper heading hierarchy without skipping levels.

**Why:** Screen readers and navigation depend on proper structure.

✅ **Good Example:**
```markdown
# Main Title (H1)

## Section (H2)

### Subsection (H3)

#### Detail (H4)
```

❌ **Bad Example:**
```markdown
# Main Title (H1)

### Subsection (H3)  ❌ Skipped H2
```

**Rule:** Each markdown file should have exactly one H1.

[Continue with 1.2, 1.3, etc.]

---

## 2. Document Templates

[Copilot-generated templates]

### 2.1 Tutorial Template

**When to use:** Step-by-step learning experiences for beginners.

**Copy this template:**

```markdown
# Tutorial: [Title]

## What You'll Learn
- Learning objective 1
- Learning objective 2

## Prerequisites
- Required knowledge
- Required tools/setup

## Time Required
[Estimate]

## Step 1: [Action]
[Instructions]

### What You Should See
[Expected result]

### If Something Went Wrong
[Troubleshooting]

## Step 2: [Action]
[Continue...]

## What's Next
- Next tutorial in series
- Related topics
```

[Continue with 2.2, 2.3, 2.4...]

---

## 3. Quality Requirements

[Copilot-generated enforceable standards]

### 3.1 Link Checking

**Requirement:** All links must be validated before merging.

**Standard:**
- Internal links use relative paths
- External links checked monthly
- Broken links fixed within 24 hours
- Link checking automated in CI/CD

**Tool:** `markdown-link-check`

**Implementation:**
```bash
# Install
npm install -g markdown-link-check

# Run
markdown-link-check docs/**/*.md

# Automate in GitHub Actions
# (see Tools section for workflow)
```

**Using Copilot to Check:**
```
@workspace Find all links in this file and verify they work
```

[Continue with 3.2, 3.3, etc.]

---

## 4. Review and Approval Process

[Copilot-generated workflow]

### 4.1 Workflow

1. **Create Branch**
   ```bash
   git checkout -b docs/your-feature
   ```

2. **Write Documentation**
   - Use appropriate template
   - Follow formatting standards
   - Test all code examples

3. **Self-Review Checklist**
   - [ ] Used @workspace to check impacts:
     ```
     @workspace Will these changes break anything?
     ```
   - [ ] Spell checked
   - [ ] Links verified
   - [ ] Examples tested
   - [ ] Follows style guide

4. **Submit Pull Request**
   - Use PR template
   - Request review from docs team
   - Link to related issues

5. **Address Feedback**
   - Respond to all comments
   - Update based on suggestions
   - Re-request review

6. **Merge**
   - Requires: 1 approval
   - Passes: All automated checks
   - No: Unresolved comments

### 4.2 Reviewer Checklist

[Copy-paste checklist for reviewers]

**Technical Accuracy:**
- [ ] Code examples are correct
- [ ] Version numbers are current
- [ ] Commands work as written
- [ ] API information is accurate

**Style & Formatting:**
- [ ] Follows markdown standards
- [ ] Consistent terminology
- [ ] Proper grammar/spelling
- [ ] Clear and concise

**Quality:**
- [ ] All links work
- [ ] Images have alt text
- [ ] Prerequisites stated
- [ ] Examples included

**Using Copilot to Review:**
- [ ] Asked @workspace about cross-file impacts
- [ ] Verified technical accuracy with Copilot
- [ ] Checked style consistency

---

## 5. Style and Voice Guidelines

[Copilot-generated style guide]

### 5.1 Tone and Voice

**Standard:** Professional but approachable, using active voice.

✅ **Good Examples:**
- "Click the Save button" (active, direct)
- "You can configure..." (second person)
- "This feature helps you..." (user-focused)

❌ **Bad Examples:**
- "The Save button should be clicked" (passive)
- "Users can configure..." (third person)
- "This feature has the ability to..." (wordy)

[Continue...]

---

## 6. Tools and Automation

[Copilot-generated tool recommendations and configs]

### 6.1 Required Tools

**markdownlint** - Enforces formatting standards

**Installation:**
```bash
npm install -g markdownlint-cli
```

**Configuration (.markdownlint.json):**
```json
{
  "default": true,
  "MD013": false,
  "MD033": {
    "allowed_elements": ["img", "br"]
  }
}
```

**VS Code Extension:**
- Install: "markdownlint" by David Anson
- Auto-fix on save

**Run Manually:**
```bash
markdownlint docs/**/*.md --fix
```

**CI/CD Integration:**
```yaml
# .github/workflows/docs-quality.yml
name: Documentation Quality

on: [pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Markdown Lint
        run: |
          npm install -g markdownlint-cli
          markdownlint docs/**/*.md
```

[Continue with other tools...]

---

## 7. Using GitHub Copilot for Documentation

### 7.1 Writing with Copilot

**Generating Content:**
```
@workspace Create a getting started guide for [feature]
```

**Improving Clarity:**
- Select text → Ctrl+I → "Make this clearer"

**Creating Examples:**
```
@workspace Generate a code example showing how to [task]
```

### 7.2 Reviewing with Copilot

**Check Cross-References:**
```
@workspace Does this change break any links in other files?
```

**Verify Consistency:**
```
@workspace Compare the terminology in this file to our other docs
```

**Find Issues:**
```
@workspace Review this documentation for technical accuracy and clarity
```

---

## Appendix A: Configuration Files

[Copilot-generated configs, ready to use]

### .markdownlint.json
[Full config]

### .github/workflows/docs-quality.yml
[Full GitHub Actions workflow]

### .cspell.json
[Spell checker config with custom dictionary]

---

## Appendix B: Example PR Description

[Template for documentation PRs]

---

## Proposing Changes to These Standards

These standards are living documents. To suggest improvements:

1. Open an issue describing the proposed change
2. Explain the rationale (why it's better)
3. Provide examples
4. Tag @docs-team for review

---

## Version History

- **v1.0** ([Date]) - Initial standards created with GitHub Copilot
- Document review process: Quarterly

---

*This document was created with GitHub Copilot @workspace to establish comprehensive documentation standards based on audit findings and industry best practices.*
```

---

## GitHub Copilot Tips for This Task

### Start with Audit Findings

Your audit reveals what standards are needed:
```
@workspace Based on the issues in my quality audit, what standards should I create?
```

### Generate, Then Refine

Don't expect perfection first try:
1. Get Copilot to generate initial version
2. Review and identify gaps
3. Ask Copilot to fill gaps or improve sections
4. Iterate until complete

### Use Examples Liberally

Examples make standards clear:
```
@workspace Add more before/after examples to this section
```

### Keep It Practical

Standards that are too complex won't be followed:
```
@workspace Simplify this section - make it more practical for busy contributors
```

---

## Success Criteria

You've completed this task when your standards document:

- ✅ Covers all major aspects of documentation quality
- ✅ Provides specific, actionable guidelines (not vague advice)
- ✅ Includes both good and bad examples
- ✅ Can be enforced through automation where possible
- ✅ Has copy-paste templates contributors can use
- ✅ Includes quick reference checklist
- ✅ Reflects issues found in your audit
- ✅ Was significantly accelerated by GitHub Copilot

---

## Time Management

- **Minutes 0-3:** Generate formatting standards and templates
- **Minutes 4-7:** Create quality requirements and review process
- **Minutes 8-11:** Generate style guide and tool recommendations
- **Minutes 12-14:** Create quick reference and polish with inline Copilot
- **Minutes 14-15:** Final review and save

---

## Scenario 1 Complete!

Congratulations! By completing all four tasks in Scenario 1, you have:

- ✅ Explored an unfamiliar repository with @workspace
- ✅ Conducted comprehensive quality audit with Copilot
- ✅ Created executive report with Copilot's synthesis
- ✅ Established standards using Copilot's generation capabilities

**You've learned to use GitHub Copilot for:**
- Repository-wide analysis (@workspace)
- Pattern recognition and issue finding
- Content generation and synthesis
- Professional document creation

---

## What's Next?

Ready for more? Move to **[Scenario 2: The Backlog Battle](../../scenario-2-backlog-battle/README.md)**

You'll learn to use GitHub Copilot to efficiently triage and manage documentation issues at scale.
