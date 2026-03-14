import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.runnables import RunnableLambda


def extract_text(msg):
    return msg.content


llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

messages = [
    SystemMessage(content="You are a concise AI tutor."),
    HumanMessage(content="Explain LangChain messages in one sentence")
]

extractor = RunnableLambda(extract_text)

chain = llm | extractor

result = chain.invoke(messages)

print(result)