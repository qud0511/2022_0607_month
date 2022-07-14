from tkinter import *
tk = Tk()

def event():
    label = Label(tk, text='집가고 싶으신가요?')
    label.pack()
    tk.mainloop()
    button['text'] = '탈락!'

button = Button(tk, text= '네', command = event)
button2 = Button(tk, text= '아니오')
button.pack(side=LEFT,padx=10, pady=10)
button2.pack(side=LEFT, padx=10, pady=10)
tk.mainloop()