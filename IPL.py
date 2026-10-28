#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("matches.csv")
print("\nDataset Loaded Successfully!")


# In[9]:


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


# In[10]:


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


# In[11]:


matches_per_season = (
    df.groupby("season")
      .size()
)

print(matches_per_season)

print(matches_per_season.idxmax())
print(matches_per_season.max())


# In[12]:


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


# In[13]:


team_wins = (
    df.dropna(subset=["winner"])
      .groupby("winner")
      .size()
      .sort_values(ascending=False)
)

print(team_wins)

top_5_teams = team_wins.head(5)

print(top_5_teams)


# In[14]:


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


# In[15]:


csk_wins = df[
    df["winner"] == "Chennai Super Kings"
]

print(
    csk_wins[
        ["season","team1","team2","winner"]
    ].head(10).to_string(index=False)
)

print("Total CSK Wins:", len(csk_wins))


# In[16]:


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


# In[17]:


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


# In[18]:


toss_by_season = pd.crosstab(
    df["season"],
    df["toss_decision"]
)

print(toss_by_season)

print(
    toss_by_season
    .idxmax(axis=1)
)


# In[19]:


top_5_venues = (
    df.groupby("venue")
      .size()
      .sort_values(ascending=False)
      .head(5)
)

print(top_5_venues)


# In[20]:


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


# In[21]:


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


# In[22]:


result_types = (
    df["result"]
      .value_counts()
)

print(result_types)


# In[23]:


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


# In[24]:


df.to_csv(
    "IPL_Matches_Cleaned.csv",
    index=False
)


# In[ ]:




