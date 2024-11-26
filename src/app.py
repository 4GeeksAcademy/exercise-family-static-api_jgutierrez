"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure(last_name="Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#     GET /members
# status_code: 200 if success. 400 if bad request (wrong info). 500 if the server encounters an error
# RESPONSE BODY (content-type: application/json):
# []  <!--- List of members -->

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }
    return jsonify(members), 200
    
@app.route('/member/<int:id>', methods=['GET'])
def get_one_member(id):
    member = jackson_family.get_member(id)
    if member:
        response = {
            "id": member["id"],
            "first_name": member["first_name"],
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
        }
        return jsonify(response), 200
    else:
        return jsonify({"error": "Member not found"}), 404




#     POST /member
# REQUEST BODY (content_type: application/json):
# {
#     id: Int,
#     first_name: String,
#     age: Int,
#     lucky_numbers: []
# }
# RESPONSE (content_type: application/json):
# status_code: 200 if success. 400 if a bad request (wrong info). 500 if the server encounters an error

@app.route('/member', methods=['POST'])
def add_member():
    request_body = request.json

    if not request_body:
        return jsonify({"msg": "Invalid JSON body"}), 400

    try:
        jackson_family.add_member(request_body)
        return jsonify({"msg": "Member added successfully"}), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 500

#     DELETE /member/<int:member_id>
# RESPONSE (content_type: application/json):
# status_code: 200 if success. 400 if a bad request (wrong info). 500 if the server encounters an error
# body: {
#     done: True
# }   
    

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):

    if not id:
        return jsonify({"error": "Invalid JSON body"}), 400
    try:
        toDeleteMember = jackson_family.delete_member(id)
        return jsonify(toDeleteMember),200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
