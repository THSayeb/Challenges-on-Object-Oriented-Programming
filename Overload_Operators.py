class A:
    def __init__(self, a):
        self.a = a
    
    def __lt__(self,other):
        if self.a < other.a:
            return("The first value of a is bigger")
        else:
            return("The second value of a is bigger")
    
    def __eq__(self, other):
        if self.a == other.a:
            return("Both are equal")

obj1 = A(45)
obj2 = A(56)
print("The values are : ", obj1.a, obj2.a)
print(obj1<obj2)

obj3 = A(89)
obj4 = A(89)
print(f"The values are : {obj3.a}, {obj4.a}")
print(obj3==obj4)