""" Generation of code with code-bison@001 using the Vertex AI Python SDK
    Requires google-cloud-aiplatform 1.26.0
"""

from google.cloud import aiplatform
from vertexai.preview.language_models import CodeGenerationModel

print(f"Vertex AI SDK version: {aiplatform.__version__}")

model = CodeGenerationModel.from_pretrained("code-bison@001")

prompt = """Generate a Docker script to create a simple linux machine 
         that has python 3.10 installed with following libraries: pandas, tensorflow, numpy"""

response = model.predict(prefix=prompt, max_output_tokens=2048, temperature=0.2)

print(f"Response from Model: {response.text}")
