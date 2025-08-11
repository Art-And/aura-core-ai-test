from docx import Document as DocxDocument
from generals.constants import FileTypes
import io
import json
from pdfplumber import open as pdf_open


class ReadDocumentsService:

    @staticmethod
    def read_pdf(blob_file):
        pdf_bytes = io.BytesIO(blob_file.download_as_bytes())
        with pdf_open(pdf_bytes) as pdf:
            return "\n".join(page.extract_text() for page in pdf.pages)

    @staticmethod
    def read_docx(blob_file):
        with DocxDocument(blob_file.download_as_bytes()) as doc:
            return "\n".join(paragraph.text for paragraph in doc.paragraphs)

    @staticmethod
    def read_json(blob_file):
        return json.dumps(json.load(blob_file), indent=4)

    def get_content_from_file(self, blob_file):
        match blob_file.content_type:
            case FileTypes.PDF.label:
                return self.read_pdf(blob_file)
            case FileTypes.DOCX.label:
                return self.read_docx(blob_file)
            case FileTypes.JSON.label:
                return self.read_json(blob_file)
            case _:
                raise Exception("File type not supported")
