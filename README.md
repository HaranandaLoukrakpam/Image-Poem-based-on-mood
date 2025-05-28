Poem Generation from Image
This document outlines a Python script designed to generate short poems from input images, influenced by a specified mood, utilizing the Google Gemini Pro Vision API. The output is rendered as a standalone HTML file for convenient viewing.

1. Introduction
The poem_generator.py script serves as a demonstration of multimodal AI capabilities, specifically the generation of creative text (poetry) in response to visual input. It processes an image and a user-defined emotional tone to produce a poem that encapsulates the image's essence while adhering to the desired mood.

2. Features
Multimodal Content Generation: Integrates image understanding with natural language generation to create descriptive poetry.
Mood-Controlled Output: Allows users to dictate the emotional tenor of the generated poem.
HTML Output Rendering: Produces a self-contained HTML file for easy display and sharing of the generated poem.
3. Prerequisites
To execute this script, the following software components and libraries are required:

Python 3.x: The script is developed in Python.
Pillow (PIL Fork): A fundamental library for image processing in Python.
Google Generative AI Library: The official Python client library for interacting with Google's Generative AI models.
These dependencies can be installed via pip:

Bash

pip install Pillow google-generativeai
4. API Key Configuration
Access to the Google Gemini API necessitates an API key.

Obtain API Key: A Google Gemini API key can be generated through the Google AI Studio.

Integration: Replace the placeholder string in the api_key variable within the poem_generator.py script with your acquired API key:

Python

api_key = "YOUR_GEMINI_API_KEY_HERE" # Update this line with your actual API key
genai.configure(api_key=api_key)
5. Usage
To run the poem generation script:

Save the Script: Save the provided Python code as poem_generator.py (or any preferred .py filename).

Execute: Open a terminal or command prompt, navigate to the directory containing the script, and execute it using the Python interpreter:

Bash

python poem_generator.py
Interactive Prompts: The script will prompt for the following inputs:

Enter the path to your image file: Provide the absolute or relative path to the image file (e.g., path/to/image.jpg, C:\Users\images\landscape.png).
Enter the desired mood for the poem: Specify an emotional mood (e.g., serene, vibrant, contemplative).
Output: Upon successful execution, an HTML file named poem_output.html will be created in the same directory. This file can be opened in any web browser to view the generated poem.

6. Code Structure and Explanation
The script is modularized into distinct functions for clarity and maintainability.

6.1. PoemFromImage(image_path: str, mood: str) -> str
This function is responsible for the core logic of poem generation.

Parameters:
image_path (str): The file path to the input image.
mood (str): The desired emotional tone for the poem.
Image Loading: Utilizes PIL.Image.open(image_path) to load the image into a Pillow Image object. Includes try-except blocks to handle FileNotFoundError and other general exceptions during image access.
Prompt Construction: Dynamically creates a text prompt for the Generative AI model, incorporating the specified mood and instructing the model to focus on visual elements.
API Call: Invokes model.generate_content([prompt, img]). This sends both the textual prompt and the image data to the configured Gemini model (gemini-1.5-flash) for multimodal content generation.
Return Value: Returns the generated poem as a string. In case of an error during image processing, an error message string is returned.
6.2. write_html(poem: str, mood: str)
This function constructs and writes the HTML output file.

Parameters:
poem (str): The generated poem text.
mood (str): The mood specified for the poem, used in the HTML title and heading.
HTML Structure: Generates a basic HTML5 document with a title, a heading indicating the poem's mood, and a <pre> tag to display the poem while preserving its formatting.
File Output: Writes the complete HTML content to a file named poem_output.html using with open("poem_output.html", "w", encoding="utf-8") as f:.
6.3. if __name__ == "__main__": block
This block serves as the script's entry point when executed directly.

User Input: Prompts the user to enter the image file path and the desired poem mood.
Function Invocation: Calls PoemFromImage with the user-provided inputs.
Conditional Output: Checks the return value of PoemFromImage. If an error message is detected (starts with "Error"), it prints the error to the console. Otherwise, it calls write_html to generate the HTML file and confirms successful completion to the user.
7. Error Handling
The script incorporates basic error handling mechanisms:

Image File Errors: Catches FileNotFoundError if the specified image path does not exist and general Exception for other issues during image loading.
Informative Messages: In case of an error, a descriptive error message is printed to the console, and the HTML file generation is skipped.
8. Customization
Users can customize aspects of the script's behavior and output:

Styling: The generated poem_output.html file includes a <link rel="stylesheet" href="style.css"> tag. Users can create a style.css file in the same directory as the script to apply custom CSS rules for visual presentation (e.g., fonts, colors, layout, responsiveness).
Poem Prompt: The prompt variable within the PoemFromImage function can be modified to alter the instructions given to the Gemini model, allowing for experimentation with different poetic styles, lengths, or thematic focuses.
