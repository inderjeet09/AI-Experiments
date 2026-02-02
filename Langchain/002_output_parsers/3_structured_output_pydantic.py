from dotenv import load_dotenv
import os
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel,Field

load_dotenv()

class ConceptLearn(BaseModel):
    summary:str = Field(description="Short Explanation")
    useCase:str = Field(description="One real world use case")

llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

structured_llm = llm.with_structured_output(ConceptLearn)

result = structured_llm.invoke(
    "Explain LangChain Runnable interface"
)


print(result)
print(type(result))