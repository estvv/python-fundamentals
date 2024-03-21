# Display function
number = 10
print("HelloWorld !")
print("I am", number, "years old !")
print(number)
array = [1, 2, 3]
print(array)

####################################################
print("-------------------------------------------")
####################################################

# Transform a variable type
number = float(number) # Number become 10.0 instead of 10
number = str(number) # Number become "10.0" instead of 10.0

char = "3"
char = int(char) # Char become 3 instead of "3"

####################################################
print("-------------------------------------------")
####################################################

# Get type of variables
print("Number type : ", type(number))
print("Char type : ", type(char))

char = str(char)

print("Char type : ", type(char))

####################################################
print("-------------------------------------------")
####################################################

# Get a number from the user
number = input("Write something : ")
print("You written : ", number)
print("Here is his type : ", type(number))

number = int(input("Write a number : "))
print("You written : ", number)
print("Here is his type : ", type(number))

####################################################
print("-------------------------------------------")
####################################################
