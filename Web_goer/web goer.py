from tkinter import *
import webbrowser

root = Tk()
root.title("Any where")
root.geometry("200x200")



def GO():
	webbrowser.open('www.'+str(entry_1.get())+'.com')


entry_1 = Entry(root, borderwidth = 15)
entry_1.pack()

button_1 = Button(root, text = "GO", command = GO, bg = 'black', fg = 'white').pack(pady = 10, padx = 10 , ipadx = 15)
button_2 = Button(root, text = 'EXIT', command = root.quit, bg = 'orange').pack(pady = 10, padx = 10, ipadx = 10)







root.mainloop()