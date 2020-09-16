import tkinter as tk

root = tk.root()


#frames
f1 = tk.Frame(root)
f2 = tk.Frame(root)
f3 = tk.Frame(root)
f4 = tk.Frame(root)


f1.grid(row = 0, column = 0)
f2.grid(row = 1, column = 0)
f3.grid(row = 1, column = 1, rowspan = 2)
f4.grid(row = 2, column = 0, columspan = 2)





root.mainloop()