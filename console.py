#!/usr/bin/python3
"""
Module console
This moulde contain the entry point to a command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """prompt user"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exist the program"""
        return True

    def do_EOF(self, line):
        """Exit program"""
        print("")
        return True

    def emptyline(self):
        """called when an empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
