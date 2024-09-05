
Before you begin, ensure you have met the following requirements:

- You have a Google API key for the Gemini model.
- You have SERPER_API_KEY
- You have Python 3.7+ installed.
- You have a blood test report in PDF format.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Pratyush-12345/Crew_Blood_Report_Agent.git
    ```
2. Make sure you create virtual enviroment for this project

2. Install the required packages:
    ```bash
    pip install -U crewai langchain langchain-community langchain-google-genai duckduckgo-search pypdf
    ```

## Configuration

1. Open the `crew.py` file.

2. Replace `'your_api_key'` with your actual Google API key and serper API KEY:
    os.environ['GOOGLE_API_KEY'] = 'your_actual_google_api_key'
    
     <!-- SerperDevTool(api_key=os.getenv('SERPER_API_KEY')) -->

3. Ensure your blood test report PDF is in the same directory as the script, or update the file path in the ANALYZER_SEARCHER description:
   

## Usage

1. Place your blood test report PDF in the same directory as the script, named `Blood_Report.pdf` (or update the file name in the script).

2. Run the script:
    ```bash
    python crew.py
    ```

3. The script will process the blood test report, analyze it, search for relevant health information, and provide recommendations.

4. The results will be saved in a file named `Health_Analysis_Recommendations.pdf` in the same directory.

## Output

- Relevant health information found from web searches.
- Specific health recommendations based on the analysis.
- Lifestyle advice and dietary suggestions.
- Any necessary medical follow-ups.



