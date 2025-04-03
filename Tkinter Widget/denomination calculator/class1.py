from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window= Tk()
window.title ("denomination calculator" )
window.configure (bg='light blue')
window.geometry ("650x400")
upload = Image.open("Tkinter Widget/denomination calculator/app_img.jpg")
upload=upload.resize((300,300))
image=ImageTk.PhotoImage(upload)
label= Label(window, image=image,bg='light blue')
label.place(x=180,y=20)
window.mainloop()

 


