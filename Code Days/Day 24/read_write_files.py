# with open("myText.txt") as myFile:
#     contents = myFile.read()
#     print(contents)

# with open("myText.txt", mode="w") as myFile:
#     myFile.write("This overwrites the content of the file.")

# with open("myText.txt", mode="a") as myFile:
#     myFile.write("\nThis text has been appended to this file.")

with open("newText.txt", mode="w") as myFile:
    myFile.write("In the write mode if the file doesn't exist a new file will be created.")