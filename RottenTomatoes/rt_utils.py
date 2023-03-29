from bs4 import BeautifulSoup
from requests import get
import datetime
import json
import time
import os

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "gzip, deflate", 
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1",
}

def change_title_if_required(title):
    if ':' in title:
        title = "--".join(title.split(':'))
    if '?' in title:
        title = "(question_mark)".join(title.split('?'))
    if '/' in title:
        title = "(slash)".join(title.split('/'))
    if ',' in title:
        title = "(comma)".join(title.split('comma'))
    return title

def check_file_existence(file_name):
    already_exists = False
    file_name = change_title_if_required(file_name)
    for json_name in os.listdir("./RottenTomatoes/rt_movie_jsons"):
        if file_name in json_name:
            already_exists = True
            break
    return already_exists

def get_movie_url(title):
    search_url = "https://www.rottentomatoes.com/search?search=" + title.lower().replace(' ', '-')
    while True:
        try:
            search_results = get(search_url, headers=HEADERS)
            break
        except Exception:
            print("Connected failed.. Retrying")
            time.sleep(0.1)
    chicken = BeautifulSoup(search_results.content, "html.parser")
    movie_url = chicken.find('search-page-media-row')
    if movie_url is None:
        return "Movie not found"
    else:
        return movie_url.find('a')['href']

def find_rating(soup):
    rt_str = soup.find("span", attrs={"data-qa":"audience-score"})
    rt_str = rt_str.replace('%',"")
    rating = float(rt_str) / 10
    return rating

def find_release_date(soup):
    rd_str = soup.find('time').string
    dt = datetime.strptime(rd_str,"%B %d, %Y")
    rd = str(dt.date())
    return rd

def find_genres(soup):
    genre_container = soup.findall('span', attrs={'class': 'info-item-value'})
    genres_str = genre_container[1].string
    genres_str = genres_str.replace(" ", "")
    genres = genres_str.split(",")
    return genres

def find_summary(soup):
    summary = soup.find('p', attrs={'data-qa': 'movie-info-synopsis'}).string
    return summary

def find_director(soup):
    director_container = soup.findall('span', attrs={'class': 'info-item-value'})
    director = director_container[3].string
    return director
