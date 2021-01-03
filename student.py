class Family:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    @classmethod
    def mand_kinder(self):
        if self.age >= 3:
            return True
        else:
            return False
