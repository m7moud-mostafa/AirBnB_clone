#!/usr/bin/python3
"""This module contains the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command line for HBNB project"""

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """End of the file command"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """No cammand is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel class"""

        if not arg:
            print("** class name missing **")
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            model = globals()[arg]()
            storage.save()
            print(model.id)

    def do_show(self, arg):
        """
        Prints the string representation of
        instance based on the class name
        """
        args = arg.split()
        length = len(args)
        if length == 0:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif length == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes and instance based on class name and id
        and saves the changes to json file
        """
        args = arg.split()
        length = len(args)
        if length == 0:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif length == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not the class name
        """
        args = arg.split()
        length = len(args)
        to_print = []
        if length == 0:
            for value in storage.all().values():
                to_print.append(str(value))
        elif length == 1 and args[0] not in globals():
            print("** class doesn't exist **")
        else:
            for value in storage.all().values():
                if value.__class__.__name__ == args[0]:
                    to_print.append(str(value))
        if (to_print):
            print(to_print)

    def do_update(self, arg):
        """Updates an instance based on class name and id"""
        args = arg.split(maxsplit=3)
        length = len(args)
        if length == 0:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif length == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            elif length == 2:
                print("** attribute name missing **")
            elif length == 3:
                print("** value missing **")
            else:
                obj = storage.all()[key]
                attr_name = args[2]
                attr_value = args[3].strip('"')

                # Attempt to cast the attribute value to the correct type
                if hasattr(obj, attr_name):
                    current_value = getattr(obj, attr_name)
                    try:
                        attr_value = type(current_value)(attr_value)
                    except (ValueError, TypeError):
                        pass

                setattr(obj, attr_name, attr_value)
                obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
