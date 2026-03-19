import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda


def clean(data):
    data["topic"] = data["topic"].strip().lower()
    return data


cleaner = RunnableLambda(clean)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a precise AI assistant."),
        ("human", "Explain {topic} clearly.")
    ]
)

llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

chain = cleaner | prompt | llm

result = chain.invoke({"topic": "   LangChain pipelines   "})

print(result.content)