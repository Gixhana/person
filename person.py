class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, I am {self.name}. I am {self.age} years old and I am {self.gender}.")

# Example usage:
person = Person("Gichana Shadrack", 25, "Male")
person.introduce()