from flask import Flask

app = Flask(__name__)


def handler():
    return 'test'


@app.route('/check_domain', methods=['GET', 'POST'])
def check_domain():
    return handler()


@app.route('/check_url', methods=['GET', "POST"])
def check_url():
    return handler()