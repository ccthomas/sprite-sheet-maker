# Documentation
* \_\_main__.py
  * Makes sure Python Version is 3.0
  * If Testing is True, Test Package is Called
  * Else Window is Created and Program Starts

## GUI Package
* window.py
  * Window Class
    * \_\_init__()
      * Initializes all Window Variables
    * add_row(image_location)
      * Adds new Row to GUI Window with image_location's Information
    * button_add_image_pressed()
      * Gets image_location from User in a File Dialog Pop Up
      * Calls add_row(image_location)
    * button_create_pressed()
      * Creates a new [SpriteSheet](Objects Package) Object
      * Loops through each row, passing the information for each Sprite into the SpriteSheet
      * Saves the SpriteSheet at a Location chosen by the User in a File Dialog Pop Up
    * button_duplicate_image_pressed()
      * Gets the image_location from the most recent row
      * Calls add_row(image_location)
    * button_reset_pressed()
      * Removes all GUI Elements
      * Resets all Variables
    * mainloop()
      * Calls Main loop in tkinter master
    * update_footer_buttons()
      * Changes the grid row number for each Footer Object in the Window GUI

## Objects Package
* spritesheet.py
  * SpriteSheet Class
    * \_\_init__()
      * Initializes all SpriteSheet Variables
    * add_image(self, image_location, row, col)
      * Resize Arrays for storing Data if lengths are less than the row or col params
      * Open Image from Image Location
      * Save the Image Information
    * create_spritesheet()
      * Find the Dimensions of the New Sprite Sheet
      * For each Image, Add it to the Sprite Sheet
    * save()
      * Save the Sprite Sheet to location Specified
    * set_save_file(file_name)
      * Set Save File
    * set_constant_cell_height(constant_cell_height)
      * Set Constant Cell Height
    * set_constant_cell_width(constant_cell_width)
      * Set Constant Cell Width
    * sum_prev_rows_widths(row_number, column_number)
      * Go through the previous rows at column_number location summing up each Row's Heights
    * sum_prev_cols_heights(row_number, column_number)
      * Go through the previous columns at row_number location summing up each Columns's Widths