from dotenv import load_dotenv
import os
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import AzureChatOpenAI
from pprint import pprint

load_dotenv()

llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

@tool
def search(query:str)->str:
    """Search for information."""
    return f"Results for: {query}"

@tool 
def get_weather(query:str)->str:
    """Get weather for a particular location."""
    return f"Its always sunny in {query}"

agent=create_agent(
    model=llm,
    tools=[search,get_weather],
    system_prompt="You are a helpful assistant.",
)

result=agent.invoke(
    {
        "messages":[
        {
            "role":"user",
            "content":"Search for information about Haryana."
        },
        {
            "role":"user",
            "content":"What is the weather in Haryana?"
        }
    ]

    }
)

pprint(result["messages"][-1].content)