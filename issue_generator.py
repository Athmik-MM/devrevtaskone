import requests

url = "https://api.devrev.ai/works.create"

headers = {
    "Authorization": "API KEY",
    "Content-Type": "application/json"
}
title = input("Enter the Issue title: ")

# Check if title is empty
if not title:
    print("No title given. Cannot raise an issue.")
    exit()

body = input("Enter the body (optional): ")

data = {
    "type": "issue",
    "applies_to_part": "PROD-2",
    "owned_by": [
        "DEVU-1"
    ],
    "title": title,
    "body": body if body else ""  # If body is not provided, set it to an empty string
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())