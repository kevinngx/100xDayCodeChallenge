import requests
from datetime import timedelta
from datetime import date

def main():
    stock = "TSLA"
    company_name = "Tesla Inc"
    
    delta = getPerformance(stock)
    print("Price change = " + "{:.2%}".format(delta))

    if (delta > 0.005 or delta < -0.005): # (delta > 0.05 or delta < -0.05)
        getNews(company_name)
        sendText()
    

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def getPerformance(stock):
    print("-- Stock Performance --")
    AV_STOCK_KEY = "GW6E87JA3G9K7LCP"
    AV_ENDPOINT = "https://www.alphavantage.co/query"
    api_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
        "interval": "5min",
        "apikey": AV_STOCK_KEY
    }
    response = requests.get(AV_ENDPOINT, params=api_params)
    response.raise_for_status()
    stock_data = response.json()

    last_refreshed = stock_data["Meta Data"]["3. Last Refreshed"]
    last_date = date.fromisoformat(last_refreshed)
    date_before = last_date - timedelta(days=1)

    day_1_price =  float(stock_data["Time Series (Daily)"][str(last_date)]["4. close"])
    day_2_price =  float(stock_data["Time Series (Daily)"][str(date_before)]["4. close"])
    # print("Price on " + str(last_date) + ": " + str(day_1_price))
    # print("Price on " + str(last_date) + ": " + str(day_2_price))
    return((day_1_price - day_2_price) / day_2_price)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def getNews():
    print("Stock News")

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

def sendText():
    print("Sending Message")

#Optional: Format the SMS message like this:
# 

if __name__ == "__main__":
    main()

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

