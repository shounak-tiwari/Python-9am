from flask import Flask,render_template,request
app = Flask(__name__)
# application page  - 1
@app.route("/")
def home():
    return render_template("index.html")
# application page - submit
@app.route("/submit/",methods = ["POST"])
def submit():
    fname = request.form["fname"]
    lname = request.form["lname"]
    fullname = fname + " " + lname
    return render_template("result.html",name = fullname)
# application page - 2
@app.route("/aboutus/")
def Info():
    return render_template("aboutus.html")
# application page - 3
@app.route("/booking/")
def BookNow():
    return render_template("booknow.html")
if __name__ == "__main__":
    app.run(debug=True)