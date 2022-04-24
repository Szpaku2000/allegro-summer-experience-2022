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

jarekIOProject = Repository.repositoryFromName("rurkajaroslaw", "IO_Project")

print(jarekIOProject.name + '\n' + jarekIOProject.languages)



