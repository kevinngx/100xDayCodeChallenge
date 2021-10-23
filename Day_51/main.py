from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

SPEED_TEST_URL = 'https://www.speedtest.net/'
TWITTER_URL = 'https://twitter.com/login?lang=en-gb'

DEV_TWITTER_USERNAME = 'kevinngx_dev'
DEV_EMAIL_PASSWORD = os.environ.get("DEV_EMAIL_PASSWORD")

def main():
    internet_speed = get_internet_speed()
    if internet_speed < 100:
        tweet_at_provider(internet_speed)

def tweet_at_provider(internet_speed):

    message = f'Hey @Optus, why am I paying $60 a month for 100mb/s download when my download speed is only {internet_speed}mb/s?'

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get(TWITTER_URL)

    time.sleep(2)
    driver.find_element(By.XPATH, "//input[contains(@name,'username')]").send_keys(DEV_TWITTER_USERNAME)
    driver.find_element(By.XPATH, "//input[contains(@name,'password')]").send_keys(DEV_EMAIL_PASSWORD)
    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span').click()

    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys(message)
    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()

    print("Login successful")

def get_internet_speed():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get(SPEED_TEST_URL)

    # Get Speed test
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
    time.sleep(40)
    download_speed = driver.find_element(By.XPATH,
                                         '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    upload_speed = driver.find_element(By.XPATH,
                                       '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    print(f'Download Speed = {download_speed}\nUpload Speed  = {upload_speed}')

    return float(download_speed)

if __name__ == '__main__':
    main()
