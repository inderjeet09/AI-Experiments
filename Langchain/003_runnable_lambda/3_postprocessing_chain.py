from dotenv import load_dotenv
import os
from langchain_openai import AzureChatOpenAI
from langchain_core.runnables import RunnableLambda

load_dotenv()

def extract_text(message):
    return message.content


llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

extractor = RunnableLambda(extract_text)

chain = llm | extractor

result = chain.invoke("Explain LangChain in one sentence")

print(result)