from commands.command import Command


class CmdCoor(Command):
    key = "coor"
    locks = "perm:(admin)"

    def func(self):
        args = self.args.strip().split()

        if len(args) != 2:
            self.caller.msg("Invalid coordinates.")
            return

        x, y = args

        try:
            x = int(x)
            y = int(y)
        except ValueError:
            self.caller.msg("Invalid coordinates.")
            return


        self.caller.ndb.wilderness.move_obj(self.caller, (x, y))
