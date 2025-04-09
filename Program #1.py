    ## Program #1: Create a GUI window that displays your favorite saying.
import tkinter

class Saying_GUI:
    def __init__(self):

            ## Create first window
        self.main_window = tkinter.Tk()

            ## Create Window Title
        self.main_window.title("My Favorite Saying")

            ## Add Text
        self.label = tkinter.Label(self.main_window, text = "Find a penny, pick it up, and all day long you'll have good luck!")

            ## Position the window
        self.label.pack()

            ## Loop through GUI
        tkinter.mainloop()


if __name__ == '__main__':
    saying_gui = Saying_GUI
