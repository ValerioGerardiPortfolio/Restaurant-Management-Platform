
import tkinter as tk
from PIL import Image, ImageTk

#database connection
import sqlite3
connection = sqlite3.connect("Rosmarino_Restaurants.db")
cursor=connection.cursor()

rows = cursor.fetchall()
for row in rows:
    print(row)
def make_reservation():
    print("Reservation functionality coming soon!")

def place_order():
    print("Place an order functionality coming soon!")

def order_with_deliveroo():
    print("To be implemented!")

# Initialize Tkinter root
root = tk.Tk()
root.title("Rosmarino Restaurant Homepage")

# Set a fixed size for the window
root.geometry("800x600")  # Set the desired width and height
root.resizable(False, False)  # Disable resizing

# Load the original image
original_image = Image.open("Rosmarino.png")

# Resize the image to fit the fixed window size
resized_image = original_image.resize((800, 600), Image.Resampling.LANCZOS)
image_display = ImageTk.PhotoImage(resized_image)

# Create a label to display the image
image_label = tk.Label(root, image=image_display)
image_label.pack(fill="both", expand=True)

# Add title label
title_label = tk.Label(root, text="Welcome to Rosmarino Restaurant", font=("Arial", 20, "bold"), bg="white")
title_label.place(relx=0.5, rely=0.1, anchor="center")

# Add buttons
reservation_button = tk.Button(root, text="Make a Reservation", font=("Arial", 12, "bold"), width=25, activebackground="green", command=make_reservation)
reservation_button.place(relx=0.2, rely=0.2, anchor="center")

order_button = tk.Button(root, text="Place an Order", font=("Arial", 12, "bold"), width=25, activebackground="green", command=place_order)
order_button.place(relx=0.5, rely=0.2, anchor="center")

deliveroo_button = tk.Button(root, text="Order with Deliveroo", font=("Arial", 12,"bold"), width=25, activebackground="green", command=order_with_deliveroo)
deliveroo_button.place(relx=0.8, rely=0.2, anchor="center")

# Run the application
root.mainloop()