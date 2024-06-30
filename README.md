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
    python scrape_data.py
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

1. **Total number of constituencies analyzed**.
2. **Top 5 states with the highest number of constituencies**.
3. **Distribution of constituencies across states**.
4. **Party-wise distribution in each state**.
5. **Winning margins in key constituencies**.
6. **Voter turnout in top constituencies**.
7. **Gender distribution of elected members**.
8. **Age distribution of elected members**.
9. **Educational qualifications of elected members**.
10. **Incumbency vs. new faces in the election**.

## Results

The results of the analysis are saved in the `results` directory as a CSV file and a detailed report in PDF format.

## Contributors

- Your Name - [@yourusername](https://github.com/yourusername)
- Additional Contributors

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
