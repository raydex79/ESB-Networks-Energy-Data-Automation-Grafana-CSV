import csv
import os


def multiply_csv_data(input_file, output_folder, output_file_name):
    """
    Multiplies data in a CSV file, rounds the results to 2 decimal places,
    and saves the result to a new CSV file.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_path = os.path.join(output_folder, output_file_name)

    try:
        with open(input_file, 'r') as infile, open(output_path, 'w', newline='') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = ['Date', 'day', 'peak', 'night']  # Keep original column order
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()

            for row in reader:
                try:
                    def safe_float(value):
                        value = value.strip()
                        return round(float(value), 2) if value else 0.0

                    row['day'] = round(safe_float(row['day']) * 0.3451, 2) # change the price of energy provided by your privider
                    row['peak'] = round(safe_float(row['peak']) * 0.3617, 2) # change the price of energy provided by your privider
                    row['night'] = round(safe_float(row['night']) * 0.1848, 2) # change the price of energy provided by your privider

                    writer.writerow({
                        'Date': row['Date'],
                        'day': row['day'],
                        'peak': row['peak'],
                        'night': row['night']
                    })

                except Exception as e:
                    print(f"Skipping row due to error: {row} ({e})")
                    continue

        print(f"Successfully processed '{input_file}' and saved to '{output_path}'")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example Usage
input_csv_file = 'energy_dnp_kwh.csv'
output_directory = '/folder/path'
output_csv_name = 'energy_dnp_eur.csv'

multiply_csv_data(input_csv_file, output_directory, output_csv_name)
