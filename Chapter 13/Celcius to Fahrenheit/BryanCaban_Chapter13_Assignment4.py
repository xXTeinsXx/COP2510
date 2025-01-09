# Celsius to Fahrenheit with a gui (Chapter 13: #4)

# importing the necessary libraries
import tkinter

# Function to convert Celsius to Fahrenheit
def convert(temp1, fahr_temp):
    try:
        temp = float(temp1.get())
        fahr = temp * 9 / 5 + 32
        fahr_temp.set(f"{fahr:.2f}")  # Update the entry2 widget with the Fahrenheit temperature
    except ValueError:
        fahr_temp.set("Invalid input")  # Handle non-numeric inputs

# creating the GUI
root = tkinter.Tk()
root.title("Celsius to Fahrenheit")

# creating the labels
label1 = tkinter.Label(root, text="Enter the temperature in Celsius:")
label2 = tkinter.Label(root, text="The temperature in Fahrenheit is:")

# creating the entry box
entry1 = tkinter.Entry(root)
entry2 = tkinter.Entry(root)

# creating a string variable to store Fahrenheit temperature
fahr_temp = tkinter.StringVar()
entry2.config(state="readonly", textvariable=fahr_temp)  # Make entry2 read-only and link it to fahr_temp

# creating the button
button = tkinter.Button(root, text="Convert", command=lambda: convert(entry1, fahr_temp))

# placing the labels and entry box on the GUI
label1.grid(row=0, column=0, padx=5, pady=5)
label2.grid(row=1, column=0, padx=5, pady=5)
entry1.grid(row=0, column=1, padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)
button.grid(row=2, column=0, columnspan=2, pady=10)

# starting the GUI
root.mainloop()
