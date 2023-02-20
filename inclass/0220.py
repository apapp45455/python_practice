# # Truthy and Falsy
# a = "dddd"
# if a:
#     print("hi")

# # while 迴圈
# # 1. 初始條件
# i = 0
# # 2. 判斷條件(是否要繼續跑)
# while i < 3:
#   print(f'hi, {2*i+1}')
#   # 3. 更新條件
#   i += 1

# # 迭代 iterate
# a = ['A','B','C','D','E']

# i = 0
# while i <= len(a)-1:
#     print(a[i])
#     i += 1

# # sep 更改間隔字元
# print("A","B","C", sep = "-")

# i = 0
# while i < len(a):
#     print(a[i], end = "")
#     i += 1

# # 以字串形式將list中的各項連結
# a = ['A','B','C','D','E']
# print('-'.join(a))

# # 雙重迴圈
# i = 1
# while i < 4:
#     k = 1
#     while k < 4:
#         print(f'{i}*{k}={i*k}')
#         k += 1
#     i += 1

# # break 結束整個迴圈
# i = 0
# while i < 5:
#     print(i)
#     if i == 2:
#         break
#     i += 1
# # continue 直接進入下一圈
# i = 0
# while i < 5:
#     if i == 2:
#         i += 1
#         continue
#     print(i)
#     i += 1

# i = 1
# while i < 4:
#     j = 1
#     while j < 4:
#         if j == i:
#             j += 1
#             continue
#         print(f"{i}*{j}={i*j}")
#         j += 1
#     i += 1

# # for 迴圈
# aa = ['A','B','C']
# # i = 0
# # while i < len(aa):
# #     print(aa[i])
# #     i += 1
# for i in aa:
#     print(i)
# print(list(range(0,10)))
# for i in range(0,10):
#     print(i)

# # enumerate
# aa = ['A','B','C']
# for i, a in enumerate(aa, start = 100):
#     print(i, a)

# # DOMjudge 固定用法 ctrl + d 結束
# import sys
# q = sys.stdin.read()
# 或
# q = """this is ok
# hi """