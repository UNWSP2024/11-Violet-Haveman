    ## Program #2: Write a GUI program that displays your name and address when a "Show Info" button is clicked.
    ## There should also be a "Quit" button which exists the GUI.

import tkinter
from tkinter import messagebox

class Info_GUI:
    def __init__(self):

            ## Create window
        self.main_window = tkinter.Tk()

            ## Create Window Title
        self.main_window.title("Personal Information")

            ## Create first button
        self.my_button = tkinter.Button(self.main_window, text = "Personal Information", command=self.do_something)

            ## Create quit button
        self.quit_button = tkinter.Button(self.main_window, text = "Quit", command=self.main_window.destroy)

            ##Pack buttons
        self.my_button.pack()
        self.quit_button.pack()

            ## Loop through GUI
        tkinter.mainloop()

            ##Display information
    def do_something(self):
        tkinter.messagebox.showinfo('Response',
                            'Violet Haveman: 14665 80th St. S. Hastings MN')


if __name__ == '__main__':
    info_gui = Info_GUI()
