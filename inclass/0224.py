# # class 小括號可有可無
# # 類別(設計稿)
# class Chair():
#     name = "椅子"
#     # 初始化
#     def __init__(self, c: str) -> None:
#         self.color = c 
    
#     def seat(self) -> None:
#         print(f'{self.color}{self.name}舒服')

#     def __str__(self) -> str:
#         return f"{self.color}的椅子"
    
#     def __eq__(self, other) -> bool:
#         return self.color == other.color

# a_chair = Chair("red") # 物件
# # a_chair.color = "red"
# b_chair = Chair("green") # 物件
# # b_chair.color = "green"
# c_chair = Chair("green")

# print(a_chair.color) # red
# print(b_chair.color) # green

# a_chair.seat() # red舒服
# b_chair.seat() # green舒服

# print(a_chair) # red的椅子
# print(b_chair) # green的椅子

# print(a_chair == b_chair) # Flase
# print(b_chair == c_chair) # True

# # 繼承
# class Sofa(Chair):
#     name = "沙發"

#     def lay(self) -> None:
#         print(f'{self.color}{self.name}可以躺ㄟ~')
    
#     def seat(self) -> None:
#         super().seat() # 呼叫所繼承的父類別
#         print("zzz")

# sofa_a = Sofa("black")
# sofa_b = Sofa("white")
# sofa_a.seat()
# sofa_b.lay()

# # 機器人練習
# class Robot:
#     def __init__(self, x: int, y: int, actions: str) -> None:
#         self.x = x
#         self.y = y
#         for action in actions:
#             if action == "U":
#                 self.up()
#             elif action == "D":
#                 self.down()
#             elif action == "L":
#                 self.left()
#             else:
#                 self.right()

#     def up(self) -> None:
#         self.y += 1
    
#     def down(self) -> None:
#         self.y -= 1

#     def left(self) -> None:
#         self.x -= 1

#     def right(self) -> None:
#         self.x += 1
    
#     def __str__(self) -> str:
#         return f"{self.x},{self.y}"

# print(Robot(0, 0, "UDLR"))

# # 讀取資料庫
# class BasedCRUD:
#     data = list(range(1, 51))

#     def read_data(self) -> list[int]:
#         return self.data

# class EvenCRUD(BasedCRUD):
#     def read_data(self) -> list[int]:
#         raw_data = super().read_data()
#         return list(filter(lambda x: x % 2 == 0, raw_data))

# print(EvenCRUD().read_data())

# import my_module as mm
# a = mm.A()
# a.hello()


# # I/O 處理
# f = open('file.txt', 'r')
# print(f.read())

# f.close()

# # 覆寫
# f = open('file.txt', 'w', encoding='utf-8')
# f.write('哈囉你好嗎')
# f.close()

# # append
# f = open('file.txt', 'a', encoding='utf-8')
# f.write('，衷心感謝')
# f.close()

# with open ('file.txt', 'w', encoding='utf-8') as f:
#     f.write('Who lives in pineapple under the sea?')

# try:
#     print(1111/0)
# except:
#     print("Error")

# try:
#     pwd = input("請輸入您的密碼: ")
#     if len(pwd)<8:
#         raise Exception("密碼長度不足")
#     if len(pwd)>16:
#         raise Exception("密碼長度太長")
# except Exception as e:
#     print("密碼長度檢查異常: " + str(e))