import os
import streamlit as st # runs on port 8051 streamlit run app.py
from langchain_community.llms import HuggingFaceEndpoint

apikey = os.environ['HUGGINGFACEHUB_API_TOKEN'] 

st.title("Test GPT creator")
prompt = st.text_input("Ask me anything!")

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"

llm = HuggingFaceEndpoint(
    repo_id=repo_id, max_length=128, temperature=0.5, token=apikey
)

if prompt:
	response = llm(prompt)
	st.write(response)

