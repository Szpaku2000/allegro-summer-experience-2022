import requests

def repositoryFromName(username, repoName):
    url = 'https://api.github.com/repos/'
    url = url + username + '/' + repoName
    req = requests.get(url)
    dictionary = req.json()
    lang_url = url + '/languages'
    languages = requests.get(lang_url).json()

    return Repository(dictionary["name"], languages)


class Repository:

    def __init__(self, name,  languages):
        self.name = name                    # string - repository name
        self.languages = languages          # dictionary (string -> int) - language name and number of bytes that it takes in repository

    def __str__(self):
        return "[ Name: " + self.name + "Languages: " + self.languages + "]"

