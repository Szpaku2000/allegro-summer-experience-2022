import json
import requests
from json import JSONEncoder
from Repository import Repository


def createRepoList(username):
    """
    Function creates list of repositories for given user

    Parameters
    ----------
    username: str
        Name of the user

    Returns
    ------
    list
        a list of repositories of the user
    """
    userURL = 'https://api.github.com/users/' + str(username) + '/repos'
    repoURL = 'https://api.github.com/repos/'
    repositories = requests.get(userURL)
    repoJSON = repositories.json()
    repoList = []
    for repository in repoJSON:
        new_url = repoURL + username + '/' + str(repository["name"]) + '/languages'
        languages = requests.get(new_url).json()
        next_repo = Repository(repository["name"], languages)
        repoList.append(next_repo)
    return repoList


def createLangDict(repoList):
    """
    Function processes data from list of repositories

    Parameters
    ----------
    repoList: Repository[]
        Name of the repository

    Returns
    ------
    dict
        a dictionary where keys are programming languages names and
        values are how many bytes of given language is in all repositories
    """

    languages = {}
    for repository in repoList:
        for key in repository.languages:
            if key in languages:
                languages[key] += repository.languages[key]
            else:
                languages[key] = repository.languages[key]

    return languages


def userFromUsername(username):
    """
    Creates User object with username from GitHub REST API

    Parameters
    ----------
    username : str
        Name of the user

    Returns
    ------
    User
        User object of user with certain username
    """

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
    """
        A class used to represent User on GitHub service

        Attributes
        ----------
        login : str
            user's login (username)
        name : str
            real name of the user
        bio : str
            user's bio
        repoList : Repository[]
            list of all the user's repositories
        languages : dict
            the dictionary where keys are languages names used in repository and values are
            numbers of bytes used in said language

    """

    def __init__(self, login, name, bio, repoList, languages):

        """
            Parameters
            ----------
            login : str
                user's login (username)
            name : str
                real name of the user
            bio : str
                user's bio
            repoList : Repository[]
                list of all the user's repositories
            languages : dict
                the dictionary where keys are languages names used in repository and values are
                numbers of bytes used in said language

        """

        self.login = login
        self.name = name
        self.bio = bio
        self.repositoryList = repoList
        self.languages = languages

    def __str__(self):
        """
        Method providing concatenation of a class to string data type
        """

        if self.login is None:
            self.login = 'NULL'
        if self.name is None:
            self.name = 'NULL'
        if self.bio is None:
            self.bio = 'NULL'
        string = "Login: " + self.login + "\nName: " + self.name + "\nBio: " + self.bio + "\nLanguages: \n"
        for key, value in self.languages.items():
            string += ('\t' + key + ' : ' + str(value) + '\n')
        return string

    def uploadUser(self, url):
        """
        Method posting user in JSON format to a given url

        Parameters
        ----------
        url : str
            URL

        """

        jsonStr = json.dumps(self.__dict__, indent=4, cls=MyEncoder)
        requests.put(url, jsonStr)


class MyEncoder(JSONEncoder):
    """
    A custom encoder class being a subclass of JSONEncoder allowing to convert User objects to JSON format
    """

    def default(self, o):
        return o.__dict__
