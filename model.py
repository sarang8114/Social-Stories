# File: model.py
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from prompts import few_shot_prompt_template
from dotenv import load_dotenv
import os

load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')


@st.cache_resource
def initialize_llm():
    return ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=google_api_key)

def generate_story(topic):

    llm = initialize_llm()
    prompt = few_shot_prompt_template.format(topic=topic)
    response=llm.invoke(prompt).content

    return response
