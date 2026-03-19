import os
from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


class APIResponse(BaseModel):
    summary: str
    use_case: str


llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an API backend."),
        ("human", "Explain {topic} with summary and use case.")
    ]
)

chain = prompt | llm.with_structured_output(APIResponse)


def get_response(topic: str):
    result = chain.invoke({"topic": topic})
    return result.model_dump()


if __name__ == "__main__":
    output = get_response("LangChain capstone")
    print(output)