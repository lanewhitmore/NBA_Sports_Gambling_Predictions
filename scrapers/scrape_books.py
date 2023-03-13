import requests
import re
import time
import bs4
import csv
import pandas as pd

def write_to_csv(list_input):
    # The scraped info will be written to a CSV here.
    try:
        with open("allBooks.csv", "a") as fopen:  # Open the csv file.
            csv_writer = csv.writer(fopen)
            csv_writer.writerow(list_input)
    except:
        return False
    
homeTeam = []
awayTeam = []
date = []
homeSpread = []
awaySpread = []
visitorSpreadOdds = []
visitorMoneyLine = []
totalPoints = []
overOdds = []
homeSpreadOdds = []
homeMoneyLine = []
underOdds = []

res = requests.get("https://www.mybookie.ag/sportsbook/nba/")
def scrape(request):
    soup = bs4.BeautifulSoup(request.text, 'html.parser')
    awaygames = soup.find_all("div", class_="game-line__visitor-line d-flex justify-content-around")
    for game in awaygames:
        awayTeam.append(game.button['data-team'])
        homeTeam.append(game.button['data-team-vs'])
        date.append(game.button["data-gamedate"])
        #liveScore_home = each_game.find("span", id = "35433529_visitor_score")
        #liveScore_away = each_game.find("span", id = "35433529_home_score")
        awaySpread.append(game.button["data-points"])
        visitorSpreadOdds.append(game.button["data-odd"])
        overOdds.append(game.find_all("button")[2]["data-odd"])
        totalPoints.append(game.find_all("button")[2]["data-points"])
        visitorMoneyLine.append(game.find_all("button")[1]["data-odd"])
    time.sleep(5)


    homegames = soup.find_all("div", class_="game-line__home-line d-flex justify-content-around")
    for game in homegames:
        homeSpreadOdds.append(game.button["data-odd"])
        homeSpread.append(game.button["data-points"])
        homeMoneyLine.append(game.find_all("button")[1]["data-odd"])
        underOdds.append(game.find_all("button")[2]["data-odd"])
    
    time.sleep(5)
            

scrape(res)

df = pd.DataFrame({'homeTeam': homeTeam, 'awayTeam': awayTeam,'date': date,'awaySpread': awaySpread, 'visitorSpreadOdds': visitorSpreadOdds,
                   'homeSpread':homeSpread, 'homeSpreadOdds': homeSpreadOdds, 'awayMoneyLine': visitorMoneyLine, 'homeMoneyLine': homeMoneyLine, 'totalPoints': totalPoints,
                   'overOdds': overOdds, 'underOdds': underOdds})
print(df)

