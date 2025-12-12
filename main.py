import streamlit as st
import os
import langchain as lc
from langchain_google_genai import GoogleGenerativeAI,ChatGoogleGenerativeAI
from dotenv import load_dotenv
import zipfile

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title ="chat bot", page_icon=":robot_face:")
st.title("website file generator")

model = "gemini-2.5-flash"
llm = ChatGoogleGenerativeAI(model=model, temperature=0.5)

prompt = st.text_area("Enter the details about website:", key="user_input")
if st.button("Generate Website"):
    with st.spinner("Generating website..."):
        message=[("system",'''You are an expert web developer with 10+ years of experience. 
Your task is to generate a complete, functional website using only HTML, CSS, and JavaScript based on the user's requirements.

Follow these rules strictly:

1. Output must follow this exact format:

--html--
[HTML code here]
--html--

--css--
[CSS code here]
--css--

--js--
[JavaScript code here]
--js--

2. Do not use emojis or special characters or non-ASCII characters in the code.                 
                  '''),
                  ("user",f"Generate a website with the following details: {prompt}")]
        response = llm.invoke(message)
        with open("index.html", "w") as f:
            f.write(response.content.split("--html--")[1])
        with open("style.css", "w") as f:
            f.write(response.content.split("--css--")[1])
        with open("script.js", "w") as f:
            f.write(response.content.split("--js--")[1])
        
        with zipfile.ZipFile("website_files.zip", "w") as f:
            f.write("index.html")
            f.write("style.css")
            f.write("script.js")

        st.download_button(
            label="Download Website Files",
            data=open("website_files.zip", "rb"),
            file_name="website_files.zip"
        )
