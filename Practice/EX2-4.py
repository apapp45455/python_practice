# 輸入為三個由空白隔開的整數。印出最大值
a = input()
b = a.split()
b_ss = map(int, b) # 將list內的字串逐一轉成數值
print(max(b_ss))

# # 另解
# a = input()
# b = a.split()
# a1 = int(b[0])
# a2 = int(b[1])
# a3 = int(b[2])
# print(int(max(a1, a2, a3)))