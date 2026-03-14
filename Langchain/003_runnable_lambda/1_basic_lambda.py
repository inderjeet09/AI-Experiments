from langchain_core.runnables import RunnableLambda

def greet(name:str):
    return f"Hello {name},Welcome to Langchain."

runnable = RunnableLambda(greet)

result= runnable.invoke("Inderjeet")

print(result)