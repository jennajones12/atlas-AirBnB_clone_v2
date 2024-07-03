#!/usr/bin/python3
""" Console module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
            "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """ HBNH console """

    # interactive/non-interactive mode determination prompt
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''


    def do_create(self, arg):
        """Create a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Show an instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Destroy an instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + '.' + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Show all instances of a class"""
        args = arg.split()
        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            instances = []
            for key, obj in objects.items():
                if len(args) == 0 or key.split('.')[0] == args[0]:
                    instances.append(str(obj))
            print(instances)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
