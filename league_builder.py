
# -*- coding: utf-8 -*-
"""
Python Web Development Techdegree
Project 2 - Soccer League Roster
---------------------------------
@author: bg
"""

import csv

teams = {
    "Sharks": [],
    "Dragons": [],
    "Raptors": []
}

FILEIN = "soccer_players.csv"
FILEOUT = "teams.txt"
NUMTEAMS = len(teams)


def readplayers():
    "Read in player dictionary from file"
    with open(FILEIN, 'r', newline='\n') as csvfile:
        players = list(csv.DictReader(csvfile, delimiter=','))
    return players


def sortedbyexperience(players):
    "Sort player records by experience level - yes or no"
    return sorted(players, key=lambda record: record["Soccer Experience"])


def teamcategorize(sortedplayers):
    "Categorize sorted players into team lists"
    teamlist = list(teams.keys())
    for idx, record in enumerate(sortedplayers):
        team = teamlist[idx % NUMTEAMS]
        teams[team].append(record)
    return teams


def writeleagueroster(teams):
    "Output team information to a file"
    with open(FILEOUT, 'w') as textfile:
        for team, records in teams.items():
            print("\n" + team, file=textfile)
            #print(20*"-", file=textfile)
            for record in records:
                seq = (
                    record["Name"],
                    record["Soccer Experience"],
                    record["Guardian Name(s)"])
                print(", ".join(seq), file=textfile)


def writeletter(teams):
    "Write letter for each player to a file"
    for team, records in teams.items():
        for record in records:
            first_name, last_name = record["Name"].split()
            file_name = "{}_{}.txt".format(first_name, last_name)
            with open(file_name, 'w') as textfile:
                str = createletter(team, record)
                print(str, file=textfile)


def createletter(team, record):
    "Create letter to parents given player record and team info"
    return """Dear {},
Your child, {}, is on the {} team.
Practice begins at noon on June 1, 2019.
Sincerely,
The Soccer League""".format(record["Guardian Name(s)"], record["Name"], team)


if __name__ == "__main__":
    players = readplayers()
    sortedplayers = sortedbyexperience(players)
    teams = teamcategorize(sortedplayers)
    writeleagueroster(teams)
    writeletter(teams)
