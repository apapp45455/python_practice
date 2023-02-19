# 請你寫一個程式，給你一個整數n>0輸出1，n=0輸出0，n<0輸出-1

a = int(input())

if a > 0:
    print("1")
elif a == 0:
    print("0")
else:
    print("-1")