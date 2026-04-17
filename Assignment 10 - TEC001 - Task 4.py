from flask import Flask, jsonify
import json
app = Flask(__name__)

with open('airports.json', 'r') as file:
    data = json.load(file)

@app.route('/airport/<text>')

def airport_info(text):
    value = data.get(text)
    if not value:
        response = {
          "status": 404,
          "error": "Not Found",
          "message": "The requested resource could not be found."
        }
    else:
        response = {
            "icao": value['icao'],
            "name": value['name'],
            "city": value['city'],
            "country": value['country']
        }
    return response
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)