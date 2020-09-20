import tkinter as tk

root = tk.Tk()


def login():
	print("LOGIN")
	w2.pack_forget()
	w1.pack()

def exit():
	root.destroy()

#Windows
w1 = tk.Frame(root)
w1.config(bg = "#A65E2E")

w2 = tk.Frame()
w2.config(bg = "#A65E2E")

#LOGIN SETUP


f1w2 = tk.Frame(w2, highlightbackground = "black", highlightthickness=1)
f1w2.config(bg = "#A65E2E")
f2w2 = tk.Frame(w2, highlightbackground = "black", highlightthickness=1)
f2w2.config(bg = "#A65E2E")

uName_label = tk.Label(f1w2,text = "User Name: ", bg = "#A65E2E")
uName_entry = tk.Entry(f1w2)


pwrd_label = tk.Label(f1w2,text = "Password: ", bg = "#A65E2E")
pwrd_entry = tk.Entry(f1w2)

login_btn = tk.Button(f2w2, text = "Login", width = 20, command = login)
nuser_btn = tk.Button(f2w2, text = "NU", width = 5)

uName_label.pack()
uName_entry.pack()
pwrd_label.pack()
pwrd_entry.pack()
login_btn.pack(side = tk.LEFT)
nuser_btn.pack(side = tk.RIGHT)

f1w2.pack(fill = tk.X, ipady = 5, ipadx = 5)
f2w2.pack(ipady = 5, ipadx = 5)
w2.pack()

#MAIN INTERFACE SETUP
#frames
f1 = tk.Frame(w1, highlightbackground = "black", highlightthickness=1)
f2 = tk.Frame(w1, highlightbackground = "black", highlightthickness=1)
f3 = tk.Frame(w1, highlightbackground = "black", highlightthickness=1)
f4 = tk.Frame(w1)


#Frame 1 Setup
# Note everything is being placed in Frame 1 and we are simply packing

cur_label = tk.Label(f1, text = "Select Currency")
variable = tk.StringVar(root)
variable.set("one") # default value

cur_select = tk.OptionMenu(f1, variable, "one", "two", "three")

cur_label.pack()
cur_select.pack()


#Frame 2 Setup

input1_label = tk.Label(f2, text = "Input Item and Value in GPL")
input2_label = tk.Label(f2, text = "GPL = GOLD PRESSED LATINUM")

item_entry = tk.Entry(f2)
value_entry =tk.Entry(f2)

#Frame 3 Setup

display = tk.Text(f3, height = 25, width = 60)
display.pack()

total_label = tk.Label(f3, text = "Valuation = ")
total_label.pack()


input1_label.pack()
input2_label.pack()

item_entry.pack()
value_entry.pack()

#Frame 4 Setup
info_btn1 = tk.Button(f4, text = "INFO 1", width = 25)
info_btn2 = tk.Button(f4, text = "INFO 2", width = 25)
info_btn3 = tk.Button(f4, text = "EXIT", width = 25, command = exit)
info_btn4 = tk.Button(f4, text = "Country",width = 25)

info_btn1.pack(side = tk.LEFT)
info_btn2.pack(side = tk.LEFT)
info_btn3.pack(side = tk.RIGHT)
info_btn4.pack(side = tk.RIGHT)
#Frame Placements
f1.grid(row = 0, column = 0, sticky = "NESW", padx = 5, pady = 5, ipadx = 2, ipady = 2)
f2.grid(row = 1, column = 0, sticky = "NESW", padx = 5, pady= 5, ipadx = 2, ipady = 2)
f3.grid(row = 0, column = 1, rowspan = 2,sticky = "NESW", padx = 5, pady = 5, ipadx = 2, ipady = 2)
f4.grid(row = 2, column = 0, columnspan = 2,sticky = "NESW", padx = 5, pady = 5, ipadx = 2, ipady = 2)


#w1.pack()


root.mainloop()