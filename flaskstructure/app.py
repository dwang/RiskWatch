import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask, request, redirect, render_template, json
from flask_cors import CORS

from flaskstructure import database, geocacher

import datetime
import imghdr

app = Flask(__name__)
CORS(app)

@app.route('/api/findRisk', methods=['GET'])
def findRisk():
    data = json.loads(request.data)
    return json.dumps(database.findRisk(data['location']))


@app.route('/api/getrisks', methods=['GET'])
def getImages():
    return json.dumps(database.getRisksBasicInfo())


@app.route('/api/addrisk', methods=['POST'])
def addRisk():
    image = request.files['image']
    hazardtype = request.form.get("hazardtype")
    location = request.form.get("location")
    filename = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day) + '-' + str(
        datetime.datetime.now().hour) + '-' + str(datetime.datetime.now().minute) + '-' + str(datetime.datetime.now().second) + '-' + str(datetime.datetime.now().microsecond)
    image.save('/var/www/html/images/' + filename)
    database.addRisk(filename, location, hazardtype)
    return redirect("http://184.73.76.65")


@app.route('/api/reversecoords', methods=['GET'])
def getReverseCoords():
    print(request.data)
    data = json.loads(request.data)
    lat = data['lat']
    lng = data['lng']
    return geocacher.reverseCoords(lat, lng)

@app.route('/api/flagimage', methods=['POST'])
def flagImage():
    return  # implement this endpoint to use database flagger


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
