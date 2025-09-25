import requests
import pandas as pd

API_KEY = 'af83ab8608b7fb6336a198f5f44ab416'
BASE_URL = 'https://api.themoviedb.org/3'

def fetch_top_rated_movies(pages=1):
    movies = []
    for page in range(1, pages+1):
        url = f'{BASE_URL}/movie/top_rated?api_key={API_KEY}&language=en-US&page={page}'
        response = requests.get(url)
        data = response.json()
        for movie in data['results']:
            movies.append({
                'id': movie['id'],
                'title': movie['title'],
                'release_date': movie['release_date'],
                'vote_average': movie['vote_average'],
                'vote_count': movie['vote_count']
            })
    return pd.DataFrame(movies)

if __name__ == "__main__":
    df = fetch_top_rated_movies(pages=2)  # fetch top 40 movies
    df.to_csv('../data/movies_raw.csv', index=False)
    print("Extracted data saved to movies_raw.csv")
