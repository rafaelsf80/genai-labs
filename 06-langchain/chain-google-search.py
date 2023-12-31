""" SerpApi is an API call to get Google search result. 
    It is the JSON representative of Google search result.
"""

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from langchain.llms import VertexAI


os.environ["SERPAPI_API_KEY"] = "XXXX"

# First, let's load the language model we're going to use to control the agent.
llm = VertexAI(temperature=0.2)

# Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Now let's test it out!
res = agent.run("What was the high temperature in SF yesterday in Fahrenheit? What is this number raised to the .023 power?")