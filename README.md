# Website File Generator (Streamlit + Gemini)

This project is a Streamlit web application that generates complete website code files (HTML, CSS, JavaScript) based on user-provided descriptions.  
It uses Google's Gemini model through LangChain to create structured output and packages the generated files into a downloadable ZIP.

---

## Features

- Generates functional website code using AI (Gemini 2.5 Flash)
- Accepts any website description through a text input
- Enforces strict output formatting using a system prompt
- Automatically extracts:
  - index.html  
  - style.css  
  - script.js
- Downloads everything as a ZIP file
- Simple, clean UI using Streamlit

---

## How It Works

1. User enters website requirements.
2. The AI model returns code formatted inside:
--html--
[HTML code here]
--html--

--css--
[CSS code here]
--css--

--js--
[JavaScript code here]
--js--
3. The script extracts each section and writes them into separate files.
4. All files are zipped and provided as a download.

---

## Requirements

- Python 3.9+
- Google API Key (Gemini)
- Streamlit
- LangChain
- langchain-google-genai
- python-dotenv

Install dependencies:

```bash
pip install streamlit langchain langchain-google-genai python-dotenv
