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
    html_file = """        <div id="config_zone" name="{{id}}" style="margin:0;width:100%; height:1100px">
            <div class="draggable" id="aaa"> </div>
        </div>"""
    Dashboard.create(name=name, desc=desc, html_file=html_file)
    return redirect(url_for('dashboard'))


@app_dl.route('/config/<dashboard_id>', methods=['GET', 'POST'])
def config(dashboard_id):
    name = Dashboard.select().where(Dashboard.id == dashboard_id).first().name
    return render_template("config.html", id=dashboard_id, name=name)


@app_dl.route('/update/<dashboard_id>', methods=['GET', 'POST'])
def update(dashboard_id):
    html = Dashboard.select().where(Dashboard.id == dashboard_id).first().html_file
    print(html)
    return html


@app_dl.route('/config/save_config_dashboard/<dashboard_id>', methods=['GET', 'POST'])
def save_config_dashboard(dashboard_id):
    a_id = int(dashboard_id)
    html = request.form.get("html")
    Dashboard.update(html_file=html).where(Dashboard.id == a_id).execute()
    return "success"


if __name__ == '__main__':
    app_dl.config['JSONIFY_MIMETYPE'] = "application/json; charset=utf-8"
    app_dl.run(port=5050, debug=True)
