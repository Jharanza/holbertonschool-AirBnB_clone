# HBNB - an AirBnB clone

## Description
In this project we create an interactive console with which we can manipulate and instantiate objects by manipulating, serializing and deserializing them, we also create an abstract storage engine and create files to test and validate the created classes

### Coding Style
All file will are written in Python programming language

### Usage
The HBNB console wil have the interactive and non-interactive mode

###Console Commands
Command	Description
all Prints all string representation of all instances based or not on the class name
help Display help page
quit Quits the console
EOF Quist the console
update Updates an instance based on the class name and id by adding or updating attribute and saves changes to a JSON file
create <class> Creates a new instance of a given class with a unique ID and saves it to a JSON file
destroy <class> <id> Deletes an instance based on the class name and id and saves it to a JSON file
show <class> <id> Prints the string representation of a class instance based on the class name and ID

### File Descriptions
- *models* directory:
  - **base_model.py:** Class *BaseModel* which all other classes inherit from. Attributes: *id, created_at, updated_at*.
  - **city.py:** Class *City*. Attributes: *state_id, name*.

## Unit Testing
Unit test are stored in the *tests* directory. To run unit test, run the following command:
"""
python3 -m unittest discover tests
"""

## Authors
- Jhonny Arana [[Jharanza](https://github.com/Jharanza)]
- Miguel Bautista [[MiguelBG12](https://github.com/MiguelBG12)]


