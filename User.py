import requests
import Repository


def userFromUsername(username):
    url = 'https://api.github.com/users/'
    url = url + username
    req = requests.get(url).json()
    login = req["login"]
    name = req["name"]
    bio = req["bio"]
    repositoryList = User.createRepoList(name)
    languages = User.createLangDict(repositoryList)

    return User(login, name, bio, repositoryList, languages)


class User:

    def __init__(self, login, name, bio, repoList, langs):
        self.login = login  # string - user's login (username)
        self.name = name  # string - user's first and last name
        self.bio = bio  # string - user's bio
        self.repositoryList = repoList # Repository[] - list of repositories of a user, it is useful in when creating languages for a user
        self.languages = langs # dictionary (string -> int) - language name and number of bytes that it takes in repository

    def __str__(self):
        return "[ Login: " + self.login + ", Name: " + self.name + ", Bio: " + self.bio + "Languages: " + self.languages + "]"

    def createRepoList(self, username):
        url = 'https://api.github.com/users/' + username + '/repos'
        repositories = requests.get(url)
        repoList = []
        for repository in repositories.json():
            languages = requests.get(url + '/' + repository["name"] + '/languages').json()
            next_repo = Repository(repository["name"], languages)
            repoList.append(next_repo)
        return repoList

    def createLangDict(self, repoList):
        languages = {}

        for repository in repoList:
            for key, value in repository.languages:
                if key in languages:
                    languages[key] += value
                else:
                    languages[key] = value

        return languages