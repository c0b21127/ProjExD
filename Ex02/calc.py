import tkinter as tk
from turtle import clear

def click_number(event): # 練習3
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    entry.insert(tk.END, num) # 練習5

def click_equal(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res) # 練習7


root = tk.Tk() # 練習1
root.geometry("300x700")

button = tk.Button(text='まだ押さないで',command=clear)
button.place(x=500,y=500,width=20,height=30)

def clear(event):
    entry.delete(0,tk.END)



entry = tk.Entry(root, width=10, font=(", 40"), justify="right") # 練習4
entry.grid(row=0, column=0, columnspan=3)

r, c = 1, 0 # r: 行を表す変数／c：列を表す変数
numbers = list(range(9, -1, -1)) # 数字だけのリスト
operators = ["+"]
operators1 = ["-"]
operators2 = ["*"]
operators3 = ["/"]


 # 演算子だけのリスト
for i, num in enumerate(numbers+operators+operators1+operators2+operators3, 1):
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
    btn.bind("<1>", click_number)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0
#Cボタン入力でオールクリア
btn = tk.Button(root, text=f"C", font=("", 30), width=4, height=2)
btn.bind("<1>", clear)
btn.grid(row=r+1, column=c-2)
#計算結果を出力
btn = tk.Button(root, text=f"=", font=("", 30), width=4, height=2)
btn.bind("<1>", click_equal)
btn.grid(row=r, column=c)

root.mainloop()