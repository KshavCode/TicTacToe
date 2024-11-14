from tkinter import * 
from tkinter.messagebox import *

# INITIALIZATION
root = Tk()
root.geometry("600x450")
root.title("TicTacToe")
c = 0
n = 0
sequence = []
sequence2 = list(range(9))
    
# FUNCTIONS
def check_game(x) :
    global sequence, sequence2, c
    if (sequence2[0]==sequence2[1]==sequence2[2] or sequence2[3]==sequence2[4]==sequence2[5] or sequence2[6]==sequence2[7]==sequence2[8] or sequence2[0]==sequence2[3]==sequence2[6] or sequence2[1]==sequence2[4]==sequence2[7] or sequence2[2]==sequence2[5]==sequence2[8] or sequence2[0]==sequence2[4]==sequence2[8] or sequence2[2]==sequence2[4]==sequence2[6]) : 
        for i in sequence :
            i.config(state=DISABLED)
        showinfo("Winner", f"{sequence2[x]} Wins!")
    elif c ==9 :
        showinfo("Tie", "It's a Tie!")

def change(x) :
    global c, sequence
    if c%2==0 :
        sequence[x].config(text="❌", state=DISABLED, background="white")
        sequence2[x] ="❌"
    else :
        sequence[x].config(text="⭕", state=DISABLED, background="white")
        sequence2[x] ="⭕"
    c += 1
    check_game(x)
    

# MAIN
for i in range(3) :
    for j in range(3) :
        sequence.append(Button(root, text="", width=3, command=lambda x=n:change(x), font="arial 50", background="#ffa3a3"))
        sequence[n].grid(row=i, column=j, padx=5, pady=5)
        n += 1
lab = Label(root, text="Press any key to restart", font="arial 15", wraplength=150)
lab.grid(row=1, column=3, padx=30)

def key_press(e) :
    global c
    for i in range(9) :
        sequence[i].config(text="", state=NORMAL, background="#ffa3a3")
        sequence2[i] = i
        c = 0

root.bind("<KeyPress>", key_press)
root.mainloop()