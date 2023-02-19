# 今天要設計一款自動把一個算式算出來的簡易計算機
a = input()

if "+" in a:
    a_sp = a.split("+")
    print(int(a_sp[0]) + int(a_sp[1]))
elif "-" in a:
    a_sp = a.split("-")
    print(int(a_sp[0]) - int(a_sp[1]))
elif "*" in a:
    a_sp = a.split("*")
    print(int(a_sp[0]) * int(a_sp[1]))
else:
    a_sp = a.split("/")
    total = int(a_sp[0]) / int(a_sp[1])
    print("{:.0f}".format(total))
