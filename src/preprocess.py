import pandas as pd
import os

def preprocess_data():
    raw_path = 'data/raw/city_day.csv'
    output_dir = 'data/processed'
    
    if not os.path.exists(raw_path):
        print(f"Error: {raw_path} not found!")
        return

    print("Loading raw data...")
    df = pd.read_csv(raw_path)
    
    # Convert 'Date' column to datetime objects
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Cities mentioned in your project scope
    target_cities = ['Delhi', 'Mumbai', 'Bengaluru', 'Kolkata']
    
    os.makedirs(output_dir, exist_ok=True)
    
    for city in target_cities:
        print(f"Processing {city}...")
        
        # 1. Filter data for the specific city
        city_df = df[df['City'] == city].copy()
        
        # 2. Handle Missing Dates (Resample to ensure daily frequency)
        # This adds rows for missing days so the timeline is continuous
        city_df.set_index('Date', inplace=True)
        city_df = city_df.asfreq('D') 
        
        # 3. Handle Missing AQI Values
        # Linear interpolation fills gaps smoothly (better than just copying previous value)
        city_df['AQI'] = city_df['AQI'].interpolate(method='time')
        
        # Fill any remaining gaps at the very start or end
        city_df['AQI'] = city_df['AQI'].ffill().bfill()
        
        # Reset index to make Date a column again
        final_df = city_df[['AQI']].reset_index()
        
        # 4. Save to a separate CSV
        save_path = os.path.join(output_dir, f"{city}.csv")
        final_df.to_csv(save_path, index=False)
        print(f"  -> Saved cleaned data to {save_path}")

if __name__ == "__main__":
    preprocess_data()