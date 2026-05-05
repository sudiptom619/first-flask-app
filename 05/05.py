from flask import Flask, render_template, request, Response, session, make_response

app = Flask(__name__, template_folder="templates")
app.secret_key = "SOME_KEY"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/set_data")
def set_data():
    session["name"] = "Mike"
    return render_template("index.html", message="Session Data Set!")


@app.route("/get_data")
def get_data():
    name = session["name"]
    return render_template("index.html", message=f"Name:{name}")


@app.route("/clear_session")
def clear_session():
    session.clear()
    return render_template("index.html", message="Session Cleared!")


@app.route("/set_cookie")
def set_cookie():
    response = make_response(render_template("index.html"))
    response.set_cookie("cookie_name", "cookie_value")
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
