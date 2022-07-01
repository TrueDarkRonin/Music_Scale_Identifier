#!/usr/bin/env python
"""
Scale Finder
By Gabriel Riley
"""
# ----------Imports---------- #
import tkinter as tk
from tkinter import ttk

# TODO
# Implement flat/sharp functionality


class ScaleFinder:
    """
    Identifies a scale given a key and it's relevant mode. Uses two tuples for keys and modes as
    well as a dictionary to expand on the intervals for each given mode. Key select defines the
    starting point in the tuple and mode select defines the intervals. GUI build in tkinter.
    """
    def __init__(self):
        """
        Creates the tuples for keys and modes and the dictionary for mode intervals.
        Defines tkinter window and style as well as populates it with labels, buttons and
        combo-boxes.
        """
        # ----------Variables---------- #
        self.keys = ('C', "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")
        self.keys_sharp = ('C', "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")
        self.keys_flat = ('C', "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B")
        self.modes = ('Ionian', "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locrian")
        self.scale_interval_dict = {"Ionian": "0,2,4,5,7,9,11",
                                    "Dorian": "0,2,3,5,7,9,10",
                                    "Phrygian": "0,1,3,5,7,8,10",
                                    "Lydian": "0,2,4,6,7,9,11",
                                    "Mixolydian": "0,2,4,5,7,9,10",
                                    "Aeolian": "0,2,3,5,7,8,10",
                                    "Locrian": "0,1,3,5,6,8,10"}
        self.scale = []

        # ----------TK Window---------- #
        self.root = tk.Tk()
        self.root.geometry('280x250')
        self.root.title('Scale Finder')
        self.root.iconbitmap("Logo.ico")
        self.root.configure(background='black')

        self.var_text = tk.StringVar()
        self.var_text.set("Select a Key and Mode")

        # ----------TK Style---------- #
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure('TButton', font=('Arial', 15), background='black', foreground='grey')
        self.style.map('TButton', background=[('active', 'red')])
        self.style.configure('TCheckbutton', background='black', foreground='grey')

        # ---------- TKLabels---------- #
        self.scale_finder_label = ttk.Label(text='Scale Finder', font=('Arial', 20),
                                            foreground='grey', background='black')
        self.scale_finder_label.grid(column=0, row=0, columnspan=4)
        self.key_select_label = ttk.Label(text='Key', font=('Arial', 12),
                                          foreground='grey', background='black')
        self.key_select_label.grid(column=0, row=1, columnspan=4)
        self.mode_select_label = ttk.Label(text='Mode', font=('Arial', 12),
                                           foreground='grey', background='black')
        self.mode_select_label.grid(column=0, row=4, columnspan=4)
        self.scale_label = ttk.Label(textvariable=self.var_text, font=('Arial', 12),
                                           foreground='grey', background='black')
        self.scale_label.grid(column=0, row=6, columnspan=4)

        # ----------TK ComboBoxes---------- #
        self.key_select_combo = ttk.Combobox(values=self.keys, state="readonly")
        self.key_select_combo.grid(column=1, row=3, columnspan=2)
        self.key_select_combo.current(0)
        self.mode_select_combo = ttk.Combobox(values=self.modes, state="readonly")
        self.mode_select_combo.grid(column=1, row=5, columnspan=2)
        self.mode_select_combo.current(0)

        # ----------TK Buttons---------- #
        self.exit_button = ttk.Button(text='Get Scale', command=self.get_scale)
        self.exit_button.grid(column=0, row=7, columnspan=2)
        self.exit_button = ttk.Button(text='Exit', command=self.root.quit)
        self.exit_button.grid(column=2, row=7, columnspan=2)

        # ----------TK Checkbox---------- #
        self.checkbox = ttk.Checkbutton(text="Use Flats", command=self.flat_sharp)
        self.checkbox.grid(column=0, row=2, columnspan=4)

        # ----------TK Table Weight---------- #
        for col_var in range(4):
            self.root.columnconfigure(col_var, weight=1)
        for row_var in range(8):
            self.root.rowconfigure(row_var, weight=1)

    def get_scale(self):
        """
        Gets selected key and mode from combo-boxes. Uses key to set starting point and mode to
        define intervals which are compare to tuple of keys to create list of new notes to
        append to list scale.
        """
        # ----------ComboBox Variables---------- #
        key = self.key_select_combo.get()
        mode = self.mode_select_combo.get()

        # ----------Intervals and Key---------- #
        key_position = self.keys.index(key)
        intervals = self.scale_interval_dict[mode]
        interval_list = list(map(int, intervals.split(",")))

        # ----------Scale List---------- #
        for i, _ in enumerate(interval_list):
            repo_index = interval_list[i] + key_position
            if repo_index >= 12:
                repo_index -= 12
            self.scale.append(self.keys[repo_index])
            i += 1
        self.var_text.set(' '.join(self.scale))

        # ----------Reset List---------- #
        self.scale = []

    def flat_sharp(self):
        """
        Flips key between flat and sharp
        """
        if self.keys == self.keys_sharp:
            self.keys = self.keys_flat
        elif self.keys == self.keys_flat:
            self.keys = self.keys_sharp


# ----------Instantiate Scale Finder---------- #
if __name__ == "__main__":
    app = ScaleFinder()
    app.root.mainloop()
