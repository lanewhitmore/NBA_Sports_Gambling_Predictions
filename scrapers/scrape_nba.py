import requests
import re
import time
import bs4
import csv
import pandas as pd

res = requests.get("https://www.basketball-reference.com/leagues/NBA_2023.html")

#resa = requests.get("https://www.nba.com/stats/teams/advanced")
team = []
w = []
l = []
pts = []
fgm = []
fga = []
thrpm  = []
thrpa = []
ftm =  []
fta = []
games = []
orb = []
drb = []
ast = []
stl = []
blk = []
tov = []
pf = []

# advanced stats
offrtg = []
defrtg = []
astP = []
ast_to = []
astRatio = []
orebP = []
drebP = []
tovP = []
efgP = []
tsP = []
pace = []
pie = []
poss = []


def scrape_nba(request_traditional): #, request_advanced):
    soup_trad = bs4.BeautifulSoup(request_traditional.text, "html.parser")
    trad_stats = soup_trad.find("table",attrs = {'id' : 'per_game-team'})
    for stat in trad_stats.find_all('tr')[1:31]:
        team.append(stat.find("td", {"data-stat": "team"}).text)
        games.append(stat.find("td", {"data-stat": "g"}).text)
        pts.append(stat.find("td", {"data-stat": "pts"}).text)
        fgm.append(stat.find("td", {"data-stat": "fg"}).text)
        fga.append(stat.find("td", {"data-stat": "fga"}).text)
        thrpm.append(stat.find("td", {"data-stat": "fg3"}).text)
        thrpa.append(stat.find("td", {"data-stat": "fg3a"}).text)
        ftm.append(stat.find("td", {"data-stat": "ft"}).text)
        fta.append(stat.find("td", {"data-stat": "fta"}).text)
        orb.append(stat.find("td", {"data-stat": "orb"}).text)
        drb.append(stat.find("td", {"data-stat": "drb"}).text)
        ast.append(stat.find("td", {"data-stat": "ast"}).text)
        stl.append(stat.find("td", {"data-stat": "stl"}).text)
        blk.append(stat.find("td", {"data-stat": "blk"}).text)
        tov.append(stat.find("td", {"data-stat": "tov"}).text)
        pf.append(stat.find("td", {"data-stat": "pf"}).text)

    time.sleep(5)



scrape_nba(res)

team_stats = pd.DataFrame({"team": team, "gamesPlayed": games, "points": pts, "fgm": fgm, "fga":fga, "fg3": thrpm, "fg3a": thrpa, 
                           "ft": ftm, "fta": fta, "assists": ast, "steals": stl, "blocks": blk, "turnovers": tov, "personalFouls": pf})
print(team_stats)