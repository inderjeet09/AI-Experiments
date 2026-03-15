import os
import asyncio
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import AzureChatOpenAI


llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)


async def run():
    response = await llm.ainvoke("Explain LangChain async execution.")
    print(response.content)


asyncio.run(run())