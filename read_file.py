import fitz

def extract_text(file):
    document = fitz.open(file)
    extracted_text = ''
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        extracted_text += page.get_text()

    return extracted_text