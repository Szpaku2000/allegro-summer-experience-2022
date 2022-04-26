import User

ja = User.userFromUsername("Szpaku2000")

print(ja)

ja.repositoryList[0].uploadRepo('https://httpbin.org/put')
ja.uploadUser('https://httpbin.org/put')




