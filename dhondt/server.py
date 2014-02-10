from flask import Flask, request, jsonify, render_template

from . import dhondt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dhondt')
def calculate_dhondt():
    votes = request.args.getlist('v', type=int)
    # TODO: sanitize input
    result = dhondt(votes, 3)
    return jsonify(result=result)