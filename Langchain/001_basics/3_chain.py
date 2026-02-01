from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI

load_dotenv()

llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

prompt=PromptTemplate(
    template="Explain {topic} in {tone} tone.",
    input_variables=["topic","tone"],
)

chain=prompt | llm

result= chain.invoke({"topic":"Himachal","tone":"fun"})

print(result.content)