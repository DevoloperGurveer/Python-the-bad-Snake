from tkinter import *
from tkinter.filedialog import asksaveasfile
root=Tk()
root.geometry('200x150')
def save():
    files=[('All files','*.*'),('Python Files','*.py'),('Text Document','*.py')]
    file=asksaveasfile(filetypes=files,defaultextension=files)
btn=Button(root,text='Save',command=lambda : save())
btn.pack(side=TOP)
mainloop()