import tkinter as tk
from tkinter import messagebox

def is_valid(board,row,col,num):
    #Check the row
    for x in range(9):
        if board[row][x]==num:
            return False
    #Check the column
    for x in range(9):
        if board[x][col]==num:
            return False

    #Check the box
    start_row=row-row%3
    start_col=col-col%3
    for i in range(3):
        for j in range(3):
            if board[i+start_row][j+start_col]==num:
                return False

    return True

def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j]=num
                        if solve_sudoku(board):
                            return True
                        board[i][j]=0
                return False

    return True

def get_board():
    board=[]
    for i in range(9):
        row=[]
        for j in range(9):
            try:
                val=int(entries[i][j].get())
            except ValueError:
                val=0
            row.append(val)
        board.append(row)
    return board

def solve_and_display():
    board=get_board()
    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, board[i][j])
    else:
        messagebox.showerror("Error","Nos solution exists")

root=tk.Tk()
root.title("Sudoku solver")

entries=[]
for i in range(9):
    row=[]
    for j in range(9):
        e=tk.Entry(root, width=2, font=('Arial',24), justify='center')
        e.grid(row=i, column=j)
        row.append(e)
    entries.append(row)

solve_button=tk.Button(root, text="Solve", command=solve_and_display)
solve_button.grid(row=10,column=0,columnspan=9)

root.mainloop()



