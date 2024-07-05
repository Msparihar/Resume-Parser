from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_json_from_text(text):
    prompt = f"""
    Parse the following resume text into a JSON format:

    {text}

    The JSON should include fields such as:
    - Personal Information (name, email, phone)
    - Summary
    - Work Experience (company, position, dates, responsibilities)
    - Education (degree, institution, graduation date)
    - Skills

    Provide the output in valid JSON format. And dont include ```json in the response.
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that parses resumes into JSON format."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content 