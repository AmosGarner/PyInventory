# PyInventory
Proof of concept for a python driven Collection Tracking System (ColTS) that manages a collection of items for the user.

## Project Info:
* Name: PyInventory
* Version: 1.0
* Author: Amos Garner
* License: MIT

## Installation Instructions:
1.  Clone Repository:
``` git clone git@github.com:AmosGarner/PyInventory.git```
2. Run the install command
```python main.py --action install --user "[Username]"```
###### The bracket ```[]``` symbols wrapping a value means that value is a variable and can be customized

## Program Features
* Create, Display, Edit, and Remove collections of items.
* Create, Remove, and Edit items in a user's collection.

### Feature Commands:

#### Collection Features:
* Create a Collection
    * Command: ```python main.py --action create_collection --user "[Username]" --name "[Collection Name]" --type [ItemType]```
* Edit a Collection
    * Command: ```python main.py --action edit_collection --user "[Username]" --name "[Collection Name]" --input "[New Collection Name]"```
* Remove a Collection
    * Command: ```python main.py --action remove_collection --user "[Username]" --name "[Collection Name]"```
* Display a Collection
    * Command: ```python main.py --action display_collection --user "[Username]" --name "[Collection Name]"```

#### Item Features:
* Insert an Item
    * Command: ```python main.py --action insert_item --user "[Username]" --name "[Collection Name]" --type [ItemType] --input "[Item Name]"~"[Special Attribute]"```
* Edit an Item
    * Command: ```python main.py --action edit_item --user "[Username]" --name "[Collection Name]" --type [ItemType] --input "[Item ID]"~"[Item Name]"~"[Special Attribute]"```
* Remove an Item
    * Command: ```python main.py --action remove_item --user "[Username]" --name "[Collection Name]" --type [ItemType] --input "[Item ID]"

## Parameters:
* ```--action```: Action that the script is going to take when running
    * ### Collection Commands:
    * install: Installs the scripts dependent directories
        * EX:   ```python main.py --action install --user bburger```
    * create_collection: Creates a blank collection of objects as per the user's choosing
        * EX:   ```python main.py --action create_collection --user agarner --name items --type item```
    * edit_collection: Edits the collection, in this program the collection's name is the only editable property
        * EX:   ```python main.py --action edit_collection --user agarner --name items --input Items```
    * remove_collection: Removes the collection file from the user's collections.
        * EX:   ```python main.py --action remove_collection --user bburger --name items```
    * ### Item Commands:
    * insert_item: Insert's an item into a user's collection.
        * EX:   ```python main.py --action insert_item --user bburger --name items --type item --input "Item Name"```
* ```--user```: The username set by the user
* ```--name```: The name of the collection
* ```--type```: The type of objects this collection will contain
    * Item: Generic item
    * Album
    * Book
    * Movie
* ```--input```: Then length of the generated collection.

## Dependencies:
* [datetime](https://docs.python.org/2/library/datetime.html): Retrieves the date and time from the system.
* [json](https://docs.python.org/2/library/json.html): Encodes data into object notation objects.
* [os.path](https://docs.python.org/2/library/os.html): Handles OS level path, file, and directory operations.
* [argparse](https://docs.python.org/2/library/argparse.html): Parses arguments provided by the user into objects.
