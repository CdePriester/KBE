from Reader.wing import Wing
from Reader.fuselage import Fuselage
from Reader.engine import Engine
from parapy.core import *


class Aircraft(Base):
    fuselage_radius = Input(4.0)
    fuselage_length = Input(30.0)
    engine_radius = Input(1.3)
    engine_length = Input(5.0)
    density = Input(1.225)
    speed = Input(120)
    n_engines = Input(4)

    # Test how git works

    @Part
    def wing(self):
        return Wing(span=5.0)

    @Part
    def engines(self):
        return Engine(quantify=self.n_engines,
                      engine_radius=self.engine_radius,
                      engine_length=self.engine_length)

    @Part
    def fuselage(self):
        return Fuselage(fuselage_radius=self.fuselage_radius,
                        fuselage_length=self.fuselage_length)

    @Attribute
    def volume(self):
        return sum(eng.volume for eng in self.engines) + self.fuselage.volume

    def calc_lift(self, Cl):
        return 0.5*Cl*self.density*self.speed**2*self.area


if __name__ == '__main__':
    from parapy.gui import display
    obj = Aircraft()
    display(obj)
