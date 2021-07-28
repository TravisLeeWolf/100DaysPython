#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

startingLetterLines = []

with open(".\Input\Letters\starting_letter.txt") as startingLetter:
    startingLetterLines = startingLetter.readlines()

with open(r".\Input\Names\invited_names.txt") as invitedNames:
    invitedNamesData = invitedNames.readlines()
    invitedNamesList = []
    for name in invitedNamesData: 
        invitedNamesList.append(name.rstrip())

for name in invitedNamesList:
    finalLetterText = startingLetterLines[0].replace("[name]", name)
    with open(f".\Output\ReadyToSend\letter_to_{name}.txt", mode="w") as outputLetter:
        for i in range(1, len(startingLetterLines)):
            finalLetterText += startingLetterLines[i]
        outputLetter.write(finalLetterText)

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp