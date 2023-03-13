import requests
import re
import time
import bs4
import csv
import pandas as pd
import numpy as np

# website
#res = requests.get("https://www.espn.com/nba/team/schedule/_/name/tor")


def scrape_nba_schedule(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    game_result = soup.find("table", class_ = "Table")

    # setting the lists for the data
    date = []
    opponent = []
    results = []
    w_l = []
    hi_points = []
    hi_rebounds = []
    hi_assists = []
    integer = 0
    # pulling the information from 
    for result in game_result.find_all("tr")[1:]:
        integer +=1
        try:
            date.append(result.find_all("td")[0].text)
            opponent.append(result.find_all("td")[1].text)
            results.append(result.find_all("td")[2].text)
            w_l.append(result.find_all("td")[3].text)
            hi_points.append(result.find_all("td")[4].text)
            hi_rebounds.append(result.find_all("td")[5].text)
            hi_assists.append(result.find_all("td")[6].text)
        except IndexError:
            if results[integer - 1] == "Postponed" or results[integer - 1] == "Canceled":
                w_l.append(np.NaN)
                hi_points.append(np.NaN)
                hi_rebounds.append(np.NaN)
                hi_assists.append(np.NaN)
            else:
                hi_rebounds.append(np.NaN)
                hi_assists.append(np.NaN)
            continue
    time.sleep(5)
    #print(len(date))
    #print(len(w_l))
    #print(len(hi_points))
    #print(len(hi_rebounds))
    #print(len(hi_assists))
    print(pd.DataFrame({"date": date, "opponent": opponent, "result": results,
                        "w_l": w_l, "hi_points": hi_points, "hi_rebounds": hi_rebounds, 
                        "hi_assists": hi_assists}))
    
#scrape_nba_schedule("https://www.espn.com/nba/team/schedule/_/name/bos/season/2013")



#"https://www.espn.com/nba/team/schedule/_/name/{}/season/2023".format(str(season))

#team = ['atl','bos','bkn','cha','chi','cle','dal','den','det','gs','hou',
        #'ind','lac','lal','mem','mia','mil','min','no','ny','okc','orl',
        #'phi','phx','por','sac','sa','tor','utah','wsh']

def browse_scrape_2023(seed_url):
    # Fetch the URL - We will be using this to append to images and info routes
    team = ['atl','bos','bkn','cha','chi','cle','dal','den','det','gs','hou',
            'ind','lac','lal','mem','mia','mil','min','no','ny','okc','orl',
            'phi','phx','por','sac','sa','tor','utah','wsh']
    seasons = [2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
        # This if clause stops the script when it hits an empty page
    for i, s in [(i,s) for i in team for s in seasons]:
        try:
            formatted_url = seed_url.format(str(i), str(s))
            print(f"Now Scraping - {formatted_url}")
            scrape_nba_schedule(formatted_url)     # Invoke the scrape function
            # Be a responsible citizen by waiting before you hit again
            time.sleep(5)
        except IndexError: 
            pass
        continue

browse_scrape_2023("https://www.espn.com/nba/team/schedule/_/name/{}/season/{}")