# allegro-summer-experience-2022

My email in recruitment process: karol.szpakow@gmail.com 

# Pre-required installations:

python -m pip install requests

pip install setuptools

# Installation

Inside directory with unpacked project:
```sh
pip install .
```
# Remarks

Right now the easiest way to post user data is to create new object using *userFromUsername(username)* function and then use its method *postUser(url)*. In this way JSON file containing login, name, bio and aggregated dictionary with user languages is posted.

In very similar way repository list is sent however after creation of *User* object we use *postRepoList(url)* function.
