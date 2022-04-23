from flask import Flask, render_template, request, jsonify, redirect, url_for, json


app = Flask(__name__)
app.secret_key = 'development key'
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.config['JSONIFY_MIMETYPE'] = "application/json; charset=utf-8"
    app.run(debug=False)
