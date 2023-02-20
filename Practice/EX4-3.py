# 讓使用者輸入一個大於等於 2 的正整數後，程式輸出小於或等於該數的「最⼤質數」

i = int(input())
j = 2
while j < i:
    while i % j == 0:
        i -= 1
        j = 2
        continue # 跳過以下階段，回到上一個迴圈
    j += 1
print(i)