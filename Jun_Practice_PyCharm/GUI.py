# https://seill.tistory.com/835


import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox

win = tk.Tk()
win.geometry("390x280")
win.title("Python tkinter")

def click_me():
    msgbox.showinfo(title="완료", message=name_entered.get() + '님 안녕하세요! ' + number.get() + ' 번을 좋아하네요 :)')

frame = tk.LabelFrame(win, text='1번 프레임', padx=15, pady=15) # padx / pady 내부여백
frame.pack(padx=10, pady=10) # padx / pady 외부여백

ttk.Label(frame, text="이름을 입력해주세요.").grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(frame, width=15, textvariable=name)
name_entered.grid(column=0, row=1)

ttk.Label(frame, text="숫자를 골라주세요.").grid(column=1, row=0)

number = tk.StringVar()
number_chosen = ttk.Combobox(frame, width=15, textvariable=number, state='readonly')
number_chosen['values'] = (1, 3, 5, 7, 9)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

action = ttk.Button(frame, text="Click!", command=click_me)
action.grid(column=2, row=1)

###### 2번째 Frame ######
frame2 = tk.LabelFrame(win, text='※ 사용시 주의사항 ※', padx=15, pady=15) # padx / pady 내부여백
frame2.pack(fill="both", expand=True, padx=10, pady=10) # padx / pady 외부여백
ttk.Label(frame2, text="1. 이런식으로 2개의 frame을 만들어서 사용하시면 됩니다.").place(x=0, y=5)
ttk.Label(frame2, text="2. 응용해서 멋진 gui를 만드세요 :)").place(x=0, y=25)

name_entered.focus()

win.mainloop()