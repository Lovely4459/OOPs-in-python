class Father:
    def __init__(self, father_name, father_age):
        self.father_name = father_name
        self.father_age = father_age

    def father_hii(self):
        print("Father name is", self.father_name)
        print("Father age is", self.father_age) 

class Son(Father):
    def __init__(self, father_name, father_age, son_name, son_age):
        super().__init__(father_name, father_age)
        self.son_name = son_name
        self.son_age = son_age

    def son_hii(self):
        print("Son name is", self.son_name)
        print("Son age is", self.son_age) 


son_obj = Son("Sanjay Sharma",67,"Mohit Sharma",27)
son_obj.father_hii()
son_obj.son_hii()