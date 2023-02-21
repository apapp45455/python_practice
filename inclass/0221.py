# aa = [1,2,3,4]
# for i, a in enumerate(aa):
#     print(a)
#     aa[i] = 100
# print(aa)

# i = 0
# while i < len(aa):
#     a = aa[i]
#     print(a)
#     i += 1

# # 串列生成式
# str_list = ['1', '2', '3'] 
# # 1. 先寫個for in
# for s in str_list:
# # 2. 把每一圈的獨立變數拿出來
# s
# # 3. 組合!
# [s for s in str_list]
# # 4. 調整需求
# print([int(s) for s in str_list])
# 等於下面程式
# a = []
# for s in str_list:
#     a.append(int(s) + 1)
# print(a)
# print("".join([str(int(s)) for s in input().split()]))

# 字典 dictionary  在其他地方稱作json
# 使用{}建立
# police = {
#     "name": "秋山麗子", 
#     "height": 161, 
#     "is_rich": True
# }
# print(police["name"]
# get 當值不存在，預設回傳None，可設定回傳值
# print(police.get("zzz", "get"))

# # 新增key
# police["money"] = 10
# print(police)
# print(type(police))

# # 更新
# police["name"] = "兩津勘吉"
# print(police)

# # 刪除
# del police["is_rich"]
# print(police)

# # 查詢
# print(police.keys())
# print(police.values())
# print(police.items())

# # 僅能判斷keys，不能判斷values
# if "height" in police:
#     print(True)

# # 可判斷values
# if 161 in police.values():
#     print(True)

# # **展開所有字典
# # 若key一樣，則回傳最後的value值
# a = {"key": 100}
# b = {"key": 300}
# c = {**a,**b}
# print(c)

# # *展開所有的清單
# a = [1,2,3]
# b = [4,5,6]
# c = [*a,*b]
# print(c)
# a = [1,2,3,4]
# print(*a,sep = "~")

# taoyuan = {
#     "名稱":"桃園",
#     "人口":100_000,
#     "是否為直轄市":"是"
# }
# taipei = {
#     "名稱":"台北",
#     "人口":300_000,
#     "是否為直轄市":"是"
# }
# miaoli = {
#     "名稱":"苗栗",
#     "人口":50_000,
#     "是否為直轄市":"否"
# }
# taiwan = [taoyuan, taipei, miaoli]
# # print(taiwan[0].get("名稱")) #提出台灣第一個地區的"名稱"
# # print(taiwan[0]["名稱"])

# tokyo = {
#     "名稱":"東京",
#     "人口":1_000_000,
#     "是否為直轄市":"是"
# }
# osaka = {
#     " 名稱":"大阪",
#     "人口":300_000,
#     "是否為直轄市":"是"
# }
# japan = [tokyo, osaka]

# earth = {"japan" : japan,
#          "taiwan" : taiwan
# }
# print(earth["japan"][1]["人口"])

# # 用字典計算字元數量
# dict = {

# }
# b = list("abcacba")
# for i in b: 
#     if i not in dict:
#         dict[i] = 1
#     else:
#         dict[i] += 1
# print(dict)

# # 利用Counter計算文字數量
# from collections import Counter
# print(Counter(input("輸入一串文字")))

# # 函式
# def tool(x: str = "*", y: int = 20) -> str:
#     """我會回傳箭頭"""
#     for i in range(0,y):
#         print(f"{i*x}")
#     for i in range(y,0,-1):
#         print(f"{i*x}")

#     return f"字元, {x}"

# # map(fn,iterable)
# # Callable 使物件可被呼叫
# # List items型態為list
# from typing import Callable, List
# def my_map(fn: Callable, items: List):
#     rtn = []
#     for item in items:
#         rtn.append(fn(item))
#     return rtn

# a = [1, 2, 3, 4, 5]
# print(my_map(str, a))

# # filter(iterable)
# a = [1, 2, 3, 4, 5]
# from typing import Iterable
# def my_filter(items: Iterable, num = int):
#     rtn = []
#     for i in items:
#         if i != num:
#             rtn.append(i)
#     return rtn
# print(my_filter(a, 3))

# # fn: Callable 可呼叫其他函式運算
# from typing import Callable, List
# def my_filter(fn: Callable, items: List) -> List:
#     rtn = []
#     for item in items:
#         if fn(item) == True:
#             rtn.append(item)
#     return rtn
# def is_over_three(n: int) -> bool:
#     return n > 3
# a = [1, 2, 3, 4, 5]
# print(my_filter(is_over_three, a))

# # lambda 直接return n<3
# print(my_filter(lambda n: n<3, a))