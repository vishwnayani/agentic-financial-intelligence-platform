from app.rag.ingestion import DocumentIngestion


def main():

    ingestion = DocumentIngestion()

    ingestion.ingest_documents()


if __name__ == "__main__":

    main()