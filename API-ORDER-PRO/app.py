from flask import Flask ,request
app = Flask(__name__)
orders = {}
@app.route("/")
def welcome():
    return {"message":"Welcome to Lucky Brews"}
@app.route("/menu",methods=["GET"])
def get_menu():
    return {"menu":["Espresso","Latte","Cappuccino","Cold Coffee"]}
@app.route("/order",methods=["POST"])
def place_order():
    data = request.json
    order_id = len(orders)+1
    orders[order_id] = {
        "item":data.get("item"),
        "quantity":data.get("quantity")
    }
    return {"message":f"Order Placed with ID{order_id}"}
@app.route("/order/<int:order_id>",methods=["PUT"])
def update_order(order_id):
    if order_id in orders:
        data = request.json
        orders[order_id]["items"]=data.get("item",orders[order_id]["item"])
        orders[order_id]["quantity"] =data.get("quantity",orders[order_id]["quantity"])
        return {"message": f"order{order_id}updated"}
    else:
        return {"message": "Order not found"},404
@app.route("/order/<int:order_id>",methods=['DELETE'])
def cancel_order(order_id):
    if order_id in orders:
        return {"message":f"order{order_id}cancelled"}
    else:
        return {"message":"Order not found"},404
if __name__ =="__main__":
    app.run(debug=True)

