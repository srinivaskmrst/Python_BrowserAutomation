import json
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()   # loads .env file

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_form_instructions(row_data: dict) -> dict:
    prompt = f"""
You are a web automation agent.

User data: {row_data}

Return ONLY JSON:
{{
  "tab": "Personal Details",
  "fields": {{
    "first_name": "{row_data.get('FirstName')}",
    "country": "{row_data.get('Country')}",
    "gender": "{row_data.get('Gender')}"
  }}
}}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return json.loads(response.choices[0].message.content)
