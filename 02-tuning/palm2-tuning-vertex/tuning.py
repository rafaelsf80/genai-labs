""" Tunes LLM model with public StackOverflow data. 
    Run "python3 get_data.py" first to get input data and then upload the JSONL file to GCS (TRAINING_DATA_URI)
"""

from typing import Union

import pandas as pd
from google.cloud import aiplatform
from vertexai.preview.language_models import TextGenerationModel

import random
import string

# Generate a uuid of a specified length(default=8)
def generate_uuid(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))

UUID = generate_uuid()

MODEL_NAME = f"genai-workshop-tuned-model-{UUID}"
PROJECT_ID = "YOUR_PROJECT_ID"   # <---- CHANGE THIS
BUCKET_NAME = "YOUR_BUCKET "     # <---- CHANGE THIS. MUST BE SAME REGION
BUCKET_URI = f"gs://{BUCKET_NAME}"
REGION = "us-central1"           # <---- CHANGE THIS (OPTIONAL)
TRAINING_DATA_URI = f"{BUCKET_URI}/training_data_stack_overflow_python_qa.jsonl"  # <---- CHANGE THIS


def tuned_model(
    project_id: str,
    location: str,
    training_data: str,
    model_display_name: str,
    train_steps=100,
):

    """Prompt-tune a new model, based on a prompt-response data.

    "training_data" can be either the GCS URI of a file formatted in JSONL format
    (for example: training_data=f'gs://{bucket}/{filename}.jsonl'), or a pandas
    DataFrame. Each training example should be JSONL record with two keys, for
    example:
      {
        "input_text": <input prompt>,
        "output_text": <associated output>
      },
    or the pandas DataFame should contain two columns:
      ['input_text', 'output_text']
    with rows for each training example.

    Args:
      project_id: GCP Project ID, used to initialize aiplatform
      location: GCP Region, used to initialize aiplatform
      training_data: GCS URI of training file or pandas dataframe of training data
      train_steps: Number of training steps to use when tuning the model.
    """

    aiplatform.init(project=project_id, location=location)
    model = TextGenerationModel.from_pretrained("text-bison@001")

    model.tune_model(
        training_data=training_data,
        model_display_name=model_display_name,
        train_steps=train_steps,
        # Tuning can only happen in the "europe-west4" location
        tuning_job_location="europe-west4",
        # Model can only be deployed in the "us-central1" location
        tuned_model_location="us-central1",
    )

    # Test the tuned model:
    print(
        model.predict(
            "Can you provide me with a Python implementation of BERT with Tensorflow? Example: "
        )
    )

    return model

# This will start the tuning job and output a URL where you can monitor the pipeline execution.
model = tuned_model(PROJECT_ID, REGION, TRAINING_DATA_URI, MODEL_NAME)

def list_tuned_models(project_id, location):

    aiplatform.init(project=project_id, location=location)
    model = TextGenerationModel.from_pretrained("text-bison@001")
    tuned_model_names = model.list_tuned_model_names()
    print(tuned_model_names)

list_tuned_models(PROJECT_ID, REGION)

def fetch_model(project_id, location):

    aiplatform.init(project=project_id, location=location)
    model = TextGenerationModel.from_pretrained("text-bison@001")
    list_tuned_models = model.list_tuned_model_names()
    tuned_model = list_tuned_models[0]

    return tuned_model

deployed_model = fetch_model(PROJECT_ID, REGION)
deployed_model = TextGenerationModel.get_tuned_model(deployed_model)

PROMPT = """
How can I save my TensorFlow model on Google Cloud Storage. Can you show me a Python example?

example: 

"""

print(deployed_model.predict(PROMPT))

