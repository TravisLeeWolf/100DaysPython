import pandas as pd
df = pd.read_csv("salaries_by_college_major.csv")

df.head() # Returns the first 5 entries of our dataframe
df.shape # To get number of rows and columns in dataframe
df.columns # Gives us the title of our columns
df.isna() # Looks for NAN (Not A Number) cells and returns true if any
df.tail() # Returns the last 5 entries of our dataframe

# Deleting rows
clean_df = df.dropna()

clean_df["Starting Median Salary"].max() # Get data from a column and return max

# Get ID of row with largest value
maxRow = clean_df["Starting Median Salary"].idxmax()
clean_df["Undergraduate Major"].loc[maxRow]
# We can access the same data in this way too
clean_df["Undergraduate Major"][maxRow]

# If we want the full row
clean_df.loc[maxRow]

# What college major has the highest mid-career salary?
# How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).
midCareerMaxRow = clean_df["Mid-Career Median Salary"].idxmax()
midCareerMajor = clean_df["Undergraduate Major"][midCareerMaxRow]
midCareerSalary = clean_df["Mid-Career Median Salary"][midCareerMaxRow]
print(f"The college major with highest mid-career salary is {midCareerMajor} with a salary of ${midCareerSalary}.")

# Which college major has the lowest starting salary and how much do graduates earn after university?
startingLowRow = clean_df["Starting Median Salary"].idxmin()
startingLowMajor = clean_df["Undergraduate Major"][startingLowRow]
startingLowSalary = clean_df["Mid-Career Median Salary"][startingLowRow]
print(f"The college major with lowest starting salary is {startingLowMajor} with a salary of ${startingLowSalary}.")

# Which college major has the lowest mid-career salary and how much can people expect to earn with this degree? 
midLowRow = clean_df["Mid-Career Median Salary"].idxmin()
midLowMajor = clean_df["Undergraduate Major"][midLowRow]
midLowSalary = clean_df["Mid-Career Median Salary"][midLowRow]
print(f"The college major with lowest mid-career salary is {midLowMajor} with a salary of ${midLowSalary}.")

# Getting the lowest risk career
spreadColumn = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spreadColumn)
clean_df.head()

# Sorting by the lowest spead
lowRisk = clean_df.sort_values('Spread')
lowRisk[['Undergraduate Major', 'Spread']].head()

# Using the .sort_values() method, can you find the degrees with the highest potential?
# Find the top 5 degrees with the highest values in the 90th percentile. 
highEarningPotential = clean_df.sort_values("Mid-Career 90th Percentile Salary", ascending=False)
highEarningPotential[["Undergraduate Major", "Mid-Career 90th Percentile Salary"]].head()

# Also, find the degrees with the greatest spread in salaries. 
# Which majors have the largest difference between high and low earners after graduation.
greatestSpread = clean_df.sort_values("Spread", ascending=False)
greatestSpread[["Undergraduate Major", "Spread"]].head()

# We can format the result using this
pd.options.display.float_format = "{:,.2f}".format
# Finding the averages between groups
clean_df.groupby("Group").mean().sort_values("Mid-Career Median Salary", ascending=False)

