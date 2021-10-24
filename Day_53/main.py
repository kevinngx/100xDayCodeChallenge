from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import time

FORM_URL = 'https://forms.gle/uSUj3VjWsbi6YGnN7'

# Domain Config
SUBURBS = 'sydney-nsw-2000'
BATHROOMS = '1-any'
BEDROOMS = '1-any'

def main():
    # Use a breakpoint in the code line below to debug your script.
    listings_url = generate_url()
    listings = get_listings(listings_url)
    for listing in listings:
        fill_form(listing['address'], listing['price'], listing['href'])
    # fill_form("99 Test St", str(999), "www.google.com")

def get_listings(listings_url):
    response = requests.get(listings_url)
    soup = BeautifulSoup(response.text, "html.parser")

    all_hrefs = soup.find_all(name="a", class_="address is-two-lines css-1y2bib4")
    all_prices = soup.find_all(name="p", class_="css-mgq8yx")

    print("Printing Address")
    all_listings = soup.find_all(name="span", class_="css-iqrvhs")
    count = 0
    listing_address = []
    for listing in all_listings:
        # print(f'{count}.{listing}')
        if (count % 2  == 0) :
            # Treat for evens
            addr_1 = listing.getText()
        else:
            # Treat for odds
            addr_2_tags = listing.find_all('span')
            city = addr_2_tags[0].text
            state = addr_2_tags[1].text
            postcode = addr_2_tags[2].text
            addr_2 = f'{city} {state} {postcode}'
            # print(f'{round(count/2, 0)}.{addr_1}{addr_2}')
            listing_address.append(f'{addr_1}{addr_2}')
        count += 1

    listings = []
    for i in range(0, len(all_hrefs)):
        listing = {}
        listing['address'] = listing_address[i]
        listing['href'] = all_hrefs[i].get('href')
        listing['price'] = all_prices[i].getText().split('$')[1].split(' ')[0].replace("pw", "")
        listings.append(listing)

    return listings

def generate_url():
    return f'https://www.domain.com.au/rent/?suburb={SUBURBS}&bedrooms={BEDROOMS}&bathrooms={BATHROOMS}&excludedeposittaken=1'

def fill_form(address, rent, link):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", False)

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get(FORM_URL)

    input_fields = driver.find_elements(By.CSS_SELECTOR,'.freebirdFormviewerComponentsQuestionTextRoot .quantumWizTextinputPaperinputMainContent .quantumWizTextinputPaperinputInputArea input')
    time.sleep(2)  # Allows time for the page to load
    input_fields[0].send_keys(address)
    input_fields[1].send_keys(rent)
    input_fields[2].send_keys(link)

    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
