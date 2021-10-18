from bs4 import BeautifulSoup
import requests

def main():
    response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    all_movies = soup.find_all(name="h3", class_="title")

    print(all_movies)
    movie_titles = [movie.getText() for movie in all_movies]
    movies = movie_titles[::-1]
    
    

        
        
    

if __name__ == '__main__':
    main()