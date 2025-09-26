\# Movie Analytics Pipeline



\## Overview

The Movie Analytics Pipeline is an end-to-end ETL project that extracts movie data from the TMDB API, transforms it, loads it into an SQLite database, and performs analysis to provide insights such as top-rated movies and year-wise trends.



\## Project Structure



movieanalytics/

├── src/

│ ├── extract.py # Extract data from TMDB API

│ ├── transform.py # Clean and transform data

│ ├── load.py # Load data into SQLite

│ ├── analysis.py # Analyze data and create visualizations

│ └── movies.db # SQLite database

├── data/

&nbsp;  ├── movies\_raw.csv

&nbsp;  └── movies\_clean.csv

└── README.md



\## Tech Stack 



Component	Technology / Library



Programming	Python 3.x

API Requests	requests

Data Processing	pandas

Database	SQLite + SQLAlchemy

Visualization	matplotlib

IDE / Editor	VS Code / PyCharm



Install dependencies using:



pip install pandas sqlalchemy matplotlib requests



\##How to Run



1.Extract Data :

&nbsp;   python src/extract.py

2.Transform Data:

&nbsp;   python src/transform.py

3.Load Data into SQLite:

&nbsp;   python src/load.py

4.Run Analysis:

&nbsp;   python src/analysis.py



\##Test Cases / Verification



&nbsp; - movies\_raw.csv created successfully

&nbsp; -movies\_clean.csv cleaned and normalized

&nbsp; -movies.db contains movies table

&nbsp; -Analysis output shows top 10 movies and scatter plot

\##Output

&nbsp;  SQLite Table (movies)

&nbsp;  Ratings vs Year Scatter Plot









