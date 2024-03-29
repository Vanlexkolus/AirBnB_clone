#!/usr/bin/python3
"""
Module console
This moulde contain the entry point to a command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """prompt user"""
    prompt = "(hbnb) "
    classes = ("BaseModel")

    def do_quit(self, line):
        """Quit command to exist the program"""
        return True

    def help_quit(self):
        """Method to exit the HBNB console"""
        print("Exit the program with formatting\n")

    def do_EOF(self, line):
        """Exit program"""
        print("")
        return True

    def help_EOF(self):
        """ Handle EOF to exit program """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """called when an empty line is entered"""
        pass

    def do_create(self, arg):
        """
        Creates a new class instance like BaseModel
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg.strip() not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            storage.save()
            print(new_instance.id)

    def help_create(self):
        """ Help info for the create command """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """
        This prints the string representation of
        an instance based on the class name and id
        """
        new = args.partition(" ")
        class_name = new[0]
        class_id = new[2]

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")

        if not class_id:
            print("** instance id missing **")
            return
        key = class_name + "." + class_id

        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """ Help information for show command """
        print("Show an individual instance of a class")
        print("[Usage]: sho <className> <objectId>\n")

    def do_destroy(self, args):
        new = args.partition(" ")
        class_name = new[0]
        class_id = new[2]

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        if not class_id:
            print("** instnace id missing **")

        key = class_name + "." + class_id
        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroy an individual instance of a class")
        print("[Usage]: destroy <className> <objectId\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
