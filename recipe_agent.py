from tools import extract_ingredients_from_image, extract_ingredients_from_text, generate_recipe

class RecipeAgent:
    def __init__(self):
        self.ingredients = None

    def run(self, input_type: str, input_data: str) -> str:
        """
        Agent workflow:
        1. Extract ingredients
        2. Check sufficiency
        3. Generate recipe (+ suggest extra ingredients if needed)
        """
        # Step 1: Extract ingredients
        if input_type == "image":
            self.ingredients = extract_ingredients_from_image(input_data)
        elif input_type == "text":
            self.ingredients = extract_ingredients_from_text(input_data)
        else:
            return "❌ Invalid input type."

        # Step 2: Generate recipe (handles insufficiency inside LLM prompt)
        recipe = generate_recipe(self.ingredients)

        return f"### 🥕 Extracted Ingredients:\n{self.ingredients}\n\n### 🍲 Suggested Recipe:\n{recipe}"
