from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning('Alert',"Stop!Say CSK on top")
button= Button(root,text="Scan for virus",command=msg)
button.place(x=69,y=42)
root.mainloop()