class User:
    
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

user_1 = User("001", "Bob")
user_2 = User("002", "Mary")

print(user_1.id)
print(user_2.followers)
