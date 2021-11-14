# PYTHON GUI
from tkinter import *
from PIL import ImageTk, Image


window = Tk()
window.geometry("1000x500")
window.title("Credit Card Validator")

#converting img data type into supperted data type for tkinter
image_path = Image.open('./Images/creditcard.png')
python_image = ImageTk.PhotoImage(image_path)
image_label = Label(window,image=python_image).pack()

entry = Entry(window)




window.mainloop()