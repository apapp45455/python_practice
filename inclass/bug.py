import requests

url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=吹風機&page=1&sort=sale/dc"

res = requests.get(url)

print(res.status_code)

res_dict = res.json()

print(res_dict['QTime'])

with open("pchome.txt", "a", encoding="utf-8") as f:
    for prod in res_dict["prods"]:
        print(prod["name"])
        f.write(prod["name"] + "\n")

f.close()