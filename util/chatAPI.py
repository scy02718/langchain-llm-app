from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

def modify_sentiment(text_input, selected_tone, selected_sentiment, strength, text_length):
    model = ChatOpenAI()
    
    prompt = PromptTemplate.from_template("""
        Change the sentiment of this text to {selected_tone} and {selected_sentiment}, with strength {strength} which is on a scale from 0 to 10.
        Keep the information as similar as possible, and keep it under {text_length}: {text_input}""")

    chain = LLMChain(llm=model, prompt=prompt)
    result = chain.run(text_input=text_input, selected_tone = selected_tone, selected_sentiment=selected_sentiment, strength=strength, text_length = text_length)
    return result

def analyze_sentiment(context, text_input):
    model = ChatOpenAI()
    
    prompt = PromptTemplate.from_template("""
        Analyze the sentiment of this text: {text_input} with this context: {context}
        If you think the context is not enough, simply say "More context is required." and we will provide more context for you.""")
    
    chain = LLMChain(llm=model, prompt=prompt)
    result = chain.run(context=context, text_input=text_input)
    return result

def analyze_suspicious_lines(age, text):
    model = ChatOpenAI()

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a very strict teacher and you are suspicious that a student wrote this text with a help of an AI"),
        ("user", """{age} years old student wrote this essay. Bring suspicious lines that you think that are AI generated. 
        Deeply consider that the student is {age} years old. Here is the text: {text}""")
    ])

    chain = LLMChain(llm=model, prompt=prompt)
    result = chain.run(age=age, text=text)
    return result

def against_debate(topic, opinion):
    model = ChatOpenAI()

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are having a debate with someone. You must win the debate by convincing the other person."),
        ("user", """{topic} is the topic of the debate. I think that {opinion} is true. You must use convincing
         arguments to convince me that I am wrong. Use true facts and logic only.""")
    ])

    chain = LLMChain(llm=model, prompt=prompt)
    result = chain.run(topic=topic, opinion=opinion)
    return result

def determine_importance(input_dict):
    model = ChatOpenAI()

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a journalist. You want to gather information about a topic, from different news articles. Since there are a lot of different articles
         and you don't have time to read all of them, you want to determine the importance of each article."""),
        ("user", """{input_dict} are the news articles, paired between title and description. Determine the importance of each article and also a short summary. 
        The importance is on a scale from 0 to 10. 0 means not important and 10 means very important.
        Explicitly tell me by saying Importance - "importance" next to the summary of the article.""")
    ])

    chain = LLMChain(llm=model, prompt=prompt)
    result = chain.run(input_dict = input_dict)
    return result