import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)

df.head() # First 5 rows
df.tail() # Last 5 rows

df.shape # Number of rows and columns

df.count() # Number of entries in each column

# Sum of each tag from highest to lowest
df.groupby("TAG").sum().sort_values("POSTS", ascending=False)

df.groupby("TAG").count().sort_values("DATE")

# Acceptable calling
df["DATE"][1]
df.DATE[1]

# Convert (str) date to datetime
df["DATE"] = pd.to_datetime(df["DATE"])
df["DATE"].head()

# Restructuring the data
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.fillna(0, inplace=True) # To add 0 to the places with NaN
reshaped_df.shape
reshaped_df.columns
reshaped_df.count()

reshaped_df.isna().values.any() # Single return for if there are any NaN values

# Working with mathplotlib
# plt.figure(figsize=(16,9))
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
# plt.xlabel('Date', fontsize=14)
# plt.ylabel('Number of Posts', fontsize=14)
# plt.ylim(0, 35000)

# plt.plot(reshaped_df.index, reshaped_df["java"], "b")
# plt.plot(reshaped_df.index, reshaped_df["python"], "g")

# for column in reshaped_df.columns:
#     plt.plot(reshaped_df.index, reshaped_df[column], linewidth=2, label=reshaped_df[column].name.title())
#     # Adding the label allows us to use a legend like below
# plt.legend(fontsize=16) 

# Smoothing out the data
# The window is number of observations that are averaged
roll_df = reshaped_df.rolling(window=12).mean()
 
plt.figure(figsize=(16,9))
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
 
# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], linewidth=2, label=roll_df[column].name)

plt.legend(fontsize=16)







