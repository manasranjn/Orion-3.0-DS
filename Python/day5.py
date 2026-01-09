age = 10

# Simple If
# if(age >18):
#     print("You can vote")


# if-else
# if(age >18):
#     print("You can vote")
# else:
#     print("You can't Vote")

# elif
# if(age<=10):
#     print("You are a kid")
# elif(age<18):
#     print('You are young')
# elif(age<50):
#     print('You are adult')
# elif(age>50):
#     print('You are senior citizen')


time = 200
# if(time>0 and time <12):
#     print("Good Morning")
# elif(time== 12):
#     print("Good Noon")
# elif(time>12 and time<18):
#     print("Good afternoon")
# elif(time>18 and time<22):
#     print("Good evening")
# elif(time>=22 and time<=24):
#     print("Good evening")
# else:
#     print("Invalid time")

# Program to check if a character is an alphabet, digit, or special character

char = input("Enter any character: ")

if char.isalpha():
    print("The character is an alphabet.")
elif char.isdigit():
    print("The character is a digit.")
else:
    print("The character is a special character.")