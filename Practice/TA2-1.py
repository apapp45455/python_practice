# 請使用while迴圈，印出指定數乘法表

i = 0
a = input()
a_sp = a.split()
b1 = int(a_sp[0])
b2 = int(a_sp[1])
result_1 = int(b1/b1)
result_2 = int(b2/b2)


while i < b2*b1:
    print(result_1,"x",result_2,"=", result_1*result_2, sep="")
    if result_2 < b2:
        result_2 += 1
    elif result_2 == b2:
        result_2 = 1
        result_1 += 1
    i += 1

# 比較好的解法：
# import sys

# in_txt = sys.stdin.read()

# in1, in2 = in_txt.split()
# in1 = int(in1)
# in2 = int(in2)

# i = 0
# while i < in1:
#     j = 0
#     while j < in2:
#         print(f'{i+1}x{j+1}={(i+1)*(j+1)}')
#         j += 1
#     i += 1