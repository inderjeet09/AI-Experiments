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


async def explain_langchain():
    print("First Call Start")
    response = await llm.ainvoke("Explain LangChain in two sentences.")
    print("First Call end")
    return response.content


async def explain_runnable_lambda():
    print("second calll start")
    response = await llm.ainvoke("Explain RunnableLambda in two sentences.")
    print("second call end")
    return response.content


async def main():

    result1, result2 = await asyncio.gather(
        explain_langchain(),
        explain_runnable_lambda()
    )

    print("\nLangChain Explanation:\n")
    print(result1)

    print("\nRunnableLambda Explanation:\n")
    print(result2)


asyncio.run(main())