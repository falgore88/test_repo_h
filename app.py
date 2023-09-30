from flask import Flask, jsonify, request, abort
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
    url = None
    print(request.args, request.data, request.is_json, request.headers)
    if request.args.get('url'):
        url = request.args.get('url')
    elif request.args.get('domain'):
        url = request.args.get('domain')
    elif request.is_json:
        if request.json.get('url'):
            url = request.json.get('url')
        elif request.json.get('domain'):
            url = request.json.get('domain')
    if not url:
        return abort(400)
    return jsonify(random.choice(data))


@app.route('/check_domain', methods=['GET', 'POST'])
def check_domain():
    return handler()


@app.route('/check_url', methods=['GET', "POST"])
def check_url():
    return handler()
