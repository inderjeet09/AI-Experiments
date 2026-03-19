import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.runnables import RunnableLambda, RunnableParallel


def word_count(data):
    return len(data.summary.split())


def char_count(data):
    return len(data.summary)


parallel = RunnableParallel(
    word_count=RunnableLambda(word_count),
    char_count=RunnableLambda(char_count)
)

# simulate structured object
class Dummy:
    def __init__(self, summary):
        self.summary = summary


dummy = Dummy("LangChain enables building AI pipelines.")

result = parallel.invoke(dummy)

print(result)