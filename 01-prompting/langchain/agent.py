import langchain
print(langchain.__version__)

from langchain.chat_models.base import BaseChatModel

from google.cloud import documentai_v1 as documentai
from google.api_core.client_options import ClientOptions

import logging

def ocr_parser(file):

    FILE_PATH = file # Getting filename, since file type is tempfile._TemporaryFileWrapper
    MIME_TYPE = "application/pdf"

    PROJECT_ID = "YOUR_PROJECT_ID" # <---- CHANGE THIS
    LOCATION = "eu"
    PROCESSOR_ID = "a99d341e2c8c2e1c" # ocr processor

    # Instantiates a client
    docai_client = documentai.DocumentProcessorServiceClient(
        client_options=ClientOptions(api_endpoint=f"{LOCATION}-documentai.googleapis.com")
    )

    RESOURCE_NAME = docai_client.processor_path(PROJECT_ID, LOCATION, PROCESSOR_ID)

    # Read the file into memory
    with open(FILE_PATH, "rb") as image:
        image_content = image.read()

    # Load Binary Data into Document AI RawDocument Object
    raw_document = documentai.RawDocument(content=image_content, mime_type=MIME_TYPE)

    # Configure the process request
    request = documentai.ProcessRequest(name=RESOURCE_NAME, raw_document=raw_document)

    # Use the Document AI client to process the sample form
    result = docai_client.process_document(request=request)

    document_object = result.document
    logging.info("Document processing complete.")
    logging.info(f"Text: {document_object.text}")
    return document_object.text



from vertexlangchain import VertexLLM, VertexEmbeddings

REQUESTS_PER_MINUTE = 150

llm = VertexLLM(
    model_name='text-bison@001',
    max_output_tokens=256,
    temperature=0.1,
    top_p=0.8,top_k=40,
    verbose=True,
)

my_text = "What day comes after Friday?"

print(llm(my_text))



# Ingest PDF files
from langchain.document_loaders import PyPDFLoader

# Load GOOG's 10K annual report (92 pages).
#url = "https://abc.xyz/investor/static/pdf/20230203_alphabet_10K.pdf"
#loader = PyPDFLoader(url)
#loader = PyPDFLoader("./AC36_5pages.pdf")
#documents = loader.load()

doc_mexico = ocr_parser('./AC36_5pages.pdf')
#doc_mexico = ocr_parser('./20230203_alphabet_10K_15pages.pdf')
print(doc_mexico)

# write a function to subscribe to a pubsub topic











