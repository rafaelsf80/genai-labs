#!/bin/bash
PROJECT_ID=argolis-rafaelsanchez-ml-dev
ENDPOINT_ID=text-bison

curl \
-X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
https://us-central1-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/us-central1/publishers/google/${ENDPOINT_ID}/text-bison:predict -d '{
  "instances": [
    { "content": "Give a short description of a machine learning model: "}
  ],
  "parameters": {
    "temperature": 0.2,
    "maxOutputTokens": 1024,
    "topP": 0.8,
    "topK": 40
  }
}'

