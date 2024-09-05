from crewai import Task
from agents import analyzer_researcher,health_advisor

Analyzer_searcher_task = Task(
    description='''
    1.Utilize the PDF Processor tool to examine the blood test report located at "D:/wingify_assignment/Blood_Report.pdf" .
    2.Assess the report to pinpoint significant health metrics.
    3.Employ the Web Search tool to gather pertinent health data related to the details in the report.
    4.Create a summary that includes both the analysis of the report and the relevant information obtained from web searches.
    ''',
    agent=analyzer_researcher,
    expected_output="A comprehensive summary of the blood test analysis and relevant health information from web searches."
)

Recommending_Task = Task(
    description='''
    1.Review the analysis and online research performed by the Blood Test Analyzer and Researcher.
    2.Based on the results, give specific health recommendations.
    3.If needed, use the Web Search tool to obtain further information to back up your recommendations.
    4.Offer advice on lifestyle changes, dietary suggestions, relevant health articles, and any necessary medical follow-up.
    5.Compile all recommendations into a well-structured, actionable report for the patient.
    ''',

    agent=health_advisor,
    expected_output="A detailed report with specific health recommendations, lifestyle advice,  dietary suggestions and some links of health articles based on the blood test analysis and research."
)