import requests
from Repository import Repository


def createRepoList(username):
    userURL = 'https://api.github.com/users/' + str(username) + '/repos'
    repoURL = 'https://api.github.com/repos/'
    repositories = requests.get(userURL)
    json = repositories.json()
    repoList = []
    for repository in json:
        new_url = repoURL + username + '/' + str(repository["name"]) + '/languages'
        languages = requests.get(new_url).json()
        next_repo = Repository(repository["name"], languages)
        repoList.append(next_repo)
    return repoList


def createLangDict(repoList):
    languages = {}

    for repository in repoList:
        for key in repository.languages:
            if key in languages:
                languages[key] += repository.languages[key]
            else:
                languages[key] = repository.languages[key]

    return languages


def userFromUsername(username):
    url = 'https://api.github.com/users/'
    url = url + username
    req = requests.get(url).json()
    login = req["login"]
    name = req["name"]
    bio = req["bio"]
    repositoryList = createRepoList(login)
    languages = createLangDict(repositoryList)

    return User(login, name, bio, repositoryList, languages)


class User:

    def __init__(self, login, name, bio, repoList, langs):
        self.login = login  # string - user's login (username)
        self.name = name  # string - user's first and last name
        self.bio = bio  # string - user's bio
        self.repositoryList = repoList  # Repository[] - list of repositories of a user, it is useful in when creating languages for a user
        self.languages = langs  # dictionary (string -> int) - language name and number of bytes that it takes in repository

    def __str__(self):
        if self.login is None:
            self.login = 'NULL'
        if self.name is None:
            self.name = 'NULL'
        if self.bio is None:
            self.bio = 'NULL'
        string = "[ Login: " + self.login + "\nName: " + self.name + "\nBio: " + self.bio + "\nLanguages: "
        for key, value in self.languages.items():
            string += (key + ' : ' + str(value) + '\n')
        return string
