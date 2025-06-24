import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Learning Path Planner", page_icon="📘")
st.title("📘 AI Learning Path Planner")
st.markdown("Use AI to generate a custom weekly learning roadmap.")

# Get the Gemini API key securely
api_key = st.secrets.get("GEMINI_API_KEY", "")

if not api_key:
    st.error("🚫 No API key found. Please set your Gemini API key in Streamlit secrets.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

# UI form
with st.form("learning_path_form"):
    subject = st.text_input("🎯 What topic do you want to learn?", value="Machine Learning")
    duration = st.slider("🗓️ Duration (in weeks)", 1, 12, 4)
    interests = st.text_area("✨ Learning preferences or goals?", value="Hands-on projects, real-world examples, beginner-friendly")
    submit = st.form_submit_button("Generate Learning Plan")

if submit:
    with st.spinner("Generating your plan with AI..."):
        prompt = f"""
        Create a unique {duration}-week learning path for the topic: {subject}.
        The learner's goals or preferences include: {interests}.
        
        Each week's plan should include:
        - Core Concepts: Key topics to focus on that week.
        - Practice: Hands-on exercises, projects, or coding tasks.
        - Resources: Recommended videos, tutorials, or articles.
        - Reflection: What to revise or journal about at the end of the week.
        
        Ensure each week builds on the last, gradually increasing in difficulty.
        Format the response in a structured weekly layout.
        """
        response = model.generate_content(prompt)
        st.subheader("📅 Your Personalized Learning Path")
        st.markdown(response.text)
