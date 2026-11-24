# Experiment 1: EDA in IPL Dataset

## Name : Ramanujam G
## Reg No. : 212224240129

# Aim:
To perform Exploratory Data Analysis (EDA) on the IPL matches dataset and derive insights about matches per season, winning teams, toss decisions, and top venues.

# Algorithm / Procedure:

**1.Import Libraries**
  Import pandas for data handling.
  Import matplotlib and seaborn for visualization.
  
**2.Load Dataset**
  Use pd.read_csv() to load the IPL matches dataset.
  Check dataset shape using .shape.
  View first 5 rows using .head().
**3.Matches per Season (Univariate Analysis)**

  Group data by season and count matches.
  Plot a bar chart to visualize growth/decline in matches.
  
**4.Top Winning Teams (Univariate Analysis)**
  Use value_counts() on the winner column.
  Plot top 5 winning teams in a bar chart.
  
**5.Toss Decisions (Univariate Analysis)**
  Count toss decision preferences (bat vs field).
  Plot results using a bar chart.
  
**6.Top Venues (Univariate Analysis)**
  Count matches per venue.
  Display top 5 venues with a horizontal bar chart.
  
**7.Draw Insights**
  Observe patterns in toss decisions.
  Identify teams with consistent winning trends.
  
  # Program 
```
import pandas as pd
# Load the IPL dataset
df = pd.read_csv("matches.csv")
```
```
print("\nQ1. DATASET UNDERSTANDING")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print(df.head())
```
```
print("\nQ2. COLUMNS AND DATA TYPES")
print(df.dtypes)
```
```
print("\nQ4. DATA CLEANING")
print("Missing values:")
print(df.isnull().sum()[df.isnull().sum() > 0])
print("Duplicate records before cleaning:", df.duplicated().sum())

df["city"] = df["city"].fillna("Unknown")
df = df.drop_duplicates().copy()

print("Missing city values after cleaning:", df["city"].isnull().sum())
print("Duplicate records after cleaning:", df.duplicated().sum())
```
```
print("\nQ5. SEASON ANALYSIS")
season_matches = df.groupby("season").size()
print(season_matches)
print("Season with most matches:", season_matches.idxmax())
print("Highest number of matches:", season_matches.max())
```
```
print("\nQ6. TOP 5 WINNING TEAMS")
team_wins = (
    df.dropna(subset=["winner"])
      .groupby("winner")
      .size()

      .sort_values(ascending=False)
)
print(team_wins.head(5))
```
```
print("\nQ7. CSK MATCHES")
csk = df[df["winner"] == "Chennai Super Kings"]
print(csk[["season", "team1", "team2", "winner"]].head(10))
print("Total CSK wins:", len(csk))
```
```
print("\nQ8. TOSS DECISION ANALYSIS")
toss_count = df["toss_decision"].value_counts()
toss_percent = df["toss_decision"].value_counts(normalize=True) * 100
print("Frequency:")
print(toss_count)
print("Percentage:")
print(toss_percent.round(2))
print("Most preferred:", toss_count.idxmax())
```
```
print("\nQ9. SEASON-WISE TOSS ANALYSIS")
toss_season = pd.crosstab(df["season"], df["toss_decision"])
print(toss_season)
print("Most preferred decision by season:")
print(toss_season.idxmax(axis=1))
```
```
print("\nQ10. TOP 5 VENUES")
venues = df.groupby("venue").size().sort_values(ascending=False)
print(venues.head(5))
```
```
print("\nQ11. WINNING MARGIN ANALYSIS")
margin_df = df.dropna(subset=["result_margin"])
largest = margin_df.loc[margin_df["result_margin"].idxmax()]
print("Largest winning margin:", largest["result_margin"])
print(largest[[
    "season", "team1", "team2", "winner",
    "result", "result_margin"
]])

print("\nTop 10 winning margins:")
print(
    margin_df.sort_values("result_margin", ascending=False)
    [["season", "team1", "team2", "winner", "result_margin"]]
    .head(10).to_string(index=False)
)
```
```
print("\nQ12. MATCH RESULT ANALYSIS")
print(df["result"].value_counts())
```
```
print("\nQ13. DATETIME CONVERSION")
print("Before conversion:", df["date"].dtype)
df["date"] = pd.to_datetime(df["date"], errors="coerce")
print("After conversion:", df["date"].dtype)
```
```
print("\nQ14. YEAR EXTRACTION")
df["year"] = df["date"].dt.year
print(df[["date", "year"]].head(10).to_string(index=False))
```
```
df.to_csv("IPL_Matches_Cleaned.csv", index=False)
print("\nCleaned dataset saved as IPL_Matches_Cleaned.csv")
```



  # Output
<img width="776" height="512" alt="Screenshot 2026-11-24 083708" src="https://github.com/user-attachments/assets/c4b2acfc-6df4-4e14-b518-3458929ae52e" />



<img width="777" height="292" alt="Screenshot 2026-11-24 083720" src="https://github.com/user-attachments/assets/b6903810-a833-4133-9654-a892efa6ff0a" />




<img width="415" height="502" alt="Screenshot 2026-11-24 083728" src="https://github.com/user-attachments/assets/050aa5fb-bc8f-4a9e-adf7-14fa10639695" />




<img width="420" height="298" alt="Screenshot 2026-11-24 083943" src="https://github.com/user-attachments/assets/706e0bce-275a-4a3b-929c-5b74c99ca475" />




<img width="412" height="485" alt="Screenshot 2026-11-24 083949" src="https://github.com/user-attachments/assets/c0cf82ac-04b3-4116-a5ba-f559ee8f4da7" />




<img width="392" height="181" alt="Screenshot 2026-11-24 083957" src="https://github.com/user-attachments/assets/71ad38cc-41f4-4f3a-87b2-0f6bea2a6fa0" />




<img width="725" height="552" alt="Screenshot 2026-11-24 084007" src="https://github.com/user-attachments/assets/76be9a9c-9508-4491-9a1d-bbe29bb90abb" />




<img width="386" height="270" alt="Screenshot 2026-11-24 084015" src="https://github.com/user-attachments/assets/adfd6e43-d139-4d47-bc21-2f058129642b" />




<img width="407" height="468" alt="Screenshot 2026-11-24 084027" src="https://github.com/user-attachments/assets/c33ae775-f7d9-461d-a0b1-d61809b9e4a1" />




<img width="301" height="411" alt="Screenshot 2026-11-24 084035" src="https://github.com/user-attachments/assets/613f8041-70b8-40b8-b653-57b3d576a09a" />



<img width="482" height="177" alt="Screenshot 2026-11-24 084041" src="https://github.com/user-attachments/assets/77e0f18a-4770-4cac-a328-751908879124" />



<img width="1105" height="490" alt="Screenshot 2026-11-24 084055" src="https://github.com/user-attachments/assets/4c5f6ae2-c43d-4765-a274-abdcfdca5e5b" />



<img width="383" height="155" alt="Screenshot 2026-11-24 084101" src="https://github.com/user-attachments/assets/ca911a84-18fb-4587-b4a6-532886f3a2c4" />



<img width="361" height="77" alt="Screenshot 2026-11-24 084107" src="https://github.com/user-attachments/assets/1d197101-a0a3-4e5b-b7fd-0b83bc19bab7" />



<img width="260" height="275" alt="Screenshot 2026-11-24 084111" src="https://github.com/user-attachments/assets/50be64ae-8229-483a-b268-ebb6e8b9c178" />




<img width="498" height="33" alt="Screenshot 2026-11-24 084117" src="https://github.com/user-attachments/assets/d169616c-d7e8-4034-9ed6-93d54ae7484e" />


 # Result:
 
  This experiment is executed successfully

