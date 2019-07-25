from app import app
from iss import *
import matplotlib.pyplot as plt
from flask import render_template


def draw_aitoff():
    plt.figure()
    plt.subplot(111, projection="aitoff")
    plt.title("Aitoff")
    plt.grid(True)
    plt.savefig('map1.png')

@app.route('/')
@app.route('/index')
def index():
    astromen = str(get_astronauts())
    position = get_position()
    draw_aitoff()

    return render_template('index.html', astromen=astromen, longitude=str(position[0]), latitude=str(position[0]))