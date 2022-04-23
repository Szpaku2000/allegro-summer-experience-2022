
class Repository:

    def __init__(self, name,  languages):
        self.name = name                    # string - repository name
        self.languages = languages          # dictionary (string -> int) - language name and number of bytes that it takes in repository

    def __str__(self):
        return "[ Name: " + self.name + "Languages: " + self.languages + "]"

