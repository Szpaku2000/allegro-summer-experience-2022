# allegro-summer-experience-2022

My email in recruitment process: karol.szpakow@gmail.com 

# Pre-required installations:

python -m pip install requests

pip install setuptools





# Uwagi

Obecnie najprostszym sposobem do tego by wysłać dane o użytkowniku jest stworzenie nowego obiektu używając funkcji *userFromUsername(username)*,po czym na obiekcie który zostaje tą funkcją zwrócony wykonać metodę *postUser(url)*. W ten sposób wysyłany jest plik JSON z loginem, nazwą, bio oraz zagregowanym słownikiem języków użytkownika.

W bardzo podobny sposób wysyłana jest lista repozytoriów jednakże po stworzeniu obiektu *User* używana jest funkcja *postRepoList(url)*
