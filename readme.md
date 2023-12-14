# Gemini NexusCraft

This project consists of two Streamlit applications that leverage the capabilities of the Gemini AI model provided by Google's GenerativeAI. The Gemini model is a powerful text and image generation model that can be used for various creative and informative purposes.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Text Generation](#text-generation)
  - [Text and Image Generation](#text-and-image-generation)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Devparihar5/Gemini-NexusCraft.git
cd Gemini-NexusCraft
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage
To run the Streamlit app for text generation, execute the following command:

```bash
streamlit run Gemini.py
```
### Text Generation
![Text Generation](https://github.com/Devparihar5/Gemini-NexusCraft/blob/main/images/text-example.png)
### Text and Image Generation
![Text and Image Generation](https://github.com/Devparihar5/Gemini-NexusCraft/blob/main/images/image-example.png)

## Configuration

In both apps, you need to enter your API key to authenticate with the Gemini model. The API key can be entered through the Streamlit sidebar. Make sure to enter a valid API key to access the model.

Additionally, you can configure various model parameters such as temperature, top_p, top_k, and max_output_tokens to control the generation process.

## Contributing

Contributions to this project are welcome. If you have any ideas, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code for your own purposes.
