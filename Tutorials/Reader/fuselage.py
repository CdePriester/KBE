from parapy.core import *
import math


class Fuselage(Base):
    fuselage_radius = Input(4.0)
    fuselage_length = Input(30.0)

    @Attribute
    def volume(self):
        return math.pi * self.fuselage_radius ** 2 * self.fuselage_length
