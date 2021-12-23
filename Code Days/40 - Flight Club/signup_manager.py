import requests

ENDPOINT = "SHEETY ENDPOINT"
AUTH_CODE = "AUTH CODE"

class SignupManager:

    def __init__(self) -> None:
        self.endpoint = ENDPOINT
        self.header = {
            "Authorization": AUTH_CODE
        }
        self.firstName = ""
        self.lastName = ""
        self.emailAddress = ""


    def addToList(self):
        if self.emailAddress != "":
            entry = {"user": {
                "firstName": self.firstName,
                "lastName": self.lastName,
                "email": self.emailAddress
            }}
            response = requests.post(self.endpoint, headers=self.header, json=entry)
            response.raise_for_status()
            print("Success! You've been added to the list, look forward to your new adventures!")


    def requestUserDetails(self):
        self.firstName = input("What is your first name?\n")
        self.lastName = input("What is your surname?\n")
        emailFirst = input("What is your email?\n")
        emailSecond = input("Type your email again:\n")
        if emailFirst == emailSecond:
            self.emailAddress = emailFirst
            self.addToList()
        else:
            print("Emails don't match.")

    def getUserDetailsToList(self):
        response = requests.get(self.endpoint, headers=self.header)
        response.raise_for_status()
        data = response.json()
        return data["users"]

    

    

    