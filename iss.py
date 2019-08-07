import requests
from ast import literal_eval as le
import matplotlib.pyplot as plt


def __validate_answer(text):
    if text["message"] != 'success':
        raise ValueError('Incorrect data')


def get_astronauts():
    try:
        r = requests.get('http://api.open-notify.org/astros.json')
    except requests.exceptions.RequestException as e:
        print(e)
    else:
        text = le(r.text)
        __validate_answer(text)
        numb_of_people = text["number"]
        return numb_of_people


def get_position()->(float, float):
    try:
        r = requests.get('http://api.open-notify.org/iss-now.json')
    except requests.exceptions.RequestException as e:
        print(e)
    else:
        text = le(r.text)
        __validate_answer(text)
        longitude = text['iss_position']['longitude']
        latitude = text['iss_position']['latitude']
        return longitude, latitude


def draw_aitoff():
    plt.figure()
    plt.subplot(111, projection="aitoff")
    plt.title("Aitoff")
    plt.grid(True)
    plt.savefig('ait.png')

