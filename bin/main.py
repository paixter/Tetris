import tkinter as tk

#===================================

def UpMenu(event):
    
    global main_choice
    main_choice -= 1
    main_choice %= 3

    if main_choice == 0:
        label_start["text"] = "> START <"
        label_start.place(x = 129, y = 199)

        label_top["text"] = "TOP"
        label_top.place(x = 229, y = 333)

    if main_choice == 1:
        label_top["text"] = "> TOP <"
        label_top.place(x = 169, y = 333)

        label_rules["text"] = "RULES"
        label_rules.place(x = 182, y = 467)

    if main_choice == 2:
        label_rules["text"] = "> RULES <"
        label_rules.place(x = 122, y = 467)

        label_start["text"] = "START"
        label_start.place(x = 189, y = 199)

def DownMenu(event):
    
    global main_choice
    main_choice += 1
    main_choice %= 3

    if main_choice == 0:
        label_start["text"] = "> START <"
        label_start.place(x = 129, y = 199)

        label_rules["text"] = "RULES"
        label_rules.place(x = 182, y = 467)

    if main_choice == 1:
        label_top["text"] = "> TOP <"
        label_top.place(x = 169, y = 333)

        label_start["text"] = "START"
        label_start.place(x = 189, y = 199)

    if main_choice == 2:
        label_rules["text"] = "> RULES <"
        label_rules.place(x = 122, y = 467)

        label_top["text"] = "TOP"
        label_top.place(x = 229, y = 333)

#=====================================
        
root = tk.Tk()
root.title("Tetris")
root.geometry("600x800")
root.resizable(False, False)
root.iconphoto(True, tk.PhotoImage(file = "Icons/icon.png"))
root.configure(bg='black')

main_choice = 0

label_start = tk.Label(text = "> START <",
                       foreground = "white",
                       background = "black",
                       font = ("system",80))
label_start.place(x = 129, y = 199)

label_top = tk.Label(text = "TOP",
                       foreground = "white",
                       background = "black",
                       font = ("system",80))
label_top.place(x = 229, y = 333)

label_rules = tk.Label(text = "RULES",
                       foreground = "white",
                       background = "black",
                       font = ("system",80))
label_rules.place(x = 182, y = 467)

root.bind('<Up>', UpMenu)
root.bind('<Down>', DownMenu)

root.mainloop()
