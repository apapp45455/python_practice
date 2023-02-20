# 使用者會輸入一個大於或等於1的整數，按照數字輸出用星號畫出圖案
a = int(input())
i = 1
while i < a + 1:
    print("*" * i)
    i += 1