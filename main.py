import streamlit as st
from model import initialize_llm, generate_story
from prompts import few_shot_prompt_template

# Configure the page
st.set_page_config(page_title="AI Story Generator", page_icon="📚")

# Streamlit app
st.title("📚 AI Story Generator")
st.write("Enter a topic, and I'll generate Social Story for you!")

# User input
user_topic = st.text_input("Enter a topic for the story:")

if st.button("Generate Story"):
    if user_topic:
        with st.spinner("Generating story..."):
            story = generate_story(user_topic)
            if story!='':
                st.success("Story generated!")
                st.write(story)
            else:
                st.warning('Topic may be explicit')
    else:
        st.warning("Please enter a topic.")

st.sidebar.header("About")
st.sidebar.write(
    "This app uses AI to generate short stories for children with ASD. "
    "The stories are designed to teach social skills and manners related to the given topic."
)