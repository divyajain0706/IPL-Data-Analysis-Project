import pandas as pd
import numpy as np

#Loading the CSV file
df = pd.read_csv(r"D:\Python Programs\pandas programs\IPL data project\matches.csv", encoding="latin1")

#Displaying the concise information about the dataset
print("Concise information about the dataset :")
print(df.info())

#Checking for missing values
print("\nChecking for missing values :")
print(df.isnull().sum())

#Droping the umpire3 column
df.drop(columns=["umpire3"],inplace=True)
print(df.columns)

#Checking whether there are duplicate values or not
print("Duplicate values if any :")
print(df.duplicated().sum())

#Count total match wins per team.
team_wins = df['winner'].value_counts()
print("Total matches win per team :")
print(team_wins)

#Team with highest wins
print("\nTeam with highest wins :")
print(team_wins.idxmax())

#Count appearances of each team in team1 and team2.
team_count = pd.concat([df['team1'], df['team2']]).value_counts()
print("Count of each team in team1 and team2 :")
print(team_count)

#Count how many times each team won the toss.
team_toss = df["toss_winner"].value_counts()
print("Count of each team in toss :")
print(team_toss)

#Analyze toss_decision choices (bat/field) frequency.
toss_frequency = df["toss_decision"].value_counts()
print("Frequency of toss decision :")
print(toss_frequency)
print("The toss decision with high frequency is :")
print(toss_frequency.idxmax())

#Compare toss_winner with winner:
df["toss_match_same"] = df["toss_winner"] == df["winner"]
same_count = df["toss_match_same"].value_counts()
print(same_count)
percentage_same = (df['toss_match_same'].sum() / len(df)) * 100
print(f"Toss winner also won the match in {percentage_same:.2f}% of matches.")

#Count frequency of player_of_match values.
player_of_match = df["player_of_match"].value_counts()
print(player_of_match)
player_rewarded = player_of_match.idxmax()
print("Player rewarded as player of the match most of the time is :")
print(player_rewarded)

#Count number of matches hosted per venue.
venue_count = df["venue"].value_counts()
print("Number of matches hsoted per venue are :")
print(venue_count)