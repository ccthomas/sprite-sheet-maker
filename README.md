# Sprite Sheet Maker

## Initial Design
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