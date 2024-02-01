#!/usr/bin/python3
""" my console """

from models import storage
from models.base_model import BaseModel
from models.user import User
import cmd
import re
import readline


class HBNBCommand(cmd.Cmd):
    """ my prototyping tool for the Airbnb clone project """
    prompt = '(hbnb) '
    lst = [User.__name__, BaseModel.__name__]

    def do_quit(self, line):
        """ quit the proto tool"""
        return True

    def help_quit(self):
        """describe what quit does"""
        print('some info')

    def do_EOF(self, line):
        """exit gracefully """
        print()
        return True

    def emptyline(self):
        """ do nothing """
        pass

    def do_create(self, cmmd):
        """ create a base model object """
        if cmmd and cmmd not in lst:
            print("** class doesn't exist **")
        elif cmmd:
            if cmmd == User.__name__:
                b = User()
            else:
                b = BaseModel()
            b.save()
            print(b.id)
        else:
            print('** class name missing **')

    def do_show(self, cmmd):
        if cmmd:
            arr = cmmd.split()

            if arr[0] not in self.lst:
                print("** class does't exist **")
            elif len(arr) != 2:
                print("** instace id missing **")
            else:
                st = arr[0] + '.' + arr[1]
                oj = storage.all()
                if st in oj:
                    print(oj[st])
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, cmmd):
        """ delete an object """
        if cmmd:
            arr = cmmd.split()

            if arr[0] not in self.lst:
                print("** class doesn't exist **")
            elif len(arr) == 2:
                st = arr[0] + '.' + arr[1]

                oj = storage.all()

                if st in oj:
                    oj.pop(st)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, cmmd):
        """ print all present object instances """
        oj = storage.all()

        if cmmd and cmmd not in self.lst:
            print("** class doesn't exist **")
        elif cmmd:
            for x in oj:
                if cmmd in x:
                    print(oj[x])
        else:
            for x in oj:
                print(oj[x])

    def do_update(self, cmmd):
        """ update the objects and saves them to file """
        oj = storage.all()

        if cmmd:
            arr = cmmd.split()

            if arr[0] in self.lst:
                if len(arr) >= 2:
                    st = arr[0] + '.' + arr[1]

                    if st in oj:
                        object_to_update = oj[st]
                        if len(arr) >= 4:
                            if re.search("^[0-9]+$", arr[3]):
                                object_to_update.update({arr[2]: int(arr[3])})
                            else:
                                object_to_update.update({arr[2]: arr[3]})
                            storage.save()
                        elif len(arr) == 3:
                            print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
