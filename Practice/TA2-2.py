# 輸入為一串數字，每個數字間以一個空白隔開，
# 數字長度不固定，請把這些數字每個各加1後輸出

# input: 1 2 3 4 5
# output: 2 3 4 5 6

a = input()
a_sp = a.split()
i = 0
c = []
while i <= len(a_sp)-1:
    c.append(str(int(a_sp[i]) + 1))
    i += 1
print(" ".join(c))

# # 另解
# import sys

# in_txt = sys.stdin.read()

# in_list = in_txt.split()

# ans = ""

# i = 0
# while i < len(in_list):
#     ans += str(int(in_list[i]) + 1) + ' '
#     i += 1

# print(ans.strip())
