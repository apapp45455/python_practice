import requests

url = "https://dummyjson.com/products"

res = requests.get(url)

print(res.status_code)

res_dict = res.json()

with open("dummy.txt", "a", encoding="utf-8") as f:
    for prod in res_dict["products"]:
        print(prod["title"])
        f.write(prod["title"] + "\n")

f.close()