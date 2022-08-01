from tkinter import *


window=Tk()
window.title("Disappearing Text App")
window.minsize(1000,600)
window.maxsize(1000,600)
title =Label(window)
subtitle =Label(window)
text =Text(window)

title.configure(
    text = "Dont stop typing !! else you are doomed",
    font =("Times","18"),pady = 20)

limit = 0

def timer():
    global limit
    limit += 1
    if limit >= 5:
        new_data =text.get(2.0,5.0)
        with open ("text.txt","w")as data_file:
            data_file.write(new_data)
            text.delete(1.0,5.0)
            return
    window.after(1000,timer)

def reset(event):
    global limit
    limit = 0


text.bind("<Key>", reset)


title.pack()
text.pack()
start_button = Button(text="Start", command=timer, pady=20).pack()
window.mainloop()



