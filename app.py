# app.py
import streamlit as st
from PIL import Image
from modules.eco_assessment import assess_sustainability
from modules.upcycle_agent import suggest_upcycle_ideas
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

st.set_page_config(page_title="EcoStyle AI", layout="wide")
st.title("♻️ EcoStyle AI – Sustainable Fashion Advisor")

uploaded = st.file_uploader("Upload Clothing Image", type=["jpg", "png", "jpeg"])
if uploaded:
    img = Image.open(uploaded)
    st.image(img, use_column_width=True)
    
    sustainability_score, material_info = assess_sustainability(img)
    st.metric("Sustainability Score", f"{sustainability_score}/10")
    st.write("**Material Info**:", material_info)

    st.divider()
    st.subheader("♻️ Upcycle Ideas")
    ideas = suggest_upcycle_ideas(img)
    st.write(ideas)

st.divider()
st.subheader("🧠 Ask EcoStyle AI")
query = st.chat_input("Ask about fashion sustainability...")
if query:
    # You’d load a vector store and LLM here
    llm = Ollama(model="tinyllama")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    retriever = FAISS.load_local("faiss_store", embeddings).as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    answer = qa_chain.run(query)
    st.markdown(answer)
