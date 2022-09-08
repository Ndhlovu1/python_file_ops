"""
Read() -> file.read() / file.read(40)
    returns every thing or specify the number of contents inside it



ReadLine() -> file.readline() / readline(10)
    returns a single line as a string


ReadLines() -> readlines() , 
    reads everything and returns it as an ordered list list allows iteration and conditional choices

---Absolute Path -> 'user/home/desktop/file.txt'
---Relative Path -> './file.txt'

"""

#Reading a file
#Using with open, it returns a list
with open('test.txt', 'r') as file :
    
    #print(file.read())
    #print()

    #print only the 1st line from the file
    #print(file.readline())
    # print()

    #print all lines will add them all to the list
    # print(file.readlines())
    # print()

    #loop through the information
    data = file.readlines()
    print(data)
    # new_list = []
    # new_list.append(data)
    # print("##################### APPENDED LIST#####################")
    # print(new_list)
    # print(type(new_list))

    # print("##################### AC####################")
    # print(data)
    # #print(type(data))

    # for line in data:
    #     print(line)

    # count = 1 
    # numbered_list = []

    # for item in data:
    #     count = count + 1
    #     if (count % 2) == 0:
    #         numbered_list.append(item)
    #         continue
    #     else:
    #         continue
    # print(numbered_list)
    # print(len(numbered_list))

    # print("############ REVERSED LIST ############")
    # numbered_list.reverse()
    # print(numbered_list)




