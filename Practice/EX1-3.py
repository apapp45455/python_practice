# 電腦課要同學分組做期末報告，分組的方式為依座號順序，每 3 個人一組。如1, 2, 3 為第一組，4, 5, 6 為第二組….以此類推。輸入同學的座號，請判斷他在哪一組。
import math

a = int(input())
b = math.ceil(a / 3)
print(b)