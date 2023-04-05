import streamlit as st
import os
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')

# Define a function to generate text using the OpenAI GPT-3 API
def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"The goal is to {prompt}. Here is a paragraph from the Bhagavad Gita:",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text

# Define the Streamlit app
st.header("Bhagavad Gita Goal Motivator")

goal = st.text_input("Enter a goal:")

if st.button("Generate motivational text"):
    text = generate_text(goal)
    st.write(text)
