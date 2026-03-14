from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_openai import AzureChatOpenAI

load_dotenv()

def normalize_topic(data):
    topic = data["topic"].strip().lower()
    return {"topic": topic}


normalizer = RunnableLambda(normalize_topic)

prompt = PromptTemplate(
    template="Explain {topic} in one sentence.",
    input_variables=["topic"],
)

llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

chain = normalizer | prompt | llm

result = chain.invoke({"topic": "   LangChain Runnable   "})

print(result.content)