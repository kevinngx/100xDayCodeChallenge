from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

DEV_EMAIL = os.environ.get("DEV_EMAIL")
DEV_EMAIL_PASSWORD = os.environ.get("DEV_EMAIL_PASSWORD")

TARGET_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

def main():
    # This section adds the option to keep the browser open until manually closed
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get(TARGET_URL)

    # Step 1 = Sign in
    driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]').click()
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(DEV_EMAIL)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(DEV_EMAIL_PASSWORD)
    driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()

    jobs = driver.find_elements(By.CSS_SELECTOR, '.jobs-search-results__list-item')
    print(jobs)
    for job in jobs:
        print(job.text)
        job.click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '.job-view-layout .jobs-save-button').click()
        print("Job Saved")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
