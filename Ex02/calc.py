import tkinter as tk
import tkinter.messagebox as tkm
root = tk.Tk()
root.title("電卓")
root.geometry("300x500")
def button_func(event):
    event.widget.config(fg="red")
root.tkinter.Tk()
for j in range(3):
    for i in range(3):
        button_name = "ボタン(" + str(i) + "," + str(j)+ ")"

        # ボタンのインスタンス作成
        button = tkinter.Button(app,text=button_name)
        button.grid(column=i, row=j)
root.mainloop()