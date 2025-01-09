# My first gui in python

import tkinter
import os
# Set environment variable
os.environ['TK_SILENCE_DEPRECATION'] = str(1)

class MyGui:
    # Create main window
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Create stringVAR objects to display the name value, street value, and city-state-zip value
        self.name_var = tkinter.StringVar()
        self.street_var = tkinter.StringVar()
        self.city_state_zip_var = tkinter.StringVar()

        # Create the two frames
        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create label widgets for stringVAR objects
        self.name_label = tkinter.Label(self.info_frame, \
                                        textvariable= self.name_var)
        self.street_label = tkinter.Label(self.info_frame, \
                                          textvariable= self.street_var)
        self.city_state_zip_label = tkinter.Label(self.info_frame, \
                                                  textvariable= self.city_state_zip_var)
        
        # pack the labels
        self.name_label.pack()
        self.street_label.pack()
        self.city_state_zip_label.pack()

        # Create buttons
        self.show_info_buttpon = tkinter.Button(self.button_frame, \
                                                text="Show Info", \
                                                command = self.show)

        self.quit_button = tkinter.Button(self.button_frame, \
                                          text="Quit", \
                                          command = self.main_window.destroy)
        
        # Pack the buttons
        self.show_info_buttpon.pack(side = "left")
        self.quit_button.pack(side = "right")

        # Pack the frames
        self.info_frame.pack()
        self.button_frame.pack()

        # Enter the tkinter mainloop
        tkinter.mainloop()
       

    # Create the show function (Function for show info button)
    def show(self):
        self.name_var.set("Bry")
        self.street_var.set("123 Main Street")
        self.city_state_zip_var.set("Place, Fl 12345")

my_gui = MyGui()
