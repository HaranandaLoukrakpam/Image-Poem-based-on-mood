import google.generativeai as genai
from PIL import Image

api_key = "AIzaSyAQcGEhdUcMcLXmgJxLSSKSp1bikcRAjWY"
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def PoemFromImage(image_path: str, mood: str) -> str:
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        return "Error: Image file not found."
    except Exception as e:
        return f"Error: Could not open image: {e}"

    prompt = f"""Generate a short poem that captures the essence of this image and evokes a {mood} mood.
    Focus on key visual elements and translate them into poetic language that resonates with the specified feeling."""

    response = model.generate_content([prompt, img])
    return response.text

def write_html(poem: str, mood: str):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Poem from Image - {mood.capitalize()} Mood</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div class="poem-box">
            <h1>Generated Poem ({mood.capitalize()} Mood)</h1>
            <pre>{poem}</pre>
        </div>
    </body>
    </html>
    """
    with open("poem_output.html", "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    image_file = input("Enter the path to your image file: ")
    poem_mood = input("Enter the desired mood for the poem: ")

    poem = PoemFromImage(image_file, poem_mood)

    if poem.startswith("Error"):
        print(poem)
    else:
        write_html(poem, poem_mood)
        print("✅ Poem generated and saved to 'poem_output.html'. Open it in a browser to view.")
