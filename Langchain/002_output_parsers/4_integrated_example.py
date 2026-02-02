from dotenv import load_dotenv
import os
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
load_dotenv()

class APIResponse(BaseModel):
    concept: str
    summary: str
    use_case: str


llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

prompt = PromptTemplate(
    template=(
        "Explain the concept: {concept}\n"
        "Provide a short summary and one use case."
    ),
    input_variables=["concept"],
)

chain = prompt | llm.with_structured_output(APIResponse)

result = chain.invoke({"concept": "LangChain Output Parsers"})

print(result)
