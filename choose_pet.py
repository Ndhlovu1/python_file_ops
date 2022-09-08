#Import the petnames
import random as rn

f = open("petnames.txt", "r")

f_content = f.read()
#Split everywhere with a new line
f_content = f_content.split("\n")

print(f_content)

print(type(f_content))

#The choice function acces any sequence parameter
print("######################RANDOM NAME######################")
print(rn.choice(f_content))

#To accept via user input

# import random
# f_name = input('Type the file name: ')
# f = open(f_name) # "r" omitted as it's the default
# f_content = f.read()
# f_content_list = f_content.split("\n")
# print(random.choice(f_content_list))
