import requests

url = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=1&primary_release_year=1992&sort_by=popularity.desc"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2N2FlZTFhYTRhMmRiM2U4YzIzNzBmOWExOWY5MGQxOSIsIm5iZiI6MTcyNDAxMjU4Mi4zNTMxOTcsInN1YiI6IjY2YjhkYThjMTMxZTJiZDNiZDA3NWIwNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._zXVSXc2SIjJRQX6XwtqqNri5E8rYZAnbDI6QSkqUmU"
}

response = requests.get(url, headers=headers)

print(response.text)