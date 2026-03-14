from dotenv import load_dotenv
import os
from langchain_openai import AzureChatOpenAI
from langchain_core.runnables import RunnableLambda

load_dotenv()

def clean(text: str) -> str:
    return text.strip()


def extract(msg):
    return msg.content


def format_output(text: str) -> str:
    return f"\nFinal Answer:\n{text}"


cleaner = RunnableLambda(clean)
extractor = RunnableLambda(extract)
formatter = RunnableLambda(format_output)

llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

pipeline = cleaner | llm | extractor | formatter

result = pipeline.invoke("Explain LangChain RunnableLambda")

print(result)