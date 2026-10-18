import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample dataset
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Fatima", "Usman",
             "Ayesha", "Bilal", "Zara", "Hamza", "Noor"],
    "Study_Hours": [2, 5, 3, 7, 4, 6, 1, 8, 3, 5],
    "Attendance": [70, 95, 75, 98, 80, 90, 60, 99, 72, 88],
    "Marks": [55, 90, 65, 96, 72, 88, 45, 98, None, 84]
}

df = pd.DataFrame(data)

# Save the original dataset
df.to_csv("students.csv", index=False)

print("First five rows:")
print(df.head())

print("\nDataset information:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())

# Fill missing marks with the median
df["Marks"] = df["Marks"].fillna(df["Marks"].median())

print("\nSummary statistics:")
print(df[["Study_Hours", "Attendance", "Marks"]].describe())

# Sort students by marks
df = df.sort_values("Marks", ascending=False)

print("\nStudents sorted by marks:")
print(df[["Name", "Marks"]])

# Students who scored at least 80
top_students = df[df["Marks"] >= 80]

print("\nStudents scoring at least 80:")
print(top_students[["Name", "Marks"]])

# Visualize marks
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Name", y="Marks")
plt.title("Marks by Student")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("student_marks.png")
plt.show()

# Visualize study hours and marks
plt.figure(figsize=(7, 5))
sns.regplot(data=df, x="Study_Hours", y="Marks")
plt.title("Study Hours vs Marks")
plt.tight_layout()
plt.savefig("study_hours_vs_marks.png")
plt.show()

# Correlation heatmap
plt.figure(figsize=(7, 5))
sns.heatmap(
    df[["Study_Hours", "Attendance", "Marks"]].corr(),
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)
plt.title("Student Data Correlations")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

# Save cleaned dataset
df.to_csv("cleaned_students.csv", index=False)

print("\nAnalysis completed!")
print("Saved: students.csv")
print("Saved: cleaned_students.csv")
print("Saved: student_marks.png")
print("Saved: study_hours_vs_marks.png")
print("Saved: correlation_heatmap.png")