""" Generation of code with code-bison@001 using the gapic client     
"""

import gradio as gr

from google.cloud import aiplatform
from google.cloud.aiplatform.gapic.schema import predict
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value

PROJECT_ID = "argolis-rafaelsanchez-ml-dev" 
LOCATION = "us-central1" 
API_ENDPOINT = "us-central1-aiplatform.googleapis.com"
ENDPOINT = "projects/argolis-rafaelsanchez-ml-dev/locations/us-central1/publishers/google/models/code-bison@001"

def predict(prompt, max_output_tokens, temperature, top_p, top_k):
    
    client_options = {"api_endpoint": API_ENDPOINT}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.PredictionServiceClient(
        client_options=client_options
    )

    parameters = {
        "temperature": temperature,
        "maxOutputTokens": max_output_tokens
        }

    instance_dict = prompt
    instance = json_format.ParseDict(instance_dict, Value())
    instances = [instance]
    parameters_dict = parameters
    parameters = json_format.ParseDict(parameters_dict, Value())
    print(instances)
    response = client.predict(
        endpoint=ENDPOINT, instances=instances, parameters=parameters
    )
    print("response")
    predictions = response.predictions
    for prediction in predictions:
        print(" prediction:", dict(prediction))
    return predictions


demo = gr.Interface(
    predict, 
    [ gr.Textbox(label="Enter prompt:", value="Write a function that checks if a year is a leap year:"),
      gr.Slider(32, 512, value=128, step = 8, label = "max_output_tokens"),
      gr.Slider(0, 1, value=0, step = 0.1, label = "temperature"),
      gr.Slider(1, 5, value=1, step = 1, label = "top_p"),
      gr.Slider(20, 400, value=40, step = 10, label = "top_k"),
    ],
    "text"
    )

demo.launch(server_name="0.0.0.0", server_port=7860)