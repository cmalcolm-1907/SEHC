def Create_user():
    user = {"name": "trial", "age": 20}
    return user


def Check_User(user):
    for item in user:
        print(f"{item}: {user[item]}")


user = Create_user

Check_User(user)
