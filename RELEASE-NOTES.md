# Versions
- [0.0.1](#version-001)
- [1.0.0](#version-100)

## Version 0.0.1
Initial Design
```
# Scene 1
|---------------------------|
|x-  Sprite Sheet Maker     |
|---------------------------|
| [Add Image]               |
|---------------------------|
- [Add Image] is a Button
 
 
# Scene 2
|===========================|
|x-  Sprite Sheet Maker     |
|===========================|
| Row Col  Image Name       |
|---------------------------|
| []  []   ImageName.png    |
| [Add Image]               |
|                           |
| [Create] [Reset]          |
|===========================|
- Row, Col, & Image Name are Labels
- [] Entry boxes, takes a number for the row and column
- ImageName.png is a EntryBox that can be endited
- [Add Image] Button that pops up a File Dialog Box to pick a Png
- [Create] Button that pops up a entry field to name the sprite sheet
- [Reset] Button that resets to Scene 1 state
 
 
# Final Scene Example
|===========================|
|x-  Sprite Sheet Maker     |
|===========================|
| Row Col  Image Name       |
|---------------------------|
| [0] [0]  ImageName0.png   |
| [0] [1]  ImageName1.png   |
| [0] [2]  ImageName2.png   |
| [1] [0]  ImageName3.png   |
| [1] [1]  ImageName4.png   |
| [2] [0]  ImageName5.png   |
| [3] [0]  ImageName6.png   |
| [Add Image]               |
|                           |
| [Create] [Reset]          |
|===========================|
```

## Version 1.0.0
* Allows User to Dynamically add Image Paths
* User can change Images Row and Column Number
* User can Create specify Same Image and create Sprite Sheet
* SSM was Developed in an afternoon for self use and was completed some restrictions
  * Only Supports PNG Files
  * The number of Sprites in each Row and Column must be less than or equal to the previous Row & Column
* NOTE: Constant Width & Height Options in GUI have not been implemented

## Version 1.1.0
* Add Functionality for the Constant Width and Height Options