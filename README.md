# Prompt Generator using LangChain with a model from Hugging Face

This is a very simple prompt that you can enter and the LLM will give you a response.

## Installation
We are going to install a few packages to enable this process.
Streamlit is a nice gui that enables you to enter prompts.
Langchain and transformers are the packages that run the LLM from HuggingFace.
Chromadb is the vector database.

```
pip3 install streamlit langchain transformers  wikipedia chromadb tiktoken --quiet
```

## Required files
`apikey.py` contains the API key you get from your Hugging Face Account. You can get this by creating a HuggingFace account and going to `https://huggingface.co/settings/account` and going clicking on the *Access Tokens* menu.

`app.py` contains the code that runs the streamlit UI and the underlying LLM

## To run
in a command window, 
```
streamlit run app.py
```

This will open a window where you can enter your prompt 
`http://localhost:8501/`

## Changelog
0.0.0 First drop