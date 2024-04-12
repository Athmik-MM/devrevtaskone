## Getting Started with DevRev API Integration

### Step 1: Generate Personal Access Token (PAT)

1. Create an account on DevRev.
2. Generate a Personal Access Token (PAT) from your account settings.
3. Store the PAT securely, as it will be required for authentication in API calls.

### Step 2: Install DevRev CLI

Install the DevRev CLI tool by following the instructions provided [here](https://developer.devrev.ai/snap-in-development/references/install-dev-rev-cli).

### Step 3: Authenticate DevRev CLI

Run the following command in the terminal, in the folder where your program is cloned:

devrev profiles authenticate -o <dev-org-slug> -u youremail@yourdomain.com

Replace `<dev-org-slug>` with your DevRev organization slug and `<youremail@yourdomain.com>` with your email address.

### Step 4: Create a Part (if not already exist)

Before creating an issue, ensure that the part to which the issue will be associated exists. Use the following API endpoint to create a part:

Endpoint: [Create Part](https://developer.devrev.ai/api-reference/parts/create)

```python
data = {
    "type": "issue",
    "applies_to_part": "PROD-2", // replace with your partsID
    "owned_by": [
        "DEVU-1" // replace with your userID
    ],
    "title": "<issue-title>",
    "body": "<issue-description>"  
}'''

Run
'''python issue_generator.py'''


Enter the issue in the terminal!
