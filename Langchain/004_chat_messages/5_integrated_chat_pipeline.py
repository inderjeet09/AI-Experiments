import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda


def normalize(data):
    data["topic"] = data["topic"].strip().lower()
    return data


def extract(msg):
    return msg.content


normalizer = RunnableLambda(normalize)
extractor = RunnableLambda(extract)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert AI engineer."),
        ("human", "Explain {topic} clearly.")
    ]
)

llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

pipeline = normalizer | prompt | llm | extractor

result = pipeline.invoke({"topic": "   LangChain chat messages   "})

print(result)