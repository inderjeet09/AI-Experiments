from dotenv import load_dotenv
import os 
from langchain.agents import create_agent
from langchain_openai import AzureChatOpenAI

load_dotenv()

llm = AzureChatOpenAI( 
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

def get_weather(city:str)->str:
    """Get weather for a giveng city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result=agent.invoke(
    {"messages":[{"role":"user","content":"What is the weather in Haryana"}]}
)
# print(result)
print(result["messages"][-1].content)