import numpy as np
import matplotlib.pyplot as plt 

def lineChart(labels, vals, player):
    plt.figure(figsize = (10, 5))

    plt.ylim(0, max(vals["appearances"]) + 10)
    plt.plot(labels, vals["goals"], marker="o", color=(1, 0, 0))
    plt.plot(labels, vals["appearances"], marker="o", color=(0.5, 0, 0)) 
    
    for index, value in enumerate(vals["goals"]):
        plt.text(index, value + 1, str(value), color=(1, 0, 0))  

    for index, value in enumerate(vals["appearances"]):
        plt.text(index, value + 1, str(value), color=(0.5, 0, 0))  
        
    plt.axhline(y=np.nanmean(vals["goals"]), linestyle="-.", color=(1, 0, 0))
    plt.text(0, np.nanmean(vals["goals"]) + 5, "GOALS", color=(1, 0, 0))
    
    plt.axhline(y=np.nanmean(vals["appearances"]), linestyle="-.", color=(0.5, 0, 0))
    plt.text(0, np.nanmean(vals["appearances"]) + 5, "APPEARANCES", color=(0.5, 0, 0))  
    
    plt.xlabel("Seasons")
    plt.title("Liverpool FC Player Stats for " + player)
    plt.show()
    
def seasonName(year):
    return str(year) + "/" + str(year + 1)
  
data = {
    2017: {
        "Mohamed Salah": {"goals": 44, "appearances": 52},
        "Roberto Firminho": {"goals": 27, "appearances": 54},
        "Sadio Mane": {"goals": 20, "appearances": 44},
        "Alex Oxlade-Chamberlain": {"goals": 5, "appearances": 42}
    },
    2018: {
        "Mohamed Salah": {"goals": 27, "appearances": 52},
        "Roberto Firminho": {"goals": 16, "appearances": 48},
        "Sadio Mane": {"goals": 26, "appearances": 50},
        "Alex Oxlade-Chamberlain": {"goals": 0, "appearances": 2}
    },
    2019: {
        "Mohamed Salah": {"goals": 23, "appearances": 48},
        "Roberto Firminho": {"goals": 12, "appearances": 52},
        "Sadio Mane": {"goals": 22, "appearances": 47},
        "Alex Oxlade-Chamberlain": {"goals": 8, "appearances": 43}
    },
    2020: {
        "Mohamed Salah": {"goals": 31, "appearances": 51},
        "Roberto Firminho": {"goals": 9, "appearances": 48},
        "Sadio Mane": {"goals": 16, "appearances": 48},
        "Alex Oxlade-Chamberlain": {"goals": 1, "appearances": 17},
        "Diogo Jota": {"goals": 13, "appearances": 30}
    },
    2021: {
        "Mohamed Salah": {"goals": 31, "appearances": 51},
        "Roberto Firminho": {"goals": 11, "appearances": 35},
        "Sadio Mane": {"goals": 23, "appearances": 51},
        "Alex Oxlade-Chamberlain": {"goals": 3, "appearances": 29},
        "Diogo Jota": {"goals": 21, "appearances": 55},
        "Luis Diaz": {"goals": 6, "appearances": 26}
    },
    2022: {
        "Mohamed Salah": {"goals": 30, "appearances": 51},
        "Roberto Firminho": {"goals": 13, "appearances": 35},
        "Alex Oxlade-Chamberlain": {"goals": 1, "appearances": 13},
        "Diogo Jota": {"goals": 7, "appearances": 28},
        "Luis Diaz": {"goals": 5, "appearances": 21}
    }
}

players = []
for season in data:
    players = players + list(data[season].keys())
    

players = list(dict.fromkeys(players))
players.sort()
    
ans = ""

while (ans != 0):
    seasons = []
    
    for i, p in enumerate(players):
        print (str(i + 1) + ": " + p)
        
    print ("0: Exit")

    while True:
        try:
            ans = int(input("Select a player"))
            break
        except:
            print("Invalid option. Please try again.")    

    if (ans == 0): break
    if (ans > len(players) or ans < 0): continue  
        
        
    player = players[ans - 1]
    stats = { "goals": [], "appearances": []}
    
    for season in data:
        if player in data[season].keys():
            seasons.append(seasonName(season))
            stats["goals"].append(data[season][player]["goals"])
            stats["appearances"].append(data[season][player]["appearances"])
            
    lineChart(seasons, stats, player)
