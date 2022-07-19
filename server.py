import pathlib
# FLASK

from flask import Flask, request, jsonify, Response, abort, send_file

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False



@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE')
    return response


@app.route('/bookmark', methods=['POST'])
def file_info():
    print(request.get_json())
    # path = request.get_json()['path']
    # return jsonify(path_utils.file_info(path))
    return Response(None, 200)
