import pypdf
import docx2txt

def parse_resume(file):
    file_extension = file.name.split('.')[-1].lower()
    
    if file_extension == 'pdf':
        return parse_pdf(file)
    elif file_extension == 'docx':
        return parse_docx(file)
    elif file_extension == 'txt':
        return parse_txt(file)
    else:
        raise ValueError("Unsupported file format")

def parse_pdf(file):
    pdf_reader = pypdf.PdfReader(file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
      page = pdf_reader.pages[page_num]
      text +="\n"+ page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False,layout_mode_strip_rotated=False)
    return text

def parse_docx(file):
    text = docx2txt.process(file)
    return text

def parse_txt(file):
    return file.read().decode('utf-8')