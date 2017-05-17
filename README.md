# PyInventory
Proof of concept for a python driven Collection Tracking System (ColTS) that manages a collection of items for the user.

## Project Info:
* Name: PyInventory
* Version: 0.1
* Author: Amos Garner
* License: MIT

## Install Commands:
Clone project repository into project directory:
```git clone git@github.com:AmosGarner/PyInventory.git```

## How to run:
```python main.py --user [Username] --type [Item Type] --name [Collection Name] --length [Collection Length]```

EX: ```python main.py --user jsmith --type item --name Items --length 10```

When you run this program it will spit out a collection of generated objects in the new ```/collections``` directory created in the project dir.

## Parameters:
* ```--user```: The username set by the user
* ```--type```: The type of objects this collection will contain
    * Item: Generic item
    * Album
    * Book
    * Movie 
* ```--name```: The name of the collection
* ```--length```: Then length of the generated collection.
* ```--test```: Test the system to generate a generic collection of each object type.

## Dependencies:
* [datetime](https://docs.python.org/2/library/datetime.html): Retrieves the date and time from the system.
* [json](https://docs.python.org/2/library/json.html): Encodes data into object notation objects.
* [os.path](https://docs.python.org/2/library/os.html): Handles OS level path, file, and directory operations.
* [argparse](https://docs.python.org/2/library/argparse.html): Parses arguments provided by the user into objects.
