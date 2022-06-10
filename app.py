# import flask libraries
from flask import Flask, jsonify, request
app = Flask(__name__)

# flask run -> server runs at http://127.0.0.1:24000/ 
@app.route("/")
def hello():
    return "Hello World!"

# mock JSON database of some staff's favorite cats 
fav_cats = [{'name': 'Harsh', 'breed': 'Indian Billi'},
        {'name': 'Mon', 'breed' : 'Calico'},
        {'name': 'Saurav', 'breed': 'All cats!'},
        {'name': 'Drshi', 'breed': 'Maine Coons'}]

@app.route('/favcat', methods=['GET'])
def get_all_cats():
    # @TODO: get all the cat entries
    return jsonify()

@app.route('/favcat/<string:name>', methods=['GET'])
def get_one_cat(name):
    # @TODO: get only one staff and their favorite cat
    return jsonify()

@app.route('/favcat', methods=['POST'])
def add_cat():
    # @TODO: add a staff and their favorite cat 
    return jsonify()

@app.route('/favcat/<string:name>', methods=['PUT'])
def edit_cat(name):
    # @TODO: modify an entry in JSON 
    return jsonify()

@app.route('/favcat/<string:name>', methods=['DELETE'])
def delete_cat(name):
    # @TODO: delete a staff and their favorite cat :(
    return jsonify()
