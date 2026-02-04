from dotenv import load_dotenv
import os
from typing import Optional
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI

load_dotenv()


class APIResponse(BaseModel):
    status: str = Field(description="success or error")
    data: Optional[str] = Field(description="response data if successful")
    error: Optional[str] = Field(description="error message if failed")


llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

prompt = PromptTemplate(
    template=(
        "Answer the following question.\n"
        "If you can answer, return status=success and put the answer in data.\n"
        "If not, return status=error and explain why in error.\n"
        "Question: {question}"
    ),
    input_variables=["question"],
)

chain = prompt | llm.with_structured_output(APIResponse)

# result = chain.invoke(
#     {"question": "What is the capital of France?"}
# )

result = chain.invoke(
    {"question": "What is my name?"}
)

print(result)
