first_number = 10
second_number = 10

# is the name as :

first_number, second_number = 10, 10

def add(first, second):
    addition = first + second
    return addition

print("Addition : ", add(first_number, second_number))

####################################################
print("-------------------------------------------")
####################################################

char = "Hello World"

print("Avant : ", char)

def modif(args):
    args = "Bye !"
    return args

char = modif(char)
print("Après : ", char)