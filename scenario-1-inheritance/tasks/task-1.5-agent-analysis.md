# Task 1.5: Advanced Content Analysis with Agents

## Objective

Use your preconfigured agents and templates from Module 0 for comprehensive content analysis and reporting.

## Prerequisites

- Completed Module 0: Workspace Preparation
- Working `.agents` and `.prompts` configuration
- Basic familiarity with GitHub Copilot Chat

## Your Challenge

Apply your custom agents and prompt templates to conduct a thorough analysis of the inherited repository using advanced AI workflows.

## Step 1: Strategic Content Analysis

Use your **content-strategist** agent to evaluate the overall content strategy:

```
@content-strategist Please analyze the content strategy for the learn-pr/wwl directory containing Microsoft Learn Fabric training modules. Focus on:
- Information architecture across the ~55 Fabric learning modules
- Learning path flow and content gaps in the Fabric training curriculum
- Strategic priorities for improvement based on Fabric service evolution
- Content governance recommendations for consistent module quality
```

### Expected Output Analysis

Review the content-strategist response for:
- **Strategic insights** about module organization across Fabric workloads
- **Learning path assessment** and gaps in the Fabric training journey
- **Content gap identification** for new Fabric features like Copilot and data agents
- **Governance recommendations** for consistent YAML metadata and includes structure

## Step 2: Technical Content Validation

Apply your **technical-validator** agent to check content accuracy:

```
@technical-validator Validate the technical accuracy of all Learn modules in learn-pr/wwl, especially:
- PySpark and SQL code examples for Fabric notebooks
- Lakehouse and medallion architecture implementation steps
- Copilot for Fabric feature instructions and screenshots
- Cross-reference links between modules and external docs
- ms.date accuracy relative to actual content currency
```

### Validation Focus Areas

Pay attention to:
- **Code example quality** and executability in Fabric notebooks
- **Step-by-step instruction completeness** for Fabric workloads
- **Version compatibility** with current Fabric service features
- **Cross-reference integrity** for [!include[]] and external links

## Step 3: Accessibility Assessment

Use your **accessibility-auditor** agent to evaluate inclusive design:

```
@accessibility-auditor Assess the accessibility compliance of the learn-pr/wwl Microsoft Learn modules for:
- WCAG 2.1 AA compliance status across all module content
- Inclusive design principles in hands-on exercises
- Navigation and screen reader compatibility in module structure
- Multi-modal content accessibility (images, code blocks, tables)
- Alt text quality for Fabric portal screenshots and diagrams
```

### Accessibility Review Checklist

Verify the agent identifies:
- **Heading structure** and navigation hierarchy
- **Alt text** for images and media
- **Color contrast** and visual accessibility
- **Language clarity** and readability

## Step 4: Comprehensive Content Audit

Apply your **content-audit** prompt for systematic analysis:

```
#content-audit @workspace Conduct a comprehensive audit of the learn-pr/wwl Microsoft Learn modules focusing on:
- Overall module structure and YAML metadata consistency
- Content quality and completeness across Fabric workloads (lakehouses, medallion, Copilot)
- Learning experience and navigation effectiveness within learning paths
- Maintenance requirements (ms.date freshness, screenshot currency)
```

### Audit Report Analysis

Look for:
- **Executive summary** with key findings
- **Prioritized issue list** with impact assessment
- **Quick wins** for immediate improvement
- **Strategic recommendations** for long-term success

## Step 5: Agent Coordination Workflow

Coordinate multiple agents for comprehensive analysis:

```
@qa-coordinator Please orchestrate a complete content review using our specialist agents:

Phase 1: @content-strategist - Strategic assessment
Phase 2: @technical-validator - Technical accuracy review  
Phase 3: @accessibility-auditor - Compliance evaluation
Phase 4: Synthesize findings into unified improvement plan
```

### Coordination Benefits

Observe how the QA coordinator:
- **Integrates insights** from multiple specialists
- **Prioritizes issues** by impact and effort
- **Creates unified action plans**
- **Reduces redundancy** between agent outputs

## Step 6: Generate Executive Report

Use your **generate-summary** prompt to create stakeholder communication:

```
#generate-summary Create an executive summary of our repository analysis including:
- Current state assessment
- Key strategic findings
- Priority improvement recommendations
- Resource requirements and timeline
- Success metrics for tracking progress
```

### Executive Report Components

Ensure the summary includes:
- **Strategic overview** suitable for leadership
- **Business impact** of identified issues
- **Resource requirements** for improvements
- **Timeline and milestones** for implementation

## Step 7: Quick Wins Implementation Plan

Apply your **quick-fixes** prompt to identify immediate improvements:

```
#quick-fixes Analyze the learn-pr/wwl modules and identify quick wins that can be implemented immediately:
- Update stale ms.date values in index.yml files
- Fix broken [!include[]] references
- Add missing alt text to media/ images
- Correct YAML formatting issues in unit files
- Update outdated Fabric terminology
```

### Quick Wins Prioritization

Focus on fixes that:
- **Require minimal effort** (<2 hours each)
- **Provide maximum user impact**
- **Build momentum** for larger improvements
- **Demonstrate immediate value**

## Step 8: Agent Performance Evaluation

Use your **output-validator** agent to assess the quality of other agents' work:

```
@output-validator Please evaluate the quality of the content analysis provided by our specialist agents:
- Completeness and accuracy of assessments
- Actionability of recommendations
- Consistency of output formats
- Overall usefulness for decision-making
```

### Quality Validation Benefits

This meta-analysis helps you:
- **Validate agent effectiveness** for your use case
- **Identify improvement opportunities** for agent configuration
- **Build confidence** in automated analysis results
- **Refine prompts** for better performance

## Reflection Questions

1. **Agent Specialization**: How did different agents provide unique perspectives on the same content?

2. **Workflow Efficiency**: How much faster was the analysis using agents vs. manual review?

3. **Quality Assessment**: Were the agent recommendations actionable and valuable?

4. **Coordination Benefits**: How did multi-agent workflows improve analysis depth?

5. **Customization Needs**: What agent modifications would improve results for your specific context?

## Success Criteria

- [ ] All agents tested with repository content
- [ ] Comprehensive analysis completed using multiple perspectives
- [ ] Executive summary generated for stakeholder communication
- [ ] Quick wins identified and prioritized
- [ ] Agent performance evaluated and optimized
- [ ] Workflow efficiency improvements documented

## Deliverables

Create these documents based on your agent analysis:

1. **Strategic Assessment Report** (content-strategist output)
2. **Technical Validation Summary** (technical-validator findings)
3. **Accessibility Compliance Report** (accessibility-auditor assessment)
4. **Executive Summary** (stakeholder communication)
5. **Quick Wins Action Plan** (immediate improvements)
6. **Agent Performance Review** (meta-analysis of AI outputs)

## Next Steps

### LLA Live Session

- [Scenario 2: Categorize](/scenario-2-backlog-battle/tasks/task-2.1-categorize.md)
- [Scenario 2: Automated Fixes](/scenario-2-backlog-battle/tasks/task-2.4-automated-fixes.md)


### Self-paced and want to explore

[Scenario 2: Categorize](/scenario-2-backlog-battle/tasks/task-2.1-categorize.md)

---

**Key Takeaway**: Advanced agent workflows transform repository analysis from a time-intensive manual process into a comprehensive, consistent, and scalable automated assessment that provides deeper insights and more actionable recommendations.