from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

video_url = "https://www.youtube.com/watch?v=BvbmxEoMcZs"
def create_vector_db_from_youtube_url(url: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(url)
    transcript = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap = 100)
    docs = splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)
    return db

def get_response_from_query(db, query, k):
    docs = db.similarity_search(query, k)
    docs_page_content = " ".join([doc.page_content for doc in docs])

    llm = OpenAI()

    prompt = PromptTemplate(
        input_variables = ["question", "docs"],
        template="""
        You are a helpful YouTube assistant that can answer questions about
        videos based on the video's transcript.input_types=

        Answer the following question : {question}
        By searching the following video transcript : {docs}

        Only use the factual information from the video transcript.
        If you don't know the answer, just say "I don't know".

        Your answer should be detailed
        """
    )

    chain = prompt | llm
    response = chain.invoke(question=query, docs=docs_page_content)
    response = response.replace("\n", " ")
    return response
    
     

