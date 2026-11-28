# =====================================================================
#
#    ____      _    ___ _     ____    ___    ____    _   _   ____  _____ ____
#   |  _ \    / \  |_ _| |   / ___|  ( _ )  / ___|  /_\ | | |/ ___|| ____/ ___|
#   | |_) |  / _ \  | || |   \___ \  / _ \/\ |  _  / _ \| | | |  _ |  _| \___ \
#   |  _ <  / ___ \ | || |___ ___) || (_>  < |_| |/ ___ \ |_| |_| || |___ ___) |
#   |_| \_\/_/   \_\___|_____|____/  \___/\/\____/_/   \_\___/\____||_____|____/
#
#   ======================  RAILS & GAUGES  ============================
#
#   PROJECT NAME : RAILS & GAUGES - A Data Journey Along the Tracks
#   DATASET      : railway_gauges.csv  (Year, Broad / Metre / Narrow Gauge, Total)
#   TOOLS USED   : Pandas (data), NumPy (maths), Matplotlib (graphs)
#   STORY: Railway tracks come in different widths called "gauges".
#          In this project we load the data, clean it, draw graphs and
#          finally answer one big question:
#          "Is the railway moving towards ONE dominant gauge?"
#
#          _______       _______       _______       _______
#     ____|_______|_____|_______|_____|_______|_____|_______|____
#     ====o=o===========o=o===========o=o===========o=o==========
#
#   HOW TO RUN : keep this main.py and the CSV file in the same folder, then
#                python main.py
#   NOTE       : All graphs are saved automatically inside a folder called
#                "graphs"
# =====================================================================


# =====================================================================
# IMPORTS  (everything the project needs, with the reason for each)
# =====================================================================
import os                          # to create the "graphs" folder
import pandas as pd                # to load the CSV and work with tables (DataFrame)
import numpy as np                 # for maths: np.diff, np.arange, np.polyfit
import matplotlib.pyplot as plt    # to draw and save the graphs


# =====================================================================
# SETTINGS  (change them here only, nowhere else)
# =====================================================================
CSV_FILE = "railway_gauges.csv"      # name of the dataset file
GRAPH_FOLDER = "graphs"                # folder where all graphs will be saved

# The three gauge columns are used again and again, so keep them in one list
GAUGES = ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]

# Create the graphs folder. exist_ok=True means "no error if it already exists"
os.makedirs(GRAPH_FOLDER, exist_ok=True)


# =====================================================================
# SCENARIO 1 : Basic Data Loading & Cleaning
# =====================================================================
"""You are given a CSV file containing railway gauge data. 
Tasks: 
1. Load the dataset into a Pandas DataFrame. 
2. Display the first 5 rows and column names. 
3. Check for missing values and replace them with 0. 
4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types."""

print("\n" + "=" * 60)
print("SCENARIO 1 : Basic Data Loading & Cleaning")
print("=" * 60)

# 1. Load the dataset into a Pandas DataFrame
df = pd.read_csv(CSV_FILE)

# 2. Display the first 5 rows and the column names
print("\nFirst 5 rows:")
print(df.head())                       # head() shows the first 5 rows by default

print("\nColumn names:")
print(list(df.columns))

# 3. Check for missing values and replace them with 0
print("\nMissing values in each column (before):")
print(df.isnull().sum())               # isnull().sum() counts empty cells per column

df = df.fillna(0)                      # fillna(0) replaces every empty cell with 0

# 4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types
numeric_columns = GAUGES + ["Total"]
for col in numeric_columns:
    # to_numeric converts text like "3521" into a number.
    # errors="coerce" turns anything that is not a number into NaN,
    # and the fillna(0) after it makes that NaN a 0 again.
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

print("\nMissing values in each column (after):")
print(df.isnull().sum())
print("\nData types after conversion:")
print(df.dtypes)

# EXTRA HELPER COLUMN used in later scenarios:
# The Year column looks like "1964-65" (text). Taking the first 4 letters
# gives the starting year as a number (1964), which lets us compare years.
df["Start_Year"] = df["Year"].str[:4].astype(int)


# =====================================================================
# SCENARIO 2 : Simple Visualization (Total track growth)
# =====================================================================
"""You want a quick understanding of total railway track growth. 
Tasks: 
1. Extract Year and Total columns. 
2. Plot a line graph showing Total tracks over years. 
3. Add: 
○ Title 
○ X and Y labels 
4. Identify whether the trend is increasing or decreasing."""

print("\n" + "=" * 60)
print("SCENARIO 2 : Total Track Growth (Line Graph)")
print("=" * 60)

# 1. Extract Year and Total columns
year_total = df[["Year", "Total"]]
print(year_total.head())

# 2. Plot a line graph of Total tracks over the years
plt.figure(figsize=(10, 5))
plt.plot(year_total["Year"], year_total["Total"], marker="o", color="darkblue")

# 3. Add title, X label and Y label
plt.title("Total Railway Tracks Over the Years")
plt.xlabel("Year")
plt.ylabel("Total Tracks")

# There are 49 year names, so showing all of them would overlap.
# We show every 4th year and rotate them for readability.
plt.xticks(range(0, len(df), 4), df["Year"][::4], rotation=45)
plt.grid(True)
plt.tight_layout()

plt.savefig(os.path.join(GRAPH_FOLDER, "total_tracks_line.png"))   # save the graph
plt.show()                                                          # show the graph
plt.close()

# 4. Identify whether the trend is increasing or decreasing
# Method 1: compare the first year with the last year
first_total = df["Total"].iloc[0]                 # total in the first year
last_total = df["Total"].iloc[-1]                 # total in the last year
change = last_total - first_total
print("\nFirst year total :", first_total)
print("Last year total  :", last_total)
print("Overall change   :", change)

# Method 2: np.polyfit(x, y, 1) draws the best straight line through the data.
# The first value it returns is the slope: slope > 0 means the line goes UP.
x_numbers = np.arange(len(df))                    # 0, 1, 2, ... for each year
slope = np.polyfit(x_numbers, df["Total"], 1)[0]
print("Trend line slope :", round(slope, 2), "per year")

if change > 0:
    print("Trend: INCREASING overall (first year -> last year).")
else:
    print("Trend: DECREASING overall (first year -> last year).")

# The slope is almost 0, so the total is nearly flat around 7000.
# The line goes up and down (it dips in the late 1990s and recovers after 2000),
# so the growth is small and not steady.
if abs(slope) < 1:
    print("Note: the fitted line is almost flat, so growth is small and uneven.")


# =====================================================================
# SCENARIO 3 : Filtering + Bar Chart (Modern railway expansion)
# =====================================================================
"""You are asked to analyze modern railway expansion. 
Tasks: 
1. Filter the dataset for years after 2000. 
2. Select Broad Gauge, Metre Gauge, and Narrow Gauge. 
3. Plot a grouped bar chart comparing all three gauges. 
4. Add legend and proper labels. 
5. Identify which gauge dominates in recent years."""

print("\n" + "=" * 60)
print("SCENARIO 3 : Years after 2000 (Grouped Bar Chart)")
print("=" * 60)

# 1. Filter the dataset for years after 2000
# Start_Year > 2000 keeps 2001-02 onwards (2000-01 is not "after" 2000)
recent = df[df["Start_Year"] > 2000]

# 2. Select Year and the three gauges
recent = recent[["Year"] + GAUGES]
print(recent)

# 3. Grouped bar chart: three bars (one per gauge) side by side for every year
x_positions = np.arange(len(recent))     # one position per year: 0, 1, 2, ...
bar_width = 0.25                         # width of each single bar

plt.figure(figsize=(12, 6))
# Each gauge is shifted left/right so the three bars do not sit on each other
plt.bar(x_positions - bar_width, recent["Broad Gauge"], bar_width, label="Broad Gauge")
plt.bar(x_positions,             recent["Metre Gauge"], bar_width, label="Metre Gauge")
plt.bar(x_positions + bar_width, recent["Narrow Gauge"], bar_width, label="Narrow Gauge")

# 4. Add legend and proper labels
plt.title("Railway Gauges After 2000")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.xticks(x_positions, recent["Year"], rotation=45)   # year names under the bars
plt.legend()
plt.tight_layout()

plt.savefig(os.path.join(GRAPH_FOLDER, "gauges_after_2000_bar.png"))
plt.show()
plt.close()

# 5. Identify which gauge dominates in recent years
# Add up each gauge over the recent years and pick the biggest one
recent_totals = recent[GAUGES].sum()
print("\nSum of each gauge after 2000:")
print(recent_totals)
print("Dominant gauge in recent years:", recent_totals.idxmax())


# =====================================================================
# SCENARIO 4 : Feature Engineering + Pie Chart (Contribution of each gauge)
# =====================================================================
"""You want to analyze the contribution of each gauge type. 
Tasks: 
1. Calculate total sum of each gauge across all years. 
2. Create a new structure (Series/DataFrame) for totals. 
3. Plot a pie chart showing percentage contribution. 
4. Add percentage labels (autopct). 
5. Interpret which gauge contributes the most."""

print("\n" + "=" * 60)
print("SCENARIO 4 : Contribution of Each Gauge (Pie Chart)")
print("=" * 60)

# 1 & 2. Total of each gauge across ALL years, stored as a new Series
gauge_totals = df[GAUGES].sum()
print(gauge_totals)

# 3 & 4. Pie chart with percentage labels
# autopct="%1.1f%%" writes the percentage with one decimal on every slice
plt.figure(figsize=(7, 7))
plt.pie(gauge_totals, labels=gauge_totals.index, autopct="%1.1f%%", startangle=90)
plt.title("Contribution of Each Gauge (All Years)")

plt.savefig(os.path.join(GRAPH_FOLDER, "gauge_contribution_pie.png"))
plt.show()
plt.close()

# 5. Interpret which gauge contributes the most
top_gauge = gauge_totals.idxmax()
top_percent = gauge_totals.max() / gauge_totals.sum() * 100
print(f"\nInterpretation: {top_gauge} contributes the most "
      f"({top_percent:.1f}% of all gauge track).")


# =====================================================================
# SCENARIO 5 : Advanced Analysis + Multiple Graphs
# =====================================================================
"""You are asked to perform a complete analysis of railway trends. 
Tasks: 
1. Create new columns: 
○ % Broad Gauge 
○ % Metre Gauge 
○ % Narrow Gauge 
2. Use NumPy (np.diff) to calculate yearly growth of Total tracks. 
3. Plot: 
○ Line graph for all gauges 
○ Stacked bar chart showing composition 
4. Highlight: 
○ Years with highest growth 
○ Decline in any gauge 
5. Provide a final conclusion: 
Is the railway system shifting towards a single dominant gauge?"""

print("\n" + "=" * 60)
print("SCENARIO 5 : Advanced Analysis + Multiple Graphs")
print("=" * 60)

# ---- 1. New columns: percentage of each gauge in the Total ----
df["% Broad Gauge"] = df["Broad Gauge"] / df["Total"] * 100
df["% Metre Gauge"] = df["Metre Gauge"] / df["Total"] * 100
df["% Narrow Gauge"] = df["Narrow Gauge"] / df["Total"] * 100
print(df[["Year", "% Broad Gauge", "% Metre Gauge", "% Narrow Gauge"]].round(1).head())

# ---- 2. Yearly growth of Total tracks using np.diff ----
# np.diff gives (next value - current value), so for 49 years we get 48 values.
# That is why the growth is matched with the years from the 2nd year onwards.
growth = np.diff(df["Total"].values)
growth_years = df["Year"].values[1:]

# ---- 3a. Line graph for all gauges ----
# Highest growth years: argsort sorts from small to big, [-3:] takes the 3 biggest
top3_index = np.argsort(growth)[-3:]
print("\nYears with the highest growth in Total tracks:")
for i in top3_index[::-1]:                       # [::-1] shows biggest first
    print(f"  {growth_years[i]}  ->  +{growth[i]}")

plt.figure(figsize=(11, 6))
for gauge in GAUGES + ["Total"]:
    plt.plot(df["Year"], df[gauge], label=gauge)

# HIGHLIGHT: draw a light red band behind each of the highest growth years
for i in top3_index:
    plt.axvspan(i + 1 - 0.5, i + 1 + 0.5, color="red", alpha=0.25)
plt.plot([], [], color="red", alpha=0.25, linewidth=8, label="Highest growth years")

plt.title("Railway Gauges Trend (All Gauges)")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.xticks(range(0, len(df), 4), df["Year"][::4], rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(os.path.join(GRAPH_FOLDER, "all_gauges_line.png"))
plt.show()
plt.close()

# ---- 3b. Stacked bar chart showing composition (in percentage) ----
# Each bar always reaches 100%, so we can clearly see how the share
# of each gauge changes with time.
plt.figure(figsize=(11, 6))
bottom_values = np.zeros(len(df))            # where the next layer should start
for col, color in zip(["% Broad Gauge", "% Metre Gauge", "% Narrow Gauge"],
                      ["tab:blue", "tab:orange", "tab:green"]):
    plt.bar(df["Year"], df[col], bottom=bottom_values, label=col, color=color)
    bottom_values = bottom_values + df[col].values   # next layer sits on top

plt.title("Composition of Railway Gauges (Stacked Bar)")
plt.xlabel("Year")
plt.ylabel("Percentage of Total (%)")
plt.xticks(range(0, len(df), 4), df["Year"][::4], rotation=45)
plt.ylim(0, 118)                             # extra space above 100% for the legend
plt.legend(loc="upper center", ncol=3)       # legend sits above the bars, not on them
plt.tight_layout()

plt.savefig(os.path.join(GRAPH_FOLDER, "gauge_composition_stacked.png"))
plt.show()
plt.close()

# ---- 4a. Highlight: yearly growth graph (green = top 3 growth, red = decline) ----
bar_colors = []
for i in range(len(growth)):
    if i in top3_index:
        bar_colors.append("green")           # highest growth years
    elif growth[i] < 0:
        bar_colors.append("red")             # years in which Total decreased
    else:
        bar_colors.append("lightgray")       # normal years

plt.figure(figsize=(11, 5))
plt.bar(growth_years, growth, color=bar_colors)
plt.axhline(0, color="black", linewidth=0.8)   # zero line
plt.title("Yearly Growth of Total Tracks (Green = Highest, Red = Decline)")
plt.xlabel("Year")
plt.ylabel("Change in Total Tracks")
plt.xticks(range(0, len(growth_years), 4), growth_years[::4], rotation=45)
plt.tight_layout()

plt.savefig(os.path.join(GRAPH_FOLDER, "yearly_growth_highlight.png"))
plt.show()
plt.close()

# ---- 4b. Highlight: decline in any gauge ----
print("\nDecline check for each gauge (np.diff < 0 means the gauge shrank):")
for gauge in GAUGES:
    change = np.diff(df[gauge].values)
    decline_count = (change < 0).sum()            # in how many years it decreased
    biggest_drop = change.min()                   # the largest single-year fall
    drop_year = growth_years[change.argmin()]     # the year when that fall happened
    print(f"  {gauge}: declined in {decline_count} of {len(change)} years, "
          f"biggest drop {biggest_drop} in {drop_year}")

# ---- 5. Final conclusion ----
first_broad = df["% Broad Gauge"].iloc[0]         # broad gauge share in first year
last_broad = df["% Broad Gauge"].iloc[-1]         # broad gauge share in last year
print(f"\nBroad Gauge share: {first_broad:.1f}% in {df['Year'].iloc[0]}  ->  "
      f"{last_broad:.1f}% in {df['Year'].iloc[-1]}")

print("\nFINAL CONCLUSION:")
print("Is the railway system shifting towards a single dominant gauge?")
if last_broad > first_broad and last_broad > 50:
    print("YES. Broad Gauge keeps growing and now makes up most of the network,")
    print("while Metre Gauge and Narrow Gauge keep shrinking over the years.")
else:
    print("NO. No single gauge is clearly taking over the network.")

# =====================================================================
#   END OF PROJECT - RAILS & GAUGES
#   All 5 scenarios done. Check the "graphs" folder for the saved images.
# =====================================================================
