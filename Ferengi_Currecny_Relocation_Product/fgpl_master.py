import tkinter as tk

root = tk.Tk()


#frames
f1 = tk.Frame(root)
f2 = tk.Frame(root)
f3 = tk.Frame(root)
f4 = tk.Frame(root)


#Frame 1 Setup
# Note everything is being placed in Frame 1 and we are simply packing

cur_label = tk.Label(f1, text = "Select Currency")
variable = tk.StringVar(root)
variable.set("one") # default value

cur_select = tk.OptionMenu(f1, variable, "one", "two", "three")
cur_select.pack()




#Frame Placements
f1.grid(row = 0, column = 0)
f2.grid(row = 1, column = 0)
f3.grid(row = 1, column = 1, rowspan = 2)
f4.grid(row = 2, column = 0, columnspan = 2)





root.mainloop()