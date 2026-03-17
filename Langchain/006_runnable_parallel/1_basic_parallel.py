import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.runnables import RunnableLambda, RunnableParallel


def to_upper(text: str):
    return text.upper()


def to_lower(text: str):
    return text.lower()


upper = RunnableLambda(to_upper)
lower = RunnableLambda(to_lower)

parallel = RunnableParallel(
    upper=upper,
    lower=lower
)

result = parallel.invoke("LangChain")

print(result)