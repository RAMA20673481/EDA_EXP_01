# Experiment 1: EDA in IPL Dataset
## Name: G.RAMANUJAM
## Register number: 212224240129
## Aim:
To perform Exploratory Data Analysis (EDA) on the IPL matches dataset and derive insights about matches per season, winning teams, toss decisions, and top venues.

## Algorithm / Procedure:

### 1.Import Libraries
  Import pandas for data handling.
  Import matplotlib and seaborn for visualization.
### 2.Load Dataset
  Use pd.read_csv() to load the IPL matches dataset.
  Check dataset shape using .shape.
  View first 5 rows using .head().
### 3.Matches per Season (Univariate Analysis)
  Group data by season and count matches.
  Plot a bar chart to visualize growth/decline in matches.
### 4.Top Winning Teams (Univariate Analysis)
  Use value_counts() on the winner column.
  Plot top 5 winning teams in a bar chart.
### 5.Toss Decisions (Univariate Analysis)
  Count toss decision preferences (bat vs field).
  Plot results using a bar chart.
### 6.Top Venues (Univariate Analysis)
  Count matches per venue.
  Display top 5 venues with a horizontal bar chart.
### 7.Draw Insights
  Observe patterns in toss decisions.
  Identify teams with consistent winning trends.
  
## Program
  
  #### Load Dataset
  ```
df = pd.read_csv("matches.csv")

print("\nDataset Loaded Successfully!")
```
#### Understanding the Dataset
```
print("\n========== A. UNDERSTANDING THE DATASET ==========")

print("\n1. DATASET SIZE")
print("Number of Rows   :", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nFirst 5 Records:")
print(df.head().to_string())

print("\n2. COLUMNS AND DATA TYPES")
print(df.dtypes.to_string())

print("\n3. UNIQUE IDENTIFIER")
print("Total Records :", len(df))
print("Unique IDs    :", df["id"].nunique())
print("Is ID Unique? :", df["id"].is_unique)
```
####  Data Quality and Cleaning
```
print("\n========== B. DATA QUALITY AND CLEANING ==========")

missing_values = df.isnull().sum()

print(
    missing_values[
        missing_values > 0
    ].to_string()
)

print("Number of Duplicate Rows:",
      df.duplicated().sum())

df["city"] = df["city"].fillna("Unknown")

df = df.drop_duplicates()

print("Missing City values after cleaning:",
      df["city"].isnull().sum())

print("Duplicates after cleaning:",
      df.duplicated().sum())
```

####  Matches Per Season

```
matches_per_season = (
    df.groupby("season")
      .size()
)

print(matches_per_season)

print(matches_per_season.idxmax())
print(matches_per_season.max())
```
#### Matches Per Season Visualization
```
matches_per_season.plot(
    kind="bar",
    figsize=(11,5)
)

plt.title("IPL Matches Per Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

#### Team Performance
```
team_wins = (
    df.dropna(subset=["winner"])
      .groupby("winner")
      .size()
      .sort_values(ascending=False)
)

print(team_wins)

top_5_teams = team_wins.head(5)

print(top_5_teams)
```
### Team Performance Visualization

```python
top_5_teams.plot(
    kind="bar",
    figsize=(9,5)
)

plt.title("Top 5 IPL Teams by Match Wins")
plt.xlabel("Team")
plt.ylabel("Number of Wins")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
```
### Filtering

```python
csk_wins = df[
    df["winner"] == "Chennai Super Kings"
]

print(
    csk_wins[
        ["season","team1","team2","winner"]
    ].head(10).to_string(index=False)
)

print("Total CSK Wins:", len(csk_wins))
```

### Toss Decision Analysis

```python
toss_decisions = (
    df["toss_decision"]
      .value_counts()
)

print(toss_decisions)

toss_percentage = (
    df["toss_decision"]
      .value_counts(normalize=True)
      * 100
)

print(toss_percentage.round(2))
```

### Toss Decision Visualization

```python
toss_decisions.plot(
    kind="bar",
    figsize=(6,4)
)

plt.title("Toss Decision Preference")
plt.xlabel("Decision")
plt.ylabel("Number of Matches")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
```

### Cross Tabulation

```python
toss_by_season = pd.crosstab(
    df["season"],
    df["toss_decision"]
)

print(toss_by_season)

print(
    toss_by_season
    .idxmax(axis=1)
)
```

### Venue Analysis

```python
top_5_venues = (
    df.groupby("venue")
      .size()
      .sort_values(ascending=False)
      .head(5)
)

print(top_5_venues)
```

### Winning Margin Analysis

```python
largest_margin = df["result_margin"].max()

largest_index = df["result_margin"].idxmax()

largest_match = df.loc[largest_index]

print(largest_margin)

print(
    largest_match[
        [
            "season",
            "team1",
            "team2",
            "winner",
            "result",
            "result_margin"
        ]
    ]
)
```

### Top 10 Winning Margins

```python
top_10_margins = (
    df.sort_values(
        by="result_margin",
        ascending=False
    )
    .head(10)
)

print(
    top_10_margins[
        [
            "season",
            "team1",
            "team2",
            "winner",
            "result_margin"
        ]
    ]
)
```

### Match Result Analysis

```python
result_types = (
    df["result"]
      .value_counts()
)

print(result_types)
```

### Data Transformation

```python
df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

df["year"] = df["date"].dt.year

df["win_type"] = (
    df["result"]
      .replace({
          "runs": "Won by Runs",
          "wickets": "Won by Wickets",
          "tie": "Tie",
          "no result": "No Result"
      })
)
```

### Save Cleaned Dataset

```python
df.to_csv(
    "IPL_Matches_Cleaned.csv",
    index=False
)
```

## Output
### Dataset Loaded Successfully

<img width="292" height="45" alt="Screenshot 2026-08-05 190457" src="https://github.com/user-attachments/assets/68cd1c2b-43d8-4f12-8ddb-f4519c25abcb" />

---

### Dataset Information

<img width="622" height="925" alt="Screenshot 2026-08-05 190742" src="https://github.com/user-attachments/assets/d5e4a303-a4e1-4891-94cc-4afb2bd9bb4a" />

---

### Matches per Season

<img width="227" height="450" alt="Screenshot 2026-08-05 190849" src="https://github.com/user-attachments/assets/7846a640-277c-4e86-af53-88e6d24cff65" />

---

<img width="730" height="623" alt="Screenshot 2026-08-05 190914" src="https://github.com/user-attachments/assets/5fdf8b56-e22a-4471-8741-79acf194f7ec" />

---

### Top 5 Winning Teams

<img width="790" height="782" alt="image" src="https://github.com/user-attachments/assets/41e0c02a-61b5-4edd-8cd9-7d594feab969" />

---

### Toss Decision Analysis

<img width="731" height="563" alt="Screenshot 2026-08-05 193206" src="https://github.com/user-attachments/assets/575c1318-6d81-4758-8996-70d82ef8cce0" />

---

### Cross-Tabulation

<img width="285" height="405" alt="image" src="https://github.com/user-attachments/assets/dfc6a0c4-6dfa-4d2b-83c9-e37e86efee25" />

---

### Top 5 Venues

<img width="461" height="148" alt="Screenshot 2026-08-05 193849" src="https://github.com/user-attachments/assets/fd124917-5dc7-4346-bf27-ce955e8e561e" />

---

### Winning Margin Analysis

<img width="732" height="648" alt="Screenshot 2026-08-05 194019" src="https://github.com/user-attachments/assets/236524c7-548b-49dc-9483-3d8f868bd141" />

---

### Match Result Analysis

<img width="262" height="137" alt="Screenshot 2026-08-05 194104" src="https://github.com/user-attachments/assets/97c1b34b-e498-4143-aa80-65a14b442500" />

---

### Data Transformation

<img width="452" height="387" alt="Screenshot 2026-08-05 194152" src="https://github.com/user-attachments/assets/63a0009f-b1bf-4b8b-affa-a9de6d909152" />

---
## Result
Thus, the Exploratory Data Analysis (EDA) on the IPL matches dataset was performed successfully.
The analysis identified the number of matches played each season, the top winning teams, toss decision preferences,
the most frequently used venues, and key insights from the data.
