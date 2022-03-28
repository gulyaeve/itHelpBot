from flask import Flask, request

app = Flask(__name__)


@app.route('/request', methods=['POST'])
def get_data_from_request():
    return request.get_data()


if __name__ == "__main__":
    app.run()