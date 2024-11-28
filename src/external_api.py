import os
from dotenv import load_dotenv
import requests

load_dotenv('.env')

API_KEY = os.getenv('API_KEY')

url = "https://api.apilayer.com/exchangerates_data/convert?to=EUR&from=USD&amount=1500"

headers= {
  "apikey": API_KEY
}

response = requests.get(url, headers=headers)

status_code = response.status_code
result = response.text

print(result)