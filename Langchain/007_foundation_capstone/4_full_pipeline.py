import os
from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableParallel


class ResponseModel(BaseModel):
    summary: str
    use_case: str


def clean(data):
    data["topic"] = data["topic"].strip()
    return data


def word_count(data: ResponseModel):
    return len(data.summary.split())


def merge(results):
    return {
        "summary": results["original"].summary,
        "use_case": results["original"].use_case,
        "word_count": results["word_count"]
    }


cleaner = RunnableLambda(clean)
word_counter = RunnableLambda(word_count)
merger = RunnableLambda(merge)


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI engineer."),
        ("human", "Explain {topic} with summary and use case.")
    ]
)


llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

structured_llm = llm.with_structured_output(ResponseModel)


# STEP 1: sequential (get structured output)
base_chain = cleaner | prompt | structured_llm


# STEP 2: parallel on structured output
parallel = RunnableParallel(
    original=RunnableLambda(lambda x: x),   # pass-through
    word_count=word_counter
)


# STEP 3: merge
pipeline = base_chain | parallel | merger


result = pipeline.invoke({"topic": "LangChain pipelines"})

print(result)