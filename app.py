from flask import Flask, request, make_response
import uvicorn

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World</h1>"


@app.route("/hello", methods=["GET", "POST"])
def hello():
    response = make_response("Hello World\n")
    response.status_code = 200
    # custom response
    response.headers["content-type"] = "application/octet-stream"
    # if request.method == 'GET':
    #     return "GET request", 200 # 200 is the status code
    # elif request.method == "POST":
    #     return "POST request"
    # else:
    #     return 'Request not allowed'

    return response


@app.route("/greet/<name>")  # name is a variable (url processors)
def greet(name):
    return f"Hello {name}"


@app.route("/calculate/<int:num1>/<int:num2>")
def calculate(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"


@app.route("/handle_url_params")  # url parameters
def handle_params():
    greeting = request.args["greeting"]
    name = request.args["name"]
    return f"{greeting} {name}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
