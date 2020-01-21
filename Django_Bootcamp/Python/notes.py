class Dog():

    # Class Object Attributes
    species = "mammal"

    # Special Initialization method
    def __init__(self,name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed
        self.age = 0

    # New bark method
    def bark(self):
        print(self.name+" just barked!")

myDog = Dog("Anakin","black","Shiba Inu")
print("My name is " + myDog.name + " and I am a " +  myDog.color +" "+ myDog.breed)
myDog.bark()
