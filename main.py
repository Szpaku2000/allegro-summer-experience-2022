import User, Repository
import requests


# req = requests.get('https://api.github.com/users/rurkajaroslaw/repos')
#
# list = req.json()
# counter = 0
#
# for element in list:
#     print(str(counter) + ":")
#     for key, value in element.items():
#         print('\t',key, ' : ', value)
#     counter += 1

ja = User.userFromUsername("Szpaku2000")

print(ja)

ja.repositoryList[0].uploadRepo('https://httpbin.org/put')
ja.uploadUser('https://httpbin.org/put')




