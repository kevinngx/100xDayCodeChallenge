import requests
from bs4 import BeautifulSoup
import smtplib, ssl
import os

ITEM_URL = "https://www.amazon.com.au/SanDisk-2TB-Extreme-Portable-SDSSDE60-2T00-G25/dp/B078T9SZ3K/ref=sr_1_7?dchild=1&keywords=ssd+sandisk+extreme&qid=1634693718&sr=8-7"
TARGET_PRICE = 600.00
DEV_EMAIL = os.environ.get("DEV_EMAIL")
DEV_EMAIL_PASSWORD = os.environ.get("DEV_EMAIL_PASSWORD")
SMTP_ADDRESS = "smtp.gmail.com"
TARGET_EMAIL = "kevinngx625@gmail.com"

def main():
    current_price = getItemPrice()
    if (current_price <= TARGET_PRICE):
        sendEmail(current_price)
    else:
        print("LOG | Price does not meet criteria, ending program execution")
    
def sendEmail(current_price):
    message = f'The product you have been tracking has fallen below your target price.\nTarget Price = ${TARGET_PRICE} \nCurrent Price = ${current_price}'
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(DEV_EMAIL, DEV_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=DEV_EMAIL,
            to_addrs=TARGET_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{ITEM_URL}"
        )
    print("LOG | EMAIL SENT")

def getItemPrice():
    request_headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38",
        "Accept-Language":"en-AU,en-GB;q=0.9,en;q=0.8,en-US;q=0.7"
    }
    response = requests.get(ITEM_URL, headers=request_headers)
    
    soup = BeautifulSoup(response.text, "lxml")
    item_price = soup.find(name="span", class_="a-offscreen").get_text().split("$")[1]

    print("LOG | Item price retrieved")
    return float(item_price)
    

def print_to_file(response_text):
    f = open("response.html", "w")
    f.write(response_text)
    f.close()


if __name__ == "__main__":
    main()