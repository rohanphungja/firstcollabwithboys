from flask import Flask, render_template , request
import pandas as pd
app = Flask(__name__)

@app.route("/login", methods = ["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template("rohan.html")
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if email == "firstcollabwithboys@gmail.com" and password == "90lpa":
            return "Succes, Hey Rohan or Piyush or Bijay"
        else:
            return "failure, Hey Rohan or Piyush or Bijay please enter correct pass or email"


    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True) 