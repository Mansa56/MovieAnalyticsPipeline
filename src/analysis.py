import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Connect to SQLite
engine = create_engine('sqlite:///movies.db')
df = pd.read_sql('SELECT * FROM movies', engine)

# Top-rated movies
top_movies = df.sort_values('Rating', ascending=False).head(10)
print("Top 10 Movies by Rating:")
print(top_movies[['Title', 'Rating']])

# Plot: Ratings vs Year
plt.figure(figsize=(10,6))
df.plot(kind='scatter', x='Year', y='Rating', alpha=0.6)
plt.title('Movie Ratings by Year')
plt.xlabel('Year')
plt.ylabel('Rating')
plt.grid(True)
plt.show()
