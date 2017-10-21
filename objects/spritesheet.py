from PIL import Image


class SpriteSheet:
    """
    Sprite Sheet Class

    Note: PNG are the only File type Supported. If Implementing other file types...
          ... look at: Image.new("RGBA", (max_width, max_height)) in create_sprite_sheet()
    """

    def __init__(self):
        self.spritesheet = None
        self.sprites = []
        self.file_name = None
        self.max_row = 0
        self.max_col = 0

        """
        Determines if the Sprite Sheet uses a constant Width and Height for all Rows and Columns
        TODO: Implement the feature listed
        """
        self.constant_cell_width = 0
        self.constant_cell_height = 0

        """
        spritesheet_width & spritesheet_height are used to find the Max Width & Height.
        note: the row or column with the highest count may not have the max size
        ex:
        - 5 small sprites with width 1 in row 0: Total Width = 5
        - 3 large sprites with width 10 in row 1: Total Width = 30
        """
        self.spritesheet_row_widths = []
        self.spritesheet_col_heights = []

    def add_image(self, image_location, row, col):
        """
        Add Image to Sprite Sheet
        :param image_location:
        :param row: Row Number in Sprite Sheet
        :param col: Column Number in Sprite Sheet
        """
        if type(row) is not int:
            row = int(row)
        if type(col) is not int:
            col = int(col)

        # Extend the size of row_widths and col_height array,
        # if they are not long enough for the row/col param
        while len(self.spritesheet_row_widths) <= row:
            self.spritesheet_row_widths.append([])
        while len(self.spritesheet_col_heights) <= col:
            self.spritesheet_col_heights.append([])

        image = Image.open(image_location)

        # Increment the width and height of a row/col with the size of the image
        width, height = image.size
        self.spritesheet_row_widths[row].append(width)
        self.spritesheet_col_heights[col].append(height)

        self.sprites.append({
            "image": image,
            "row_number": row,
            "column_number": col
        })

    def create_spritesheet(self):
        """Create Sprite Sheet"""

        max_width = max([sum(row_in) for row_in in self.spritesheet_row_widths])
        max_height = max([sum(row_in) for row_in in self.spritesheet_col_heights])
        self.spritesheet = Image.new("RGBA", (max_width, max_height))  # RGBA is for PNG, Will not allow saving of GIF

        for sprite_info in self.sprites:
            image = sprite_info["image"]
            row_number = sprite_info["row_number"]
            column_number = sprite_info["column_number"]

            width, height = image.size

            left = self.sum_prev_cols_heights(row_number, column_number)
            upper = self.sum_prev_rows_widths(row_number, column_number)
            right = left + width
            lower = upper + height

            box = (left, upper, right, lower)
            self.spritesheet.paste(image, box)

    def save(self):
        """
        Saves the Spritesheet to self.file_name.
        """
        file_parts = self.file_name.split(".")
        file_extension = file_parts[len(file_parts)-1]
        if file_extension.lower() == "png":
            self.spritesheet.save(self.file_name, file_extension)
        else:
            print("File Extension", file_extension, "Not Supported")

    def set_save_file(self, file_name):
        """Set File Name for Sprite Sheet"""
        self.file_name = file_name

    def set_constant_cell_height(self, constant_cell_height):
        """Set whether the Sprite Sheet will have a Constant Height"""
        self.constant_cell_height = constant_cell_height

    def set_constant_cell_width(self, constant_cell_width):
        """Set whether the Sprite Sheet will have a Constant Width"""
        self.constant_cell_width = constant_cell_width

    def sum_prev_rows_widths(self, row_number, column_number):
        """Sum the Previous Row Widths in a Col"""
        row_number = row_number - 1
        sum_prev_row = 0
        while row_number >= 0:
            sum_prev_row = sum_prev_row + self.spritesheet_col_heights[column_number][row_number]
            row_number = row_number - 1
        return sum_prev_row

    def sum_prev_cols_heights(self, row_number, column_number):
        """Sum the Previous Column Heights in a Row"""
        column_number = column_number - 1
        sum_prev_col = 0
        while column_number >= 0:
            sum_prev_col = sum_prev_col + self.spritesheet_row_widths[row_number][column_number]
            column_number = column_number - 1
        return sum_prev_col

