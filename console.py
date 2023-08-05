#!/usr/bin/python3
"""Entry point for the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Interpreter class from cmd"""
    prompt = '(hbnb)'

    def do_EOF(self, line):
        """Quits the console when Ctrl D entered"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Overrides parent empty line method"""
        pass

    def do_help(self, line):
        """Display help information for commands"""
        print("\n")
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("Quit command to exit the program")
        print("\n")
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
