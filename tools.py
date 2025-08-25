import base64
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

def extract_ingredients_from_image(image_path: str) -> str:
    """Extracts ingredients list from an image."""
    with open(image_path, "rb") as f:
        image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

    messages = [
        {"role": "system", "content": "You are an expert chef. Extract visible ingredients clearly from the image."},
        {"role": "user", "content": [
            {"type": "text", "text": "Extract all ingredients visible in this image."},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}}
        ]}
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=400
    )
    return response.choices[0].message.content.strip()


def extract_ingredients_from_text(user_text: str) -> str:
    """Extracts ingredients from raw text input."""
    return user_text.strip()


def generate_recipe(ingredients: str) -> str:
    """Generate recipe and suggest extra ingredients if needed."""
    messages = [
        {"role": "system", "content": (
            "You are a master chef. Use the given ingredients to suggest a recipe. "
            "If ingredients are insufficient, recommend extra ingredients. "
            "Finally, write a clear step-by-step recipe."
        )},
        {"role": "user", "content": f"My ingredients: {ingredients}"}
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=600
    )
    return response.choices[0].message.content.strip()
