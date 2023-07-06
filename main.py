import warnings
warnings.filterwarnings('ignore')
from pprint import pprint
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import LanguageParser
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    Language,
)
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

wd = "/Users/cole.mcintosh/Desktop/PyAutomations/Action-Center/elc"

loader = GenericLoader.from_filesystem(
    wd,
    glob="*",
    suffixes=[".py"],
    parser=LanguageParser()
)
docs = loader.load()

py_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=60, chunk_overlap=0
)

result = py_splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings()

db = FAISS.from_documents(docs, embeddings)

query = "What is the endpoint used?"
docs = db.similarity_search(query)

pprint(docs)
