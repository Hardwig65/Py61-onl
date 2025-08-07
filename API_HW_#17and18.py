import requests

coin_id = 'bitcoin'
url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"

headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": "CG-LZLYTpfReraNvXY2hb8qX1fE"
}
response = requests.get(url, headers=headers)

# Используя requests вывести информацию об каком-то одном instance.


# print(response.json())


# Проанализируйте ваше API. Например: извлеките определенные данные из ответа ( получите заголовки новостей из JSON-ответа и вывести их на экран).
if response.status_code == 200:
    data = response.json()
    print(data.get("market_cap_rank"),
          data.get("name"),
          data.get("symbol"),
          data.get("market_data").get("current_price").get('usd'), sep='        ')
else:
    print("Ошибка   =>  ", response.status_code)

# Получить данные из API, отсортировав их по какому-либо признаку. Например, если вы используете API для получения новостей покажите только новости определенной категории или из определенного источника.

# url = f"https://api.coingecko.com/api/v3/coins/list"
#
# response = requests.get(url, headers=headers)
# data = response.json()
# sorted_coins = sorted(data, key=lambda coin: coin['name'])
# print(sorted_coins)
