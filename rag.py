from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def get_vector_db():
    schema = ["Employees(id, name, salary)"]

    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_texts(schema, embeddings)

    return db