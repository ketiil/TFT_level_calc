import tkinter as tk
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, N, Checkbutton, Radiobutton, Frame, SUNKEN, LabelFrame, \
    GROOVE, RIDGE, DISABLED, S
from tkinter.ttk import Style


def hide_items(name):
    name.grid_remove()


def show_items(name):
    name.grid()


class Gui:

    def __init__(self, master):
        self.master = master
        master.title("TFT Level Calculator")
        master["bg"] = "#565656"

        # self.frame = Frame(master, width=540, height=320)

        self.BASE_INC = 5
        self.PVP_WIN = 1
        self.AVG_PIRATE_INC = 1.75

        self.entered_xp = 0
        self.remaining_xp = 0
        self.cur_lvl = 0
        self.cost_to_lvl = 0
        self.cur_gold = 0
        self.cur_winstreak_gold = 0
        self.gold_per_round = 0
        self.rounds_to_lvl = 0
        self.streak_value = 0
        self.streak_counter = 1
        self.win_s = IntVar()
        self.loss_s = IntVar()
        self.win_s.set(0)
        self.loss_s.set(0)

        self.is_win_streak = True  # Loss streak if false

        self.level_xp = [2, 2, 6, 12, 20, 32, 50, 70]

        # Text box (right top) #
        self.text_box = LabelFrame(master, relief=SUNKEN, borderwidth=2)
        # self.text_box["bg"] = "#565656"
        self.text_box.grid(row=0,
                           column=1,
                           rowspan=5,
                           columnspan=6,
                           sticky=W + E + N,
                           pady=(5, 5),
                           padx=(5, 5))

        # Level box (left top-bottom) #
        self.level_box = LabelFrame(master, relief=SUNKEN, borderwidth=2)
        self.level_box["bg"] = "#565656"
        self.level_box.grid(row=0, rowspan=8, column=0, pady=(5, 5), padx=(5, 5))

        # Winstreak box #
        self.ws_box = LabelFrame(master, relief=SUNKEN, borderwidth=2)
        self.ws_box.grid(row=5, column=1, columnspan=2, pady=(5, 5), padx=(5, 5), sticky=W+E)

        # Text fields #
        self.cur_lvl_label = Label(self.text_box,       text="Current lvl:")
        self.remaining_xp_label = Label(self.text_box,  text="Remaining xp:")
        self.cur_xp_label = Label(self.text_box,        text="Current xp:")
        self.cost_label = Label(self.text_box,          text="Cost to level:")
        self.rounds_to_lvl_label = Label(self.text_box, text="Approx. rounds to level:")

        self.cur_lvl_value_text = IntVar()
        self.cur_lvl_value_text.set(self.cur_lvl)
        self.cur_lvl_value = Label(self.text_box, textvariable=self.cur_lvl_value_text)

        self.remaining_xp_value_text = IntVar()
        self.remaining_xp_value_text.set(self.remaining_xp)
        self.remaining_xp_value = Label(self.text_box, textvariable=self.remaining_xp_value_text)

        self.cur_xp_value_text = IntVar()
        self.cur_xp_value_text.set(self.entered_xp)
        self.cur_xp_value = Label(self.text_box, textvariable=self.cur_xp_value_text)

        self.cost_value_text = IntVar()
        self.cost_value_text.set(self.cost_to_lvl)
        self.cost_value = Label(self.text_box, textvariable=self.cost_value_text)

        self.rounds_to_lvl_text = IntVar()
        self.rounds_to_lvl_text.set(self.rounds_to_lvl)
        self.rounds_value = Label(self.text_box, textvariable=self.rounds_to_lvl_text)

        vcmd = master.register(self.validate)  # we have to wrap the command
        self.cur_xp = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        # Level buttons
        level1_btn = Button(self.level_box, text="Level 1", command=lambda: self.reg_level(1))
        level2_btn = Button(self.level_box, text="Level 2", command=lambda: self.reg_level(2))
        level3_btn = Button(self.level_box, text="Level 3", command=lambda: self.reg_level(3))
        level4_btn = Button(self.level_box, text="Level 4", command=lambda: self.reg_level(4))
        level5_btn = Button(self.level_box, text="Level 5", command=lambda: self.reg_level(5))
        level6_btn = Button(self.level_box, text="Level 6", command=lambda: self.reg_level(6))
        level7_btn = Button(self.level_box, text="Level 7", command=lambda: self.reg_level(7))
        level8_btn = Button(self.level_box, text="Level 8", command=lambda: self.reg_level(8))
        # level9_btn = Button(master, text="Level 9", command=lambda: self.reg_level(9))

        level1_btn.grid(row=0, column=0, padx=5, pady=(5, 0))
        level2_btn.grid(row=1, column=0)
        level3_btn.grid(row=2, column=0)
        level4_btn.grid(row=3, column=0)
        level5_btn.grid(row=4, column=0)
        level6_btn.grid(row=5, column=0)
        level7_btn.grid(row=6, column=0)
        level8_btn.grid(row=7, column=0, pady=(0, 5))
        # level9_btn.grid(row=8, column=0)

        # XP Button
        self.xp_btn = Button(master, text="Enter xp", command=lambda: self.reg_xp(self.entered_xp))

        # Radiobuttons (winstreaks)
        style = Style(self.ws_box)
        style.configure("TRadiobutton", )
        self.ws1_btn = Radiobutton(self.ws_box, value=1, command=lambda: self.win_streak_gold(0))
        self.ws1_btn.select()  # start position
        self.ws2_btn = Radiobutton(self.ws_box, value=2, command=lambda: self.win_streak_gold(0))
        self.ws3_btn = Radiobutton(self.ws_box, value=3, command=lambda: self.win_streak_gold(1))  # 1 extra gold/round
        self.ws5_btn = Radiobutton(self.ws_box, value=4, command=lambda: self.win_streak_gold(2))  # 2 extra gold/round
        self.ws7_btn = Radiobutton(self.ws_box, value=5, command=lambda: self.win_streak_gold(3))  # 3 extra gold/round

        self.ws1_btn.grid(row=1, column=0, sticky=W)
        self.ws2_btn.grid(row=1, column=1, sticky=W)
        self.ws3_btn.grid(row=1, column=2, sticky=W)
        self.ws5_btn.grid(row=1, column=3, sticky=W)
        self.ws7_btn.grid(row=1, column=4, sticky=W)

        self.ws1_label = Label(self.ws_box, text="1")
        self.ws2_label = Label(self.ws_box, text="2")
        self.ws3_label = Label(self.ws_box, text="3")
        self.ws5_label = Label(self.ws_box, text="5")
        self.ws7_label = Label(self.ws_box, text="7+")

        self.ws1_label.grid(row=2, column=0, sticky=W + N + E)
        self.ws2_label.grid(row=2, column=1, sticky=W + N + E)
        self.ws3_label.grid(row=2, column=2, sticky=W + N + E)
        self.ws5_label.grid(row=2, column=3, sticky=W + N + E)
        self.ws7_label.grid(row=2, column=4, sticky=W + N + E)

        # Win streak option buttons
        self.next_btn = Button(master, text="Next round",
                               command=lambda: self.streak_incrementer(self.cur_winstreak_gold))
        self.next_btn.grid(row=6, column=1, sticky=W+N, padx=(5, 5))
        self.reset_btn = Button(master, text="Reset", command=lambda: self.reset_streak_counter(False))
        self.reset_btn.grid(row=6, column=2, sticky=W+N, padx=(5, 5))

        # Checkbuttons
        self.win_streak_btn = Checkbutton(master,
                                          bg="#565656",
                                          bd=0,
                                          text="Win streak",
                                          fg="#FFFFFF",
                                          onvalue=1,
                                          offvalue=0,
                                          variable=self.win_s,
                                          command=lambda: self.win_toggle())
        self.win_streak_btn["bd"] = 0
        self.loss_streak_btn = Checkbutton(master,
                                           text="Loss streak",
                                           bg="#565656",
                                           bd=0,
                                           onvalue=1,
                                           offvalue=0,
                                           variable=self.loss_s,
                                           command=lambda: self.loss_toggle())
        self.pirates = Checkbutton(master, text="Pirates")

        # LAYOUT #

        # Row 0
        self.cur_lvl_label.grid(row=0, column=1, sticky=W, padx=(5, 0), pady=(5, 0))
        self.cur_lvl_value.grid(row=0, column=6, columnspan=2, sticky=E, pady=(5, 0))
        # hide_items(self.cur_lvl_label)
        hide_items(self.cur_xp_value)
        # hide_items(self.cur_lvl_label)
        hide_items(self.cur_lvl_value)
        # Row 1
        self.remaining_xp_label.grid(row=1, column=1, sticky=W, padx=(5, 0))
        self.remaining_xp_value.grid(row=1, column=6, columnspan=2, sticky=E)
        # hide_items(self.remaining_xp_label)
        hide_items(self.remaining_xp_value)
        # Row 2
        self.cur_xp_label.grid(row=2, column=1, sticky=W, padx=(5, 0))
        self.cur_xp_value.grid(row=2, column=6, columnspan=2, sticky=E)
        # hide_items(self.cur_xp_label)
        hide_items(self.cur_xp_value)
        # Row 3
        self.cost_label.grid(row=3, column=1, sticky=W, padx=(5, 0))
        self.cost_value.grid(row=3, column=6, columnspan=2, sticky=E)
        # hide_items(self.cost_label)
        hide_items(self.cost_value)
        # Row 4
        self.rounds_to_lvl_label.grid(row=4, column=1, sticky=W, padx=(5, 0), pady=(0, 5))
        self.rounds_value.grid(row=4, column=6, columnspan=2, sticky=E, pady=(0, 5))
        # Row 5
        self.cur_xp.grid(row=7, column=1, columnspan=2, sticky=W + E, padx=5, pady=(0, 5))
        self.xp_btn.grid(row=7, column=3, sticky=W, padx=(0, 5))

        # Checkbox alternatives
        self.win_streak_btn.grid(row=5, column=3, sticky=N+W, padx=(5, 5), pady=(5, 0))
        self.loss_streak_btn.grid(row=5, column=3, sticky=S+W, padx=(5, 5), pady=(0, 5))
        self.pirates.grid(row=6, column=3, sticky=W, padx=(0, 5))
        #hide_items(self.win_streak_btn)
        #hide_items(self.loss_streak_btn)
        hide_items(self.pirates)

        # Next round button


        # Close
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=9, column=3, pady=(0, 5))

    def validate(self, new_text):
        if not new_text:  # the field is being cleared
            self.entered_xp = 0
            return True

        try:
            self.entered_xp = int(new_text)
            return True
        except ValueError:
            return False

    def reg_level(self, level):
        self.cur_lvl = int(level)
        self.cur_lvl_value_text.set(self.cur_lvl)

        show_items(self.cur_lvl_label)
        show_items(self.cur_lvl_value)

        self.remaining_xp = self.level_xp[self.cur_lvl - 1]
        self.remaining_xp_value_text.set(self.remaining_xp)

        show_items(self.remaining_xp_label)
        show_items(self.remaining_xp_value)

    def reg_xp(self, xp):
        self.entered_xp = int(xp)
        self.cur_xp_value_text.set(self.entered_xp)
        self.calc_diff()
        self.cur_xp.delete(0, END)  # reset textbox

    def calc_diff(self):
        xp_needed = self.level_xp[self.cur_lvl - 1]
        self.remaining_xp = (xp_needed - self.entered_xp)
        if self.remaining_xp >= 0:
            self.remaining_xp_value_text.set(self.remaining_xp)
        elif self.remaining_xp < 0:
            self.remaining_xp_value_text.set(0)
        self.calc_cost()

    def calc_cost(self):
        if self.remaining_xp % 4 == 0:
            self.cost_to_lvl = self.remaining_xp / 4
            self.cost_value_text.set(int(self.cost_to_lvl) * 4)
        elif self.remaining_xp % 4 <= 4:
            remainder = self.remaining_xp % 4
            if remainder < 4:
                self.cost_to_lvl = 1 + self.remaining_xp // 4
                if self.cost_to_lvl < 0:
                    self.cost_value_text.set(0)
                self.cost_value_text.set(int(self.cost_to_lvl) * 4)

        show_items(self.cur_xp_label)
        show_items(self.cur_xp_value)
        show_items(self.cost_label)
        show_items(self.cost_value)

    def calc_gold_pr_round(self):
        if self.pirates:
            self.gold_per_round += self.AVG_PIRATE_INC
        if self.win_streak_btn:
            self.gold_per_round += self.cur_winstreak_gold + self.PVP_WIN
        if self.loss_streak_btn:
            self.gold_per_round += self.cur_winstreak_gold
        self.gold_per_round += self.BASE_INC
        print(self.gold_per_round)

    def win_streak_gold(self, value):
        self.cur_winstreak_gold = value

    def loss_toggle(self):
        if self.win_s.get() == 1:
            self.win_streak_btn.deselect()
            self.loss_streak_btn.select()
            self.reset_streak_counter(True)
            self.is_win_streak = False

    def win_toggle(self):
        if self.loss_s.get() == 1:
            self.loss_streak_btn.deselect()
            self.win_streak_btn.select()
            self.reset_streak_counter(True)
            self.is_win_streak = True

    def streak_incrementer(self, value):
        self.streak_value = value
        self.streak_counter += 1
        if self.streak_counter == 2:
            self.ws2_btn.select()
        elif self.streak_counter == 3:
            self.ws3_btn.select()
        elif self.streak_counter == 5:
            self.ws5_btn.select()
        elif self.streak_counter >= 7:
            self.ws7_btn.select()

    def reset_streak_counter(self, btn_click):
        self.streak_value = 0
        self.streak_counter = 1
        self.ws1_btn.select()
        if not btn_click:
            if self.win_s.get() == 1:
                self.win_streak_btn.deselect()
                self.loss_streak_btn.select()
            else:
                self.loss_streak_btn.deselect()
                self.win_streak_btn.select()



def main():
    root = tk.Tk()
    gui = Gui(root)
    root.mainloop()


main()
