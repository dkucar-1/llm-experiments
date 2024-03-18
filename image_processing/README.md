# Image Caption Generator

Given an image input, this will generate a caption. 

## Installation
```pip3 install -r requirements.txt```

## Required files
You need to get a HuggingFace access token and saving it to your local environment as `OPENAI_API_TOKEN`. 

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
