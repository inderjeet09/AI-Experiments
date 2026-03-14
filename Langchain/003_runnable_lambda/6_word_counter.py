import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import AzureChatOpenAI
from langchain_core.runnables import RunnableLambda


def extract_text(message):
    return message.content


def count_words(text: str):
    words = text.split()
    return {
        "text": text,
        "word_count": len(words)
    }


extractor = RunnableLambda(extract_text)
counter = RunnableLambda(count_words)

llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

pipeline = llm | extractor | counter

result = pipeline.invoke("Explain LangChain RunnableLambda in two sentences")

print(result)