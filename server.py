# import pathlib
# # FLASK
#
# from flask import Flask, request, jsonify, Response, abort, send_file
#
# app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False
#
#
#
# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE')
#     return response
#
#
# @app.route('/bookmark', methods=['POST'])
# def file_info():
#     print(request.get_json())
#     # path = request.get_json()['path']
#     # return jsonify(path_utils.file_info(path))
#     return Response(None, 200)


from fastapi import Request

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/')
async def save_tabs(request: Request):
    payload = await request.json()
    print(payload)
    return {'status': 'ok'}

# @app.post('/')
# async def save_tabs(request: Request):
#     if not secrets.compare_digest(token, TOKEN):
#         raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='access denied: invalid token')
#
#     code = subprocess.run(COMMAND, check=False, cwd=CWD).returncode
#     if code == 0:
#         return {'status': 'success'}
#     raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, f'command failed with exit code: {code}')
