from UserRepositoryData import User

ja = User.userFromUsername("Szpaku2000")

print(ja)

ja.postRepoList('https://httpbin.org/put')
ja.postUser('https://httpbin.org/put')




