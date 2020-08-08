import requests
import json


def get_data(description, location):
    global result

    url = 'https://jobs.github.com/positions.json'
    params = {
        'description': description,
        'location': location
    }
    result = requests.get(url, params=params)
    return result


def save_data(description, location):
    get_data(description, location)
    with open('job_offers.json', 'w', encoding='utf-8') as file:
        file.write(result.text)


def read_data():
    with open('job_offers.json', encoding='utf-8') as read_file:
        load_offers = json.load(read_file)
        return load_offers
