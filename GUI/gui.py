import tkinter as g
root = g.Tk()
root.title("first gui")
root.config(bg="red")

root.geometry("600x800")

label = g.Label(root,text="enter the name").grid(row=0,column=0,padx=60,pady=60)
inp = g.Entry(root).grid(row=0,column=1) 
btn = g.Button(root,text="enter",width=30,height=2,fg= "blue").grid(row=1,column=0,padx=60)

root.mainloop()