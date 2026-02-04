from dotenv import load_dotenv
import os
from pydantic import BaseModel, Field
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

class ValidationResult(BaseModel):
    is_valid: bool = Field(description="Whether the statement is correct")
    reason: str = Field(description="Short explanation for the decision")


llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

prompt = PromptTemplate(
    template=(
        "Determine whether the following statement is correct:\n{statement}"
    ),
    input_variables=["statement"],
)

structured_llm = llm.with_structured_output(ValidationResult)

statement = "LangChain replaces the need for Python."

chain= prompt | structured_llm
result = chain.invoke({"statement":statement})

print(result)
print(type(result))
