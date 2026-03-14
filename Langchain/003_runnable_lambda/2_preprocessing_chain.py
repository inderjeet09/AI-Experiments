from dotenv import load_dotenv
import os
from langchain_core.runnables import RunnableLambda
from langchain_openai import AzureChatOpenAI

load_dotenv()

def clean_text(text: str) -> str:
    return text.strip().lower()


cleaner = RunnableLambda(clean_text)

llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

chain = cleaner | llm



result = chain.invoke("   WHAT IS LANGCHAIN?   ")

print(result.content)