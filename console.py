#!/usr/bin/python3
"""This module contains the command interpreter"""
import cmd
from models.base_model import BaseModel
# from models.amenity import BaseModel
# from models.city import BaseModel
# from models.place import BaseModel
# from models.review import BaseModel
# from models.state import BaseModel
from models import storage


classes = ["BaseModel"]
class HBNBCommand(cmd.Cmd):
	"""Command line for HBNB project"""

	prompt = "(hbnb) "

	def do_EOF(self, arg):
		"""End of the file command"""
		return True

	def do_quit(self, arg):
		"""Quit command to exit the program"""
		return True

	def do_create(self, arg):
		"""Creates a new instance of BaseModel class"""
		if self.does_class_exist(arg):
			cls = globals()[arg]
			instance = cls()
			instance.save()
			print(instance.id)

	def do_show(self, arg):
		"""
		Prints the string representation of 
		instance based on the class name
		"""
		if self.does_class_exist(arg):
			key = self.to_key_format(arg)
			if key:
				objects = storage.all()
				if key in objects:
					print(objects[key])
				else:
					print("** no instance found **")

	def do_destroy(self, arg):
		"""
		Deletes and instance based on class name and id
		and saves the changes to json file
		"""
		if self.does_class_exist(arg):
			key = self.to_key_format(arg)
			if key:
				objects = storage.all()
				if key in objects:
					del objects[key]
					storage.save()
				else:
					print("** no instance found **")

	def do_all(self, arg):
		"""
		Prints all string representation of all
		instances based or not the class name
		"""
		objects = storage.all()
		to_print = []
		if not arg:
			for key in objects.keys():
				to_print.append(str(objects[key]))
		elif self.does_class_exist(arg):
			for key in objects.keys():
				if arg in key:
					to_print.append(str(objects[key]))
		if to_print:
			print(to_print)

	def do_update(self, arg):
		"""Updates an instance based on class name and id"""
		if self.does_class_exist(arg):
			key = self.to_key_format(arg)
			if key:
				objects = storage.all()
				if key in objects:
					attr = arg.split()[2]
					value = arg.split()[3]
					value_cls_name = getattr(objects[key], attr).__class__.__name__
					cls = globals()[value_cls_name]
					value = cls(value)
					setattr(objects[key], attr, value)
					storage.save()


	@staticmethod
	def does_class_exist(arg):
		"""Checks if the class name exists"""
		if not arg:
			print("** class name missing **")
			return False
		elif arg.split()[0] not in classes:
			print ("** class doesn't exist **")
			return False
		return True

	@staticmethod
	def to_key_format(arg):
		"""Returns a string formatted as __objects keys"""
		packed_list = arg.split()
		if len(packed_list) < 2:
			print("** instance id missing **")
			return None
		else:
			return "{}.{}".format(packed_list[0], packed_list[1])


if __name__ == "__main__":
	HBNBCommand().cmdloop()
