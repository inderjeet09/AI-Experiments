import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a concise AI tutor."),
        ("human", "Explain {topic} briefly.")
    ]
)


llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

chain = prompt | llm


for chunk in chain.stream({"topic": "LangChain streaming"}):
    print(chunk.content, end="", flush=True)