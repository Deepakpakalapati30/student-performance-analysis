import pandas as pd
df = pd.read_csv("Day7(Proj)/students_performance.csv")
print(df)
print(df.isnull().sum())
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print(df)
avg_marks = df.groupby("Department")["Marks"].mean()
print(avg_marks)

import matplotlib.pyplot as plt
avg_marks.plot(kind="bar")

plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.title("Average Marks by Department")

plt.show()