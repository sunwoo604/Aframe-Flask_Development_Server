from flask import Flask, render_template, request,jsonify

import Data_pH as dp

previous_molecules = 'A, H'
previous_f_log_beta = '0'
previous_s_log_beta = '0'
previous_f_init_conc = '0.01'
previous_s_init_conc = '0.02'
previous_f_add_conc = '0'
previous_s_add_conc = '-0.15'

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("input.html")

@app.route("/result", methods=['POST','GET'])
def result():
    global previous_molecules
    global previous_f_log_beta
    global previous_s_log_beta
    global previous_f_init_conc
    global previous_s_init_conc
    global previous_f_add_conc
    global previous_s_add_conc
    output = request.form.to_dict()
    name = output["name"]
    beta1=request.form['beta1']
    beta2=request.form['beta2']
    c01=request.form['c01']
    c02=request.form['c02']
    cadded0=request.form['cadded0']
    cadded1=request.form['cadded1']
    if(name == ''):
        name = previous_molecules
    else:
        previous_molecules = name
    if(beta1 == ''):
        beta1 = previous_f_log_beta
    else:
        previous_f_log_beta = beta1
    if(beta2 == ''):
        beta2 = previous_s_log_beta
    else:
        previous_s_log_beta = beta2
    if(c01 == ''):
        c01 = previous_f_init_conc
    else:
        previous_f_init_conc = c01
    if(c02 == ''):
        c02 = previous_s_init_conc
    else:
        previous_s_init_conc = c02
    if(cadded0 == ''):
        cadded0 = previous_f_add_conc
    else:
        previous_f_add_conc = cadded0
    if(cadded1 == ''):
        cadded1 = previous_s_add_conc
    else:
        previous_s_add_conc = cadded1
    data=dp.DataPh(name,beta1,beta2,c01,c02,cadded0,cadded1)

    return render_template("index.html", out=data)

@app.route('/ajax', methods = ['POST'])
def ajax_request():
    global previous_molecules
    global previous_f_log_beta
    global previous_s_log_beta
    global previous_f_init_conc
    global previous_s_init_conc
    global previous_f_add_conc
    global previous_s_add_conc
    molecules = request.form["name"]
    f_log_beta=request.form["beta1"]
    s_log_beta = request.form["beta2"]
    f_init_conc = request.form["c01"]
    s_init_conc = request.form["c02"]
    f_add_conc = request.form["cadded0"]
    s_add_conc = request.form["cadded1"]
    if(molecules == ''):
        molecules = previous_molecules
    else:
        previous_molecules = molecules
    if(f_log_beta == ''):
        f_log_beta = previous_f_log_beta
    else:
        previous_f_log_beta = f_log_beta
    if(s_log_beta == ''):
        s_log_beta = previous_s_log_beta
    else:
        previous_s_log_beta = s_log_beta
    if(f_init_conc == ''):
        f_init_conc = previous_f_init_conc
    else:
        previous_f_init_conc = f_init_conc
    if(s_init_conc == ''):
        s_init_conc = previous_s_init_conc
    else:
        previous_s_init_conc = s_init_conc
    if(f_add_conc == ''):
        f_add_conc = previous_f_add_conc
    else:
        previous_f_add_conc = f_add_conc
    if(s_add_conc == ''):
        s_add_conc = previous_s_add_conc
    else:
        previous_s_add_conc = s_add_conc
    data=dp.DataPh(molecules,f_log_beta, s_log_beta, f_init_conc, s_init_conc, f_add_conc, s_add_conc)
    return jsonify(out=data)

if __name__=='__main__':
    app.run(debug=True,port=5001)