# 🥘 AI Recipe Assistant (Agentic AI)

This project is an **Agentic AI system** built with LangGraph and OpenAI that takes an **image of ingredients**, extracts them using AI, and suggests possible recipes.  
If the provided ingredients are not sufficient, the agent recommends **additional ingredients** to complete the recipe.  

---

## 🚀 Features
- Upload an **image of ingredients**.
- Agent extracts ingredients from the image using OpenAI Vision API.
- Suggests a **recipe** based on available ingredients.
- If ingredients are insufficient, agent recommends **additional ingredients**.
- Built with **LangGraph** for agent orchestration.

---

## 🛠️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/abdulsamad183/cooking_agent.git
cd cooking_agent


### 2️⃣ Create a Virtual Environment (optional but recommended)
```bash
python -m venv env
source env/bin/activate   # On Linux/Mac
env\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up OpenAI API Key
Create a .env file in the project root directory and add your OpenAI API key:
```bash
OPENAI_API_KEY=your_api_key_here
```

### 5️⃣ Run the Application
```bash
python app.py
```

---
