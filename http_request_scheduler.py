import schedule
import time
import requests

def perform_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        print(f"Ответ от {url}: {response.status_code}")
    except requests.exceptions.HTTPError as http_err:
        print(f"Произошла ошибка  в ссылке(HTTP): {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Произошла ошибка: {req_err}")

def main():
    url = 'https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT'  
    lay = 5  
    interval = 10 

    schedule.every(lay).seconds.do(lambda: schedule.every(interval).seconds.do(perform_request, url))

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()