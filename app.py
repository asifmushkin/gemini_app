from dotenv import load_dotenv
load_dotenv() ##loading environment variable

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load gemini pro model to get responses
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


## Initialize streamlit app

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

input = st.text_input("Input: ",key="input")
submit = st.button("Ask me the question")

## when the submit is close

if submit:
    response = get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)


