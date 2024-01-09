""" Example of chains with Vertex AI:
    Chains allow us to combine multiple components together to create a single, coherent application. For example, we can create a chain that takes user input, formats it with a PromptTemplate, and then passes the formatted response to an LLM 
"""

from langchain.llms import VertexAI
from langchain import PromptTemplate, LLMChain

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm = VertexAI()
llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "Which was the Roland Garros winner in the year Carlos Alcaraz was born?"

print(llm_chain.run(question))
# So, the final answer is Juan Carlos Ferrero.