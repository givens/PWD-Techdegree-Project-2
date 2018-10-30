
import csv

"""
Create variables and programming logic to divide the 18 players into three teams: Sharks, Dragons and Raptors. Make sure the teams have the same number of players on them, and that the experience players are divided equally across the three teams.

Create a text file named teams.txt that includes the name of a team, followed by the players on that team. List all three teams and their players.

In the list of teams include the team name on one line, followed by a separate line for each player. Include the player's name, whether the player has experience playing soccer, and the player's guardian names. Separate each bit of player information by a comma. For example, the text file might start something like this:
Sharks
Frank Jones, YES, Jim and Jan Jones
Sarah Palmer, YES, Robin and Sari Washington
Joe Smith, NO, Bob and Jamie Smith

Before you submit your project for review, make sure you can check off all of the items on the Student Project Submission Checklist. The checklist is designed to help you make sure you’ve met the grading requirements and that your project is complete and ready to be submitted!


If you are stuck on how to get started with this project, have a look at the Project-01 Study Guide.

"""


FILEIN = "soccer_players.csv"
FILEOUT = "teams.txt"
NUMTEAMS = 3

teams = {
        "Sharks": [],
        "Dragons": [],
        "Raptors": []
        }

def readplayers():
    with open(FILEIN, newline='\n') as csvfile:
        players = list(csv.DictReader(csvfile, delimiter=','))
    return players

def sortedbyexperience(players):
    return sorted(players, key=lambda k: k["Soccer Experience"])

def teamcategorize(sortedplayers):
    teamlist = list(teams.keys())
    for idx, player in enumerate(sortedplayers):
        team = teamlist[idx % NUMTEAMS]
        teams[team].append(player)
    return teams

def writeleagueroster(teams):
    with open(FILEOUT, 'w') as textfile:
        for team, names in teams.items():
            print(team, file=textfile)
            print(20*"-", file=textfile)
            for name in names:
                print(name["Name"], file=textfile)
            print("\n", file=textfile)

if __name__ == "__main__":
    players = readplayers()
    sortedplayers = sortedbyexperience(players)
    teams = teamcategorize(sortedplayers)
    writeleagueroster(teams)