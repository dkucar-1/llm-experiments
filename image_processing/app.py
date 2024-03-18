import os
from tempfile import NamedTemporaryFile
import streamlit as st 
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI

from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.memory import ConversationBufferMemory

from tools import ImageCaptionTool

apikey = os.environ['OPENAI_API_TOKEN'] 

tools = [ImageCaptionTool()]

conversational_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True
)

llm = ChatOpenAI(
    openai_api_key=apikey,
    temperature=0.5
)

agent = initialize_agent(
    agent="chat-conversational-react-description",
    tools=tools,
    llm=llm,
    max_iterations=5,
    verbose=True,
    memory=conversational_memory,
    early_stopping_method='generate'
)
      
st.title("AI Image Descriptor")

uploaded_file = st.file_uploader("Choose a file", type=["jpeg", "jpg", "png"])

if uploaded_file:
    # display image
    st.image(uploaded_file, use_column_width=True)

    # text input
    user_question = st.text_input("Ask a question about your image:")

    st.write("Chat Bot's Reply") if user_question else None
  
    with NamedTemporaryFile(dir='.') as f:
        f.write(uploaded_file.getbuffer())
        image_path = f.name

        # write agent response
        if user_question != "":
            with st.spinner(text="In progress..."):
                response = agent.run(f"{user_question}, this is the image path: {image_path}")
                st.write(response)

