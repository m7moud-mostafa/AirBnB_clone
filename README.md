# AirBnB Clone - The Console

## Description

Welcome to the AirBnB clone project! This project is the first step towards building a full web application that mimics the AirBnB platform. In this initial phase, we are focused on creating a command interpreter that will manage the AirBnB objects. This command interpreter, or console, will allow users to create, modify, delete, and query various objects such as Users, Places, Cities, and more.

## Command Interpreter

### How to Start It

To start the command interpreter, navigate to the root directory of the project and execute the following command:

```bash
$ ./console.py
```

### How to Use It

Once the console is running, you can use several commands to interact with the AirBnB objects.

#### Commands:

- `help`: Displays a list of available commands.
- `quit` or `EOF`: Exits the command interpreter.
- `create <ClassName>`: Creates a new instance of `ClassName`, saves it to the JSON file, and prints the id.
- `show <ClassName> <id>`: Prints the string representation of an instance based on the class name and id.
- `destroy <ClassName> <id>`: Deletes an instance based on the class name and id, and saves the change into the JSON file.
- `all [<ClassName>]`: Prints all string representations of all instances or instances of a specific class.
- `update <ClassName> <id> <attribute name> "<attribute value>"`: Updates an instance based on the class name and id by adding or updating an attribute.

### Examples

#### Interactive Mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) create User
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show User 49faff9a-6318-451f-87b6-910505c55907
[User] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2024, 5, 13, 6, 0, 0, 0), 'updated_at': datetime.datetime(2024, 5, 13, 6, 0, 0, 0), 'email': '', 'password': '', 'first_name': '', 'last_name': ''}
(hbnb) quit
```

#### Non-Interactive Mode

```bash
$ echo "create User" | ./console.py
49faff9a-6318-451f-87b6-910505c55907
$ echo "show User 49faff9a-6318-451f-87b6-910505c55907" | ./console.py
[User] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2024, 5, 13, 6, 0, 0, 0), 'updated_at': datetime.datetime(2024, 5, 13, 6, 0, 0, 0), 'email': '', 'password': '', 'first_name': '', 'last_name': ''}
```

## Project Structure

```
AirBnB_Console
├── models/
│   ├── __init__.py
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── engine/
│       ├── __init__.py
│       └── file_storage.py
├── tests/
├── AUTHORS
├── console.py
└── README.md
```

## Requirements

- All Python files should be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5).

## Authors

* Mahmoud Mostafa Ahmed <mah2002moud@gmail.com>
* Rokia Nofal <email>