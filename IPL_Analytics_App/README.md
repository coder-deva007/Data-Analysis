# IPL Analytics App 📊

A **Streamlit** web application for interactive analysis and visualization of the **Indian Premier League (IPL)** data. The app provides insights into player performances, team statistics, match analytics, and interactive visualizations based on IPL match data.

The project is deployed in streamlit cloud: https://ipl-analytics-app.streamlit.app/
---

## Table of Contents

1. [About the Project](#about-the-project)
2. [Features](#features)
3. [How to Run Locally](#how-to-run-locally)
4. [Folder Structure](#folder-structure)
5. [Tech Stack](#tech-stack)

---

## About the Project

The **IPL Analytics App** helps users explore IPL data through insightful visualizations and detailed analytics. The app uses **Streamlit**, **Pandas**, and **Plotly** for a seamless experience and allows users to:

- Analyze player statistics such as runs scored, batting averages, and wickets taken.
- Visualize the performance of teams, including win percentages, match results, and highest margins of victory.
- Access match-level insights, including **runs per over**, **cumulative runs**, and **super over** statistics.

---

## Features

### **Player Analytics**:
- **Top 10 Players**: Filter the top 10 players by:
  - **Runs Scored**
  - **Batting Average**
  - **Batting Strike Rate**
  - **Wickets Taken**
- Separate tables for **batters** and **bowlers**.

### **Team Insights**:
- **Team Records**: View the total number of matches played, wins, losses, and win percentages.
- **Biggest Win Margins**: Displays matches with the largest victory margins.
- **Highest First Innings Scores**: Displays top scores in the first innings.
- **Highest Successful Chases**: Displays successful chases with the highest targets.
- **Super Over Matches**: Shows matches that went into a Super Over.

### **Match Visualizations**:
- **Over-by-Over Runs (Bar Chart)**: View runs scored per over for both innings.
- **Over-by-Over Runs (Line Chart)**: View runs scored in each over with dynamic interactivity.
- **Cumulative Runs**: Track cumulative runs scored by each team over the course of the match.
- Interactive visualizations with **hover details** showing the runs and wickets for each over.

---

## How to Run Locally

To run the app locally, follow these steps:

### Prerequisites
- Python 3.x
- Required libraries: `Streamlit`, `Pandas`, `Plotly`, `NumPy`

### Steps to Run Locally

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/coder-deva007/ipl-analytics-app.git
    cd ipl-analytics-app
    ```

2. **Install Dependencies**:
    - Create a virtual environment (optional but recommended).
    - Install the required dependencies listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

3. **Prepare Data**:
    - Download or prepare the IPL datasets:
      - `players_clean.csv`: Player statistics
      - `matches_clean.csv`: Match results data
      - `deliveries_clean.csv`: Ball-by-ball delivery data
      - `match_info.csv`: Match-level information
    - Place these CSV files in the `./IPL_Analytics_App/data/` directory.

4. **Run the Streamlit App**:
    ```bash
    streamlit run app.py
    ```
    The app should now be accessible in your browser at `http://localhost:8501`.

---

## Folder Structure

Here’s an overview of the folder structure for this project:
```
ipl-analytics-app/
│
├── app.py # Main Streamlit application file
├── data/ # Folder containing dataset files
│ ├── players_clean.csv # Player performance data
│ ├── matches_clean.csv # Match results data
│ ├── deliveries_clean.csv# Ball-by-ball data
│ └── match_info.csv # Match-level data
├── requirements.txt # Required Python libraries
└── README.md # Project documentation (this file)
```
---

## Tech Stack

- **Python 3.x**: Backend programming language for data manipulation and visualization.
- **Streamlit**: For building the web-based interactive dashboard.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations, including cumulative sums.
- **Plotly**: For interactive visualizations (bar charts, line charts, scatter plots).

---