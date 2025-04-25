import pandas as pd
import os

# === SETTINGS ===
input_file = 'energy_30min_eur.csv'  # Your input file
output_directory = '/folder/path'  # <-- Change this to your folder
output_filename = 'energy_30min_eur_week.csv'

# Make sure the directory exists
os.makedirs(output_directory, exist_ok=True)

# Read the CSV file
df = pd.read_csv(input_file)

# Convert 'Read Date and End Time' to datetime
df['Read Date and End Time'] = pd.to_datetime(df['Read Date and End Time'], format='%Y-%m-%d %H:%M:%S')

# Format it back to 'YYYY-MM-DD HH:MM' (no seconds)
df['Read Date and End Time'] = df['Read Date and End Time'].dt.strftime('%Y-%m-%d %H:%M')

# Add a new column 'week' with the week number
df['week'] = pd.to_datetime(df['Read Date and End Time']).dt.isocalendar().week

# Save to the specific directory
output_path = os.path.join(output_directory, output_filename)
df.to_csv(output_path, index=False)

print(f"Week column added and file saved to {output_path} successfully!")
