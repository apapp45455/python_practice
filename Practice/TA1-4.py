# 今天要設計一款能夠自動對獎的大樂透對獎程式，請試著想想看該如何完成!
# 假設此樂透只可以選5個號碼，號碼介於1~20，只有再對中三個號碼以上時才算中獎，對中三個號碼即可得獎金100元，4個號碼獎金1000元，5個號碼獎金10000元
a = input()
a = a.split(",")
a_sp1 = a[0].split()
a_sp2 = a[1].split()

bingo = 0
if a_sp1[0] in a_sp2:
    bingo += 1
if a_sp1[1] in a_sp2:
    bingo += 1
if a_sp1[2] in a_sp2:
    bingo += 1
if a_sp1[3] in a_sp2:
    bingo += 1
if a_sp1[4] in a_sp2:
    bingo += 1

if bingo == 3:
    print("100")
elif bingo == 4:
    print("1000")
elif bingo == 5:
    print("10000")
else:
    print("0")