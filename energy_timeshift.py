import pandas as pd
from datetime import timedelta
import os

def timeshift_csv(input_filepath, output_folder, output_filename, time_shift_minutes=-30):
    """
    Timeshifts the 'Read Date and End Time' column in a CSV file by a specified number of minutes.

    Args:
        input_filepath (str): The path to the input CSV file.
        output_folder (str): The path to the output folder where the modified CSV will be saved.
        output_filename (str): The name of the output CSV file.
        time_shift_minutes (int, optional): The number of minutes to shift the time by. Defaults to -30.
    """

    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(input_filepath)

        # Convert the 'Read Date and End Time' column to datetime objects
        df['Read Date and End Time'] = pd.to_datetime(df['Read Date and End Time'], format='%d-%m-%Y %H:%M')

        # Apply the time shift
        df['Read Date and End Time'] = df['Read Date and End Time'] + timedelta(minutes=time_shift_minutes)

        # Format the 'Read Date and End Time' column back to the original string format.
        df['Read Date and End Time'] = df['Read Date and End Time'].dt.strftime('%Y-%m-%d %H:%M')

        # Ensure the output directory exists
        os.makedirs(output_folder, exist_ok=True)

        # Create the full output filepath
        output_filepath = os.path.join(output_folder, output_filename)

        # Save the modified DataFrame to a new CSV file
        df.to_csv(output_filepath, index=False)

        print(f"Successfully timeshifted data and saved to: {output_filepath}")

    except FileNotFoundError:
        print(f"Error: Input file not found at {input_filepath}")
    except ValueError as e:
        print(f"Error: Could not parse date. Ensure the date format is correct. Details: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    # Example usage:
    input_file = 'energy_download.csv'  # Replace with your input CSV file path
    output_directory = '/folder/path'  # Replace with your desired output directory
    output_file = 'energy_30min_kwh.csv'  # Replace with your desired output filename
    timeshift_csv(input_file, output_directory, output_file)
