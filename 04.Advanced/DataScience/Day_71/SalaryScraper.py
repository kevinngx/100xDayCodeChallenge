import requests
from bs4 import BeautifulSoup

def get_salary_data():
  # Construct the URL for the Payscale salary search
  url = f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"

  # Send the request to Payscale
  response = requests.get(url)
  
#   print(response.content)

  # Parse the HTML of the salary search results page
  soup = BeautifulSoup(response.text, "html.parser")
  
  # Find the salary data in the page
  salary_data = soup.find_all("tr", {"class": "data-table__row"})

  # Return the salary data
  return salary_data
  
# Example usage
salary_data = get_salary_data()

salary_list = []

for row in salary_data:

    cells = row.findChildren('td')
    row_data = {}

    rank = 'tbc'
    major = 'tbc'
    degree_type = 'tbc' 
    early_career_pay = 'tbc'
    mid_career_pay = 'tbc'
    high_meaning = 'tbc'

    for cell in cells:
        data = cell.find('span', {'class': 'data-table__value'}).string
        if "Rank" in str(cell): row_data['rank'] = data
        if "Major" in str(cell): row_data['major'] = data
        if "Degree Type" in str(cell): row_data['degree_type'] = data
        if "Early Career Pay" in str(cell): row_data['early_career_pay'] = data
        if "Nid-Career Pay" in str(cell): row_data['mid_career_pay'] = data
        if "High Meaning" in str(cell): row_data['high_meaning'] = data

    print(f'row data = {row_data}')
    salary_list.append(row_data)

print(salary_list)
    
