from parapy.core import *
import math

class Engine(Base):
    engine_radius = Input(1.3)
    engine_length = Input(5.0)

    @Attribute
    def volume(self):
        return math.pi * self.engine_radius**2 * self.engine_length
