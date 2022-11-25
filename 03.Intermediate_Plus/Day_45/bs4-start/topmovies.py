from bs4 import BeautifulSoup
import requests

def main():
    response = requests.get("https://www.timeout.com/newyork/movies/best-movies-of-all-time")
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    all_movies = soup.find_all(name="h3", class_="_h3_cuogz_1")
    movie_titles = []

    for movie in all_movies:
        # print(movie.getText())
        movie_titles.append(movie.getText())
    
    movies = movie_titles[:100]
    print(movies)

    with open("movies.txt", mode="w") as file:
        for movie in movies:
            file.write(f'{movie}\n')
    
    

        
        
    

if __name__ == '__main__':
    main()