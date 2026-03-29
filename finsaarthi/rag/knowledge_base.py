import os
from pathlib import Path
from typing import List, Optional

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_core.documents import Document

class FinSaarthiKnowledgeBase:
    def __init__(self, persist_directory: str = "finsaarthi/rag/chromadb"):
        self.persist_directory = persist_directory
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=200
        )
        self.vectordb = None
        self._initialize_vectordb()

    def _initialize_vectordb(self):
        """Initialize or load the vector database."""
        if os.path.exists(self.persist_directory):
            self.vectordb = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embeddings
            )
        else:
            # Create an empty vector store if it doesn't exist
            self.vectordb = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embeddings
            )

    def add_documents_from_folder(self, folder_path: str):
        """Load and index all PDFs from a specified folder."""
        loader = DirectoryLoader(folder_path, glob="**/*.pdf", loader_cls=PyPDFLoader)
        docs = loader.load()
        chunks = self.text_splitter.split_documents(docs)
        
        if chunks:
            self.vectordb.add_documents(chunks)
            print(f"Successfully indexed {len(chunks)} chunks from {folder_path}.")
        else:
            print("No documents found to index.")

    def add_text_content(self, text: str, metadata: dict = None):
        """Add raw text content to the knowledge base."""
        doc = Document(page_content=text, metadata=metadata or {})
        chunks = self.text_splitter.split_documents([doc])
        self.vectordb.add_documents(chunks)
        print(f"Added {len(chunks)} text chunks to knowledge base.")

    def query(self, query: str, k: int = 4) -> List[Document]:
        """Query the knowledge base for relevant documents."""
        if not self.vectordb:
            return []
        return self.vectordb.similarity_search(query, k=k)

# Example Usage
if __name__ == "__main__":
    kb = FinSaarthiKnowledgeBase()
    # Initial context seeding (Handled by ingestion script later)
    # kb.add_text_content("The Old Tax Regime 2024-25 has slabs of 5%, 20%, and 30%.", {"source": "manual"})
    # results = kb.query("What are the tax slabs?")
    # for res in results:
    #     print(res.page_content)
