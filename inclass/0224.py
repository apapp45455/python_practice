# class 小括號可有可無
# 類別(設計稿)
class Chair():
    # 初始化
    def __init__(self, c: str) -> None:
        self.color = c 
    
    def seat(self) -> None:
        print(f'{self.color}舒服')

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