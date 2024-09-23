from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from prompts import few_shot_prompt_template, few_shot_prompt_template_image, get_story_list
from dotenv import load_dotenv
import os

load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')

@st.cache_resource
def initialize_llm():
    return ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=google_api_key)

# Generate full content: story, story list, and image prompt
def generate_content(topic):
    llm = initialize_llm()

    # Generate the story
    prompt_story = few_shot_prompt_template.format(topic=topic)
    story = llm.invoke(prompt_story).content

    # Generate the image prompt
    prompt_image = few_shot_prompt_template_image.format(story=story)
    image_prompt = llm.invoke(prompt_image).content

    # Split the story into two parts
    story_list = get_story_list(story)

    return {
        'story': story,
        'story_list': story_list,
        'image_prompt': image_prompt
    }
