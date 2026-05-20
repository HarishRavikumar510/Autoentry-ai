import fitz
import re


def extract_text_from_pdf(uploaded_file):

    pdf_bytes = uploaded_file.read()

    doc = fitz.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    text = ""

    for page in doc:

        text += page.get_text()

    return text


def extract_fields_from_text(text):

    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    phone_pattern = r"\b[6-9]\d{9}\b"

    emails = re.findall(email_pattern, text)

    phones = re.findall(phone_pattern, text)

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    name = lines[0] if lines else ""

    return {

        "Name": name,

        "Email": emails[0] if emails else "",

        "Phone": phones[0] if phones else "",

        "Extracted Text": text[:500]
    }