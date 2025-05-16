# Create a list of fav movies
fav_movies = ["Saving Pvt Ryan", "Black Hawk Down", "Scarface", "The Godfather", "Arival"]

print(fav_movies)

print("These are 5 of my favorite movies")

print("...wait, here is the list again. I've added another one.")

fav_movies.append("Interstellar")
print(fav_movies)

print("Here is a new list. I've removed my least favorite of the 6 movies above...:")

fav_movies.remove("Interstellar")
print(fav_movies)

for item in fav_movies:
    print(item)

print("Now, here is one of my favorite books.")

book = {
    "title": "1984", 
    "Author": "George Orwell", 
    "Year": "1949"
    }
book["genre"] = "Fiction"
book["Year"] = 'The book came out in 1949, but today, it is 2025'

for key, value in book.items():
    print(f"{key}: {value}")
