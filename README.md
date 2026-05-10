# 📊 Student Data Analysis & Report Generator

A Python-based **Student Data Analysis Tool** built using **Pandas** and **NumPy** that reads student data from a CSV file, cleans it, adds intelligent features like grades and pass/fail status, and generates a detailed city-wise report.

---

## 🚀 Features

- 📂 Load student data from CSV file
- 🔍 Understand the dataset — shape, info, description, sample rows
- 🧹 Clean data — handle null values and remove duplicates
- 🏅 Auto-assign **Grades** (A / B / C / Fail) based on marks
- ✅ Auto-assign **Pass/Fail Status** based on marks
- 📋 Generate detailed **Report Card** including:
  - Top 5 students by marks
  - List of all failed students
  - Average marks per city
  - Topper (max marks) per city
  - Total students per city

---

## 🛠️ Technologies Used

- **Language:** Python 3
- **Libraries:** Pandas, NumPy
- **Concepts:** Data Cleaning, Feature Engineering, GroupBy Analysis, CSV Handling

---

## 📌 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/priyanshupatel-tech/Student-Data-Analysis.git
   cd Student-Data-Analysis
   ```

2. Install required libraries:
   ```bash
   pip install pandas numpy
   ```

3. Make sure `student.csv` is in the same folder, then run:
   ```bash
   python analysis.py
   ```

---

## 🖥️ Menu Options

```
=================================== Menu ===================================
1. Understand Data Frame
2. Cleaned Data
3. Report Card of Data Frame
4. Exit
```

---

## 🧠 Grading Logic

| Marks | Grade |
|-------|-------|
| > 90  | A     |
| > 75  | B     |
| > 50  | C     |
| ≤ 50  | Fail  |

| Marks | Status |
|-------|--------|
| > 50  | Pass   |
| ≤ 50  | Fail   |

---

## 🖥️ Sample Report Output

```
========================== Report of Student ===============================
-------------------------- Top 5 Student ----------------------------------
   Name        City   Marks  Status  Grades
   Priya       Delhi   98     Pass     A
   Rahul       Mumbai  95     Pass     A
   ...

-------------------------- Fail Student ------------------------------------
   Name        City    Marks  Status  Grades
   Ankit       Pune    40     Fail    Fail
   ...

------------------------ Average Marks of Each City -------------------------
City
Delhi     78.5
Mumbai    82.3
...

------------------------- Total Student of Each City -----------------------
City
Delhi     45
Mumbai    38
...
```

---

## 📂 Project Structure

```
Student-Data-Analysis/
│
├── analysis.py      # Main application file
├── student.csv      # Input dataset (student records)
└── README.md
```

---

## 💡 Learning Outcomes

- Reading and exploring real-world CSV data using Pandas
- Cleaning data — handling null values with `fillna()` and removing duplicates
- Feature engineering using `np.where()` for conditional columns
- Performing GroupBy analysis for city-wise insights
- Building a complete data analysis pipeline in Python

---

## 👨‍💻 Author

**Priyanshu Patel**
- 🔗 [LinkedIn](https://www.linkedin.com/in/priyanshupatel-tech/)
- 💻 [GitHub](https://github.com/priyanshupatel-tech)
