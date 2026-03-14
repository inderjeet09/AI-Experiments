import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import AzureChatOpenAI
from langchain_core.runnables import RunnableLambda


def validate_input(text: str):
    if len(text) > 100:
        raise ValueError("Input too long. Maximum allowed length is 100 characters.")
    return text


validator = RunnableLambda(validate_input)

llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

chain = validator | llm

result = chain.invoke("Explain LangChain RunnableLambda in 2 lines")

print(result.content)