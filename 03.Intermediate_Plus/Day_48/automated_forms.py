from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

TARGET_URL = "https://en.wikipedia.org/wiki/Main_Page"

def main():

    # This section adds the option to keep the browser open until manually closed
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get(TARGET_URL)

    # Method 1
    # element = driver.find_element(By.CSS_SELECTOR, '#articlecount  a')
    # element.click()

    # Method 2
    # element = driver.find_element(By.LINK_TEXT, 'All portals')
    # element.click()

    # Searching
    search = driver.find_element(By.NAME, 'search')
    search.send_keys('Python')
    search.send_keys(Keys.ENTER)

if __name__ == "__main__":
    main()