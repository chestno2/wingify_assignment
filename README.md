
Before you begin, ensure you have met the following requirements:

- You have a Google API key for the Gemini model.
- You have SERPER_API_KEY
- You have Python 3.7+ installed.
- You have a blood test report in PDF format.

## Installation
1. Clone the Repo
2. Make sure you create virtual enviroment for this project
   python -m venv venv

2. Install the required packages:
    In requirements.txt

## Configuration

1. Open the `crew.py` file.

2. Replace `'your_api_key'` with your actual Google API key and serper API KEY:
   
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



