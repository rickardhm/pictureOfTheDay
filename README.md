# Picture of the Day Retriever
This Python script retrieves the "Picture of the Day" (POTD) from NASA's Astronomy Picture of the Day (APOD) API and stores it locally in a JSON file named potd_[day].json, where [day] is the current day of the week (e.g., potd_Monday.json). If the script is run multiple times on the same day, it reads the POTD from the local file to minimize API calls. It also logs information using the Python logging module.

## Requirements
- Python 3.x
- requests module (pip install requests)
## Setup
1. Clone or download the repository.

1. Install the required dependencies using pip:

```Copy code
pip install requests
Usage
Run the script using Python:
```
```Copy code
python theCall.py
```
## Description
1. The script first attempts to retrieve the POTD from the local file corresponding to the current day of the week.
1. If the local file is not found or if the file's content does not match the current day's POTD, it calls the NASA APOD API to fetch the latest POTD.
1. The retrieved POTD information is then written to the local file for future reference.
1. The script logs relevant information using the logging module, such as reading from file, calling NASA API, writing to file, and the retrieved POTD details.
## Logging
The script uses the Python logging module to log information at different levels:

- INFO: Informational messages, such as reading from file, writing to file, and displaying the POTD details.
- DEBUG: Debugging messages, including the date retrieved from NASA API.
- ERROR: Error messages if any exceptions occur during the execution of the script.
## Notes
Ensure that your system has internet connectivity to retrieve the latest POTD from the NASA APOD API.
NASA API key used in the script (DEMO_KEY) is a demonstration key and has usage limitations. Replace it with your own API key for unrestricted access.