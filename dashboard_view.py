from flask import Flask, render_template, request, jsonify, redirect, url_for, json
from sql_model import Dashboard

app_dl = Flask(__name__)
app_dl.secret_key = 'hello key'
app_dl.config['JSON_AS_ASCII'] = False


@app_dl.route('/dashboard')
def dashboard():
    dashboards = Dashboard.select()
    return render_template("dashboard_list.html", dashboards=dashboards)


@app_dl.route('/add_dashboard', methods=['GET', 'POST'])
def add_dashboard():
    name = request.form.get("name")
    desc = request.form.get("desc")
    Dashboard.create(name=name, desc=desc)
    return redirect(url_for('dashboard'))
    # return redirect('/dashboard')


@app_dl.route('/config')
def config():
    return render_template("config.html")


if __name__ == '__main__':
    app_dl.config['JSONIFY_MIMETYPE'] = "application/json; charset=utf-8"
    app_dl.run(port=5001, debug=True)
