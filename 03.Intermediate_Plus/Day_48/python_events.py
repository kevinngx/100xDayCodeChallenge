from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

TARGET_URL = "https://www.python.org/"

def main():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get(TARGET_URL)

    title_elements = driver.find_elements(By.CSS_SELECTOR, '.event-widget .shrubbery .menu a')
    date_elements = driver.find_elements(By.CSS_SELECTOR, '.event-widget .shrubbery .menu time')

    #  I used min here to avoid any array out of bounds exceptions in case there are fewer events or dates picked up
    python_events = {}
    for x in range(0, min(len(title_elements), len(date_elements))):
        python_events[x] = {}
        python_events[x]['Time'] = date_elements[x].text
        python_events[x]['Name'] = title_elements[x].text

    print(python_events)
    driver.close()

if __name__ == "__main__":
    main()