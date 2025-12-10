import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def plot_city_trend(city_name):
    """
    Reads the processed city data and plots the AQI trend.
    """
    file_path = f"data/processed/{city_name}.csv"
    if not os.path.exists(file_path):
        print(f"Data for {city_name} not found. Run src/preprocess.py first.")
        return

    # Load Data
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Plot Setup
    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    
    # Line Plot
    sns.lineplot(x='Date', y='AQI', data=df, color='tab:blue', label='Daily AQI')
    
    # Add Danger Lines (Indian CPCB Standards)
    plt.axhline(y=200, color='orange', linestyle='--', alpha=0.7, label='Poor (200)')
    plt.axhline(y=400, color='red', linestyle='--', alpha=0.7, label='Severe (400)')
    
    # Formatting
    plt.title(f'Air Quality Trends: {city_name}', fontsize=16)
    plt.xlabel('Year')
    plt.ylabel('AQI Value')
    plt.legend()
    
    # Save Plot
    save_dir = "reports/figures"
    os.makedirs(save_dir, exist_ok=True)
    save_path = f"{save_dir}/{city_name}_trend.png"
    plt.savefig(save_path)
    print(f"Chart saved to {save_path}")
    plt.close()

if __name__ == "__main__":
    # Test it on Delhi
    plot_city_trend("Delhi")