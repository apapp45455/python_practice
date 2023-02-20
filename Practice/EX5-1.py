# 在輸入字串中，有些英文字母僅出現一次，也有些出現多次。
# 你的程式會保留所有在輸入字串中僅出現一次的字母，
# 但對於多次出現的字母將只保留「最後一個」，其他相同者均捨棄。
# 你保留下來的字母之先後順序應與原字串的順序相同。

#ABACDEAD -> BCEAD

a = input()
a_list = list(a)
i = []
for i in a_list:
    while a_list.count(i) != 1:
        a_list.remove(i)
print("".join(a_list))