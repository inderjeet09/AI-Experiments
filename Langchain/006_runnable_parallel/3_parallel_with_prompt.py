import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel


llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)


summary_prompt = ChatPromptTemplate.from_messages(
    [("human", "Summarize: {text}")]
)

keywords_prompt = ChatPromptTemplate.from_messages(
    [("human", "Extract keywords: {text}")]
)


parallel = RunnableParallel(
    summary=summary_prompt | llm,
    keywords=keywords_prompt | llm
)

result = parallel.invoke({"text": "LangChain is used for building LLM applications."})

print(result["summary"].content)
print(result["keywords"].content)