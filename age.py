name=input(str("Please enter your name:"))
#str limits user input to be of type string
#input is keyword that prompts the user to enter a value from the keyboard
age=int(input("Please enter your age:"))
#int limits user inpout to be of type integer
def SayYear(age):
    returnYear=100-age+2022
    return returnYear
print("Hello", name, ", You will turn 100 years in the year", SayYear(40))

#pip command is used to install packages in python programming