import pandas as pd
from datetime import datetime, time
import os

# === CONFIGURATION ===
input_file = 'energy_30min_kwh.csv'  # Replace with the path to your CSV file
output_folder = '/folder/path'  # Replace with your desired folder
output_filename = 'energy_30min_eur.csv'  # Replace with desired output file name

# Define your multipliers for specific time ranges
# Format: (start_time, end_time): multiplier
multipliers = {
    (time(0, 0), time(7, 30)): 0.1848, # change the price of energy provided by your privider
    (time(8, 0), time(16, 30)): 0.3451, # change the price of energy provided by your privider
    (time(17, 0), time(18, 30)): 0.3617, # change the price of energy provided by your privider
    (time(19, 0), time(22, 30)): 0.3451, # change the price of energy provided by your privider
    (time(23, 0), time(23, 30)): 0.1848 # change the price of energy provided by your privider
}

# === FUNCTION TO FIND MULTIPLIER BASED ON TIME ===
def get_multiplier(t):
    for (start, end), multiplier in multipliers.items():
        if start <= t <= end:
            return multiplier
    return 1  # default multiplier if no match

# === MAIN SCRIPT ===
df = pd.read_csv(input_file)

# Convert the 'Read Date and End Time' to datetime
df['Read Date and End Time'] = pd.to_datetime(df['Read Date and End Time'])

# Extract time and apply multiplier
df['Time'] = df['Read Date and End Time'].dt.time
df['Multiplier'] = df['Time'].apply(get_multiplier)
df['Price'] = (df['Read Value'] * df['Multiplier']).round(2)

# Drop columns you don't want in the output
df.drop(columns=['Time', 'Multiplier'], inplace=True)

# Save to file
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, output_filename)
df.to_csv(output_path, index=False)

print(f"File saved to {output_path}")
