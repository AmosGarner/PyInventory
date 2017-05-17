# PyInventory
Proof of concept for a python driven Collection Tracking System (ColTS) that manages a collection of items for the user.

## Project Info:
* Name: PyInventory
* Version: 1.0
* Author: Amos Garner
* License: MIT

## Install Commands:
Clone project repository into project directory:
```git clone git@github.com:AmosGarner/PyInventory.git```

## How to run:
```python main.py --user [Username] --type [Item Type] --name [Collection Name] --length [Collection Length]```

EX: ```python main.py --user jsmith --name item --name Items --length 10```

When you run this program it will spit out a collection of generated objects in the new ```/collections``` directory created in the project dir.

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
