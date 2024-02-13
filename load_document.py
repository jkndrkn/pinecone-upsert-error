from os import environ

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Pinecone

EMBEDDING_MODEL = "embed-english-v3.0"
INDEX_NAME = "answers-dev-jde-test-768"
TRIALS = 50
TEXT_PATH = "my_text.txt"

loader = TextLoader(TEXT_PATH)
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

print("docs length:", len(docs))

embedder = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")

for i in range(0, TRIALS):
    print("trial: ", i, flush=True)
    Pinecone.from_documents(docs, embedder, index_name=INDEX_NAME)
