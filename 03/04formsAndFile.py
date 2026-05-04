from flask import Flask, render_template, request, Response
import pandas as pd
import openpyxl

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        if "username" in request.form.keys() and "password" in request.form.keys():
            user = request.form["username"]
            password = request.form["password"]

            if user == "Sudipto" and password == "Mitra":
                return "Success"
            else:
                return "Failure"


@app.route("/file_upload", methods=["GET", "POST"])
def file_upload():
    file = request.files["file"]
    if file.content_type == "text/plain":
        return file.read().decode()
    elif file.content_type in [
        "application/vnd.ms-excel",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ]:
        df = pd.read_excel(file)
        return df.to_html()


@app.route("/convert_csv", methods=["GET", "POST"])
def convert_csv():
    file = request.files["file"]
    df = pd.read_excel(file)
    response = Response(
        df.to_csv(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attatchment; filename=result.csv"},
    )
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
