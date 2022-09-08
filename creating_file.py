#trapping exceptions

try:
    #Creating a new file 
    #enable write mode

    with open('new_file.txt', 'w') as file:
    #file.write("W must score ove 90")
    #Writing multiple line, which accepts a list, each comma represents a new line starting
    #Each time you run this it'll replace all your old text
    #Below is a list
        text_to_add = ['This is another line',\
                '\nAbove we must not that we are replacing each line',\
                '\nThis is another line\n']
        file.writelines(text_to_add)

except FileNotFoundError as e:
    print("Error :",e)

except Exception as e:
    print("Something went wrong :", e)


