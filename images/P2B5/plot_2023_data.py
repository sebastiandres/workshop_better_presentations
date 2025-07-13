import matplotlib.pyplot as plt
import pandas as pd
import os

# Load the data
data_dict = {"thermal":39506.288, "hydro":3416.997, "wind":701.606, "solar":3210.432, "nuclear":30410.464}
df = pd.DataFrame(data_dict.items(), columns=["source", "value"])

# Sort the bars decreasingly by value
df = df.sort_values(by="value", ascending=True)
# Add a percentage
total = df["value"].sum()
df["percentage"] = 100*df["value"]/total

# Plot the bars
fig, ax = plt.subplots(figsize=(10,6))
ax.barh(df["source"], df["value"], color="lightgrey")

# Remove top and right splines
ax.spines[["top", "right"]].set_visible(False)

# Remove the ticks on the left
ax.tick_params(left=False)

# Change the ticks on the bottom to be multiples of 10000
ax.xaxis.set_major_locator(plt.MultipleLocator(10000))

# Add the format to be multiples of 10,000
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: f"{x:,.0f}"))

# Add gray line to the major ticks
#ax.xaxis.grid(True, linestyle="-", color="gray", alpha=0.25)

# Add the percentage to the total
for i, source in enumerate(df["source"].unique()):
    m = df["source"]==source
    x = df.loc[m, "value"].values[0]
    y = i
    percentage_float = df.loc[m, "percentage"].values[0]
    percentage_str = f"{percentage_float:.1f}%"
    ax.text(x, y, percentage_str)
    print(x, y, percentage_str)

# Add a title
ax.set_title("Czechia Gross Energy Production by source (2023)")

# Add xlabel
ax.set_xlabel("Value (GWh)")

# Save the figure
figname = "2023_data.png"
plt.savefig(figname)
print(f"open {figname}")