import sys
a = sys.stdin.read() #系統會抓資料，測試要自行改數值

j = 1
for i in a.splitlines():
    print(i + str(j))
    j += 1