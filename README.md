# Customer-Segmentation-Insights
Customer segmentation project using a retail dataset. Includes data extraction, EDA, K-Means clustering, and an interactive Tableau dashboard. Demonstrates Python, SQL, data visualisation, and machine learning skills. Future work includes advanced analysis and deployment.

## Project Overview
This project aims to conduct an in-depth analysis of a retail transactional and demographic dataset to identify actionable insights. The goal is to segment customers based on their purchasing behavior and demographics, laying the groundwork for targeted marketing strategies and data-driven decision-making.

## Repository Structure
```
customer-segmentation-insights/
|-- data/                     # Folder containing raw and cleaned data files
|-- notebooks/
|   |-- 1_data_exploration.ipynb  # Initial exploration and data overview
|   |-- 2_data_cleaning.ipynb     # Comprehensive data cleaning and preprocessing
|-- visuals/                   # Visuals and plots from EDA
|-- README.md                 # Project overview and setup guide
|-- requirements.txt          # List of Python dependencies
```

## Getting Started
This section will guide you through the process of setting up your local environment to run the Advanced Financial Analytics System. Follow these instructions to get started.

### Clone the Repository
Start by cloning the repository to your local machine. Replace `yourusername` with your GitHub username and adjust the repository name if it's different:

```bash
git clone https://github.com/yourusername/Customer-Segmentation-Insights.git
cd Customer-Segmentation-Insights
```
### Set Up Python Environment
It is recommended to use a virtual environment for Python projects to manage dependencies effectively. Here's how you can set it up:

```bash
# Create a virtual environment (Unix/macOS)
python3 -m venv venv
source venv/bin/activate

# Create a virtual environment (Windows)
python -m venv venv
.\venv\Scripts\activate
```
### Install Dependencies
With your virtual environment activated, install the project dependencies by running:

```bash
pip install -r requirements.txt
```

### To run a Jupyter Notebook**:
Replace `1_data_initial_exploration.ipynb` with the notebook name you want to run
   ```bash
   jupyter notebook notebooks/1_data_initial_exploration.ipynb
   ```

## Acknowledgments
This project uses a retail dataset from [Kaggle](https://www.kaggle.com/datasets/bhavikjikadara/retail-transactional-dataset) contributed by Bhavik Jikadara, licensed under CC BY 4.0.
