""" Example of models with Vertex AI:
    Models (LLMs) are a core component of LangChain. Vertex AI class supports several models (text-bison@001, chat-bison@001, ...)
    LangChain is not a provider of LLMs, but rather provides a standard interface through which you can interact with a variety of LLMs.
"""

from langchain.llms import VertexAI
from langchain import PromptTemplate, LLMChain

REQUESTS_PER_MINUTE = 300

# Text model instance integrated with langChain
llm = VertexAI(
    model_name='text-bison@001',
    max_output_tokens=256,
    temperature=0.1,
    top_p=0.8,
    top_k=40,
    verbose=True,
)

print(llm("who are you?"))
# I am powered by PaLM 2, which stands for Pathways Language Model 2, a large language model from Google AI.