try: # Something that might cause an exception
    file = open("aFile.txt")
    aDictionary = {"key": "value"}
    print(aDictionary["key"])
except FileNotFoundError: # Do this if there was an exception
    file = open("aFile.txt", "w")
    file.write("Something")
except KeyError as errorMessage:
    content = file.read()
    print(content)
# else: # Do this if there were NO exceptions
finally: # Do this no matter what happens
    file.close()
    print("Flie was closed.")