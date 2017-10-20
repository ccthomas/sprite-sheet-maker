from PIL import Image


class SpriteSheet:
    def __init__(self):
        self.spritesheet = None
        self.sprites = []
        self.file_name = None
        self.max_row = 0
        self.max_col = 0

        """
        Determines if the Sprite Sheet uses a constant Width and Height for all Rows and Columns
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
        self.spritesheet_width = []
        self.spritesheet_height = []

    def set_save_file(self, file_name):
        """Set File Name for Sprite Sheet"""
        self.file_name = file_name

    def set_constant_cell_width(self, constant_cell_width):
        """Set whether the Sprite Sheet will have a Constant Width"""
        self.constant_cell_width = constant_cell_width

    def set_constant_cell_height(self, constant_cell_height):
        """Set whether the Sprite Sheet will have a Constant Height"""
        self.constant_cell_height = constant_cell_height

    def add_image(self, image_location, row, col):
        """Add Image to Sprite Sheet"""
        if type(row) is not int:
            row = int(row)
        if type(col) is not int:
            col = int(col)

        while len(self.spritesheet_width) <= col:
            self.spritesheet_width.append(0)

        while len(self.spritesheet_height) <= row:
            self.spritesheet_height.append(0)

        image = Image.open(image_location)
        width, height = image.size
        self.spritesheet_width[col] = self.spritesheet_width[col] + width
        self.spritesheet_height[row] = self.spritesheet_height[row] + height

        self.sprites.append({
            "image": image,
            "row_number": row,
            "column_number": col
        })

    def create_spritesheet(self):
        """Create Sprite Sheet"""

        max_width = max(self.spritesheet_width)
        max_height = max(self.spritesheet_height)
        self.spritesheet = Image.new("RGB", (max_width, max_height))

        for sprite_info in self.sprites:
            image = sprite_info["image"]
            row_number = sprite_info["row_number"]
            column_number = sprite_info["column_number"]

            left = int(column_number * self.spritesheet_width[column_number])
            upper = int(row_number * self.spritesheet_height[row_number])
            right = (column_number + 1) * self.spritesheet_width[column_number]
            lower = (row_number + 1) * self.spritesheet_height[row_number]
            self.spritesheet.paste(image, (left, upper, right, lower))

    def save_sprite_sheet(self):
        self.spritesheet.save(self.file_name)

