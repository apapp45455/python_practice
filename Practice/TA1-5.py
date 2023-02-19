# 今天要設計一款能夠自動判斷身分證是否合法的程式，身分證的判斷是有既定的公式的
a = input()
c = 0
d = int(a[1]) * 8 + int(a[2]) * 7 + int(a[3]) * 6 + int(a[4]) * 5 + int(a[5]) * 4 +int(a[6]) * 3 + int(a[7]) * 2 + int(a[8]) * 1 + int(a[9]) * 1
if a[0] == "A":
    c = 1 + 0 * 9
    total = (c + d) % 10
elif a[0] == "B":
    c = 1 + 1 * 9
    total = (c + d) % 10
elif a[0] == "C":
    c = 1 + 2 * 9
    total = (c + d) % 10
elif a[0] == "D":
    c = 1 + 3 * 9
    total = (c + d) % 10
elif a[0] == "E":
    c = 1 + 4 * 9
    total = (c + d) % 10
elif a[0] == "F":
    c = 1 + 5 * 9
    total = (c + d) % 10
elif a[0] == "G":
    c = 1 + 6 * 9
    total = (c + d) % 10
elif a[0] == "H":
    c = 1 + 7 * 9
    total = (c + d) % 10
elif a[0] == "I":
    c = 3 + 4 * 9
    total = (c + d) % 10
elif a[0] == "J":
    c = 1 + 8 * 9
    total = (c + d) % 10
elif a[0] == "K":
    c = 1 + 9 * 9
    total = (c + d) % 10
elif a[0] == "L":
    c = 2 + 0 * 9
    total = (c + d) % 10
elif a[0] == "M":
    c = 2 + 1 * 9
    total = (c + d) % 10
elif a[0] == "N":
    c = 2 + 2 * 9
    total = (c + d) % 10
elif a[0] == "O":
    c = 3 + 5 * 9
    total = (c + d) % 10
elif a[0] == "P":
    c = 2 + 3 * 9
    total = (c + d) % 10
elif a[0] == "Q":
    c = 2 + 4 * 9
    total = (c + d) % 10
elif a[0] == "R":
    c = 2 + 5 * 9
    total = (c + d) % 10
elif a[0] == "S":
    c = 2 + 6 * 9
    total = (c + d) % 10
elif a[0] == "T":
    c = 2 + 7 * 9
    total = (c + d) % 10
elif a[0] == "U":
    c = 2 + 8 * 9
    total = (c + d) % 10
elif a[0] == "V":
    c = 2 + 9 * 9
    total = (c + d) % 10
elif a[0] == "W":
    c = 3 + 2 * 9
    total = (c + d) % 10
elif a[0] == "X":
    c = 3 + 0 * 9
    total = (c + d) % 10
elif a[0] == "Y":
    c = 3 + 1 * 9
    total = (c + d) % 10
elif a[0] == "Z":
    c = 3 + 3 * 9
    total = (c + d) % 10

if total == 0:
    print("合法")
else:
    print("不合法")