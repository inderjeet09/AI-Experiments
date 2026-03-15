import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.runnables import RunnableLambda


def slow_echo(text: str):
    return text


runnable = RunnableLambda(slow_echo)

for chunk in runnable.stream("Hello LangChain, what is your function, my name is inderjeet"):
    print(chunk)