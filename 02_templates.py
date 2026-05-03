from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    # myvalue = "Neural Nine"
    # myresults = 10 + 20
    # return render_template("index.html", myvalue=myvalue, myresults=myresults)
    mylist = [10, 20, 30, 40, 50]
    my_message = "hello world"
    return render_template("index.html", my_message=my_message, mylist=mylist)


@app.route("/other")  # redirect
def redirect_to_other():
    return redirect(url_for("index"))


@app.template_filter("reverse")
def reverse(s):
    return s[::-1]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
