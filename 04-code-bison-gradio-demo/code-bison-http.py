""" Generation of code with code-bison@001 using the HTTP REST
    Replace with your OAuth2 token (60 min expiration)
"""

import requests
import json

model_id = 'code-bison'
project_id = "argolis-rafaelsanchez-ml-dev"
api_subdomain = 'us-central1-aiplatform'

token = "ya29....."  # <--- REPLACE WITH YOUR OAUTH2 TOKEN (gcloud auth application-default print-access-token)

resp = requests.post(
  f'https://{api_subdomain}.googleapis.com/v1/projects/{project_id}/locations/us-central1/publishers/google/models/{model_id}:predict',
  headers={
    'Content-Type': 'application/json', 
    'Authorization': 'Bearer ' + token,
  },
  json={
    "instances": [
    { "prefix": "# Write a function that checks if a year is a leap year.",
      "suffix": ""
    }
  ],
    "parameters": {
    "task": "GENERATION",
    "temperature": 0.2,
    "maxOutputTokens": 256,
    "candidateCount": 1,
  }
  }
)

print(resp.json()['predictions'][0]['content'])