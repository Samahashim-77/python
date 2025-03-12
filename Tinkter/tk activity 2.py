import tkinter as tk
window= tk.Tk()
for  c in range(4):
    for r in range(4):
        frame=tk.Frame(master=window, relief=tk.RAISED,borderwidth=1)
        frame.grid(row=r, column=c, padx=5, pady=5)
        label= tk.Label(master=frame,text=f"Row{r}\nColumn{c}" )
        label.pack()
window.mainloop()
                    
