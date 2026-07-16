"""
Movie Sentiment Analysis
-------------------------
Analyzes movie ratings and converts them into sentiment labels
(positive / neutral / negative), then lets the user search for
movies and see their sentiment score.

Data source: MovieLens dataset (movies.csv, ratings.csv)
https://grouplens.org/datasets/movielens/
"""

import os
import sys
import pandas as pd

MOVIES_FILE = "movies.csv"
RATINGS_FILE = "ratings.csv"


def load_data(movies_path: str, ratings_path: str) -> pd.DataFrame:
    """Load and merge the movies and ratings CSV files."""
    if not os.path.exists(movies_path):
        sys.exit(f"Error: '{movies_path}' not found. Please add it to the project folder.")
    if not os.path.exists(ratings_path):
        sys.exit(f"Error: '{ratings_path}' not found. Please add it to the project folder.")

    movies = pd.read_csv(movies_path)
    ratings = pd.read_csv(ratings_path)
    return pd.merge(ratings, movies, on="movieId")


def rating_to_sentiment(rating: float) -> str:
    """Convert a numeric rating into a sentiment label."""
    if rating >= 4:
        return "positive"
    elif rating == 3:
        return "neutral"
    else:
        return "negative"


def compute_sentiment_scores(data: pd.DataFrame) -> pd.DataFrame:
    """Add a sentiment column and compute a positivity score per movie."""
    data = data.copy()
    data["sentiment"] = data["rating"].apply(rating_to_sentiment)

    sentiment_stats = (
        data.groupby("title")["sentiment"]
        .value_counts()
        .unstack()
        .fillna(0)
    )

    # Make sure all three sentiment columns exist even if a category is missing
    for col in ["positive", "neutral", "negative"]:
        if col not in sentiment_stats.columns:
            sentiment_stats[col] = 0

    sentiment_stats["score"] = sentiment_stats["positive"] / (
        sentiment_stats["positive"] + sentiment_stats["negative"] + sentiment_stats["neutral"]
    )

    return sentiment_stats.sort_values("score", ascending=False)


def search_movies(sorted_movies: pd.DataFrame, query: str) -> pd.DataFrame:
    """Return movies whose title contains the given (case-insensitive) query."""
    query = query.lower()
    return sorted_movies[sorted_movies.index.str.lower().str.contains(query)]


def main():
    data = load_data(MOVIES_FILE, RATINGS_FILE)
    sorted_movies = compute_sentiment_scores(data)

    movie_name = input("Enter a movie name: ").strip()
    matches = search_movies(sorted_movies, movie_name)

    if not matches.empty:
        print("\n🎬 Top Matching Movies:\n")
        print(matches.head(10))
    else:
        print("\n❌ No matching movie found.")


if __name__ == "__main__":
    main()
