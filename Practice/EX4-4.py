# 機器人行走一步的指令包括 U、D、L、R 的 4 種內容（均為半型字），
# 分別代表機器人向上一步（U）, 向下一步（D）, 向左一步（L）, 向右一步（R）。
# 請判斷機器人走完輸入字串中的所有指令後，是否會正好回到出發點？
a = input()
a_sp = list(a)
u_count = a.count("U")
d_count = a.count("D")
l_count = a.count("L")
r_count = a.count("R")
if u_count == d_count and l_count == r_count:
    b = "Y"
else:
    b = "N"
print(b)