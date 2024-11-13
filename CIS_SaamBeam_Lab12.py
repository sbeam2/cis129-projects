# Saam Beam
# November 12 2024
# CIS Lab 12


class Pet():

    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

    def setName(self, name):
        self.name = name

    def setType(self, type):
        self.type = type

    def setAge(self, age):
        self.age = age

    def returnName(self):
        return self.name

    def returnType(self):
        return self.type

    def returnAge(self):
        return self.age

# list to store pet in a different way in order to print it later in an easy to read form
petList = []

# input asking the user if they would like to make their first/new pet
startScript = input("Would you like to make a new pet? ")


if startScript in ["y", "yes", "Y", "Yes", "YES", "ye", "Ye", "YE"]:
    pickName = input("What is your pets name? ")
    pickType = input("What type of pet do you have? ")
    pickAge = input("How old is your pet? (In years) ")
    yourPet = Pet(pickName, pickType, pickAge)
    print("Your pets name is", yourPet.returnName() + ".", "The type of pet you have is a(n)", yourPet.returnType() + ".", "Your pet is", yourPet.returnAge(), "years old")
    petList.append([yourPet.returnName(), yourPet.returnType(), yourPet.returnAge()])
    print(petList)
else:
    print("Come back when you're ready")