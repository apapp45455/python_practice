# # 換行 \n
# print("hhhh\nfffff")
# # 換行 """ '''
# print("""fffff
# dddd""")

# # len 計算字串長度
# a = "dddddddd"
# print(len(a))

# # split 分開
# str1 = '1 2 3 4 5'
# print(str1.split()) # ['1', '2', '3', '4', '5']
# str2 = '1,2,3,4,5'
# print(str2.split(',')) # ['1', '2', '3', '4', '5']

# # splitlines
# str1 = """1
# 2
# 3
# 4
# 5"""
# print(str1.splitlines())

# # 顯示至小數點後兩位
# a = 3.1425926
# print("{:.2f}".format(a))
# b = 100
# print("{:.2f}".format(b))

# # 顯示分隔符號
# a = 100000000
# print("{:,}".format(a))
# b = 100_000_000
# print("{:,}".format(b))

# # list 建立，內容盡量為同一型態
# empty_list = []
# weekdays = ['Monday', 'Tuesday', 'Wednesday']
# years = [2000, 2001, 2002, 2003]

# # 索引值 index
# #            0         1          2
# weekdays = ['Monday', 'Tuesday', 'Wednesday']
# print(weekdays[0]) # Monday

# # slice 尾數不包含
# str1 = '1234567'
# print(str1[0]) # 1
# print(str1[0:3]) # 123
# print(str1[3:-1]) # 4567
# print(str1[0:len(str1)]) # 1234567
# print(str1[0:]) # 1234567
# print(str1[:]) # 1234567
# print(str1[::2]) # 1357 從頭開始間隔2取值
# print(str1[::-1]) # 7654321

# # append 加入
# a = []
# a.append("A")
# print(a)
# a.append(["B"])
# print(a)

# # del[] 刪除特定位置
# num_list = [1, 2, 3, 4, 5, 6]
# del num_list[2] # 刪除第2個位置的值
# print(num_list) # [1, 2, 4, 5, 6]

# # remove 刪除特定值
# num_list = [1, 2, 2, 3, 4, 5, 6]
# num_list.remove(2) # 刪除1個2
# print(num_list) # [1, 2, 3, 4, 5, 6]

# # in
# num_list = [6, 5, 4, 3, 2, 1]
# print(2 in num_list) # True
# print(11 in num_list) # False

# # sort 排序
# num_list = [1, 2, 3, 4, 5, 6, 7, 2, 3, 5, 2]
# s_list = sorted(num_list)
# print(num_list.sort())  # None 
# print(sorted(num_list))  # [1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 7]
# print(sorted(num_list, reverse=True)) # [7, 6, 5, 5, 4, 3, 3, 2, 2, 2, 1]
# print(s_list)
# # sorted() 會回傳list, sort() 不會回傳

# # len list長度
# num_list = [1, 2, 3, 4, 5, 6, 7, 2, 3, 5, 2]
# print(len(num_list))  # 11

# # split 切字
# str1 = '1 2 3 4 5'
# print(str1.split()) # ['1', '2', '3', '4', '5']
# str2 = '1,2,3,4,5'
# print(str2.split(',')) # ['1', '2', '3', '4', '5']

# # strip 去空白
# str1 = '    Hello     '
# print(str1.strip()) # Hello

# # count 算字串次數
# str1 = 'This is a apple'
# print(str1.count('is')) # 2

# # zfill() 在字串前面加上0(幾位數)
# str1 = '99'
# print(str1.zfill(5)) # 00099

# # if (最上層最嚴格)
# # if 條件:
#     # 做事情1
# # elif:
#     # 做事情2
# # else:
#     # 做事情3
# buy_count = 10
# see_suika = True # 是否看到西瓜
# if see_suika:
#     buy_count = 1
# print(f'買{buy_count}個包子')

# # 如果年紀大於18，顯示歡迎光臨
# # 如果年紀小於18，但是money大於10000也顯示歡迎光臨
# # 否則顯示謝謝惠顧
# age = 10
# money = 22222
# if age > 18:
#     print("歡迎光臨")
# elif money > 10000:
#     print("歡迎光臨")
# else:
#     print("謝謝惠顧")

# if age >= 18:
#     print("歡迎光臨")
# else:
#     if money > 10000:
#         print("歡迎光臨")
#     else:
#         print("謝謝惠顧")

# # 背後是數字的比較
# # 1. 是不是平手
# # 2. 你是不是贏了
# # 3. 電腦贏了
# import random
# key_word = ['剪刀', '石頭', '布']
# user = int(input('[0]剪刀, [1]石頭, [2]布:'))
# rand_num = random.randint(0, 2)
# print('你出了: ', key_word[user])
# print('電腦出了: ', key_word[rand_num])
# if user == rand_num:
#     print("dual")
# elif user == (rand_num + 1) % 3:
#     print("you win")
# else:
#     print("you lose")