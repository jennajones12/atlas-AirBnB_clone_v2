#!/usr/bin/python3
""" Console for managing instances of classes """

import cmd
import shlex
import os
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}

class HBNBCommand(cmd.Cmd):
    """ HBNB console class """

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ Exit the console with EOF (Ctrl+D) """
        return True

    def emptyline(self):
        """ Do nothing on empty input """
        pass

    def do_quit(self, arg):
        """ Quit the console """
        return True

    def _parse_key_value(self, args):
        """ Parse key=value pairs from args """
        parsed_dict = {}
        for arg in args:
            if "=" in arg:
                key, value = arg.split('=', 1)
                if value.startswith('"') and value.endswith('"'):
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
                            pass
                parsed_dict[key] = value
        return parsed_dict

    def do_create(self, arg):
        """ Create a new instance of a class """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        new_dict = self._parse_key_value(args[1:])
        instance = classes[class_name](**new_dict)
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """ Show string representation of an instance """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = class_name + "." + args[1]
        obj_dict = storage.all()
        if obj_key in obj_dict:
            print(obj_dict[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Delete an instance based on the class name and id """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = class_name + "." + args[1]
        obj_dict = storage.all()
        if obj_key in obj_dict:
            del obj_dict[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ Show all instances or all instances of a class """
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = storage.all()
        else:
            class_name = args[0]
            if class_name not in classes:
                print("** class doesn't exist **")
                return
            obj_dict = storage.all(classes[class_name])
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print(obj_list)

    def do_update(self, arg):
        """ Update an instance based on the class name and id """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = class_name + "." + args[1]
        obj_dict = storage.all()
        if obj_key not in obj_dict:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        value = args[3]
        if value.isdigit():
            value = int(value)
        elif '.' in value and all(c.isdigit() or c == '.' for c in value):
            value = float(value)
        setattr(obj_dict[obj_key], args[2], value)
        storage.save()

if __name__ == '__main__':
    # Fetching environment variables
    mysql_user = os.getenv('HBNB_MYSQL_USER')
    mysql_pwd = os.getenv('HBNB_MYSQL_PWD')
    mysql_host = os.getenv('HBNB_MYSQL_HOST')
    mysql_db = os.getenv('HBNB_MYSQL_DB')
    storage_type = os.getenv('HBNB_TYPE_STORAGE')
    hbnb_env = os.getenv('HBNB_ENV')

    # Print environment variables for debugging
    print(f"Using environment variables:")
    print(f"HBNB_MYSQL_USER: {mysql_user}")
    print(f"HBNB_MYSQL_PWD: {mysql_pwd}")
    print(f"HBNB_MYSQL_HOST: {mysql_host}")
    print(f"HBNB_MYSQL_DB: {mysql_db}")
    print(f"HBNB_TYPE_STORAGE: {storage_type}")
    print(f"HBNB_ENV: {hbnb_env}")

    HBNBCommand().cmdloop()
