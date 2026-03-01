class vector1:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"The 2dvector is {self.i}i + {self.j}j")
        
      
class vector2(vector1):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k=k
    def show(self):
        print(f"The 3d vector is {self.i}i +  {self.j}j + {self.k}k")

i=int(input("Enter i:"))
j=int(input("Enter j:"))
k=int(input("Enter k:"))
    
v1=vector1(i,k)
v2=vector2(i,j,k)
v2.show()
v1.show()
