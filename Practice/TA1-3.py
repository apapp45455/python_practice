# 輸入會有三個值，第一個值是星期幾，第二個值是股票的單價，第三個值是今日成交總量，
# 每個值之間用一個空白隔開，假設此股票在星期五、六、日是不開市的，所以如果是在這幾天，請回傳"不開市"
a = input()
a_sp = a.split()
day = a_sp[0]
price = []
price.append(int(a_sp[1]))
price.append(int(a_sp[2]))

if day == "星期五" or day == "星期六" or day == "星期日":
    print("不開市")
else:
    print(price[0] * price[1])