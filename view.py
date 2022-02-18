from flask import Flask, render_template, request

import Data_pH as dp

app=Flask(__name__)

@app.route("/")
def home():
    output=dp.DataPh()
    return render_template("index.html", out=output)

@app.route("/result", methods=['POST','GET'])
def result():
    output = request.form.to_dict()
    name = output["name"]

    return render_template("index.html", name =[10,0,-10])

if __name__=='__main__':
    app.run(debug=True,port=5001)