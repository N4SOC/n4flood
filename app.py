import requests
import json
from flask import Flask,render_template,send_from_directory
app = Flask(__name__)

@app.route('/flood')
def showstatus():
    stations=["4001-level-stage-i-15_min-mASD","4037-level-stage-i-15_min-mASD","4043-level-stage-i-15_min-mASD","4011-level-stage-i-15_min-mASD","4085-level-stage-i-15_min-mASD"]
    levels={}
    for station in stations:
        riverdata=requests.get("https://environment.data.gov.uk/flood-monitoring/id/measures/" + station).json()
        levels[(riverdata["items"]["label"]).split("-")[0]]=riverdata["items"]["latestReading"]["value"]
    return json.dumps({"riverlevels":levels})
    #{'Derby St Marys FLOW - level-stage-i-15_min-mASD': 1.402, 'Yorkshire Bridge LVL - level-stage-i-15_min-mASD': 0.863, 'Matlock LVL - level-stage-i-15_min-mASD': 1.934, 'Mytham Bridge LVL - level-stage-i-15_min-mASD': 1.46, 'Chatsworth LVL - level-stage-i-15_min-mASD': 1.786}

@app.route('/healthcheck')
def healthcheck():
    return {'status': 'alive'}

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
