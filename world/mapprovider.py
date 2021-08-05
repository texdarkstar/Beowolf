from typeclasses.rooms import SystemRoom
from typeclasses.objects import RoomTokenObject

from evennia import settings, create_object
from evennia.utils import inherits_from
from evennia.contrib.wilderness import *

class MapProvider(WildernessMapProvider):
    room_typeclass = SystemRoom

    def is_valid_coordinates(self, wilderness, coordinates):
        return True

    def at_prepare_room(self, coordinates, caller, room):
        """
        Called when a room gets activated for certain coordinates. This happens
        after every object is moved in it.
        This can be used to set a custom room desc for instance or run other
        customisations on the room.

        Args:
            coordinates (tuple): the coordinates as (x, y) where room is
                located at
            caller (Object): the object that moved into this room
            room (WildernessRoom): the room object that will be used at that
                wilderness location
        Example:
            An example use of this would to plug in a randomizer to show different
            descriptions for different coordinates, or place a treasure at a special
            coordinate.
        """
        x, y = room.coordinates
        token = None

        token = room.search("roomtoken", typeclass=RoomTokenObject)

        if not token:
            token = create_object(RoomTokenObject, location=room, key="roomtoken_(%d, %d)" % (x, y))
        else:
            pass

        room.db.token = token
            

