from tkinter import *
from PIL import Image, ImageTk
window = Tk()
window.title('my rose')
window.geometry('400x400')
Rose= Image.open('rose.jfif')
image1= ImageTk.PhotoImage(Rose)
window.mainloop()

