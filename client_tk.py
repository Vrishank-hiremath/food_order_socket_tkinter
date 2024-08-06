import socket
import math
from tkinter import Tk, Label, Entry, Button

def send_order():
    order = order_entry.get()
    location = location_entry.get()
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.146.145', 8000))
    
    client_socket.send(order.encode())
    client_socket.send(location.encode())
    
    response = client_socket.recv(1024).decode()
    response_label.configure(text=response)
    
    client_socket.close()

window = Tk()
window.title("Order Client")

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
menu_display = "Menu:\n"
for item, cost in menu.items():
    menu_display += f"{item} (₹{cost})\n"
menu_label = Label(window, text=menu_display)
menu_label.pack()

order_label = Label(window, text="Enter your order (separate items by commas):")
order_label.pack()
order_entry = Entry(window)
order_entry.pack()

location_label = Label(window, text="Enter your Address:")
location_label.pack()
location_entry = Entry(window)
location_entry.pack()

send_button = Button(window, text="Place Order", command=send_order)
send_button.pack()

response_label = Label(window, text="")
response_label.pack()

window.mainloop()