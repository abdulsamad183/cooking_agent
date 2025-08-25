import streamlit as st
from recipe_agent import RecipeAgent

st.set_page_config(page_title="🍳 Agentic Recipe Assistant", layout="centered")

st.title("🤖🍳 Agentic Recipe Assistant")
st.write("An AI Agent that extracts ingredients (image/text), checks sufficiency, and generates recipes.")

uploaded_file = st.file_uploader("📷 Upload an image of ingredients", type=["jpg", "jpeg", "png"])
user_text = st.text_area("✍️ Or type your ingredients (comma separated)", "")

if st.button("Run Agent"):
    agent = RecipeAgent()

    if uploaded_file:
        with open("temp.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())
        output = agent.run("image", "temp.jpg")
        st.markdown(output)

    elif user_text.strip():
        output = agent.run("text", user_text)
        st.markdown(output)

    else:
        st.warning("⚠️ Please upload an image or enter ingredients.")
