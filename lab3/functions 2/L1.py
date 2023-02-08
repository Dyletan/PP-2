from movies import movies
def good(movie):
    return movie["imdb"] > 5.5

def sublist(movies):
    subl = list()
    for movie in movies:
        if(good(movie)):
            subl.append(movie)
    return subl

def filterMovies(movies, category):
    subl = list()
    for movie in movies:
        if(movie["category"] == category):
            subl.append(movie)
    return subl

def avgScore(movies):
    sum = 0
    for movie in movies:
        sum += movie["imdb"]
    return sum/len(movies)

def avgCategoryScore(movies, category):
    subl = filterMovies(movies, category)
    return avgScore(subl)

# print(sublist(movies))
# print(filterMovies(movies, "Action"))
# print(avgScore(movies))
# print(avgCategoryScore(movies, "Romance"))