from dotenv import load_dotenv
import os
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = AzureChatOpenAI(
    deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

prompt=PromptTemplate(
    template="Explain {topic} in {number} sentences",
    input_variables=["topic","number"],
)

formatted_prompt=prompt.invoke({"topic":"Haryana","number":4})
result=llm.invoke(formatted_prompt)
print(result.content)

