from flask import Flask, request
from faker import Faker
import pandas as pd
import requests



app = Flask(__name__)



@app.route('/')
def start():
    return('Flask homework')



@app.route('/requirements/')
def requirements():
    with open('requirements.txt', 'r') as file:
        req = file.read()
        return req



@app.route('/generate-users/')
def gen():
    fake = Faker()
    users = {}
    amount = request.args.get('amount', default = 100, type = int)
    for i in range(amount):
        fake.name()
        fake.email()
        users = {fake.name(): fake.email()}
    return users



@app.route('/mean/')
def average():
    data = pd.read_csv('hw.csv')
    height = data[' "Height(Inches)"'].mean()
    weight = data[' "Weight(Pounds)"'].mean()
    return 'Average height is ' + str(height) +' and average weight is ' + str(weight)



@app.route('/space/')
def astro_now():
    req = requests.get('http://api.open-notify.org/astros.json')
    astro = req.json()["number"]
    return str(astro) + ' astronauts are in space now'



if __name__ == '__main__':
    app.run(debug=True)