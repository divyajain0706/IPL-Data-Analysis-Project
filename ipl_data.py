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