# Python SDK

## Installation

```bash
pip install neuroflow-sdk
```

## Example

```python
from neuroflow import Client

client = Client(api_key="YOUR_API_KEY")

response = client.query(
    question="What is AI?"
)

print(response)
```