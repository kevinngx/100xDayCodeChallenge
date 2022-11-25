import requests
from datetime import timedelta
from datetime import date
import os

def main():
    stock = "TSLA"
    company_name = "Tesla"
    
    delta = getPerformance(stock)
    print("Price change = " + "{:.2%}".format(delta))

    if (delta > 0.005 or delta < -0.005): # (delta > 0.05 or delta < -0.05)
        recent_news = getNews(company_name)
        sendText(recent_news)
    

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def getPerformance(stock):
    print("-- Stock Performance --")
    os.environ["AV_STOCK_KEY"] = "GW6E87JA3G9K7LCP"
    AV_STOCK_KEY = os.environ.get('AV_STOCK_KEY')
    AV_ENDPOINT = "https://www.alphavantage.co/query"
    #print(AV_STOCK_KEY)
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
    return((day_1_price - day_2_price) / day_2_price)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def getNews(company_name):
    print("-- Stock News --")
    os.environ["NEWS_API_KEY"] = "8418834c55b74e61b04355d0291cacb7"
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    NEWS_API_ENDPOINT = "https://newsapi.org/v2/top-headlines"
    api_params = {
        "q": company_name,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(NEWS_API_ENDPOINT, params=api_params).json()
    return response['articles'][0]["title"]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

def sendText():
    pass

if __name__ == "__main__":
    main()

