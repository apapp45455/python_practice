# 輸入為一組西元年，請根據以上規則判斷是否為閏年，若為閏年請回傳True，否則False
a = int(input())

if a % 4 != 0:
    print(False)
elif a % 4 == 0 and a % 100 != 0:
    print(True)
elif a % 100 == 0 and a % 400 != 0:
    print(False)
elif a % 400 == 0:
    print(True)
else:
    print(False)