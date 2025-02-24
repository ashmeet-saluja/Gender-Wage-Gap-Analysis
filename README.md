## Gender-Wage-Gap-Analysis

## Overview
This project analyzes the gender wage gap using a synthetic dataset of employee records across various industries and positions. The analysis aims to quantify disparities in salaries between genders, identify key factors contributing to these differences, and provide actionable insights to reduce inequities in the workplace.

## Key Features
Dataset:

Includes over 50,000 synthetic employee records with attributes such as gender, position, base salary, bonus, years of experience, and more.
Simulates real-world gender pay disparities for analysis.
Analysis:

Quantifies the gender pay gap across various roles and industries.
Visualizes salary distributions, average salaries by gender, and the relationship between experience and salary.
Identifies employees earning below the average salary for their gender and position.
Visualizations:

Bar Charts: Average salaries by gender and by position.
KDE Plot: Salary distribution for each gender.
Scatter Plot: Experience vs. salary by gender.
Dashboard Integration:

Saves processed data for further visualization in tools like Tableau.
Technologies Used
Python Libraries:
Pandas for data manipulation and aggregation.
Matplotlib and Seaborn for creating visualizations.
File Handling:
Outputs data in CSV format for dashboard creation.
Project Structure

##Code:
analysis.py: Python script for data analysis and visualization.
Outputs:
Tableau_Gender_Salary_Data.csv: Processed data ready for visualization in Tableau.
How to Use
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/gender-wage-gap-analysis.git
Install the required Python libraries:
bash
Copy code
pip install pandas matplotlib seaborn
Run the analysis script:
bash
Copy code
python analysis.py
Open the output CSV (Tableau_Gender_Salary_Data.csv) in Tableau or any visualization tool to create dashboards.
Insights
This project highlights:

Salary inequities across genders and roles.
The influence of experience and position on wage disparities.
Data-driven recommendations for closing the gender pay gap.
Contributing
Contributions to improve the dataset, analysis, or visualizations are welcome. Please create a pull request or open an issue to discuss your ideas.

## License
This project is open-source and available under the MIT License.
