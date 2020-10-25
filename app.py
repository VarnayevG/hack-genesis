from flask import Flask, render_template, request
from poll import helper_q1_data, helper_q2_data, helper_q3_data, filename
import os
app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/trial')
def trial_page():
    return render_template('trial.html')


@app.route('/trial/results')
def trial_results():
    return render_template('trial_results.html')


@app.route('/stocks_currency_description')
def stocks_currency_description():
    return render_template('stocks_currency_description.html')


@app.route('/bonds_plans_description')
def bonds_plans_description():
    return render_template('bonds_plans_description.html')


@app.route('/helper')
def helper():
    return render_template('helper.html')


@app.route('/helper/q1')
def helper_q1():
    return render_template('q1.html', data=helper_q1_data)


@app.route('/helper/q2')
def helper_q2():
    vote = request.args.get('field')
    print(vote)
    out = open(filename, 'a')
    out.write(vote + '\n')
    out.close()

    return render_template('q2.html', data=helper_q2_data)


@app.route('/helper/q3')
def helper_q3():
    vote = request.args.get('field')
    print(vote)
    out = open(filename, 'a')
    out.write(vote + '\n')
    out.close()

    return render_template('q3.html', data=helper_q3_data)


@app.route('/helper/results')
def helper_results():
    vote = request.args.get('field')
    print(vote)
    out = open(filename, 'a')
    out.write(vote + '\n')
    out.close()
    f = open(filename, 'r+')
    f.truncate(0)
    return render_template('helper_results.html')


@app.route('/purchase')
def purchase():
    return render_template('purchase.html')
    
 
if __name__ == "__main__":
    app.run(debug=True)
