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
police = {
    "name": "秋山麗子", 
    "height": 161, 
    "is_rich": True
}
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

# 刪除
del police["is_rich"]
print(police)