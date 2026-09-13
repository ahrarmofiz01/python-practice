users = {
    "A": ["Inception", "Avatar", "Titanic"],
    "B": ["Avatar", "Titanic", "Interstellar"],
    "C": ["Inception", "Interstellar", "Avengers"]
}

user = "A"

recommended = []

for other_user in users:
    if other_user != user:

        for movie in users[other_user]:

            if movie not in users[user] and movie not in recommended:
                recommended.append(movie)

print("Recommended movies:")

for movie in recommended:
    print(movie)


