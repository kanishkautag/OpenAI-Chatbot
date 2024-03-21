from langchain.llms import OpenAI
import streamlit as st
import os

## Function to load OpenAI model and get responses

def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-3.5-turbo-instruct", temperature=0.5)
    response = llm(question)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input_text = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

## If ask button is clicked

if submit:
    response = get_openai_response(input_text)
    st.subheader("The Response is")
    st.write(response)
