# 起始條件，第一個數字為0，第二個數字為1，後面的數字為前面兩個數字的相加
# 0 1 1 2 3 5 8 13 21 …
first = 0
second = 1

a = int(input())
if a == 1:
    print(first)
elif a == 2:
    print(second)
else:
    i = 0
    while i < a - 2:
        first, second = second, first + second
        i += 1
    print(second)