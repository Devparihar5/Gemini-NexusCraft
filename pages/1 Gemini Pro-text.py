import google.generativeai as genai
import streamlit as st

# Function to initialize session state
def initialize_session_state():
    return st.session_state.setdefault('api_key', None)

# Main Streamlit app
def text_page():
    st.title("Gemini NexusCraft")

    # Initialize session state
    initialize_session_state()

    # Configure API key
    api_key = st.sidebar.text_input("Enter your API key:", value=st.session_state.api_key)

    # Check if the API key is provided
    if not api_key:
        st.sidebar.error("Please enter your API key.")
        st.stop()
    else:
        # Store the API key in session state
        st.session_state.api_key = api_key

    genai.configure(api_key=api_key)

    
    # Set up the model configuration options
    temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.9, 0.1)
    top_p = st.sidebar.number_input("Top P", 0.0, 1.0, 1.0, 0.1)
    top_k = st.sidebar.number_input("Top K", 1, 100, 1)
    max_output_tokens = st.sidebar.number_input("Max Output Tokens", 1, 5000, 2048)

    # Set up the model
    generation_config = {
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        "max_output_tokens": max_output_tokens,
    }


    safety_settings = [
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      }
    ]
    prompt = st.text_input("Enter your Query:")
    # Check if the query is provided
    if not prompt:
        st.error("Please enter your query.")
        st.stop()

    if st.button("Ask Gemini"):
        gemini = genai.GenerativeModel(model_name="gemini-pro",
                                      generation_config=generation_config,
                                      safety_settings=safety_settings)
                

        prompt_parts = [prompt]

        response = gemini.generate_content(prompt_parts)
        # st.write(response.text)
        st.write(response.text)

# Run the Streamlit app
if __name__ == "__main__":
    text_page()