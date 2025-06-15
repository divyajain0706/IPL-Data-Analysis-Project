import pandas as pd
import numpy as np

#Loading the CSV file
df = pd.read_csv(r"D:\Python Programs\pandas programs\IPL data project\matches.csv", encoding="latin1")
print(df.head(10))