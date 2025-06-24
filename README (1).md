# Gemini AI Learning Path Planner (Streamlit)

This is a simple AI-powered learning planner built using Streamlit and Google Gemini (via `google-generativeai`).

## 🌐 Live Usage

Deploy this app on [Streamlit Cloud](https://streamlit.io/cloud) and add your Gemini API key in the **Secrets Manager**.

## 🛠 Requirements

- Python 3.10+
- Streamlit
- Google Generative AI (`google-generativeai`)

## 📦 How to Run Locally

1. Clone the repo
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Add your Gemini API key to `.streamlit/secrets.toml`:
```
GEMINI_API_KEY = "your-key-here"
```
4. Run:
```
streamlit run learning_path_planner_app.py
```
