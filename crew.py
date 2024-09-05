from crewai import Crew, Process
from agents import analyzer_researcher,health_advisor
from tasks import Analyzer_searcher_task , Recommending_Task
from fpdf import FPDF
from dotenv import load_dotenv

load_dotenv()



# Print out loaded environment variables for debugging

crew = Crew(
    agents=[analyzer_researcher, health_advisor],
    tasks=[Analyzer_searcher_task,Recommending_Task],
    verbose=True,
    process=Process.sequential
)

# Execute the crew's tasks
result = crew.kickoff()


# Assuming result is a tuple or list, convert it to a string
if isinstance(result, (tuple, list)):
    result_text = "\n".join(str(item) for item in result)
else:
    result_text = str(result)  # If it's a single string, just convert it

# Create a PDF of the result using FPDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Add a title
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, txt="Blood Test Analysis and Health Recommendations", ln=True, align='C')

# Add the result content
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, result_text)  # Use the formatted result text


output_pdf_path = "D:/wingify_assignment/Health_Analysis_Recommendations.pdf"
pdf.output(output_pdf_path)

print(f"PDF generated and saved at {output_pdf_path}")


