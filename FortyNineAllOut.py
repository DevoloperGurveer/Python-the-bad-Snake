from tkinter import *
window=Tk()
window.title("Event Handler")
window.geometry=("100X100")
def handle_keypress(event):
    print(event.char)
    window.hind("<Key>",handle_keypress)
def handle_click(event):
        print("\n Haarcb!")
button=Button(text="Click Me!")
button.pack()
button.bind("<Button-1>",handle_click)
window.mainloop()