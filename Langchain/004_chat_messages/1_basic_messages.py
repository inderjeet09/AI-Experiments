import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

messages = [
    SystemMessage(content="You are a concise technical assistant."),
    HumanMessage(content="Explain LangChain in one sentence.")
]

response = llm.invoke(messages)
print(response.content)