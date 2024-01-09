""" Memory and State in Chains and Agents
"""

from langchain import ConversationChain
from langchain.llms import VertexAI

llm = VertexAI(temperature=0.85)
conversation = ConversationChain(llm=llm, verbose=True)

conversation.predict(input="Hi there")

conversation.predict(input="Can you please list the name of all presidents in the USA in the last ten years ?.")
# No imprime nada. NO funciona este prompt


