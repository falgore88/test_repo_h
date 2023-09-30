from flask import Flask, jsonify, request
import csv
import random

app = Flask(__name__)

data = []
with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append({
            'category': row[0],
            'theme': row[1]
        })


def handler():
    if request.args.get('url'):
        url = request.args.get('url')
    elif request.args.get('domain'):
        url = request.args.get('domain')
    elif request.is_json:
        url = request.json.get('url')
    
    print(url)
    return jsonify(random.choice(data))


@app.route('/check_domain', methods=['GET', 'POST'])
def check_domain():
    return handler()


@app.route('/check_url', methods=['GET', "POST"])
def check_url():
    return handler()
