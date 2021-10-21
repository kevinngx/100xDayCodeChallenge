from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

TARGET_URL = "https://en.wikipedia.org/wiki/Main_Page"

def main():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get(TARGET_URL)

    element = driver.find_element(By.CSS_SELECTOR, '#articlecount  a')
    article_count = element.text
    print(f'Article Count = {article_count}')
    driver.close()

if __name__ == "__main__":
    main()