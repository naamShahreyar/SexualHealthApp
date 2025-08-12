import streamlit as st
from modules.retriever import search
from modules.llm import generate_response
from modules.prompt import build_rag_prompt

st.set_page_config(page_title="Sexual Health RAG", layout="wide")
st.title("Sexual Health Q&A")

query = st.text_input("Ask a question:")
if st.button("Search") and query:
    # Retrieve
    results = search(query, k=5)

    retrieved_info = ""
    for i, res in enumerate(results):
        retrieved_info += f"Chunk {i+1}:\n{res.page_content}\nSource: {res.metadata['source']}\nUrl: {res.metadata['url']}\n\n"

    # Build prompt
    prompt = build_rag_prompt(retrieved_info, query)

    # Stream output
    placeholder = st.empty()
    output_text = ""
    for chunk in generate_response(prompt, stream=True):
        output_text += chunk
        placeholder.markdown(output_text)

