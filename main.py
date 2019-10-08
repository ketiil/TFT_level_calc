
import tkinter as tk
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, N, Checkbutton, Frame, SUNKEN, LabelFrame


def hide_items(name):
    name.grid_remove()


def show_items(name):
    name.grid()


class Gui:

    def __init__(self, master):
        self.master = master
        master.title("TFT Level Calculator")
        master.bg = "Blue"

        self.total = 0
        self.entered_xp = 0
        self.remaining_xp = 0
        self.cur_lvl = 0
        self.cost = 0
        self.cur_gold = 0
        self.BASE_INC = 5
        self.PVP_WIN = 1
        self.AVG_PIRATE_INC = 1.75

        self.level_xp = [2, 2, 6, 12, 20, 32, 50, 70]

        # Text box (right top) #
        self.text_box = LabelFrame(master, relief=SUNKEN, borderwidth=2)
        self.text_box.grid(row=0,
                           column=1,
                           rowspan=5,
                           columnspan=4,
                           sticky=W+E+N,
                           pady=(5, 0),
                           padx=5)

        # Level box (left top-bottom) #
        self.level_box = LabelFrame(master, relief=SUNKEN, borderwidth=2)
        self.level_box.grid(row=0, rowspan=8, column=0)

        # Text fields #
        self.cur_lvl_label = Label(self.text_box, text="Current lvl:")
        self.remaining_xp_lbl = Label(self.text_box, text="Remaining xp:")
        self.cur_xp_lbl = Label(self.text_box, text="Current xp:")
        self.cost_lbl = Label(self.text_box, text="Cost to level:")

        self.cur_lvl_value_text = IntVar()
        self.cur_lvl_value_text.set(self.cur_lvl)
        self.cur_lvl_value = Label(self.text_box, textvariable=self.cur_lvl_value_text)

        self.remaining_xp_label_text = IntVar()
        self.remaining_xp_label_text.set(self.remaining_xp)
        self.remaining_xp_label = Label(self.text_box, textvariable=self.remaining_xp_label_text)

        self.cur_xp_label_text = IntVar()
        self.cur_xp_label_text.set(self.entered_xp)
        self.cur_xp_label = Label(self.text_box, textvariable=self.cur_xp_label_text)

        self.cost_label_text = IntVar()
        self.cost_label_text.set(self.cost)
        self.cost_label = Label(self.text_box, textvariable=self.cost_label_text)

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
        #level9_btn = Button(master, text="Level 9", command=lambda: self.reg_level(9))

        level1_btn.grid(row=0, column=0, pady=(5, 0))
        level2_btn.grid(row=1, column=0)
        level3_btn.grid(row=2, column=0)
        level4_btn.grid(row=3, column=0)
        level5_btn.grid(row=4, column=0)
        level6_btn.grid(row=5, column=0)
        level7_btn.grid(row=6, column=0)
        level8_btn.grid(row=7, column=0, pady=(0, 5))
        #level9_btn.grid(row=8, column=0)

        # XP Button
        self.xp_btn = Button(master, text="Enter xp", command=lambda: self.reg_xp(self.entered_xp))

        # Checkbuttons
        self.win_streak = Checkbutton(master, text="Win streak")
        self.pirates = Checkbutton(master, text="Pirates")

        ### LAYOUT ###


        # Row 0
        self.cur_lvl_label.grid(row=0, column=1, sticky=W, pady=(5, 0))
        self.cur_lvl_value.grid(row=0, column=2, columnspan=2, sticky=E)
        hide_items(self.cur_lvl_label)
        hide_items(self.cur_xp_label)
        self.cur_lvl_label.grid_remove()
        self.cur_lvl_value.grid_remove()
        # Row 1
        self.remaining_xp_lbl.grid(row=1, column=1, sticky=W)
        self.remaining_xp_label.grid(row=1, column=2, columnspan=2, sticky=E)
        self.remaining_xp_lbl.grid_remove()
        self.remaining_xp_label.grid_remove()
        # Row 2
        self.cur_xp_lbl.grid(row=2, column=1, sticky=W)
        self.cur_xp_label.grid(row=2, column=2, columnspan=2, sticky=E)
        self.cur_xp_lbl.grid_remove()
        self.cur_xp_label.grid_remove()
        # Row 3
        self.cost_lbl.grid(row=3, column=1, sticky=W)
        self.cost_label.grid(row=3, column=2, columnspan=2, sticky=E, pady=(0, 5))
        self.cost_lbl.grid_remove()
        self.cost_label.grid_remove()
        # Row 5
        self.cur_xp.grid(row=5, column=1, columnspan=2, sticky=W + E, padx=5)
        self.xp_btn.grid(row=5, column=3)

        self.win_streak.grid(row=6, column=1, sticky=W)
        self.pirates.grid(row=7, column=1, sticky=W)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=9, column=3)

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

        self.remaining_xp = self.level_xp[self.cur_lvl-1]
        self.remaining_xp_label_text.set(self.remaining_xp)

        show_items(self.remaining_xp_lbl)
        show_items(self.remaining_xp_label)

    def reg_xp(self, xp):
        self.entered_xp = int(xp)
        self.cur_xp_label_text.set(self.entered_xp)
        self.calc_diff()
        self.cur_xp.delete(0, END)  # reset textbox

    def calc_diff(self):
        xp_needed = self.level_xp[self.cur_lvl-1]
        self.remaining_xp = (xp_needed - self.entered_xp)
        if self.remaining_xp >= 0:
            self.remaining_xp_label_text.set(self.remaining_xp)
        else:
            self.remaining_xp_label_text.set(0)
        self.calc_cost()

    def calc_cost(self):
        if self.remaining_xp%4 == 0:
            self.cost = self.remaining_xp/4
            self.cost_label_text.set(self.cost*4)
        elif self.remaining_xp%4 <= 4:
            remainder = self.remaining_xp % 4
            if remainder < 4:
                self.cost = 1 + self.remaining_xp//4
                self.cost_label_text.set(self.cost*4)

        show_items(self.cur_xp_lbl)
        show_items(self.cur_xp_label)
        show_items(self.cost_lbl)
        show_items(self.cost_label)



def main():
    root = tk.Tk()
    gui = Gui(root)
    root.mainloop()


main()
