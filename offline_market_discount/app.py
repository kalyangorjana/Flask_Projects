from flask import flask,request,render_template


app = flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

if __name__ = "__main__":
    app.run(host = "0.0.0.0", port = 5002)