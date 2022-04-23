
def userFromUsername(username):
    #TODO
    pass

def userFromJSON(json):
    #TODO
    pass

class User:

    def __init__(self, login, name, bio, languages):
        self.login = login                  # string - user's login (username)
        self.name = name                    # string - user's first and last name
        self.bio = bio                      # string - user's bio
        self.languages = languages          # dictionary (string -> int) - language name and number of bytes that it takes in repository

    def __str__(self):
        return "[ Login: " + self.login + ", Name: " + self.name + ", Bio: " + self.bio + "Languages: " + self.languages + "]"





