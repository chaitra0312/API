from flask import Flask ,jsonify,request
app = Flask(__name__)
user = [
    {"id":1, "name":"chaitra"},
    {"id":2, "name":"lucky"}
]
@app.route("/users",methods=["GET"])
def get_users():
    return jsonify(users)
@app.route("/users",methods=["POST"])
def add_users():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify({"message":"User added succesfully!"}),201

if __name__ == "__main__":
    app.run(debug=True)
