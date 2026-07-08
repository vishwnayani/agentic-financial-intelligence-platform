"""
ingestion.py

Reads all financial documents, extracts metadata,
chunks them and stores them in ChromaDB.
"""

from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

from app.rag.chunking import get_text_splitter
from app.rag.vector_store import get_vector_store


DATA_PATH = Path("data/uploads")


DOCUMENT_TYPES = {
    "annual_report.pdf": "10-K",
    "quarterly_report.pdf": "10-Q"
}


class DocumentIngestion:

    def __init__(self):

        self.text_splitter = get_text_splitter()

        self.vector_store = get_vector_store()

    def ingest_documents(self):

        documents = []

        for company_folder in DATA_PATH.iterdir():

            if not company_folder.is_dir():
                continue

            company = company_folder.name

            print(f"\nProcessing {company}")

            for pdf in company_folder.glob("*.pdf"):

                filename = pdf.name.lower()

                if "annual" in filename:
                    document_type = "10-K"

                elif "quarter" in filename:
                    document_type = "10-Q"

                else:
                    document_type = "Unknown"

                loader = PyPDFLoader(str(pdf))

                pages = loader.load()

                for page_number, page in enumerate(pages, start=1):

                    page.metadata.update(
                        {
                            "company": company,
                            "document_type": document_type,
                            "page": page_number,
                            "source": filename,
                        }
                    )

                    chunks = self.text_splitter.split_documents(
                        [page]
                    )

                    documents.extend(chunks)

        print()

        total_chunks = len(documents)

        print(f"Total Chunks : {total_chunks}")

        BATCH_SIZE = 100

        for i in range(0, total_chunks, BATCH_SIZE):

            batch = documents[i:i + BATCH_SIZE]

            self.vector_store.add_documents(batch)

            print(
                f"Stored {min(i + BATCH_SIZE, total_chunks)} / {total_chunks} chunks"
            )

        print()

        print("Documents successfully stored in ChromaDB.")