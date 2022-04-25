import requests
import Repository

def userFromUsername(username):
    url = 'https://api.github.com/users/'
    url = url + username
    req = requests.get(url)
    # TODO
    # login =
    # name =
    # bio =
    # languages =

    return User()


class User:

    def __init__(self, login, name, bio):
        self.login = login  # string - user's login (username)
        self.name = name  # string - user's first and last name
        self.bio = bio  # string - user's bio
        self.repositoryList = self.createRepoList(name) # Repository[] - list of repositories of a user, it is useful in when creating languages for a user
        self.languages = self.createLangDict(self.repositoryList) # dictionary (string -> int) - language name and number of bytes that it takes in repository

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