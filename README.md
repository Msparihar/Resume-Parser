# Resume Parser

This application uses Streamlit and ChatGPT to parse resumes and convert them into JSON format.

## Setup

1. Clone the repository

2. Install the required packages:

```python
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

4. Run the Streamlit app:

```
streamlit run app.py
```

## Usage

1. Upload a resume file (PDF, DOCX, or TXT format)
2. Click on "Parse Resume"
3. The parsed JSON output will be displayed

## Note

This application uses the OpenAI API, which may incur costs. Please be aware of your usage and any associated fees.
