import pandas as pd
import os

# Time buckets. Change the time range to your need.
def categorize_time(dt):
    t = dt.time()
    if (
        (t >= pd.to_datetime("08:00").time() and t <= pd.to_datetime("16:30").time()) or
        (t >= pd.to_datetime("19:00").time() and t <= pd.to_datetime("22:30").time())
    ):
        return 'day'
    elif t >= pd.to_datetime("17:00").time() and t <= pd.to_datetime("18:30").time():
        return 'peak'
    elif (
        (t >= pd.to_datetime("00:00").time() and t <= pd.to_datetime("07:30").time()) or
        (t >= pd.to_datetime("23:00").time() and t <= pd.to_datetime("23:30").time())
    ):
        return 'night'
    else:
        return 'other'

def process_energy_data(file_path, output_filename):
    # Load CSV
    df = pd.read_csv(file_path)

    # Convert datetime column
    df['Read Date and End Time'] = pd.to_datetime(df['Read Date and End Time'])

    # Extract date and bucket
    df['Date'] = df['Read Date and End Time'].dt.date
    df['Bucket'] = df['Read Date and End Time'].apply(categorize_time)

    # Group and pivot
    grouped = df[df['Bucket'] != 'other'].groupby(['Date', 'Bucket'])['Read Value'].sum().round(3).unstack(fill_value=0)

    # Ensure all expected columns are present
    for col in ['day', 'peak', 'night']:
        if col not in grouped.columns:
            grouped[col] = 0.0

    # Reorder and reset index
    result = grouped[['day', 'peak', 'night']].reset_index()

    # Define output folder and make sure it exists
    output_folder = '/folder/path'
    os.makedirs(output_folder, exist_ok=True)

    # Construct full output path
    output_path = os.path.join(output_folder, output_filename)

    # Save to CSV
    result.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")

# Example usage:
process_energy_data('energy_30min_kwh.csv', 'energy_dnp_kwh.csv')
