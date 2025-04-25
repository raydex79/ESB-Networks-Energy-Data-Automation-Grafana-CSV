# ESB Networks Energy Data Automation

This project automates the process of downloading and processing smart meter energy data from [ESB Networks](https://www.esbnetworks.ie/), converting it into `.csv` files ready to be used in **Grafana** with the **Infinity Data Source plugin**.

## 📘 Long story short. How I Made These Grafana Scripts
I'm not a programmer and don’t know much about databases—but I needed some scripts to work in Grafana. With help from AI, I was able to build them step by step.

These scripts came together through questions, experiments, and learning as I went. I hope they help someone else just like AI helped me!

## ✨ What It Does

With a single terminal command, the scripts will:

- Download your energy data.
- Adjust the timestamps.
- Organize data into **Day/Night/Peak** buckets.
- Add pricing based on your energy rate.
- Create weekly breakdowns.
- Output `.csv` files for easy visualization in Grafana.

##  Scripts Overview

| Script | Purpose |
|--------|---------|
| `energy.py` | Main controller script. Runs all other scripts in order. |
| `energy_download.py` | Downloads your energy data and saves it to a file. *(Original source credit: [badger707/esb-smart-meter-reading-automation](https://github.com/badger707/esb-smart-meter-reading-automation), adapted by Raydex.)* |
| `energy_timeshift.py` | Shifts all timestamps back by 30 minutes to match your local time. I have an Energia as a provider and the first reading starts at 00:00 |
| `energy_dnp.py` | Organizes readings into Day, Night, and Peak buckets and groups by day. |
| `energy_30min_eur.py` | Multiplies each 30-min reading by your electricity rate and adds a Price column. |
| `energy_dnp_eur.py` | Converts DNP (Day/Night/Peak) usage into price-based data. |
| `energy_30min_kwh_week.py` | Adds a 'Week' column to your 30-min usage file. |
| `energy_30min_eur_week.py` | Adds a 'Week' column to your price-based usage file. |

## 🖥️ How to Use

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run the main script:

```bash
sudo python3 energy.py
```
💡 Raydex runs this automatically with **Task Scheduler on a Synology NAS** for full automation.

## 🛠️ How to Create a Scheduled Task on Synology NAS (Run as root)
To run a Python script (energy.py) on your Synology NAS using Task Scheduler, follow these steps:

1. **Log in to DSM** (Synology's web interface).
2. Open **Control Panel → Task Scheduler**.
3. Click **Create → Scheduled Task → User-defined script**.
4. In the **General tab**:
   - Give your task a name (e.g., Run `Energy Script`).
   - Set **User** to `root`.
5. In the **Task Settings** tab, enter the command:

```bash
cd /your_folder_path
python3 energy.py
```

6. (Optional) Set a schedule under the **Schedule** tab.
7. Click **OK** to save.

## ⚠️ Before You Start

You must update some settings in the scripts:

- Your **MPRN**, **account number**, or **credentials** in `energy_download.py`.
- Your **price per kWh** in `energy_30min_eur.py` and `energy_dnp_eur.py`.
- **Folder paths.**
- **Filenames** if you want to use differnet name for your input and ouput files

Open the scripts in any text editor and look for comments like:

```bash
# TODO: Change this
```

## 📊 Output

Each script produces a new .csv file that gets more refined. These files can be imported directly into **Grafana using the Infinity data source** to create energy usage dashboards.

## 🙌 Credits

- Script adapted from [badger707/esb-smart-meter-reading-automation](https://github.com/badger707/esb-smart-meter-reading-automation)
- Developed and maintained by **Raydex**
