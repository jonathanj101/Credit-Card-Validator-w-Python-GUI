# PYTHON GUI
from tkinter import *
from PIL import ImageTk, Image


# class Card_Validation():
#     def __init__(self, card_number):
#         # check if card consist of 16 digits
#         self.card_number = card_number

#         if card_number == 16:
#             pass
#         else:
#             pass

#     def is_card_numbers_only(self):
#         # check if input contain only number
#         if int(self.card_number):
#             pass
#         else:
#             pass
#     def card_starting_number(self):
#         # check if card number starts with 9 or 7 or 3
#         pass



window = Tk()
window.geometry("1000x500")
window.title("Credit Card Validator")

#converting img data type into supperted data type for tkinter
image_path = Image.open('./Images/creditcard.png')
python_image = ImageTk.PhotoImage(image_path)
image_label = Label(window,image=python_image).pack()

entry = Entry(window)




window.mainloop()