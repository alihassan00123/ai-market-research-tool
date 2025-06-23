import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_text_with_gpt(text):
    prompt = f"""
You are an intelligent assistant that reads messy, mixed news content and organizes it into clean, well-labeled sections.

1. Read the raw text.
2. Identify important events, countries, or topics.
3. Categorize into sections like:
   - 📰 Politics & Diplomacy
   - ⚔️ Military & Conflict
   - 🧬 Science & Technology
   - 🌍 Global Affairs
   - ⚠️ Disasters & Accidents
   - 🧑‍🤝‍🧑 Society & Human Rights
   - 💬 Public Opinion & Protests

Use markdown formatting with:
- Clear headers (##)
- Bullet points
- Short summaries for each category

Make the output structured and easy to read.

News text:
\"\"\"{text[:3000]}\"\"\"
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"
