def sprite_sheet_test_case_1():
    """Tests Sprite Sheet with focus on Rows"""

    from objects.spritesheet import SpriteSheet
    spritesheet = SpriteSheet()

    # Set File
    spritesheet.set_save_file("/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_outputs/"
                              "/test_case_1_output.png")

    # Row 1: 32x32 Sprites
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32/red_32x32.png"
    spritesheet.add_image(img, 0, 0)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32" \
          "/orange_32x32.png"
    spritesheet.add_image(img, 0, 1)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32" \
          "/yellow_32x32.png"
    spritesheet.add_image(img, 0, 2)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32/green_32x32" \
          ".png"
    spritesheet.add_image(img, 0, 3)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32/blue_32x32" \
          ".png"
    spritesheet.add_image(img, 0, 4)
    # Row 2: 64x32 Sprites
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/64x32/pink_64x32" \
          ".png"
    spritesheet.add_image(img, 1, 0)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/64x32" \
          "/purple_64x32.png"
    spritesheet.add_image(img, 1, 1)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/64x32/teal_64x32" \
          ".png"
    spritesheet.add_image(img, 1, 2)
    # Row 3: 29x36 Sprites
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/29x36" \
          "/orange_29x36.png"
    spritesheet.add_image(img, 2, 0)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/29x36/green_29x36" \
          ".png"
    spritesheet.add_image(img, 2, 1)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/29x36/blue_29x36" \
          ".png"
    spritesheet.add_image(img, 2, 2)

    spritesheet.create_spritesheet()
    spritesheet.save()


def sprite_sheet_test_case_2():
    """Tests Sprite Sheet with focus on Columns"""
    from objects.spritesheet import SpriteSheet
    spritesheet = SpriteSheet()

    # Set File
    spritesheet.set_save_file("/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_outputs/"
                              "/test_case_2_output.png")

    # Col 1: 32x32 Sprites
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32/red_32x32.png"
    spritesheet.add_image(img, 0, 0)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32" \
          "/orange_32x32.png"
    spritesheet.add_image(img, 1, 0)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32" \
          "/yellow_32x32.png"
    spritesheet.add_image(img, 2, 0)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32/green_32x32" \
          ".png"
    spritesheet.add_image(img, 3, 0)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32/blue_32x32" \
          ".png"
    spritesheet.add_image(img, 4, 0)
    # Col 2: 64x32 Sprites
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/64x32/pink_64x32" \
          ".png"
    spritesheet.add_image(img, 0, 1)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/64x32" \
          "/purple_64x32.png"
    spritesheet.add_image(img, 1, 1)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/64x32/teal_64x32" \
          ".png"
    spritesheet.add_image(img, 2, 1)
    # Col 3: 29x36 Sprites
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/29x36" \
          "/orange_29x36.png"
    spritesheet.add_image(img, 0, 2)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/29x36/green_29x36" \
          ".png"
    spritesheet.add_image(img, 1, 2)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/29x36/blue_29x36" \
          ".png"
    spritesheet.add_image(img, 2, 2)

    spritesheet.create_spritesheet()
    spritesheet.save()


def sprite_sheet_test_case_3():
    """
    Tests Sprite Sheet with focus on Rows, where the Last Row has the most amount of Sprites

    The Goal here is to test sum_prev_rows_widths() function
    """

    from objects.spritesheet import SpriteSheet
    spritesheet = SpriteSheet()

    # Set File
    spritesheet.set_save_file("/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_outputs/"
                              "/test_case_1_output.png")

    # Row 1: 32x32 Sprites
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32/red_32x32.png"
    spritesheet.add_image(img, 2, 0)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32" \
          "/orange_32x32.png"
    spritesheet.add_image(img, 2, 1)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32" \
          "/yellow_32x32.png"
    spritesheet.add_image(img, 2, 2)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32/green_32x32" \
          ".png"
    spritesheet.add_image(img, 2, 3)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32/blue_32x32" \
          ".png"
    spritesheet.add_image(img, 2, 4)
    # Row 2: 64x32 Sprites
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/64x32/pink_64x32" \
          ".png"
    spritesheet.add_image(img, 1, 0)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/64x32" \
          "/purple_64x32.png"
    spritesheet.add_image(img, 1, 1)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/64x32/teal_64x32" \
          ".png"
    spritesheet.add_image(img, 1, 2)
    # Row 3: 29x36 Sprites
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/29x36" \
          "/orange_29x36.png"
    spritesheet.add_image(img, 0, 0)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/29x36/green_29x36" \
          ".png"
    spritesheet.add_image(img, 0, 1)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/29x36/blue_29x36" \
          ".png"
    spritesheet.add_image(img, 0, 2)

    spritesheet.create_spritesheet()
    spritesheet.save()


def sprite_sheet_test_case_4():
    """Tests Sprite Sheet with focus on Rows and constant Width and Height"""

    from objects.spritesheet import SpriteSheet
    spritesheet = SpriteSheet()
    spritesheet.set_constant_cell_width(1)
    spritesheet.set_constant_cell_height(1)

    # Set File
    spritesheet.set_save_file("/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_outputs/"
                              "/test_case_4_output.png")

    # Row 1: 32x32 Sprites
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32/red_32x32.png"
    spritesheet.add_image(img, 0, 0)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32" \
          "/orange_32x32.png"
    spritesheet.add_image(img, 0, 1)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32" \
          "/yellow_32x32.png"
    spritesheet.add_image(img, 0, 2)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32/green_32x32" \
          ".png"
    spritesheet.add_image(img, 0, 3)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32/blue_32x32" \
          ".png"
    spritesheet.add_image(img, 0, 4)
    # Row 2: 64x32 Sprites
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/64x32/pink_64x32" \
          ".png"
    spritesheet.add_image(img, 1, 0)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/64x32" \
          "/purple_64x32.png"
    spritesheet.add_image(img, 1, 1)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/64x32/teal_64x32" \
          ".png"
    spritesheet.add_image(img, 1, 2)
    # Row 3: 29x36 Sprites
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/29x36" \
          "/orange_29x36.png"
    spritesheet.add_image(img, 2, 0)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/29x36/green_29x36" \
          ".png"
    spritesheet.add_image(img, 2, 1)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/29x36/blue_29x36" \
          ".png"
    spritesheet.add_image(img, 2, 2)

    spritesheet.create_spritesheet()
    spritesheet.save()


def sprite_sheet_test_case_5():
    """Tests Sprite Sheet with focus on Columns and constant Width and Height"""
    from objects.spritesheet import SpriteSheet
    spritesheet = SpriteSheet()

    spritesheet.set_constant_cell_width(1)
    spritesheet.set_constant_cell_height(1)

    # Set File
    spritesheet.set_save_file("/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_outputs/"
                              "/test_case_5_output.png")

    # Col 1: 32x32 Sprites
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32/red_32x32.png"
    spritesheet.add_image(img, 0, 0)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32" \
          "/orange_32x32.png"
    spritesheet.add_image(img, 1, 0)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32" \
          "/yellow_32x32.png"
    spritesheet.add_image(img, 2, 0)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32/green_32x32" \
          ".png"
    spritesheet.add_image(img, 3, 0)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/32x32/blue_32x32" \
          ".png"
    spritesheet.add_image(img, 4, 0)
    # Col 2: 64x32 Sprites
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/64x32/pink_64x32" \
          ".png"
    spritesheet.add_image(img, 0, 1)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/64x32" \
          "/purple_64x32.png"
    spritesheet.add_image(img, 1, 1)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/64x32/teal_64x32" \
          ".png"
    spritesheet.add_image(img, 2, 1)
    # Col 3: 29x36 Sprites
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/29x36" \
          "/orange_29x36.png"
    spritesheet.add_image(img, 0, 2)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/29x36/green_29x36" \
          ".png"
    spritesheet.add_image(img, 1, 2)
    img = "/Users/CCThomasMac/Documents/Python/SpriteSheetMaker/test/resources/test_case_inputs/29x36/blue_29x36" \
          ".png"
    spritesheet.add_image(img, 2, 2)

    spritesheet.create_spritesheet()
    spritesheet.save()


def start():
    sprite_sheet_test_case_1()
    sprite_sheet_test_case_2()
    # sprite_sheet_test_case_3()
    sprite_sheet_test_case_4()
    sprite_sheet_test_case_5()
