from flask import Flask, jsonify, request
from path_finder import PathFinder

app = Flask(__name__)


@app.route('/api/map', methods=['POST'])
def return_data():
    request_data = request.data.decode("utf-8")
    with open('temp.xml', 'w+') as temp:
        temp.write(request_data)
    return jsonify(PathFinder.get_shortest_paths('temp.xml'))


if __name__ == '__main__':
    app.run(debug=True)
