import User, Repository
import requests


req = requests.get('https://api.github.com/users/rurkajaroslaw/repos')

print(req.json())




