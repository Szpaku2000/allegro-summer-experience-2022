from UserRepositoryData import User

me = User.userFromUsername("Szpaku2000")

print(me)

me.postRepoList('https://httpbin.org/put')
me.postUser('https://httpbin.org/put')




