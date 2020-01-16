from tkinter import *

def main():
    
    root = Tk()
    
    screen = Canvas(root, width=800, height=500)
    screen.pack()
    
    screen.create_line(0, 0, 200, 100)
    screen.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

    screen.create_rectangle(50, 25, 150, 75, fill="blue")

    screen.create_oval(10, 10, 20, 20, fill="red")
    screen.create_oval(200, 200, 220, 220, fill="blue")
    
    
    sx = Scrollbar(root, orient="horizontal", command=screen.xview)
    sx.grid(row=1, column=0, sticky="ew")
    sy = Scrollbar(root, orient="vertical", command=screen.yview)
    sy.grid(row=0, column=1, sticky="ns")
    
    screen.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)
    screen.configure(scrollregion=screen.bbox("all"))
             
    # def callback():
    #     b.config(relief=SUNKEN)
    #     
    # b = Button(root, text="OK", command=callback)
    # b.pack()
    
    root.mainloop()

if __name__ == '__main__':
    main()