# Poem Generator from Image (Beginner Guide)

## Overview

This project is a simple Python script that generates short poems from images using Google Gemini AI.
You provide:

* an image
* a mood (such as calm, sad, or vibrant)

The script creates a poem and saves it as an HTML file that you can open in a browser.

---

## Features

* Generate poems from images
* Control the mood of the poem
* Output as a standalone HTML file

---

## Requirements

Install the required libraries:

```bash
pip install Pillow google-generativeai
```

---

## API Setup

1. Get an API key from Google AI Studio
2. Add it in your script:

```python
api_key = "YOUR_API_KEY"
```

---

## How to Run

```bash
python poem_generator.py
```

You will be prompted to enter:

* Image path (e.g. `image.jpg`)
* Mood (e.g. `calm`, `dark`, `romantic`)

---

## Output

* A file named `poem_output.html` will be created
* Open it in your browser to view the generated poem

---

## How It Works

1. Loads the image using Pillow
2. Sends the image and mood to the Gemini API
3. Receives a generated poem
4. Writes the poem into an HTML file

---

## Error Handling

* If the image path is incorrect, an error message is shown
* If the API fails, the HTML file is not created

---

## Customization

* Modify the prompt in the code to change poem style
* Add a `style.css` file to improve the appearance of the HTML output

---

## Summary

This project is a beginner-friendly introduction to:

* AI-based content generation
* working with images in Python
* generating simple web output
