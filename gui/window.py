from objects.spritesheet import SpriteSheet
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Button, Checkbutton, Entry, IntVar, Label, W
import tkinter as tk


class Window:
    """
    GUI Window
    """

    def __init__(self):
        """Initialize Sprite Sheet Maker Window"""
        self.master = tk.Tk()
        self.master.title('Sprite Sheet Maker')
        self.master.geometry("280x280")
        self.master.resizable(width=True, height=True)

        self.current_dir = "/"
        self.constant_cell_width = IntVar()  # Not Implemented
        self.constant_cell_height = IntVar()  # Not Implemented
        self.row_entry = {}
        self.col_entry = {}
        self.img_entry = {}

        # Header Labels
        self.label_row = None
        self.label_col = None
        self.label_img = None

        # Footer Buttons
        self.footer_buttons_row_offset = 0
        self.button_add_image = None
        self.button_duplicate_image = None
        self.checkbutton_constant_cell_width = None  # Not Implemented
        self.checkbutton_constant_cell_height = None  # Not Implemented
        self.button_create = None
        self.button_reset = None

        # Add First Row
        self.button_add_image = Button(self.master, command=self.button_add_image_pressed, text="Add Image")
        self.button_add_image.grid(row=self.footer_buttons_row_offset, column=0, columnspan=2, sticky=W)

    def add_row(self, image_location):
        """Add New Row"""
        if len(self.row_entry) == 0:
            # Add Header
            self.label_row = Label(self.master, text="row")
            self.label_col = Label(self.master, text="column")
            self.label_img = Label(self.master, text="Image Location")

            self.label_row.grid(row=0, column=0)
            self.label_col.grid(row=0, column=1)
            self.label_img.grid(row=0, column=2, columnspan=2, sticky=W)

            # Add Duplicate Button
            self.button_duplicate_image = Button(self.master, command=self.button_duplicate_image_pressed,
                                                 text="Duplicate Previous")

            # Add Checkbutton Constants
            self.checkbutton_constant_cell_width = Checkbutton(self.master, text="Constant Cell Width",
                                                               variable=self.constant_cell_width, onvalue=1,
                                                               offvalue=0, width=20)
            self.checkbutton_constant_cell_height = Checkbutton(self.master, text="Constant Cell Width",
                                                                variable=self.constant_cell_height, onvalue=1,
                                                                offvalue=0, width=20)

            # Add Create & Reset Buttons
            self.button_create = Button(self.master, command=self.button_create_pressed, text="Create")
            self.button_reset = Button(self.master, command=self.button_reset_pressed, text="Reset")

            self.update_footer_buttons()

        self.update_footer_buttons()

        e = Entry(self.master, width=2)
        e.insert(0, 0)
        e.grid(row=len(self.row_entry) + 1, column=0)
        self.row_entry[repr(len(self.row_entry))] = e

        e = Entry(self.master, width=2)
        e.insert(0, 0)
        e.grid(row=len(self.col_entry) + 1, column=1)
        self.col_entry[repr(len(self.col_entry))] = e

        e = Entry(self.master, width=len(image_location))
        e.insert(0, image_location)
        e.grid(row=len(self.img_entry) + 1, column=2, columnspan=3)
        self.img_entry[repr(len(self.img_entry))] = e

    def button_add_image_pressed(self):
        """Get Image File Location"""
        image_location = askopenfilename(initialdir=self.current_dir, title="Select Image")

        if image_location != "":
            self.current_dir = "/"
            dir_list = image_location.split("/")
            for i in range(len(dir_list)):
                if i != range(len(dir_list)):
                    self.current_dir = dir_list[i] + "/"

            self.add_row(image_location)

    def button_create_pressed(self):
        """Create Sprite Sheet"""
        file_name = asksaveasfilename()

        spritesheet = SpriteSheet()
        spritesheet.set_save_file(file_name)
        spritesheet.set_constant_cell_width(self.constant_cell_width)
        spritesheet.set_constant_cell_height(self.constant_cell_height)

        len_of_entry = len(self.row_entry)
        for entry_num in range(len_of_entry):
            row = self.row_entry[repr(entry_num)].get()
            col = self.col_entry[repr(entry_num)].get()
            img = self.img_entry[repr(entry_num)].get()

            spritesheet.add_image(img, row, col)

        spritesheet.create_spritesheet()
        spritesheet.save()

    def button_duplicate_image_pressed(self):
        """Duplicate Previous Image"""
        image_location = self.img_entry[repr(len(self.img_entry)-1)].get()
        self.add_row(image_location)

    def button_reset_pressed(self):
        # Erase GUI Objects
        self.label_row.grid_forget()
        self.label_col.grid_forget()
        self.label_img.grid_forget()

        self.button_add_image.grid_forget()
        self.button_duplicate_image.grid_forget()
        self.checkbutton_constant_cell_width.grid_forget()
        self.checkbutton_constant_cell_height.grid_forget()
        self.button_create.grid_forget()
        self.button_reset.grid_forget()

        len_of_entry = len(self.row_entry)
        for entry_num in range(len_of_entry):
            self.row_entry[repr(entry_num)].grid_forget()
            self.col_entry[repr(entry_num)].grid_forget()
            self.img_entry[repr(entry_num)].grid_forget()

        # Global Vars
        self.current_dir = "/"
        self.constant_cell_width = IntVar()  # Not Implemented
        self.constant_cell_height = IntVar()  # Not Implemented
        self.row_entry = {}
        self.col_entry = {}
        self.img_entry = {}

        # Footer Buttons
        self.footer_buttons_row_offset = 0
        self.button_add_image = None
        self.button_duplicate_image = None
        self.checkbutton_constant_cell_width = None  # Not Implemented
        self.checkbutton_constant_cell_height = None  # Not Implemented
        self.button_create = None
        self.button_reset = None

        # Add First Row
        self.button_add_image = Button(self.master, command=self.button_add_image_pressed, text="Add Image")
        self.button_add_image.grid(row=self.footer_buttons_row_offset, column=0, columnspan=2, sticky=W)

    def mainloop(self):
        """main loop for tkinter window"""
        self.master.mainloop()

    def update_footer_buttons(self):
        """Update Footer Buttons Grid Location"""
        self.footer_buttons_row_offset = self.footer_buttons_row_offset + 1

        self.button_add_image.grid(row=self.footer_buttons_row_offset, column=0, columnspan=2, sticky=W)
        self.button_duplicate_image.grid(row=self.footer_buttons_row_offset, column=2, columnspan=2, sticky=W)
        self.checkbutton_constant_cell_width.grid(row=self.footer_buttons_row_offset + 1, column=0, columnspan=3,
                                                  sticky=W)
        self.checkbutton_constant_cell_height.grid(row=self.footer_buttons_row_offset + 2, column=0, columnspan=3,
                                                   sticky=W)
        self.button_create.grid(row=self.footer_buttons_row_offset + 3, column=0, columnspan=2, sticky=W)
        self.button_reset.grid(row=self.footer_buttons_row_offset + 3, column=2, columnspan=2, sticky=W)
