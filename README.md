# Lok Sabha Election Data Analysis

## Project Description

This project involves scraping data from the recently concluded Lok Sabha election results from the Election Commission of India's website. The objective is to analyze the data and derive key insights. The project uses BeautifulSoup for web scraping and PySpark for data processing and analysis.

## Prerequisites

To run this project, you will need the following:

- Python 3.x
- PySpark
- BeautifulSoup
- Pandas

## Installation

1. **Clone the Repository**:

    ```sh
    git clone https://github.com/yourusername/lok-sabha-election-analysis.git
    cd lok-sabha-election-analysis
    ```

2. **Set up a virtual environment** (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the scraping script**:

    ```sh
    python scraping-script.py
    ```

    This script will fetch the data from the specified URL and save it as a CSV file (`election_results.csv`).

2. **Run the analysis script**:

    ```sh
    python analyze_data.py
    ```

    This script will use PySpark to process the data and generate the report with key insights.

## Methodology

### Data Scraping

The data scraping is done using BeautifulSoup. The script fetches the webpage content, parses the HTML to locate the relevant table, and extracts the required columns (Constituency and State).

### Data Analysis

The analysis is performed using PySpark. The key steps involved are:

1. **Loading the Data**: The scraped data is loaded into a Spark DataFrame.
2. **Data Cleaning**: Any necessary data cleaning steps are performed.
3. **Deriving Insights**: Various transformations and actions are applied to derive key insights from the data.

### Insights

The report generated includes the following key insights:

1. **Top performing party by total votes**.
2. **Candidate with the largest margin of victory**.
3. **Average margin by party**.
4. **Constituency with the smallest margin**.
5. **Top candidates by total votes**.
6. **Competitive constituencies (margin < 50000)**.
7. **Party strongholds by average margin**.
8. **No of seats won by each party**.
9. **Voting Efficiency**.

## Contributors

- Your Name - [@Bavisettisivaavinash](https://github.com/Bavisettisivaavinash)
