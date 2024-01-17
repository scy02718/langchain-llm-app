from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def quickstart():
    llm = OpenAI()
    chat_model = ChatOpenAI()

    text = "What would be a good topics to talk with your girlfriend?"
    messages = [HumanMessage(content=text)]

    llm_result = llm.invoke(text)
    chat_model_result = chat_model.invoke(messages)

    print(llm_result)
    print(chat_model_result)

def prompt_template():
    llm = OpenAI()
    chat_model = ChatOpenAI()

    prompt = PromptTemplate.from_template("What is a good time to go to {place}?")
    prompt.format(place="the bed")

    llm_result = llm.invoke(prompt)
    chat_model_result = chat_model.invoke(prompt)
    
    print(llm_result)
    print(chat_model_result)

if __name__ == "__main__":
    quickstart()