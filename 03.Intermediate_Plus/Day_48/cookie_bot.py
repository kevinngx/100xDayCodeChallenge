from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

TARGET_URL = "https://orteil.dashnet.org/experiments/cookie"

def main():
    # This section adds the option to keep the browser open until manually closed
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get(TARGET_URL)

    # Cookie
    cookie = driver.find_element(By.CSS_SELECTOR, '#cookie')

    # Items
    items = driver.find_elements(By.CSS_SELECTOR, "#store div")
    item_ids = []
    for item in items:
        print(item.text)
        item_ids.append(item.get_attribute("id"))


    timeout = time.time() + 2
    while True:
        cookie.click()
        #  Every 5  seconds
        if time.time() > timeout:

            # Get Store items & prices
            store_items = driver.find_elements(By.CSS_SELECTOR, '#store b')
            prices = []
            # names = []
            # store = {}
            for item in store_items:
                if item.text !="":
                    prices.append(item.text.split(" - ")[1].replace(",", ""))
                    # names.append(item.text.split(" - ")[0])
            print("Prices: ")
            print(prices)

            # for x in range(0, len(prices)):
            #     store[x] = {}
            #     store[x]['Item'] = names[x]
            #     store[x]['Price'] = prices[x]
            # print(store)

            # Create a dictionary of store  items and prices
            cookie_upgrades = {}
            for n in range(len(prices)):
                cookie_upgrades[prices[n]] = item_ids[n]
            print("Cookie Upgrades:  ")
            print(cookie_upgrades)

            # Check Balance
            current_balance = int(driver.find_element(By.ID, "money").text.replace(",", ""))
            print(f'Current Balance = {current_balance}')

            # Buy any affordable item
            for cost in cookie_upgrades:
                if int(cost) < int(current_balance):
                    print(f"Purchasing upgrade {cookie_upgrades[cost]} at Cost:{cost}")
                    current_balance -= int(cost)
                    driver.find_element(By.ID, cookie_upgrades[cost]).click()
                    print(f"Purchase completed, new balance = {current_balance}")
                    break

            # From top down
            timeout += 1


if __name__ == "__main__":
    main()