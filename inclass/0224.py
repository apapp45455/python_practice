# class 小括號可有可無
# 類別(設計稿)
class Chair():
    name = "椅子"
    # 初始化
    def __init__(self, c: str) -> None:
        self.color = c 
    
    def seat(self) -> None:
        print(f'{self.color}{self.name}舒服')

    def __str__(self) -> str:
        return f"{self.color}的椅子"
    
    def __eq__(self, other) -> bool:
        return self.color == other.color

a_chair = Chair("red") # 物件
# a_chair.color = "red"
b_chair = Chair("green") # 物件
# b_chair.color = "green"
c_chair = Chair("green")

print(a_chair.color) # red
print(b_chair.color) # green

a_chair.seat() # red舒服
b_chair.seat() # green舒服

print(a_chair) # red的椅子
print(b_chair) # green的椅子

print(a_chair == b_chair) # Flase
print(b_chair == c_chair) # True

# 繼承
class Sofa(Chair):
    name = "沙發"

    def lay(self) -> None:
        print(f'{self.color}{self.name}可以躺ㄟ~')

sofa_a = Sofa("black")
sofa_b = Sofa("white")
sofa_a.seat()
sofa_b.lay()
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

