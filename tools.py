from langchain.tools import BaseTool
from langchain_community.document_loaders import PyPDFLoader
from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv

load_dotenv()
class PDFProcessorTool(BaseTool):
    name = "PDF Processor"
    description = "Process a PDF file and extract its content"

    def _run(self, file_path: str) -> str:
        try:
            loader = PyPDFLoader(file_path)
            pages = loader.load_and_split()
            return "\n".join(page.page_content for page in pages)
        except Exception as e:
            return f"Error processing PDF: {str(e)}"

    async def _arun(self, file_path: str) -> str:
        return self._run(file_path)

pdf_tool = PDFProcessorTool()

web_search_tool = SerperDevTool(api_key=os.getenv('SERPER_API_KEY'))
