from pypdf import PdfReader
from os_path_scripts import PROJECT_ROOT_PATH, resources
import os


def test_pdf():
    pdf_path = os.path.join(PROJECT_ROOT_PATH, resources, 'docs-pytest-org-en-latest.pdf')
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)

    assert number_of_pages == 412
