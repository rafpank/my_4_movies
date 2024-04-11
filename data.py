# WRITE YOUR CODE HERE
favMovies = [
    {
    "title" : "Matrix",
    "year" : 1999,
    "rating" : 8.7,
    "description" : "When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.",
    "rezyseria": [
        "Andrew Wachowski",
        "Larry Wachowski",

    ],
    "scenarzysci" : [
        "Andrew Wachowski",
        "Larry Wachowski",
    ],
    "gwiazdy" : [
        "Keanu Reeves",
        "Carrie-Anne Moss",
        "Laurence Fishburne",
        "Hugo Weaving",
    ],
    "gatunki" :[
        "Akcja", 
        "Sci-Fi",
    ],
},
{
    "title" : "Seven",
    "year" : 1995,
    "rating" : 8.6,
    "description" : "Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives.",
    "rezyseria": ["David Fincher"],
    "scenarzysci" : ["Andrew Kevin Walker"],
    "gwiazdy" : [
    "Morgan Freeman",
    "Brad Pitt",
    "Gwyneth Paltrow",
    "Kevin Spacey",
    ],
    "gatunki" : [
        "Kryminał",
        "Thriller",
    ],
},
{
    "title" : "Pulp Fiction",
    "year" : 1994,
    "rating" : 8.8,
    "description" : "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
    "rezyseria": [
   "Quentin Tarantino"
   ],
   "scenarzysci" :[
       "Quentin Tarantino"
   ],
   "gwiazdy" : [
       "John Travolta", 
       "Samuel L. Jackson", 
       "Uma Thurman", 
       "Bruce Willis",
   ],
   "gatunki" : [
       "Gangsterski",
   ],
},
{
    "title" : "Forrest Gump",
    "year" : 1994,
    "rating" : 8.8,
    "description" : "The history of the United States from the 1950s to the '70s unfolds from the perspective of an Alabama man with an IQ of 75, who yearns to be reunited with his childhood sweetheart.",
    "rezyseria": [
        "Robert Zemeckis",
    ],
    "scenarzysci" : [
        "Eric Roth",
    ],
    "gwiazdy" : [
        "Tom Hanks",
        "Robin Wright",
        "Sally Field",
        "Gary Sinise",
    ],
    "gatunki" : [
        "Dramat",
        "Komedia",
    ],
}]
#print("Tytuł pierwszego filmu to: " + favMovies[0]["title"])
#print("Rok premiery drugiego filmu to: ", favMovies[1]["year"])
#print("Ocena IMDB trzeciego filmu to: ", favMovies[2]["rating"])
#print("Krótki opis czwartego filmu to: " + favMovies[3]["description"])
#print(favMovies[0]["gwiazdy"][3])

#print("Głównym reżyserem pierwszego filmu jest: " + favMovies[0]["rezyseria"][0])
#print("Głównym scenarzystą drugiego filmu jest: " + favMovies[1]["scenarzysci"][0])
#print("Główną gwiazdą trzeciego filmu jest: " + favMovies[2]["gwiazdy"][0])
#print("Głównym gatunkiem czwartego filmu jest: "+ favMovies[3]["gatunki"][0])
#averageRating = ((favMovies[0]["rating"] + favMovies[1]["rating"] + favMovies[2]["rating"] + favMovies[3]["rating"]) / 4)
#yearOfToday = 2024
#averageAge = ((yearOfToday - favMovies[0]["year"] + yearOfToday - favMovies[1]["year"] + yearOfToday - favMovies[2]["year"] + yearOfToday - favMovies[3]["year"]) / 4)
#print("Średnia ocen filmów to:", averageRating) 
#print("Średni wiek filmów:", averageAge)

for movie in favMovies: #pętla dukująca tytuły wszystkich filmów z listy favMovies
    print(movie["title"])

numbers_of_movies = 0 #Pętla while drukująca tytuły filmów (pamiętaj o zakończeniach pętli)
while numbers_of_movies < len(favMovies):
    print(favMovies[numbers_of_movies]["title"])
    numbers_of_movies += 1

total_rate = 0 
for rate in favMovies: #Pętla licząca średnią ocen
    total_rate += rate["rating"]
    print(total_rate)
average_rate = total_rate/len(favMovies)
print(average_rate)

newest_movie = favMovies[0]

for movie in favMovies: #Pętla wyszukująca najnowszego filmu
     
   if movie["year"] > newest_movie["year"]:
      newest_movie = movie
print(newest_movie["title"])

star_by_movies = ""
for movie in favMovies:
    star_by_movies += movie["title"] + "\n\n"
    for star in movie["gwiazdy"]:
        star_by_movies += star + ",\n"
    star_by_movies += "\n\n"
print(star_by_movies)

#print(movie["title"] + "\n", movie["gwiazdy"])
