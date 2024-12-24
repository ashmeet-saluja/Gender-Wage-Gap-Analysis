#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Gender_Wage_Gap_Analysis_Dataset_with_Disparities.csv")

# Step 1: Explore the Dataset
print("Dataset Overview:\n", df.head())
print("\nDataset Summary:\n", df.describe())
print("\nMissing Values:\n", df.isnull().sum())

# Step 2: Calculate Average Salaries by Gender
average_salary_by_gender = df.groupby("Gender")["Base_Salary"].mean().sort_values()
print("\nAverage Salary by Gender:\n", average_salary_by_gender)

# Step 3: Calculate Gender Pay Gap
try:
    male_salary = average_salary_by_gender.get("Male", 0)
    female_salary = average_salary_by_gender.get("Female", 0)
    pay_gap = (male_salary - female_salary) / male_salary * 100 if male_salary > 0 else 0
    print(f"\nGender Pay Gap: {pay_gap:.2f}%")
except ZeroDivisionError:
    print("\nError calculating pay gap: Division by zero.")

# Step 4: Visualization - Average Salaries by Gender
plt.figure(figsize=(8, 6))
average_salary_by_gender.plot(kind="bar", color=["blue", "pink", "grey"])
plt.title("Average Salary by Gender", fontsize=16)
plt.ylabel("Average Salary", fontsize=12)
plt.xlabel("Gender", fontsize=12)
plt.xticks(rotation=0)
plt.show()

# Step 5: Salary by Gender and Position
salary_by_gender_position = df.groupby(["Gender", "Position"])["Base_Salary"].mean().unstack()
salary_by_gender_position.plot(kind="bar", figsize=(12, 6), stacked=True, colormap="viridis")
plt.title("Average Salary by Gender and Position", fontsize=16)
plt.ylabel("Average Salary", fontsize=12)
plt.xlabel("Position", fontsize=12)
plt.legend(title="Gender", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Step 6: Salary Distribution by Gender
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x="Base_Salary", hue="Gender", fill=True, common_norm=False, alpha=0.5)
plt.title("Salary Distribution by Gender", fontsize=16)
plt.xlabel("Base Salary", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.legend(title="Gender")
plt.show()

# Step 7: Experience vs. Salary by Gender
plt.figure(figsize=(10, 6))
valid_data_found = False  # Track valid data points
for gender in df["Gender"].unique():
    subset = df[df["Gender"] == gender]
    if not subset.empty:
        valid_data_found = True
        plt.scatter(subset["Experience_Years"], subset["Base_Salary"], alpha=0.6, label=f"{gender} ({len(subset)} records)")

if valid_data_found:
    plt.title("Experience vs. Salary by Gender", fontsize=16)
    plt.xlabel("Years of Experience", fontsize=12)
    plt.ylabel("Base Salary", fontsize=12)
    plt.legend(title="Gender", loc="upper left")
    plt.show()
else:
    print("\nNo valid data points found for any gender to plot.")

# Step 8: Identify Employees with Below-Average Salaries
low_salary_employees = df[df["Base_Salary"] < df.groupby(["Gender", "Position"])["Base_Salary"].transform("mean")]
print("\nEmployees with Below-Average Salaries:\n", low_salary_employees[["Name", "Gender", "Position", "Base_Salary"]].head())

# Step 9: Save Data for Tableau Dashboard
dashboard_data = df.groupby(["Gender", "Position"])["Base_Salary"].mean().reset_index()
dashboard_data.to_csv("Tableau_Gender_Salary_Data.csv", index=False)
print("\nData saved for Tableau dashboard: 'Tableau_Gender_Salary_Data.csv'")


# In[ ]:




