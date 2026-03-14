import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import AzureChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage


llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)


messages = [
    SystemMessage(content="You are a helpful AI tutor."),
    HumanMessage(content="What is LangChain?")
]


response1 = llm.invoke(messages)

print("AI:", response1.content)


messages.append(response1)


messages.append(
    HumanMessage(content="Why is it useful?")
)


response2 = llm.invoke(messages)

print("\nAI:", response2.content)