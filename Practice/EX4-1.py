# 反轉句子中的單字

i = 0
n = []
a = input()
a_sp = a.split()
while i <= len(a_sp) -1:
    b = a_sp[i]
    i += 1
    n.append(b[::-1])
print(" ".join(n))