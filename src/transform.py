import pandas as pd

def transform_movies(df):
    # Extract Year from release_date
    df['Year'] = pd.to_datetime(df['release_date'], errors='coerce').dt.year
    df['Year'] = df['Year'].fillna(0).astype(int)
    
    # Keep relevant columns
    df = df[['title', 'Year', 'vote_average', 'vote_count']]
    
    # Rename columns
    df.columns = ['Title', 'Year', 'Rating', 'VoteCount']
    
    return df

if __name__ == "__main__":
    df = pd.read_csv('../data/movies_raw.csv')
    df_clean = transform_movies(df)
    df_clean.to_csv('../data/movies_clean.csv', index=False)
    print("Transformed data saved to movies_clean.csv")
