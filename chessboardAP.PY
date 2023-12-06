import tkinter as tk
class chessboardApp:
    def __init__(self,master):
        self.master=master
        self.master.title("Chess Game")
        self.board_frame=tk.Frame(master)
        self.board_frame.pack()
        self.create_chessboard()
    def create_chessboard(self):
        for row in range(8):
            for col in range(8):
                color="white"if(row+col)%2==0 else "black"
                square=tk.Frame(self.board_frame,bg=color,width=50,height=50)
                square.grid(row=row,column=col)
if __name__=="__main__":
    root=tk.Tk()
    app=chessboardApp(root)
    root.mainloop()
        