"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom
from evennia.contrib.wilderness import *


class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """

    pass

class SystemRoom(WildernessRoom):
    def get_display_name(self, looker, **kwargs):
        """
        Displays the name of the object in a viewer-aware manner.

        Args:
            looker (TypedObject): The object or account that is looking
                at/getting inforamtion for this object.

        Returns:
            name (str): A string containing the name of the object,
                including the DBREF if this user is privileged to control
                said object and also its coordinates into the wilderness map.

        Notes:
            This function could be extended to change how object names
            appear to users in character, but be wary. This function
            does not change an object's keys or aliases when
            searching, and is expected to produce something useful for
            builders.
        """
        x, y = self.coordinates
        name = "Deep Space"

        if self.db.token:
            name = self.db.token.get_uwp()

        if self.locks.check_lockstring(looker, "perm(Builder)"):
            # looker.msg("|gelevation (%f)|n" % elevation)
            # looker.msg("|bmoisture (%f)|n" % moisture)
            # looker.msg("|rtemperature (%f)|n" % temperature)

            name = "{}(#{})".format(name, self.id)
        else:
            pass

        name += " {0}".format(self.coordinates)
        return name
