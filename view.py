from flask import Flask, render_template, request,jsonify

import Data_pH as dp
previous_name = 'A, H'
previous_num = '0'
app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("sample.html")

@app.route("/result", methods=['POST','GET'])
def result():
    global previous_name
    global previous_num
    output = request.form.to_dict()
    name = output["name"]
    num=output["num"]
    previous_name = name
    previous_num = num
    data=dp.DataPh(name,num)

    return render_template("index.html", out=data)

@app.route('/ajax', methods = ['POST'])
def ajax_request():
    global previous_name
    global previous_num
    name = request.form["name"]
    num=request.form['num']
    if(name == ''):
        name = previous_name
    else:
        previous_name = name
    if(num == ''):
        num = previous_num
    else:
        previous_num = num
    data=dp.DataPh(name,num)
    return jsonify(out=data)

if __name__=='__main__':
    app.run(debug=True,port=5001)