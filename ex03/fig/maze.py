from cgitb import reset
import tkinter as tk
from turtle import clear
import maze_maker as mm # 練習8

# 練習5
def key_down(event):
    global key
    key = event.keysym



# 練習6
def key_up(event):
    global key
    key = ""

def search_left(): #右手法攻略
    global piece_dir,piece_x,piece_y
    if frameCount % 10 == 0:
        for i in range(4):
            dir = (piece_dir+3+i)%4
            x = piece_x + cx[dir]
            y = piece_y + cy[dir]
            if mm[x][y] == 0 or mm[x][y] == 3:
                break
        piece_dir = dir
        piece_x = x
        piece_y = y


# 練習7
def main_proc():
    global mx, my
    global cx, cy
    if key == "Up":
        my -= 1
    if key =="w": #壁貫通機能
        my -= 1    
    if key == "Down":
        my += 1
    if key == "s": #壁貫通機能
        my += 1
    if key == "Left":
        mx -= 1
    if key == "a": #壁貫通機能
        mx -= 1
    if key == "Right":
        mx += 1
    if key == "d": #壁貫通機能
        mx +=1
    if key == "s": #ｓキーを押したら開始
        search_left
    if key == "enter":
        reset
    if maze_lst[my][mx] == 0: # 床なら
        cx, cy = mx*100+50, my*100+50
    else: # 壁なら
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") # 練習1

    # 練習2
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    # 練習9,10
    maze_lst = mm.make_maze(15, 9)
    #print(len(maze_lst)) 9x15

    # print(maze_lst) # 1:壁／0:床
    mm.show_maze(canv, maze_lst) 

    #if mm[cx][cy] ==2:
        #canv.delete("all")
        #canv.create_text(160,160,text="gool",font=(None),fill="red")

    # 練習3
    tori = tk.PhotoImage(file="fig/11.png") 
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canv.create_image(cx, cy, image=tori, tag="tori")

    # 練習4
    key = "" # 現在押されているキーを表す

    # 練習5,6
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)    

    # 練習7
    main_proc()

    root.mainloop()