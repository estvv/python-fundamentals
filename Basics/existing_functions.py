# Display function
number = 10
print("Salut !")
print("J'ai",number,"ans !")
print(number)

# Transform a variable type
number = float(number) # Number become 10.0 instead of 10
number = str(number) # Number become "10.0" instead of 10.0

char = "3"
char = int(char) # Char become 3 instead of "3"

# Get type of variables
print("Number type : ", type(number))
print("Char type : ", type(char))

char = str(char)

print("Char type : ", type(char))

# Get a number from the user
number = input("Écris quelque chose : ")
print("Voici ce que tu as écris : ", number)
print("Ainsi que son type : ", type(number))

number = int(input("Donne un nombre : "))
print("Voici ce que tu as écris : ", number)
print("Ainsi que son type : ", type(number))

