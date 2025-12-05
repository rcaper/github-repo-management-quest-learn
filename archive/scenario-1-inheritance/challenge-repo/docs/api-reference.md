# TechFlow API Reference

The TechFlow API allows you to programmatically create and manage workflows.

## Base URL

All API requests should be made to:

```
https://api.techflow.com/v2
```

## Authentication

TechFlow uses API keys for authentication. Include your API key in the header:

```
Authorization: Bearer YOUR_API_KEY
```

## Endpoints

### Workflows

#### List Workflows
```
GET /workflows
```

Returns a list of all workflows.

**Response:**
```json
{
  "workflows": [
    {
      "id": "wf_123",
      "name": "My Workflow",
      "status": "active"
    }
  ]
}
```

#### Create Workflow
```
POST /workflows
```

Creates a new workflow.

**Request Body:**
```json
{
  "name": "My New Workflow",
  "description": "Workflow description",
  "triggers": []
}
```

### Get Workflow
```
GET /workflows/{workflow_id}
```

Retrieves details about a specific workflow.

#### Update Workflow

```
PUT /workflows/{workflow_id}
```

Updates an existing workflow.

#### Delete Workflow

```
DELETE /workflows/{workflow_id}
```

Deletes a workflow permanently.

### Executions

#### List Executions

```
GET /executions
```

Returns execution history.

#### Trigger Execution

```
POST /workflows/{workflow_id}/execute
```

Manually triggers a workflow execution.

## Rate Limiting

The API is rate limited to 100 requests per minute per API key.

If you exceed the rate limit, you'll receive a 429 status code.

## Error Codes

- 200 - Success
- 400 - Bad Request
- 401 - Unauthorized
- **404** - Not Found
- 429 - Rate Limit Exceeded
- 500 - Server Error

## SDKs

We provide official SDKs for:
- Python
- JavaScript
- Ruby
- Go

See the [SDK documentation](sdk-docs.md) for more details.

## Examples

### Python Example

```python
import techflow

client = techflow.Client(api_key="your_key")

# List workflows
workflows = client.workflows.list()

# Create a workflow
workflow = client.workflows.create(
    name="My Workflow",
    triggers=["manual"]
)
```

### JavaScript Example
```javascript
const TechFlow = require('techflow-sdk');

const client = new TechFlow({ apiKey: 'your_key' });

// List workflows
client.workflows.list().then(workflows => {
  console.log(workflows);
});
```

## Webhooks

TechFlow can send webhooks to your application when events occur.

Configure webhooks in your dashboard at https://dashboard.techflow.com/webhooks

### Webhook Events

- `workflow.created`
- `workflow.updated`
- `workflow.deleted`
- `execution.started`
- `execution.completed`
- `execution.failed`

## Support

For API support, contact api-support@techflow.com

---
Last updated: November 2020
