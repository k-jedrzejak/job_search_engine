from flask import request
import json

# get Data

result = None


def getData(description, location):
    global result

    url = 'https://jobs.github.com/positions.json'
    params = {
        'desription': description,
        'location': location
    }
    result = request.get(url, params=params)
    return result


# save data  json
def saveData(description, location):
    getData(description,location)
    with open('job_offers.json', 'w') as file:
        file.write(result.text)


# rad data json
def readData(description, location):
    with open('job_offers.json', 'w') as read_file:
        load_offers = json.dumb(read_file)
        return load_offers
