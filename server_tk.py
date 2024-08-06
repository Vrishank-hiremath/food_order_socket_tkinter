import socket
import tkinter as tk

menu = {
    "pasta": 150,
    "pizza": 300,
    "sandwich": 80,
    "burger": 120,
    "salad": 70,
    "taco": 200,
    "burrito": 250,
    "brownie": 100,
    "rice bowl": 180,
    "icecream": 60,
    "lasangna": 130,
    "kebab": 50
}

def process_order(order):

    total_cost = 0
    order_items = order.split(",")
    for item in order_items:
        item = item.strip()
        if item in menu:
            total_cost += menu[item]

    if total_cost > 600:
        discount_amount = total_cost * 0.1
        total_cost *= 0.9
        return total_cost, discount_amount

    return total_cost, 0

def handle_client_request(client_socket):

    order = client_socket.recv(1024).decode()
    location = client_socket.recv(1024).decode()

    print("Received order:", order)
    print("Delivery Location:", location)

    total_cost, discount_amount = process_order(order)
    if discount_amount > 0:
        response = f"Your order costs ₹{total_cost:.2f} after a discount of ₹{discount_amount:.2f} has been applied."
    else:
        response = f"Your order costs ₹{total_cost:.2f}."

    window = tk.Tk()
    window.title("Order Information")

    response_label = tk.Label(window, text=response, font=("Arial", 14))
    response_label.pack(padx=20, pady=20)

    window.mainloop()

    client_socket.send(response.encode())
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.146.145', 8000))
server_socket.listen(5)

print("Server started. Waiting for connections...")

while True:
    client_socket, client_address = server_socket.accept()
    print("Connection from:", client_address)

    handle_client_request(client_socket)