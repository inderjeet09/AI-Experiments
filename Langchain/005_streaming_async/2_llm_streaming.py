import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import AzureChatOpenAI


llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)


for chunk in llm.stream("Explain LangChain streaming briefly."):
    print(chunk.content, end="", flush=True)