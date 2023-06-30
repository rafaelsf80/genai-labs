""" Example of chain class, a basic chain which takes an input and passes it to a prompt template.
"""

from langchain.prompts import PromptTemplate
from langchain.llms import VertexAI

llm = VertexAI(temperature=0.9)

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}"
)

from langchain.chains import LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("hammers"))