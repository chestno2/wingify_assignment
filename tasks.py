from crewai import Task
from agents import analyzer_researcher,health_advisor

Analyzer_searcher_task = Task(
    description='''
    1. Use the PDF Processor tool to read the blood test report at " D:/wingify_assignment/Blood_Report.pdf"  .
    2. Analyze the report and identify key health indicators.
    3. Use the Web Search tool to find relevant health information based on the report's contents.
    4. Compile a summary of the findings and relevant web information.
    ''',
    agent=analyzer_researcher,
    expected_output="A comprehensive summary of the blood test analysis and relevant health information from web searches."
)

Recommending_Task = Task(
    description='''
    1. Review the analysis and web research provided by the Blood Test Analyzer and Researcher.
    2. Based on this information, provide specific health recommendations.
    3. If needed, use the Web Search tool to find additional information for your recommendations.
    4. Include lifestyle advice, dietary suggestions, some links of health article and any necessary medical follow-ups.
    5. Compile all recommendations  into a clear,  actionable report for the patient.
    ''',
    agent=health_advisor,
    expected_output="A detailed report with specific health recommendations, lifestyle advice,  dietary suggestions and some links of health articles based on the blood test analysis and research."
)