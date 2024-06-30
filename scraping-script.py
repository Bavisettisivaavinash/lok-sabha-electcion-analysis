import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of URLs to scrape
urls = [
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-369.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-742.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1680.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-140.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-582.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1745.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-805.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3369.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3620.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3529.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3165.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1888.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1420.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-547.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-772.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-852.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-860.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-545.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-804.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1847.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-544.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1458.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-834.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1998.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-83.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-664.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-911.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1534.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1142.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3388.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2757.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1584.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2484.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3482.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1658.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1046.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2989.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2070.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-160.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-118.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-743.htm'
]

all_data = []

# Loop through each URL
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the party information from span inside h2 tags
        party_tag = soup.find('h2').find('span')
        party = party_tag.text.strip() if party_tag else 'Unknown Party'
        
        # Extract the party name from the span text
        if party.startswith("Winning Candidate (") and party.endswith(")"):
            party = party[len("Winning Candidate ("):-1].strip()
        
        # Find the table
        table = soup.find('table', {'class': 'table table-striped table-bordered'})
        if table:
            for row in table.find_all('tr')[1:]:  # Skip the header row
                cols = row.find_all('td')
                if len(cols) > 0:
                    won = cols[1].text.strip()  # Assuming the first column is the number of seats won
                    candidate = cols[2].text.strip()  # Third column is the candidate's name
                    leading = cols[3].text.strip()
                    total = cols[4].text.strip()
                    all_data.append([party, candidate, won, leading, total])
        else:
            print(f"Table not found on {url}")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Convert to DataFrame and save to CSV
df = pd.DataFrame(all_data, columns=['Party', 'Candidate', 'Constituency', 'Total Votes', 'Margin'])
df.to_csv('lok_sabha_results.csv', index=False)

print("Data scraped and saved to lok_sabha_results.csv")
