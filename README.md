# 🥘 AI Recipe Assistant

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
```

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
streamlit run app.py
```
---
## 💡 Contributing

We welcome contributions from everyone! Whether it's fixing a bug, improving documentation, or adding a new feature — your help makes this project better.

### 🐛 Reporting Issues
If you discover a bug or have a suggestion, please [open an issue](../../issues) and describe it clearly.

### ✨ Feature Requests
Got an idea to make this project more awesome? Share your thoughts in the issues section and let's discuss!

### 📦 Pull Requests
- Fork the repository
- Create a new branch for your feature/fix
- Commit your changes with a clear message
- Open a Pull Request and describe your changes
