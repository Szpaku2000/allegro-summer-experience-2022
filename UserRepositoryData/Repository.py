import json
import requests


def repositoryFromName(username, repoName):
    """
    Creates Repository object with username and repository name

    Parameters
    ----------
    username : str
        Name of the user
    repoName: str
        Name of the repository

    Raises
    ------
    NotImplementedError
        If no username or repository name is passed as an argument
    """

    if username is None or repoName is None:
        raise NotImplementedError("Both username and repository name need to be provided")

    url = 'https://api.github.com/repos/'
    url = url + username + '/' + repoName
    req = requests.get(url)
    dictionary = req.json()
    lang_url = url + '/languages'
    languages = requests.get(lang_url).json()

    return Repository(dictionary["name"], languages)


class Repository:
    """
    A class used to represent Repository on GitHub service

    Attributes
    ----------
    name : str
        the name of the repository
    languages : dict
        the dictionary where keys are languages names used in repository and values are
        numbers of bytes used in said language

    """

    def __init__(self, name, languages):
        """
        Parameters
        ----------
        name : str
            The name of the repository
        languages : dict
            the dictionary where keys are languages names used in repository and values are
            numbers of bytes used in said language
        """

        self.name = name                    # string - repository name
        self.languages = languages

    def __str__(self):
        """
        Method providing concatenation of a class to string data type
        """

        string = "[ \nName: " + self.name + "Languages: "
        for key, value in self.languages.items():
            string += ('\t' + key + ' : ' + str(value) + '\n')
        string += '\n]'
        return string

    def uploadRepo(self, url):
        """
        Method that uploads Repository as JSON file to a server

        Parameters
        ----------
        url : str
            Server to which json is being PUT
        """
        jsonstr = json.dumps(self.__dict__)
        requests.put(url, jsonstr)
