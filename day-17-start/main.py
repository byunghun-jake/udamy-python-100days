class User:
    # Constructor
    def __init__(self, user_id, user_name, follower=0, following=0):
        print("new user being created...")
        self.id = user_id
        self.username = user_name
        self.followers = follower
        self.following = following

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "김병훈")
user_2 = User("002", "남경빈")

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)
