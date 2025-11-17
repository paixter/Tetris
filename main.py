import tkinter as tk

from threading import Thread
from playsound import playsound 
def music():
    playsound('music.mp3')
    music()
Thread(target = music, daemon=True).start()


#===================================

def UpMainMenu(event):
    
    global main_choice
    main_choice -= 1
    main_choice %= 3

    if main_choice == 0:
        label_menu_start["text"] = "> START <"
        label_menu_start.place(x = 129, y = 199)

        label_menu_top["text"] = "TOP"
        label_menu_top.place(x = 229, y = 333)

    if main_choice == 1:
        label_menu_top["text"] = "> TOP <"
        label_menu_top.place(x = 169, y = 333)

        label_menu_rules["text"] = "RULES"
        label_menu_rules.place(x = 182, y = 467)

    if main_choice == 2:
        label_menu_rules["text"] = "> RULES <"
        label_menu_rules.place(x = 122, y = 467)

        label_menu_start["text"] = "START"
        label_menu_start.place(x = 189, y = 199)

def DownMainMenu(event):
    
    global main_choice
    main_choice += 1
    main_choice %= 3

    if main_choice == 0:
        label_menu_start["text"] = "> START <"
        label_menu_start.place(x = 129, y = 199)

        label_menu_rules["text"] = "RULES"
        label_menu_rules.place(x = 182, y = 467)

    if main_choice == 1:
        label_menu_top["text"] = "> TOP <"
        label_menu_top.place(x = 169, y = 333)

        label_menu_start["text"] = "START"
        label_menu_start.place(x = 189, y = 199)

    if main_choice == 2:
        label_menu_rules["text"] = "> RULES <"
        label_menu_rules.place(x = 122, y = 467)

        label_menu_top["text"] = "TOP"
        label_menu_top.place(x = 229, y = 333)

def ReturnMainMenu(event):
    
    global main_choice

    if main_choice == 0:
        frame_main_menu.pack_forget()
        frame_game.pack()
        frame_game.focus_set()

    if main_choice == 1:
        frame_main_menu.pack_forget()
        frame_top.update()
        frame_top.pack()
        frame_top.focus_set()
    
    if main_choice == 2:
        frame_main_menu.pack_forget()
        frame_rules.pack()
        frame_rules.focus_set()

def ReturnGameMenu(event):
    
    frame_game.pack_forget()
    frame_main_menu.pack()
    frame_main_menu.focus_set()

def NGameMenu(event):

    global frame_game_field
    frame_game_field.destroy()

    frame_game_field = tk.Frame(frame_game,
                            width = 400,
                            height = 800,
                            bg = "black")

    f = open("field.txt", "r")
    score = f.readline().replace("\n","")
    lines = f.readline().replace("\n","")
    trt = f.readline().replace("\n","")
    a = []
    for i in f:
        a.append(i.replace("\n","").split(","))
    f.close()

    y = 760
    for i in a:
        x = 0
        for j in i:
            if j == "1":
                shape_game = tk.Label(frame_game_field,
                                      image = big_blue_block_image,
                                      borderwidth = 0)
                shape_game.place(x = x, y = y)
                
            elif j == "2":
                shape_game = tk.Label(frame_game_field,
                                      image = big_green_block_image,
                                      borderwidth = 0)
                shape_game.place(x = x, y = y)
                
            elif j == "3":
                shape_game = tk.Label(frame_game_field,
                                      image = big_purple_block_image,
                                      borderwidth = 0)
                shape_game.place(x = x, y = y)

            elif j == "4":
                shape_game = tk.Label(frame_game_field,
                                      image = big_red_block_image,
                                      borderwidth = 0)
                shape_game.place(x = x, y = y)

            elif j == "5":
                shape_game = tk.Label(frame_game_field,
                                      image = big_yellow_block_image,
                                      borderwidth = 0)
                shape_game.place(x = x, y = y)
                
            x += 40
        y -= 40

    frame_game_field.place(x = 0, y = 0)

    frame_game_statistics_score_user = tk.Label(frame_game_statistics,
                                                text = score,
                                                fg = "white",
                                                bg = "gray15",
                                                font = ("system",25))
    frame_game_statistics_score_user.place(x = 10, y = 445)

    frame_game_statistics_lines_user = tk.Label(frame_game_statistics,
                                                text = lines,
                                                fg = "white",
                                                bg = "gray15",
                                                font = ("system",25))
    frame_game_statistics_lines_user.place(x = 10, y = 565)

    frame_game_statistics_trt_user = tk.Label(frame_game_statistics,
                                              text = trt + "%",
                                              fg = "white",
                                              bg = "gray15",
                                              font = ("system",25))
    frame_game_statistics_trt_user.place(x = 10, y = 685)
    
    frame_game.update()

def ReturnTopMenu(event):
    
    frame_top.pack_forget()
    frame_main_menu.pack()
    frame_main_menu.focus_set()

def ReturnRulesMenu(event):
    
    frame_rules.pack_forget()
    frame_main_menu.pack()
    frame_main_menu.focus_set()

#=====================================
        
#Настройка окна        
root = tk.Tk()
root.title("Tetris")
root.geometry("600x800")
root.resizable(False, False)
root.iconphoto(True, tk.PhotoImage(file = "Image/icon.png"))
root.configure(bg='black')

#Импорт блоков
blue_block_image = tk.PhotoImage(file = "Image/blue_block.png")
green_block_image = tk.PhotoImage(file = "Image/green_block.png")
purple_block_image = tk.PhotoImage(file = "Image/purple_block.png")
red_block_image = tk.PhotoImage(file = "Image/red_block.png")
yellow_block_image = tk.PhotoImage(file = "Image/yellow_block.png")

big_blue_block_image = blue_block_image.zoom(2,2)
big_green_block_image = green_block_image.zoom(2,2)
big_purple_block_image = purple_block_image.zoom(2,2)
big_red_block_image = red_block_image.zoom(2,2)
big_yellow_block_image = yellow_block_image.zoom(2,2)

#Настройка главного меню
frame_main_menu = tk.Frame(root,
                           width = 600,
                           height = 800,
                           bg = 'black')

main_choice = 0

label_menu_start = tk.Label(frame_main_menu,
                            text = "> START <",
                            fg = "white",
                            bg = "black",
                            font = ("system",80))
label_menu_start.place(x = 129, y = 199)

label_menu_top = tk.Label(frame_main_menu,
                          text = "TOP",
                          fg = "white",
                          bg = "black",
                          font = ("system",80))
label_menu_top.place(x = 229, y = 333)

label_menu_rules = tk.Label(frame_main_menu,
                            text = "RULES",
                            fg = "white",
                            bg = "black",
                            font = ("system",80))
label_menu_rules.place(x = 182, y = 467)

frame_main_menu.bind("<Up>", UpMainMenu)
frame_main_menu.bind("<Down>", DownMainMenu)
frame_main_menu.bind("<Return>", ReturnMainMenu)

frame_main_menu.pack()
frame_main_menu.focus_set()

#Настройка окна с игрой
frame_game = tk.Frame(root,
                      width = 600,
                      height = 800,
                      bg = "black")

frame_game.bind("n", NGameMenu)
frame_game.bind("<Return>", ReturnGameMenu)

    #Поле с статистикой
frame_game_statistics = tk.Frame(frame_game,
                                 width = 200,
                                 height = 800,
                                 bg = "gray15")
frame_game_statistics.place(x = 400, y = 0)

frame_game_statistics_score = tk.Label(frame_game_statistics,
                                       text = "SCORE",
                                       fg = "white",
                                       bg = "gray15",
                                       font = ("system",25))
frame_game_statistics_score.place(x = 10, y = 400)

frame_game_statistics_lines = tk.Label(frame_game_statistics,
                                       text = "LINES",
                                       fg = "white",
                                       bg = "gray15",
                                       font = ("system",25))
frame_game_statistics_lines.place(x = 10, y = 520)

frame_game_statistics_trt = tk.Label(frame_game_statistics,
                                       text = "TRT",
                                       fg = "white",
                                       bg = "gray15",
                                       font = ("system",25))
frame_game_statistics_trt.place(x = 10, y = 640)

    #Игровое полe
frame_game_field = tk.Frame(frame_game,
                            width = 400,
                            height = 800,
                            bg = "black")
frame_game_field.place(x = 0, y = 0)

#Настройка окна с топом
frame_top = tk.Frame(root,
                     width = 600,
                     height = 800,
                     bg = "black")

label_top_name = tk.Label(frame_top,
                          text = "NAME",
                          fg = "white",
                          bg = "black",
                          font = ("system",18))
label_top_name.place(x = 38, y = 0)

label_top_score = tk.Label(frame_top,
                           text = "SCORE",
                           fg = "white",
                           bg = "black",
                           font = ("system",18))
label_top_score.place(x = 370, y = 0)

label_top_trt = tk.Label(frame_top,
                           text = "TRT",
                           fg = "white",
                           bg = "black",
                           font = ("system",18))
label_top_trt.place(x = 524, y = 0)

    #Игрок
label_top_1 = tk.Label(frame_top,
                           text = "99999999",
                           fg = "white",
                           bg = "black",
                           font = ("system",18))
label_top_1.place(x = 370, y = 40)

label_top_1 = tk.Label(frame_top,
                           text = "1. WWWWWWWWWWW",
                           fg = "white",
                           bg = "black",
                           font = ("system",18))
label_top_1.place(x = 0, y = 40)

label_top_1 = tk.Label(frame_top,
                           text = "100%",
                           fg = "white",
                           bg = "black",
                           font = ("system",18))
label_top_1.place(x = 524, y = 40)

frame_top.bind("<Return>", ReturnTopMenu)

#Настройка окна с правилами
frame_rules = tk.Frame(root,
                       width = 600,
                       height = 800,
                       bg = "black")

label_rules_rules = tk.Label(frame_rules,
                             text = open("rules.txt", "r").read(),
                             justify = "left",
                             fg = "white",
                             bg = "black",
                             font = ("system",17))
label_rules_rules.place(x = 0, y = 0)

frame_rules.bind("<Return>", ReturnRulesMenu)

    #Фигуры в окне с правилами
        #1
shape_rules_1_1 = tk.Label(frame_rules,
                           image = blue_block_image,
                           borderwidth = 0)
shape_rules_1_1.place(x = 60, y = 710)

shape_rules_1_2 = tk.Label(frame_rules,
                           image = blue_block_image,
                           borderwidth = 0)
shape_rules_1_2.place(x = 80, y = 710)

shape_rules_1_3 = tk.Label(frame_rules,
                           image = blue_block_image,
                           borderwidth = 0)
shape_rules_1_3.place(x = 100, y = 710)

shape_rules_1_4 = tk.Label(frame_rules,
                           image = blue_block_image,
                           borderwidth = 0)
shape_rules_1_4.place(x = 100, y = 730)

        #2
shape_rules_2_1 = tk.Label(frame_rules,
                           image = green_block_image,
                           borderwidth = 0)
shape_rules_2_1.place(x = 130, y = 710)

shape_rules_2_2 = tk.Label(frame_rules,
                           image = green_block_image,
                           borderwidth = 0)
shape_rules_2_2.place(x = 150, y = 710)

shape_rules_2_3 = tk.Label(frame_rules,
                           image = green_block_image,
                           borderwidth = 0)
shape_rules_2_3.place(x = 150, y = 730)

shape_rules_2_4 = tk.Label(frame_rules,
                           image = green_block_image,
                           borderwidth = 0)
shape_rules_2_4.place(x = 170, y = 710)

        #3
shape_rules_3_1 = tk.Label(frame_rules,
                           image = purple_block_image,
                           borderwidth = 0)
shape_rules_3_1.place(x = 200, y = 710)

shape_rules_3_2 = tk.Label(frame_rules,
                           image = purple_block_image,
                           borderwidth = 0)
shape_rules_3_2.place(x = 200, y = 730)

shape_rules_3_3 = tk.Label(frame_rules,
                           image = purple_block_image,
                           borderwidth = 0)
shape_rules_3_3.place(x = 220, y = 710)

shape_rules_3_4 = tk.Label(frame_rules,
                           image = purple_block_image,
                           borderwidth = 0)
shape_rules_3_4.place(x = 240, y = 710)

        #4
shape_rules_4_1 = tk.Label(frame_rules,
                           image = red_block_image,
                           borderwidth = 0)
shape_rules_4_1.place(x = 270, y = 730)

shape_rules_4_2 = tk.Label(frame_rules,
                           image = red_block_image,
                           borderwidth = 0)
shape_rules_4_2.place(x = 290, y = 730)

shape_rules_4_3 = tk.Label(frame_rules,
                           image = red_block_image,
                           borderwidth = 0)
shape_rules_4_3.place(x = 290, y = 710)

shape_rules_4_4 = tk.Label(frame_rules,
                           image = red_block_image,
                           borderwidth = 0)
shape_rules_4_4.place(x = 310, y = 710)

        #5
shape_rules_5_1 = tk.Label(frame_rules,
                           image = yellow_block_image,
                           borderwidth = 0)
shape_rules_5_1.place(x = 340, y = 710)

shape_rules_5_2 = tk.Label(frame_rules,
                           image = yellow_block_image,
                           borderwidth = 0)
shape_rules_5_2.place(x = 360, y = 710)

shape_rules_5_3 = tk.Label(frame_rules,
                           image = yellow_block_image,
                           borderwidth = 0)
shape_rules_5_3.place(x = 380, y = 710)

shape_rules_5_4 = tk.Label(frame_rules,
                           image = yellow_block_image,
                           borderwidth = 0)
shape_rules_5_4.place(x = 400, y = 710)

        #6
shape_rules_6_1 = tk.Label(frame_rules,
                           image = blue_block_image,
                           borderwidth = 0)
shape_rules_6_1.place(x = 430, y = 710)

shape_rules_6_2 = tk.Label(frame_rules,
                           image = blue_block_image,
                           borderwidth = 0)
shape_rules_6_2.place(x = 430, y = 730)

shape_rules_6_3 = tk.Label(frame_rules,
                           image = blue_block_image,
                           borderwidth = 0)
shape_rules_6_3.place(x = 450, y = 710)

shape_rules_6_4 = tk.Label(frame_rules,
                           image = blue_block_image,
                           borderwidth = 0)
shape_rules_6_4.place(x = 450, y = 730)

        #7
shape_rules_7_1 = tk.Label(frame_rules,
                           image = green_block_image,
                           borderwidth = 0)
shape_rules_7_1.place(x = 480, y = 710)

shape_rules_7_2 = tk.Label(frame_rules,
                           image = green_block_image,
                           borderwidth = 0)
shape_rules_7_2.place(x = 500, y = 710)

shape_rules_7_3 = tk.Label(frame_rules,
                           image = green_block_image,
                           borderwidth = 0)
shape_rules_7_3.place(x = 500, y = 730)

shape_rules_7_4 = tk.Label(frame_rules,
                           image = green_block_image,
                           borderwidth = 0)
shape_rules_7_4.place(x = 520, y = 730)

root.mainloop()
