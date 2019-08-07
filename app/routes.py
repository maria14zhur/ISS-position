from app import app
from iss import *
import matplotlib.pyplot as plt
from flask import render_template




@app.route('/')
@app.route('/index')
def index():
    astromen = str(get_astronauts())
    position = get_position()
    plt.figure()
    plt.subplot(111, projection="aitoff")
    plt.title("Aitoff")
    plt.grid(True)
    plt.savefig(r'.\app\static\ait.png')

    return render_template('index.html', astromen=astromen, longitude=position[0], latitude=position[1])