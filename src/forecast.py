import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import os

def forecast_aqi(city_name, days_ahead=365):
    """
    Trains a Prophet model and forecasts AQI for the specified city.
    """
    file_path = f"data/processed/{city_name}.csv"
    if not os.path.exists(file_path):
        print(f"Error: Data for {city_name} not found. Run src/preprocess.py first.")
        return

    print(f"Generated forecast for {city_name}...")
    
    # 1. Load Data
    df = pd.read_csv(file_path)
    
    # 2. Prepare Data for Prophet
    # Prophet strictly requires columns named 'ds' (Date) and 'y' (Value)
    df = df.rename(columns={'Date': 'ds', 'AQI': 'y'})
    
    # 3. Train Model
    # yearly_seasonality=True helps it learn the winter pollution spike pattern
    model = Prophet(yearly_seasonality=True, daily_seasonality=False)
    model.fit(df)
    
    # 4. Make Future Dates
    future = model.make_future_dataframe(periods=days_ahead)
    
    # 5. Predict
    forecast = model.predict(future)
    
    # 6. Plot Results
    # Prophet has a built-in plotter that looks professional
    fig1 = model.plot(forecast)
    plt.title(f'{city_name} AQI Forecast (Next {days_ahead} Days)', fontsize=16)
    plt.xlabel('Date')
    plt.ylabel('AQI')
    
    # Add a red line for "Severe" pollution limit
    plt.axhline(y=400, color='red', linestyle='--', label='Severe Limit (400)')
    plt.legend()
    
    # Save Plot
    save_dir = "reports/figures"
    os.makedirs(save_dir, exist_ok=True)
    save_path = f"{save_dir}/{city_name}_forecast.png"
    plt.savefig(save_path)
    print(f"Forecast chart saved to {save_path}")
    
    # Optional: Save the forecast numbers to CSV
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(days_ahead).to_csv(
        f"data/processed/{city_name}_forecast_data.csv", index=False
    )

if __name__ == "__main__":
    # You can change this to "Mumbai", "Bengaluru", etc.
    forecast_aqi("Delhi")