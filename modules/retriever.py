from langchain_qdrant import QdrantVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from config import QDRANT_PATH, COLLECTION_NAME


embeddings = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")
def get_retriever():
    vectorstore = QdrantVectorStore.from_existing_collection(
                                                    embedding=embeddings,
                                                    collection_name="demo_collection",
                                                    path="./tmp/langchain_qdrant"
                                                )
    return vectorstore

def search(query, k=5):
    retriever = get_retriever()
    results = retriever.similarity_search(query, k=k)
    return results
