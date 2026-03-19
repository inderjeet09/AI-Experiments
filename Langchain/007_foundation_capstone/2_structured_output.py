import os
from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel, Field
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


class ResponseModel(BaseModel):
    summary: str = Field(description="Short explanation")
    use_case: str = Field(description="One real-world use case")


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a technical assistant."),
        ("human", "Explain {topic} with summary and use case.")
    ]
)

llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

chain = prompt | llm.with_structured_output(ResponseModel)

result = chain.invoke({"topic": "LangChain RunnableParallel"})

print(result)