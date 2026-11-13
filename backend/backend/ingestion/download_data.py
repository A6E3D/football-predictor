import urllib.request
import os

BASE_URL = "https://www.football-data.co.uk/mmz4281/{season}/E0.csv"
SEASONS = ["2021", "2122", "2223", "2324", "2425", "2526"]
SAVE_DIR = "data/raw"

os.makedirs(SAVE_DIR, exist_ok=True)

for season in SEASONS:
    url = BASE_URL.format(season=season)
    dest = os.path.join(SAVE_DIR, f"E0_{season}.csv")
    urllib.request.urlretrieve(url, dest)
    print(f"Downloaded {dest}")