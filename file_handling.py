
"""
Python has two file hand

open() ¬ close()

open 
    read
    write
    create

    Accepts 2 Arguments
        open(filename/file location , <MODE i.e. read(r -> text format / rb - binary,
                                                 r+ -> reading and writing), 
                                                 write(w) , 
                                                 create (a -> edit/append date )
                                                 ))

                                                

close
    no args

    to close often open a file with() the , automatically closes the file
        with open ('test.txt', 'r' as file) :


opening a file with binary format
    file handling -> text

    open(<FILE_NAME>, r)

    open(<FILE_NAME>, r+)

    open(<FILE_NAME>, W)

    open(<FILE_NAME>, a)        
    
    ----- ALL DEFAULT FORMAT FOR THESE IS TEXT BUT BINARY IS BETTER FOR PERFORMANCE-----
    *********TO SET IT TO OPEN WITH BINARY pass b together with the mode**************

    open(<FILE_NAME>, r)b

    open(<FILE_NAME>, rb+)

    open(<FILE_NAME>, Wb)

    open(<FILE_NAME>, ab)        
    

"""

#File handling

# #declare file
# file = open('test.txt', mode='r')


# #read file
# #Read line only opens a single line whereas read opens it as an array with multiple lines
# data = file.readline()
# d2 = file.read()

# print(data,"\n",d2)

#below is better for exception handling

with open('test.txt', mode='r') as file:
    data = file.readline()
    print(data)


