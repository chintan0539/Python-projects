import requests
import os
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY='98J08T3DV78YIZFY'
NEWS_API_KEY='02c9919209064399a7de11fc3b4145bd'

account_sid = 'AC6f8d019d05c76a24871a4753f2b34999'
auth_token = '2e32cc9c765280232d824448241b042a'
client = Client(account_sid, auth_token)



stock_parameters={
'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'outputsize':'compact',
    'apikey':STOCK_API_KEY
}
news_parameters={
    'qInTitle':COMPANY_NAME,
    'apiKey':NEWS_API_KEY
}

# ********************************************************CODE**********************************************************************************
stock_response=requests.get(STOCK_ENDPOINT,params=stock_parameters)
stock_response.raise_for_status()
stock_info=list(stock_response.json()['Time Series (Daily)'].items())[:3]
yesterday_closing=float(stock_info[1][1]['4. close'])
day_before_closing=float(stock_info[2][1]['4. close'])
stock_difference=abs(yesterday_closing-day_before_closing)

stock_percentage=(stock_difference/yesterday_closing)*100
status=""
if yesterday_closing>day_before_closing:
    status="HIGH"
else:
    status="LOW"




if stock_percentage>5:
    news_response = requests.get(NEWS_ENDPOINT, news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()['articles'][:3]

    for article in articles:
        message = client.messages \
            .create(
            body=f"TSLA: {round(stock_percentage,2)} {status} \nHeadline: {article['title']} Brief: {article['description']}.",
            from_='+12023357029',
            to='+917769938811'
        )

        print(message.status)





