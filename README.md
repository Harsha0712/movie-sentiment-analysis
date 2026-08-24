---
updated: 2026-08-24T15:59:15.131Z
editedBy: Harsha0712
generator: ForkLeaf — https://github.com/praneeth132006/ForkLeaf
---

# 🎬 Movie Sentiment Analysis

A simple Python script that analyzes movie ratings from the [MovieLens dataset](https://grouplens.org/datasets/movielens/) and converts them into sentiment labels (**positive / neutral / negative**). It then lets you search for a movie by name and see how positively it's rated overall.

## How it works

1. Loads `movies.csv` and `ratings.csv` and merges them on `movieId`.
2. Converts each numeric rating into a sentiment:
   - Rating ≥ 4 → `positive`
   - Rating == 3 → `neutral`
   - Rating &lt; 3 → `negative`
3. Computes a **positivity score** per movie: `positive / (positive + neutral + negative)`.
4. Lets you search movies by (partial, case-insensitive) title and shows the top 10 matches sorted by score.

## Setup

1. Clone this repo:

   ```bash
   git clone https://github.com/<your-username>/movie-sentiment-analysis.git
   cd movie-sentiment-analysis
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Add the dataset files `movies.csv` and `ratings.csv` to the project folder (download them from [MovieLens](https://grouplens.org/datasets/movielens/)). These files are not included in the repo — see `.gitignore`.

## Usage

```bash
python movie_sentiment_analysis.py
```

You'll be prompted to enter a movie name, and it will print the top 10 matching titles with their sentiment breakdown and score.

### Example

```
Enter a movie name: matrix

🎬 Top Matching Movies:

                                  negative  neutral  positive  score
title
The Matrix (1999)                     5.0     10.0      85.0   0.85
The Matrix Reloaded (2003)           20.0     15.0      50.0   0.59
```

## Project structure

```
movie-sentiment-analysis/
├── movie_sentiment_analysis.py
├── requirements.txt
├── .gitignore
└── README.md
```

## License

This project is open source and available under the [MIT License](LICENSE).

# 

![image.png](assets/2026-08-24-image-3b1d.png)

```mermaid
flowchart TD
```