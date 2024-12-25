# Movie Recommendation System

This project builds a Content-Based Movie Recommendation System using TMDB datasets and various text processing techniques.

## Features Implemented:

1. **Data Preprocessing**:
   - Merged TMDB movies and credits datasets.
   - Selected relevant columns: `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, `crew`.
   - Processed genres, keywords, cast, and crew to extract useful information.
   - Combined all textual data into a single `tags` column.

2. **Text Processing**:
   - Converted text data to lowercase and removed spaces.
   - Applied stemming using NLTK's PorterStemmer.
   - Vectorized the `tags` column using `CountVectorizer` with a maximum of 5000 features and English stopword removal.

3. **Similarity Computation**:
   - Computed pairwise cosine similarity of movie vectors to identify related movies.

4. **Recommendation Functionality**:
   - Developed a function to recommend top 5 similar movies based on cosine similarity.

5. **API Integration**:
   - Used TMDB API to fetch movie details and images for enhanced user experience.

6. **Serialization**:
   - Serialized the processed data (`movies_dict`) and similarity matrix using Python's `pickle` for future use.

## How to Run:

1. **Prerequisites:**
   - Install required libraries: `pandas`, `numpy`, `nltk`, `scikit-learn`, `requests`.

2. **Setup:**
   - Place the TMDB dataset files (`tmdb_5000_movies.csv`, `tmdb_5000_credits.csv`) in the project directory.
   - Run the Python script to preprocess the data and generate recommendations.

3. **Recommendation:**
   - Use the `recommend(movie_title)` function to get similar movies for any given title in the dataset.

## Outputs:

- **Pickle Files:**
  - `movies_dict.pkl`: Serialized dictionary of processed movie data.
  - `similarity.pkl`: Serialized cosine similarity matrix.

- **Example Recommendation:**
  ```
  recommend("Spectre")
  Output:
  - Skyfall
  - Quantum of Solace
  - Casino Royale
  - Mission: Impossible - Ghost Protocol
  - Die Another Day
  ```

## Additional Information:
- TMDB API is used to fetch movie images and details for improved visuals.
