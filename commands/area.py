from evennia import settings, create_object
from commands.command import Command
# from typeclasses.rooms import OverworldRoom
from world.noiselib import generate_elevation, generate_biome


class CmdArea(Command):
    key = "area"
    aliases = ["map"]
    locks = "cmd:all()"
    help_category = "General"

    def func(self):
        wilderness_script = self.caller.ndb.wilderness
        if not wilderness_script:
            self.caller.msg("You aren't in a wilderness!")
            return

        radius = 18
        string = ""
        strings = ["+-" + "--" * int(radius * 2) + "-+"]

        x, y = self.caller.location.coordinates

        # room = create_object(OverworldRoom, key="tmp_room")
        # array = list()


        for _y in range(y - radius, y + radius + 1):
            for _x in range(x - radius, x + radius + 1):
                if _x == x and _y == y:
                    tile = "><"
                # elif _x < 0 or _y < 0 or _x > settings.MAP_WIDTH or _y > settings.MAP_HEIGHT:
                    # tile = "  "
                else:
                    # room.db.x, room.db.y = _x, _y
                    # noise = generate_elevation(_x, _y)
                    # array.append(noise)
                    biome = generate_biome(_x, _y)

                    # if noise < settings.MAP_ELEVATION["water"]:
                        # tile = "|C~~"
                    # elif noise < settings.MAP_ELEVATION["shallow water"]:
                        # tile = "|c@@"
                    # elif noise < settings.MAP_ELEVATION["land"]:
                        # tile = "|g.."
                    # elif noise < settings.MAP_ELEVATION["hill"]:
                        # tile = "|x^^"
                    # elif noise < settings.MAP_ELEVATION["mountain"]:
                        # tile = "|x##"
                    # else: 
                        # tile = "|w##"
                        # self.caller.msg("ERROR: Noise value for {x} {y} outside threshold: {val}".format(x=_x, y=_y, val=noise))
                    tile = biome[1]

                string += tile

            strings.append("||" + string + "||")
            string = ""

        strings.append("+-" + "-" * int(radius * 4) + "-+")
        strings.reverse()
        area = "\n".join(strings)

        self.caller.msg(area)
        # self.caller.msg("avg val: |g%f|n" % (sum(array) / len(array)))
        # self.caller.msg("max val: |g%f|n" % max(array))
        # room.delete()

