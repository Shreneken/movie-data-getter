
# Scraping IMDB 

## Current data: All movies from top 250 movies list

## TO-DO: 
- list of movies
- change format to lists
- make data format for review

#### data format for each `movieName_releaseData_Director.json`:
 ```js
   {
      rating: rating_here,
      release_data: release_date_here,
      num_reviews: number_of_reviews_here,
      genre : [genre_here],
      summary: summary_here,
      reviews: [reviewContent] 
   }

   //each reviewContent obj format:
   {
    review_title: review_title
    content: review_content
    review_date: review_date_here
   }
 ```

-TOP 1000 most popular movies in imdB + Top 250 worst rated movies



#### Getting movie data 
  - Run `./run_py_scripts.sh` in your terminal while under the `imdb` directory. If running from Windows, use `Git Bash`, WSL or any other alternative for bash shell 

    OR

  - Run `imdb.py` which will add `movieName_releaseData_Director.json` for each movie inside the `imdb_movie_jsons` directory
  - Then run `sorter.py` to categorize the `movieName_releaseData_Director.json` files into different directors sorted by release date.

  - `imdb.py` will also create a `imdBData.json` if it does not already exist. This file contains data in top250 movies list form imdB.


- Checkout `imdb_utils.py` for any helper functions.
