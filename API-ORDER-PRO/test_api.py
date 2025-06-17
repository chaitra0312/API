import requests

# 1. Place an Order (POST)
order_data = {
    "item": "Cappuccino",
    "quantity": 2
}

response = requests.post("http://127.0.0.1:5000/order", json=order_data)
print("POST Response:", response.json())

# 2. Update the Order (PUT)
update_data = {
    "item": "Cappuccino",
    "quantity": 3
}

response = requests.put("http://127.0.0.1:5000/order/1", json=update_data)
print("PUT Response:", response.json())

# 3. Cancel the Order (DELETE)
response = requests.delete("http://127.0.0.1:5000/order/1")
print("DELETE Response:", response.json())
