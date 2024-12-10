# SHUNYI AQI DASHBOARD✨

This project is focused on analyzing and visualizing the Air Quality Index (AQI) data from Shunyi, China, between 2013 and 2017. The primary goal is to explore trends in air quality, understand seasonal patterns, and visualize the AQI categories (Good, Moderate, Unhealthy, etc.) using various plots and interactive dashboards.
The analysis is visualized using Streamlit, an interactive framework that allows users to filter AQI data by date and AQI range and explore the data through charts and metrics.

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

Ensure you have the following installed:
- Python 3.10 or higher
- Jupyter Notebook
- Required libraries listed in `requirements.txt`

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ngaeninurul/data_analyst_project.git
   cd data_analyst_project
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the data**:
   Ensure the `data/` directory contains the required CSV files.

### Running the Notebook

To analyze the data, open the Jupyter Notebook:

```bash
jupyter notebook notebook.ipynb
```

### Running the Dashboard

Run the interactive dashboard using the following command:

```bash
python dashboard/dashboard.py
```

### Accessing the Dashboard via URL

To access the dashboard, refer to the **url.txt** file, which contains the link to the hosted version of the dashboard.

### Deployment

To deploy the dashboard to a server, ensure that the dependencies in `requirements.txt` are installed in the target environment. You can use a web server or a hosting service that supports Python applications.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Air quality data provided in the `data/` directory.
- Dashboard designed using Python's visualization libraries.
