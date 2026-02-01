from dotenv import load_dotenv
import os
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

def describe_state(state:str)->str:
    """ Describes any given state. """

    llm = AzureChatOpenAI(
        deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
        openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
        openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    )

    prompt=PromptTemplate(
        template="Describe {givenState} in fun way.",
        input_variables=["givenState"],
    )

    chain=prompt | llm

    result=chain.invoke({"givenState":state})

    return result.content


if __name__== "__main__":
    output=describe_state("Haryana")
    print(output)