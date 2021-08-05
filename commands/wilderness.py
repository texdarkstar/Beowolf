from evennia.contrib import wilderness
from commands.command import Command
from world.mapprovider import MapProvider


class CmdWilderness(Command):
    '''wilderness <create/enter/destroy> <wilderness name>
    '''
    key = "wilderness"
    locks = "cmd:false()"
    helpstring = "Syntax: wilderness <create/enter/destroy>"

    def func(self):
        args = self.args.strip().lower().split()

        if not args:
            self.caller.msg(self.helpstring)
            return

        elif len(args) < 2:
            self.caller.msg(self.helpstring)
            return

        action, *wilderness_name = args
        wilderness_name = " ".join(wilderness_name)

        if action == "create":
            wilderness.create_wilderness(name=wilderness_name, mapprovider=MapProvider())

            self.caller.msg("Created wilderness '{wilderness_name}'".format(**locals()))
            return

        elif action == "enter":
            wilderness.enter_wilderness(self.caller, name=wilderness_name)
            self.caller.execute_cmd("look")

            self.caller.msg("Entered wilderness '{wilderness_name}'".format(**locals()))
            return

