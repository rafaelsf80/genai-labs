""" Agents use an LLM to determine which actions to take and in what order. An action can either be using a tool and observing its output, or returning a response to the user. 
    There are four available agents: AgentType.REACT_DOCSTORE, AgentType.ZERO_SHOT_REACT_DESCRIPTION, AgentType.SELF_ASK_WITH_SEARCH, AgentType.CONVERSATIONAL_REACT_DESCRIPTION
    This sample covers `AgentType.REACT_DOCSTORE` which is described in the ReAct paper https://arxiv.org/pdf/2210.03629.pdf
"""

from langchain import Wikipedia # pip3 install wikipedia
from langchain.llms import VertexAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.agents.react.base import DocstoreExplorer

docstore=DocstoreExplorer(Wikipedia())
tools = [
    Tool(
        name="Search",
        func=docstore.search,
        description="useful for when you need to ask with search"
    ),
    Tool(
        name="Lookup",
        func=docstore.lookup,
        description="useful for when you need to ask with lookup"
    )
]

# Text model instance integrated with langChain
llm = VertexAI(
    model_name='text-bison@001',
    max_output_tokens=256,
    temperature=0.1,
    top_p=0.8,
    top_k=40,
    verbose=True,
)

react = initialize_agent(tools, llm, agent=AgentType.REACT_DOCSTORE, verbose=True)

#question = "Author David Chanoff has collaborated with a U.S. Navy admiral who served as the ambassador to the United Kingdom under which President?"
question = "Writer Arturo Perez Reverte wrote a novel about a famous battle in the 19th century. Tell me who won that battle."
react.run(question)