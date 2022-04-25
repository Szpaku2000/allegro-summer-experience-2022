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

defunkt = User.userFromUsername("defunkt")

print(defunkt)





