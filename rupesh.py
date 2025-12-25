import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. DATA SETUP
# -----------------------------
data = {
    "Employee": ["A", "B", "C", "D", "E"],
    "Q1": [70, 85, 60, 90, 75],
    "Q2": [75, 88, 65, 92, 78],
    "Q3": [80, 90, 70, 95, 82],
    "Q4": [85, 92, 72, 97, 88],
}

df = pd.DataFrame(data)
df.set_index("Employee", inplace=True)

# -----------------------------
# 2. PERFORMANCE CALCULATIONS
# -----------------------------
df["Average"] = np.mean(df, axis=1)
overall_average = df["Average"].mean()
quarter_average = df.drop(columns="Average").mean()

# -----------------------------
# 3. TEXT INSIGHTS
# -----------------------------
print("\n📌 EMPLOYEE PERFORMANCE SUMMARY\n")
print(df)

print("\n📌 QUARTER-WISE AVERAGE PERFORMANCE\n")
print(quarter_average)

print("\n📌 OVERALL AVERAGE PERFORMANCE:", round(overall_average, 2))

# Improvement areas
improvement_needed = df[df["Average"] < overall_average]

print("\n⚠ EMPLOYEES NEEDING IMPROVEMENT\n")
print(improvement_needed if not improvement_needed.empty else "None")

# -----------------------------
# 4. VISUALIZATIONS
# -----------------------------

# A. Performance Trend
plt.figure()
for emp in df.index:
    plt.plot(["Q1", "Q2", "Q3", "Q4"],
             df.loc[emp][["Q1", "Q2", "Q3", "Q4"]],
             marker='o',
             label=emp)

plt.title("Performance Trend Over Time")
plt.xlabel("Quarter")
plt.ylabel("Performance Score")
plt.legend()
plt.grid(True)
plt.show()

# B. Average Performance Comparison
plt.figure()
df["Average"].plot(kind="bar")
plt.axhline(overall_average, linestyle="--", label="Overall Average")

plt.title("Average Performance Comparison")
plt.ylabel("Score")
plt.legend()
plt.show()

# C. Quarter-wise Performance
plt.figure()
quarter_average.plot(kind="bar")

plt.title("Quarter-wise Average Performance")
plt.ylabel("Score")
plt.show()

# D. Performance Heatmap
plt.figure()
plt.imshow(df.drop(columns="Average"), aspect="auto")
plt.colorbar(label="Score")

plt.xticks(range(4), ["Q1", "Q2", "Q3", "Q4"])
plt.yticks(range(len(df.index)), df.index)

plt.title("Performance Heatmap")
plt.show()
