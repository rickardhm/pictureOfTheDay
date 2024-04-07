import datetime
import json
import logging
import theLogger
logger = logging.getLogger('staging')
import requests

# 1. Trying to retrieve the picture of the day from a file.
# 2. If no file is present it then tries to get json from NASA
# 3. If json is read from NASA it then tries to write the information to a file

response = ""
missingFile = False
today = datetime.datetime.now().date()
day = datetime.datetime.now().strftime("%A")
# example potd_Monday.json
filename = "potd_" + day + ".json"

def readFile(filename):
    f = open(filename, "r")
    response = format(f.read())
    response = json.loads(response)
    f.close()
    logger.info("Reading from file " + filename)
    return response


def callNASA():
    response = requests.get("https://api.nasa.gov:443/planetary/apod?api_key=DEMO_KEY").json()
    logger.info("Reading from NASA")
    return response

# retrieving the json
try:
    response = readFile(filename)
except:
    missingFile = True
    response = callNASA()

# examine the validity of the date
try:
    nasaDate = response["date"]
    logger.debug(nasaDate)
    # writes a new file if date is no match
    if (missingFile or (format(nasaDate) != format(today))):
        f = open(filename, "w")
        f.write(json.dumps(response, indent=4))
        f.close()
        logger.info("writing the response to " + filename)
except TypeError as e:
    logger.exception(e)
except:
    logger.exception("Eeek!")

logger.info("The picture of the day is")
logger.info("title: " + response["title"])
logger.info("url: " + response["url"])
