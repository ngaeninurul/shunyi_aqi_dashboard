# SHUNYI AQI DASHBOARD✨


## Overview

This project focuses on analyzing and visualizing the Air Quality Index (AQI) data from Shunyi, China (2013-2017). It explores trends, seasonal patterns, and AQI categories (Good, Moderate, Unhealthy, etc.). Data visualization is powered by Streamlit, enabling interactive exploration.

## Project Structure

- **all_data.csv**: A cleaned and combined dataset used for analysis.
- **notebook.ipynb**: Jupyter Notebook containing the data analysis workflow.
- **requirements.txt**: List of required Python packages to run the project.
- **url.txt**: Text file containing the URLs or descriptions of data sources.
- **dashboard/dashboard.py**: Python script to generate the interactive dashboard.
- **dashboard/logo.png**: Logo used in the dashboard.
- **data/**: Directory containing individual CSV files for air quality data from various locations.

## Features

1. **Data Analysis**: Explore and analyze air quality trends using `notebook.ipynb`.
2. **Interactive Dashboard**: Visualize air quality insights through a dashboard implemented in `dashboard.py`.

## Getting Started

### Prerequisites
- Python 3.10 or higher
- Jupyter Notebook
- Required libraries listed in `requirements.txt`

### Setup Environment - Anaconda
```bash
conda create --name aqi_env python=3.10
conda activate aqi_env
pip install -r requirements.txt
```

### Setup Environment - Shell/Terminal
```bash
mkdir data_analyst_project
cd data_analyst_project
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Usage

### Clone the Repository
```bash
git clone https://github.com/ngaeninurul/data_analyst_project.git
cd data_analyst_project
```

### Run the Notebook
```bash
jupyter notebook notebook.ipynb
```

### Run the Dashboard
```bash
streamlit run dashboard/dashboard.py
```

### Access the Dashboard
Check the `url.txt` file for the link to the hosted version of the dashboard.

---

## Deployment

To deploy the dashboard on a server, install dependencies in the target environment and configure Streamlit with hosting solutions like Heroku or AWS.

---

## License
This project is licensed under the MIT License.

## Acknowledgments
- Data sourced from the `data/` directory.
- Visualizations powered by Python libraries.
```
