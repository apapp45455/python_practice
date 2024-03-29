# ⻄元年份除以4不可整除，為平年。False
# ⻄元年份除以4可整除，且除以100不可整除，為閏年。True
# ⻄元年份除以100可整除，且除以400不可整除，為平年。False
# ⻄元年份除以400可整除，為閏年。True
# 以下為舉例說明:
# 除了不是400的倍數的100的倍數以外，四的倍數的年份均為閏年，閏年這年會多⼀天 (2⽉29
# ⽇)。
# 任何能以 4 整除的年份都是閏年：例如 1980 年、1984 年、1988 年、1992 年及 1996 年都是
# 閏年。
# 不過，仍必須將⼀個⼩錯誤列入考量。⻄曆規定能以 100 (例如1900 年) 整除的年份，同時也要
# 能以 400 整除，才算是閏年。
# 下列年份不是閏年：1700、1800、1900、2100、2200、2300、2500、2600。
# 原因是這些年份能以 100 整除，但無法以 400 整除。
# 下列年份為閏年：1600、2000、2400。
# 閏年，請輸出「a leap year」，否則請輸出「a normal year」
a = int(input())

if a % 4 != 0:
    print("a normal year")
elif a % 4 == 0 and a % 100 != 0:
    print("a leap year")
elif a % 100 == 0 and a % 400 != 0:
    print("a normal year")
elif a % 400 == 0:
    print("a leap year")
else:
    print("a normal year")