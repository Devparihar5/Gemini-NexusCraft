import google.generativeai as genai
import streamlit as st
import json
import requests
import re

# Function to initialize session state
def initialize_session_state():
    return st.session_state.setdefault('api_key', None)

# Main Streamlit app
def home():
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

    # Check if the API key is provided
    if not api_key:
        st.sidebar.error("Please enter your API key.")
        st.stop()
    genai.configure(api_key=api_key)

    
    model = 'gemini-pro-vision' 
    # Sidebar option to choose image source
    image_source = st.sidebar.radio("Choose Image Source:", ["URL", "Upload"])
    prompt = st.text_input("Enter your Query:")
    if image_source == "URL":
        # Input for image URL
        image_url = st.sidebar.text_input("Enter the image URL:")
        # Prepare content for Gemini model
        contents = [
                {
                    "parts": [
                        {
                            "text":prompt
                        },
                        {
                            "image": {
                                "image_url": image_url
                            }
                        }
                    ]
                }
            ]
        
    else:
        # Input for uploading an image
        image_url = st.sidebar.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])


        # Prepare content for Gemini model
        contents = [
                {
                    "parts": [
                        {
                            "text":prompt
                        },
                        {
                            "image": {
                                "uploaded_file": image_url
                            }
                        }
                    ]
                }
            ]

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

    safety_settings = "{}"
    # Check if the query is provided
    if not prompt:
        st.error("Please enter your query.")
        st.stop()


    # generation_config = json.loads(generation_config)
    safety_settings = json.loads(safety_settings)
    stream = False
    for content in contents:
        for n, part in enumerate(content['parts']):
            if image:=part.get('image', None):
                if uploaded_file := image.get('uploaded_file', None):
                    data = uploaded_file.read()
                    mime_type = uploaded_file.type
                elif image_url := image.get('image_url', None):
                    try:
                        response = requests.get(image_url)
                        response.raise_for_status()  # Raise an HTTPError for bad responses

                        data = response.content
                        mime_type = response.headers['content-type']

                        # Continue processing with the image data

                    except requests.exceptions.HTTPError as http_err:
                        st.write(f"HTTP error occurred while fetching the image: {http_err}")
                    except requests.exceptions.RequestException as req_err:
                        st.write(f"An error occurred while fetching the image: {req_err}")
                    except Exception as e:
                        st.write(f"An unexpected error occurred: {str(e)}")
                else:
                    raise ValueError('Either uploaded_file or image_url must be provided.')
        
                if mime_type is None:
                    # Guess!
                    mime_type = 'image/png'

                blob = {'data': data, 'mime_type': mime_type}
                content['parts'][n] = blob
    st.image(data)
    gemini = genai.GenerativeModel(model_name=model)

    response = gemini.generate_content(
        contents,
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=False)
    st.subheader("Gemini:")
    data_str = str(response.candidates[0])
            
    # Use regular expressions to extract the text part
    match = re.search(r'text: "(.*?)"', data_str)
    if match:
        extracted_text = match.group(1)
        st.write(extracted_text)
   
# Run the Streamlit app
if __name__ == "__main__":
    home()
