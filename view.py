from flask import Flask, render_template, request,jsonify

import Data_pH as dp

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("sample.html")

@app.route("/result", methods=['POST','GET'])
def result():
    output = request.form.to_dict()
    name = output["name"]
    num=output["num"]
    data=dp.DataPh(name,num)

    return render_template("index.html", out=data)

@app.route('/ajax', methods = ['POST'])
def ajax_request():
    name = request.form["name"]
    num=request.form['num']
    data=dp.DataPh(name,num)
    return jsonify(out=data)

if __name__=='__main__':
    app.run(debug=True,port=5001)