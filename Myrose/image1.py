from tkinter import *
from PIL import Image, ImageTk
window = Tk()
window.title('my rose')
window.geometry('400x400')
Rose= Image.open('rose2.png')
image1= ImageTk.PhotoImage(Rose)

label=Label(window,image=image1, height=200, width=150)
label.place(x=50, y=50)
window.mainloop()


