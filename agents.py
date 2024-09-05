from crewai import Agent
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import pdf_tool,web_search_tool

load_dotenv()
os.environ['CREWAI_DISABLE_TELEMETRY'] = 'true'

# Set up your Google API key
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")


# Initialize the Gemini model
gemini = ChatGoogleGenerativeAI(model="gemini-pro")


analyzer_researcher = Agent(
    role='Blood Test Analyzer and Researcher',
    goal='Analyze blood test reports and find relevant health information',
    backstory='You are an expert in interpreting blood test results and conducting medical research.',
    verbose=True,
    allow_delegation=False,
    tools=[pdf_tool, web_search_tool],
    llm=gemini
    
)

health_advisor = Agent(
    role='Health Advisor',
    goal='Provide health recommendations based on blood test results and research',
    backstory='You are an experienced health advisor with a background in nutrition and preventive medicine.',
    verbose=True,
    allow_delegation=False,
    tools=[web_search_tool],
    llm=gemini
)