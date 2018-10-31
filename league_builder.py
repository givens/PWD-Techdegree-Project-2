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
    "Raptors": [],
}

FILE_IN = "soccer_players.csv"
FILE_OUT = "teams.txt"
NUM_TEAMS = len(teams)


def read_players():
    "Read in player dictionary from file"
    with open(FILE_IN, 'r', newline='\n') as csv_file:
        players = list(csv.DictReader(csv_file, delimiter=','))
    return players


def sort_by_experience(players):
    "Sort player records by experience level - yes or no"
    return sorted(players, key=lambda record: record["Soccer Experience"])


def categorize_by_team(sortedplayers):
    "Categorize sorted players into team lists"
    team_list = list(teams.keys())
    for idx, record in enumerate(sorted_players):
        team = team_list[idx % NUM_TEAMS]
        teams[team].append(record)
    return teams


def write_league_roster(teams):
    "Output team information to a file"
    with open(FILE_OUT, 'w') as text_file:
        for team, records in teams.items():
            print("\n" + team, file=text_file)
            for record in records:
                seq = (
                    record["Name"],
                    record["Soccer Experience"],
                    record["Guardian Name(s)"])
                print(", ".join(seq), file=text_file)


def write_letter(teams):
    "Write letter for each player to a file"
    for team, records in teams.items():
        for record in records:
            first_name, last_name = record["Name"].split()
            file_name = "{}_{}.txt".format(first_name, last_name)
            with open(file_name, 'w') as text_file:
                str = create_letter(team, record)
                print(str, file=text_file)


def create_letter(team, record):
    "Create letter to parents given player record and team info"
    return """Dear {},
Your child, {}, is on the {} team.
Practice begins at noon on June 1, 2019.
Sincerely,
The Soccer League""".format(record["Guardian Name(s)"], record["Name"], team)


if __name__ == "__main__":
    players = read_players()
    sorted_players = sort_by_experience(players)
    teams = categorize_by_team(sorted_players)
    write_league_roster(teams)
    write_letter(teams)
