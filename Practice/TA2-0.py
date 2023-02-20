# 請使用while迴圈，印出指定數字的跌代加總。
# 例如題目是5
# 必須輸出從1開始加到5的答案15
# 1+2+3+4+5=15
a = int(input())
b = 0
c = 1
d = 0
e = 0

while b <= a-1:
    d = c + b
    b += 1
    e = e + d
print(e)