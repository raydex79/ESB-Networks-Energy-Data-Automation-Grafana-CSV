import subprocess
import os

# Folder where your scripts are located
script_folder = '/folder/path'  # Change this to your folder path

# List of script filenames inside the folder
scripts = ['energy_download.py', 'energy_timeshift.py', 'energy_dnp.py', 'energy_30min_eur.py', 'energy_dnp_eur.py', 'energy_30min_kwh_week.py', 'energy_30min_eur_week.py']

for script in scripts:
    script_path = os.path.join(script_folder, script)
    
    print(f"Running {script_path}...")
    result = subprocess.run(['python', script_path])
    
    if result.returncode != 0:
        print(f"{script} failed with return code {result.returncode}")
        break
    else:
        print(f"{script} completed successfully.\n")


