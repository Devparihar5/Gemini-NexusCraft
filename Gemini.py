import streamlit as st
import pandas as pd

# Data provided
data = {
    'Capability': ['MMLU', 'CoT@32*', 'Big-Bench Hard', 'DROP', 'HellaSwag', 'GSM8K', 'maj1@32', 'MATH', 'HumanEval', 'Natural2Code'],
    'Benchmark': ['Representation of questions in 57 subjects', 'Reasoning', 'Reading comprehension (F1 Score)', 'Commonsense reasoning for everyday tasks', 'Basic arithmetic manipulations', 'Basic arithmetic manipulations', 'Python code generation', 'Challenging math problems', 'Python code generation', 'Python code generation'],
    'Higher is better': [90.0, 86.4, 83.6, 82.4, 87.8, 94.4, 92.0, 53.2, 74.4, 74.9],
    'Description': ['CoT@32*', '5-shot** (reported)', '3-shot', 'Variable shots', '10-shot*', 'maj1@32', '5-shot CoT (reported)', '4-shot', '0-shot (IT)*', '0-shot']
}
# Create a DataFrame from the data
df = pd.DataFrame(data)

# Page Title
st.title("Google's Gemini Model Guide 🚀🤖")

# Introduction
st.header("Introduction to Google's Gemini Model")
st.sidebar.markdown("[Why Gemini?](#why-gemini)")

st.write("""
Welcome to the forefront of cutting-edge AI with Google's Gemini model! 🚀🤖 
In this comprehensive guide, we'll dive deep into the intricacies of leveraging the power of GenerativeAI through Gemini. From seamless installation steps to fine-tuning configurations, and exploring the myriad benefits, this guide is your key to unlocking the full potential of this groundbreaking model.
""")

# Why Gemini?
st.header("🌐 Why Gemini?")
st.sidebar.markdown("[Installation](#installation)")

st.write("""
Gemini stands at the intersection of innovation and AI prowess. Its capabilities extend beyond the ordinary, promising a new era of generative content creation that's both powerful and dynamic.
""")
st.table(df)
# Learn More section
st.header("📚 Learn More")
# Add a clickable link
st.markdown("""
For a deeper understanding and additional insights, check out accompanying [blog post](https://deepmind.google/technologies/gemini/#introduction) dedicated to Google's Gemini Model. Let's embark on this exciting journey together! 🌟🔍.
""", unsafe_allow_html=True)