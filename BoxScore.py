import requests
from bs4 import BeautifulSoup
import re

r = requests.get('http://www.espn.com/nba/boxscore?gameId=401070755')
soup = BeautifulSoup(r.text, 'html.parser')


def main():
    stats()


def getClass(className, x):
    results = soup.find_all('td', attrs={'class': className})
    return str(results[x].text)


def stats():
    records = []
    results = soup.find_all('td', attrs={'class': 'name'})

    x = 0
    for result in results:
        results = soup.find_all('td', attrs={'class': 'name'})
        if x == 13 or x == 28:
            name = 'Total'
        elif x == 14 or x == 29:
            name = 'Percentages'
        else:
            name = str(results[x].find('span'))[6:-7]
        minutes = getClass('min', x)
        field_goals = getClass('fg', x)
        three_pt = getClass('3pt', x)
        free_throws = getClass('ft', x)
        o_reb = getClass('oreb', x)
        d_reb = getClass('dreb', x)
        rebounds = getClass('reb', x)
        assists = getClass('ast', x)
        steals = getClass('stl', x)
        blocks = getClass('blk', x)
        turnovers = getClass('to', x)
        points = getClass('pts', x)
        x = x + 1
        records.append((name, minutes, field_goals, three_pt, free_throws, o_reb, d_reb, rebounds, assists, steals,
                        blocks, turnovers, points))

    print("Name", "Minutes", "Field Goals", "Three Pointers", "Free Throws", "Offensive Rbs", "Defensive Rbs", "Rbs",
          "Assists", "Steals", "Blks", "Turnovers", "Points")

    y = 0
    for something in records:
        print(records[y])
        y = y + 1


main()
