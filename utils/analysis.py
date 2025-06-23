import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_text_with_gpt(text):
    prompt = f"Provide a concise market research analysis for the following content:\n\n{text[:3000]}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"
