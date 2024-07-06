import streamlit as st
from resume_parser import parse_resume
from chatgpt_helper import generate_json_from_text

def main():
    st.title("Resume Parser")

    uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx", "txt"])

    if uploaded_file is not None:
        resume_text = parse_resume(uploaded_file)
        
        if st.button("Parse Resume"):
            with st.spinner("Parsing resume..."):
                try:
                    json_output = generate_json_from_text(resume_text)
                    st.json(json_output)
                except Exception as e:
                    st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()