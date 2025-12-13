# Air Quality Index (AQI) Analysis and Forecasting

## Project Overview
This project focuses on analyzing historical Air Quality Index (AQI) data from major Indian cities—Delhi, Mumbai, Bengaluru, and Kolkata—to identify pollution trends and forecast future AQI levels.  
Time series analysis and the Facebook Prophet forecasting model are used to predict potential pollution spikes, supporting data-driven decision-making for environmental monitoring and public health awareness.

---

## Key Features
- Data cleaning using time-based interpolation to ensure continuous time-series data.
- Historical AQI trend visualization with reference thresholds based on CPCB standards.
- Forecasting AQI values for the next 365 days using Facebook Prophet.
- Automatic detection of seasonal patterns such as winter pollution peaks.

---

## Folder Structure
```
AQI-Analysis-Forecasting/
│
├── data/
│   ├── raw/                 # Original dataset (city_day.csv)
│   └── processed/           # Cleaned, city-wise CSV files
│
├── src/
│   ├── preprocess.py        # Data cleaning and city-wise splitting
│   ├── visualizer.py        # Historical AQI trend visualization
│   └── forecast.py          # Forecasting using Facebook Prophet
│
├── reports/
│   └── figures/             # Generated trend and forecast plots
│
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## Setup and Installation

### Install Dependencies
```
pip install -r requirements.txt
```

### Prepare the Dataset
Download the Air Quality Data in India dataset from Kaggle and place the file `city_day.csv` inside the `data/raw/` directory.

---

## How to Run

### 1. Preprocess the Data
```
python src/preprocess.py
```

### 2. Visualize Historical Trends
```
python src/visualizer.py
```
Output files are saved in `reports/figures/`.

### 3. Forecast Future AQI
```
python src/forecast.py
```
The forecast plot with confidence intervals is saved in `reports/figures/`.

---

## Technical Approach

### Data Imputation
Linear interpolation is used to fill missing values, with forward and backward filling applied to edge cases.

### Modeling
Facebook Prophet is employed for forecasting due to its robustness to missing data, trend changes, and strong seasonal effects.

### Pollution Thresholds
- AQI above 200: Poor
- AQI above 400: Severe

These thresholds are displayed on trend visualizations for reference.

---

## Tech Stack
- Python 3.x
- Facebook Prophet
- Pandas
- Matplotlib and Seaborn

---

## License
This project is intended for academic and assignment use.
