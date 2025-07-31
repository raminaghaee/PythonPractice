


class person():
    name = "Ramin"
    age = 30
    gender = "male"
    score = 100

Ramin = person()
print(Ramin.name)
print(Ramin.age)
print(Ramin.gender)

Zahra = person()
Zahra.name = "Zahra"
print(Zahra.name)
print(Zahra.age)


class Person1():
    def __init__(self, name, age, gender,score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def NameAndAge(self):
        return self.name, self.age

somi = Person1("somi",35,"female",100)
print(somi.name)
print(somi.age)
print(somi.NameAndAge())


class Person2():
    def __init__(self, age, weight, height , cr , gender):
        self.age = age
        self.weight = weight
        self.height = height
        self.cr = cr
        self.gender = gender
    def bmi(self):
        return self.weight / ((self.height /100 )**2)
    def gfr(self):
        if self.gender == "male":
            return ((140 - self.age) * self.weight) / (72 * self.cr)
        elif self.gender == "female":
            return (((140 - self.age) * self.weight) /(72 * self.cr)) * 0.85
        else:
             print("please check gender")
