# Quick Start Tutorial

Get up and running with TechFlow in under 10 minutes!

## What You'll Build

In this tutorial, you'll create a simple workflow that:
- Triggers when a file is uploaded
- Processes the file
- Sends a notification

Let's get started!

## Step One - Install TechFlow

If you haven't already, install TechFlow:

```bash
pip install techflow
```

Verify the installation:
```bash
techflow version
```

## Step Two - Create Your First Workflow

### 1. Initialize a new project

```bash
mkdir my-first-workflow
cd my-first-workflow
techflow init
```

### 2. Define your workflow

Create a file called workflow.yaml:

```yaml
name: File Processor
triggers:
  - type: file_upload
    path: /uploads

steps:
  - name: Process File
    action: transform
    parameters:
      format: json

  - name: Send Notification
    action: notify
    parameters:
      channel: email
      recipient: user@example.com
```

### 3. Deploy your workflow

```bash
techflow deploy workflow.yaml
```

### 4. Test it out

Upload a test file:

```bash
techflow upload test.txt
```

You should see output showing your workflow execution!

## Step Three - Monitor Your Workflow

View recent executions:

```bash
techflow executions list
```

Check execution details:

```
techflow executions get <execution_id>
```

## Step Four - Make Changes

Edit your `workflow.yaml` file to add more steps:

```yaml
steps:
  - name: Validate File
    action: validate

  - name: Process File
    action: transform

  - name: Store Result
    action: save
    path: /results

  - name: Send Notification
    action: notify
```

Redeploy:
```bash
techflow deploy workflow.yaml
```

## What's Next?

Now that you've created your first workflow, explore more advanced features:

- **Conditional Logic** - Add if/else conditions to your workflows
- **Error Handling** - Handle failures gracefully
- **Scheduling** - Run workflows on a schedule
- Integrations - Connect to external services

Check out our [advanced tutorials](../guides/advanced-workflows.md) to learn more!

## Troubleshooting

**Issue: `techflow: command not found`**

Make sure you've installed TechFlow and it's in your PATH.

**Issue: Authentication failed**

Verify your API key in `~/.techflow/config.yaml`

**Issue: Deployment fails**

Check that your YAML syntax is correct using:
```bash
techflow validate workflow.yaml
```

## Need Help?

- Documentation: docs.techflow.example.com
- Community: community.techflow.com
- Support: support@techflow.com

---

Congratulations! You've created your first TechFlow workflow. 🎉
