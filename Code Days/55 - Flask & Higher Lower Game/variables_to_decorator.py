
class User:
    def __init__(self, name) -> None:
        self.name = name
        self.isLoggedIn = False

def isAuthenticatedDecorator(function):
    def wrapper(*args, **kwargs):
        if args[0].isLoggedIn == True:
            function(args[0])
        else:
            print(f"You're not logged in.")
    return wrapper

@isAuthenticatedDecorator
def createBlogPost(user):
    print(f"This is {user.name}'s new blog post.")

newUser = User("Bob")
newUser.isLoggedIn = True
createBlogPost(newUser)
