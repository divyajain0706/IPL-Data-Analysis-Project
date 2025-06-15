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