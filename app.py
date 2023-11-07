from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/')
def home():
    return "Hello! Please edit the above URl after the forward slash (/) for the GET request."

@app.route('/hello', methods=['GET'])
def hello_get():
    """
    This endpoint returns a greeting message.
    ---
    parameters:
      - name: first 
        in: query
        type: string
        required: false
        default: World
      - name: last
        in: query
        type: string
        required: false
    responses:
      200:
        description: A greeting message
    """
    first = request.args.get('first', 'World')
    last = request.args.get('last', '')
    firstCapital = first.capitalize()
    lastCapital = last.capitalize()
    return f'Hello, {firstCapital} {lastCapital}!'

if __name__ == '__main__':
    app.run(debug=True)


## test CURL for post:
# curl -X POST http://localhost:5000/hello -H "Content-Type: application/json" -d '{"name": "Cooper"}'

## test CURL for get:
# curl -X GET http://localhost:5000/hello?name=Cooperper