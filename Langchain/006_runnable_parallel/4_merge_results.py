import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.runnables import RunnableLambda, RunnableParallel


def length(text: str):
    return len(text)


def words(text: str):
    return len(text.split())


def merge(results):
    return f"Length: {results['length']}, Words: {results['words']}"


parallel = RunnableParallel(
    length=RunnableLambda(length),
    words=RunnableLambda(words)
)

merger = RunnableLambda(merge)

chain = parallel | merger

result = chain.invoke("LangChain is powerful")

print(result)