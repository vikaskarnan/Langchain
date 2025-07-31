from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
model="gemini-2.5-flash"

def hello_langchain(prompt):
    """instantiates a chatGoogleGenerativeAI model and
    invokes it  with a simple prompt.
    prints the model's response.
    """
    llm=ChatGoogleGenerativeAI(model=model,api_key=api_key)
    response = llm.invoke(prompt)
    return response.content

if __name__ == "__main__":
    print(hello_langchain("Hello, LangChain!"))