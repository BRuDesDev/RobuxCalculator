import tkinter as tk


# Function to calculate equivalent USD value
def calculate_usd():
    try:
        # Get the value from the first entry widget
        robux = float(robux_entry.get())
        # Calculate the equivalent USD value
        usd = robux * 0.0125
        print(f"USD: {usd}")
        # Update the text in the second entry widget
        usd_entry.delete(0, tk.END)  # Clear previous value
        usd_entry.insert(0, str(usd))  # Insert new value
    except ValueError:
        # Handle non-numeric input
        usd_entry.delete(0, tk.END)  # Clear previous value
        usd_entry.insert(0, "Invalid input")


# Create and configure the root window
root = tk.Tk()
root.title("Robux Calculator")
root.configure(background="purple")
root.minsize(200, 200)
root.maxsize(900, 900)


# Load the image into script
image = tk.PhotoImage(file="robuxCalcLogo.png")

# Create the label for the image
img_label = tk.Label(root, image=image, bg="purple")
img_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the entry Text label
robux_entry_label = tk.Label(root, text="Robux to Convert", font=("Helvetica", 15, "normal"), bg="purple", fg="white")
robux_entry_label.grid(row=2, column=0, columnspan=1, padx=10, pady=10)

# Create the entry field for Robux input
robux_entry = tk.Entry(root, width=6, borderwidth=2)
robux_entry.grid(row=2, column=1)

# Bind the function to the entry widget's KeyRelease event
robux_entry.bind("<KeyRelease>", lambda event: calculate_usd())

# Show the final calculation
usd_entry_label = tk.Label(root, text="Equivalent Value in USD: ", font=("Helvetica", 15, "normal"), bg="purple", fg="white")
usd_entry_label.grid(row=2, column=2)

# Create the entry field for USD output
usd_entry = tk.Entry(root, width=6, borderwidth=2)
usd_entry.grid(row=2, column=3)

root.mainloop()


